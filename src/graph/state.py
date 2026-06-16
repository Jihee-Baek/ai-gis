from typing import TypedDict, Optional

class ProjectState(TypedDict):
    user_request: str
    prd_path: Optional[dict]
    architecture_path: Optional[dict]
    backend_design_path: Optional[dict]
    frontend_design_path: Optional[dict]
    backend_structure_path: Optional[dict]
    frontend_structure_path: Optional[dict]
    backend_codegen_path: Optional[dict]
    frontend_codegen_path: Optional[dict]
    reviewer_path: Optional[dict]
    devops_plan_path: Optional[dict]
    test_plan_path: Optional[dict]
