from src.services.json_loader import JsonLoader

def initialize_node(state):
    print("=" * 20, "Start initialize_node")
    
    # 로드할 파일 목록 정의
    outputs = {
        "prd_path": "outputs/prd.json",
        "architecture_path": "outputs/architecture.json",
        "backend_design_path": "outputs/backend_design.json",
        "frontend_design_path": "outputs/frontend_design.json",
        "backend_structure_path": "outputs/backend_structure.json",
        "frontend_structure_path": "outputs/frontend_structure.json",
        "backend_codegen_path": "outputs/backend_codegen.json",
        "frontend_codegen_path": "outputs/frontend_codegen.json",
        "reviewer_path": "outputs/reviewer.json",
        "devops_plan_path": "outputs/devops_plan.json",
        "test_plan_path": "outputs/test_plan.json"
    }
    
    updates = {}
    for key, path in outputs.items():
        if JsonLoader.load(path):
            updates[key] = path
        else:
            updates[key] = None
    
    updates["sync_status"] = False
    return updates
