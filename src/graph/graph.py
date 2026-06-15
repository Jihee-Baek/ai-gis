from langgraph.graph import (StateGraph, END)
from src.graph.state import ProjectState
from src.nodes.pm_node import pm_node
from src.nodes.architect_node import architect_node

builder = StateGraph(ProjectState)
builder.add_node("pm", pm_node)
builder.add_node("architect", architect_node)
builder.set_entry_point("pm")
builder.add_edge("pm", "architect")
builder.add_edge("architect", END)
graph = builder.compile()