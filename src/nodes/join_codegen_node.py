def join_codegen_node(state):
    print('='*20, 'Start join_codegen_node')

    if not state.get("backend_codegen_path"):
        raise ValueError(
            "backend_codegen_path not found"
        )

    if not state.get("frontend_codegen_path"):
        raise ValueError(
            "frontend_codegen_path not found"
        )

    return state