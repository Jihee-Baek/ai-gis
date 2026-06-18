from src.services.json_loader import JsonLoader
from src.services.output_writer import OutputWriter


def project_writer_node(state):
    print("=" * 20, "Start project_writer_node")

    backend_path = state.get("backend_codegen_path")
    frontend_path = state.get("frontend_codegen_path")

    # [수정] 둘 중 하나라도 없으면 건너뛰는 것이 아니라, 있는 것만이라도 처리하도록 변경하고
    # 현재 문서 동기화 모드인지 확인하는 로직 보강
    if not backend_path and not frontend_path:
        print("Skipping project_writer_node: No codegen paths found (Documentation Sync Mode)")
        return state

    # Backend 처리
    if backend_path:
        try:
            backend = JsonLoader.load(backend_path)
            if backend and "generated_files" in backend:
                for file in backend["generated_files"]:
                    OutputWriter.write_file(f"project/backend/{file['path']}", file["content"])
                    print(f"[BACKEND] Created/Updated: {file['path']}")
        except Exception as e:
            print(f"[BACKEND] Project Write Error: {e}")

    # Frontend 처리
    if frontend_path:
        try:
            frontend = JsonLoader.load(frontend_path)
            if frontend and "generated_files" in frontend:
                for file in frontend["generated_files"]:
                    OutputWriter.write_file(f"project/frontend/{file['path']}", file["content"])
                    print(f"[FRONTEND] Created/Updated: {file['path']}")
        except Exception as e:
            print(f"[FRONTEND] Project Write Error: {e}")

    return state