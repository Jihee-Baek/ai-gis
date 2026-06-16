def join_design_node(state):
    print('='*20, 'Start join_design_node')

    if not state.get("backend_design_path"):
        raise ValueError(
            "backend_design_path not found"
        )

    if not state.get("frontend_design_path"):
        raise ValueError(
            "frontend_design_path not found"
        )

    return state