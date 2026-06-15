from langgraph.graph import (StateGraph, END)
from src.graph.state import ProjectState
from src.nodes.pm_node import pm_node
from src.nodes.architect_node import architect_node
from src.nodes.backend_node import backend_node
from src.nodes.frontend_node import frontend_node
from src.nodes.join_node import join_node
from src.nodes.reviewer_node import reviewer_node
from src.nodes.devops_node import devops_node
from src.nodes.qa_node import qa_node

builder = StateGraph(ProjectState)
builder.add_node("pm", pm_node)
builder.add_node("architect", architect_node)
builder.add_node("backend", backend_node)
builder.add_node("frontend", frontend_node)
builder.add_node("join", join_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("devops", devops_node)
builder.add_node("qa", qa_node)
builder.set_entry_point("pm")
builder.add_edge("pm", "architect")
builder.add_edge("architect", "backend")
builder.add_edge("architect", "frontend")
builder.add_edge(["backend", "frontend"], "join")
builder.add_edge("join", "reviewer")
builder.add_edge("reviewer", "devops")
builder.add_edge("devops", "qa")
builder.add_edge("qa", END)

graph = builder.compile()