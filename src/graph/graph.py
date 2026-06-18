from langgraph.graph import (StateGraph, END)
from src.graph.state import ProjectState
from src.nodes.initialize_node import initialize_node
from src.nodes.pm_node import pm_node
from src.nodes.architect_node import architect_node
from src.nodes.backend_design_node import backend_design_node
from src.nodes.frontend_design_node import frontend_design_node
from src.nodes.join_design_node import join_design_node
from src.nodes.backend_structure_node import backend_structure_node
from src.nodes.frontend_structure_node import frontend_structure_node
from src.nodes.join_structure_node import join_structure_node
from src.nodes.backend_codegen_node import backend_codegen_node
from src.nodes.frontend_codegen_node import frontend_codegen_node
from src.nodes.join_codegen_node import join_codegen_node
from src.nodes.reviewer_node import reviewer_node
from src.nodes.devops_node import devops_node
from src.nodes.qa_node import qa_node
from src.nodes.project_writer_node import project_writer_node
from src.nodes.analyzer_node import code_analyzer_node
from src.nodes.sync_node import doc_sync_node

def router(state):
    """
    사용자 요청에 따라 기획부터 시작할지, 코드 분석부터 시작할지 결정한다.
    """
    req = state["user_request"]
    if any(keyword in req for keyword in ["코드 분석", "문서 최신화", "분석해서", "반영해줘"]):
        return "code_analyzer"
    return "pm"

builder = StateGraph(ProjectState)

builder.add_node("initialize", initialize_node)
builder.add_node("pm", pm_node)
builder.add_node("architect", architect_node)
builder.add_node("backend_design", backend_design_node)
builder.add_node("frontend_design", frontend_design_node)
builder.add_node("join_design", join_design_node)
builder.add_node("backend_structure", backend_structure_node)
builder.add_node("frontend_structure", frontend_structure_node)
builder.add_node("join_structure", join_structure_node)
builder.add_node("backend_codegen", backend_codegen_node)
builder.add_node("frontend_codegen", frontend_codegen_node)
builder.add_node("join_codegen", join_codegen_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("devops", devops_node)
builder.add_node("qa", qa_node)
builder.add_node("project_writer", project_writer_node)
builder.add_node("code_analyzer", code_analyzer_node)
builder.add_node("doc_sync", doc_sync_node)

builder.set_entry_point("initialize")

builder.add_conditional_edges("initialize", router)

builder.add_edge("pm", "architect")
builder.add_edge("architect", "backend_design")
builder.add_edge("architect", "frontend_design")
builder.add_edge(["backend_design", "frontend_design"], "join_design")
builder.add_edge("join_design", "reviewer")
builder.add_edge("reviewer", "backend_structure")
builder.add_edge("reviewer", "frontend_structure")
builder.add_edge(["backend_structure", "frontend_structure"], "join_structure")
builder.add_edge("join_structure", "backend_codegen")
builder.add_edge("join_structure", "frontend_codegen")
builder.add_edge(["backend_codegen", "frontend_codegen"], "join_codegen")
builder.add_edge("join_codegen", "devops")
builder.add_edge("devops", "qa")
builder.add_edge("qa", "code_analyzer") # 품질 검증 후 코드 분석 루프 추가
builder.add_edge("code_analyzer", "doc_sync")
builder.add_edge("doc_sync", "project_writer")
builder.add_edge("project_writer", END)

graph = builder.compile()