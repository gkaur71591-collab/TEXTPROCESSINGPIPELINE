from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END


# State
class TextState(BaseModel):
    text: str = ""
    word_count: int = 0


# Nodes
def greeting_node(state: TextState):
    return {
        "text": state.text + " Welcome to LangGraph!"
    }


def uppercase_node(state: TextState):
    return {
        "text": state.text.upper()
    }


def word_count_node(state: TextState):
    return {
        "word_count": len(state.text.split())
    }


# Create graph
graph = StateGraph(TextState)


# Add nodes
graph.add_node("greeting", greeting_node)
graph.add_node("uppercase", uppercase_node)
graph.add_node("word_count", word_count_node)


# Add edges
graph.add_edge(START, "greeting")
graph.add_edge("greeting", "uppercase")
graph.add_edge("uppercase", "word_count")
graph.add_edge("word_count", END)


# Compile
app = graph.compile()


# Run graph
result = app.invoke(
    {
        "text": "I love Python"
    }
)


print(result)