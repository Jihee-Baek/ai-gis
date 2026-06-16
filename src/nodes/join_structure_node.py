def join_structure_node(state):
    print('='*20, 'Start join_structure_node')

    if not state.get("backend_structure_path"):
        raise ValueError(
            "backend_structure_path not found"
        )

    if not state.get("frontend_structure_path"):
        raise ValueError(
            "frontend_structure_path not found"
        )

    return state