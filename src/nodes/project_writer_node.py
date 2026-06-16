from src.services.json_loader import JsonLoader
from src.services.output_writer import OutputWriter


def project_writer_node(state):
    print("=" * 20, "Start project_writer_node")

    backend = JsonLoader.load(state["backend_codegen_path"])
    frontend = JsonLoader.load(state["frontend_codegen_path"])

    # backend = JsonLoader.load("outputs/backend_codegen.json")
    # frontend = JsonLoader.load("outputs/frontend_codegen.json")

    # Backend
    for file in backend["generated_files"]:

        OutputWriter.write_file(f"project/backend/{file['path']}", file["content"])
        print(f"[BACKEND] Created: {file['path']}")

    # Frontend
    for file in frontend["generated_files"]:

        OutputWriter.write_file(f"project/frontend/{file['path']}", file["content"])
        print(f"[FRONTEND] Created: {file['path']}")

    return state