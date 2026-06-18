import json
import os
from pathlib import Path

def update_codegen_json(project_dir, output_json_path, prefix=""):
    if not os.path.exists(output_json_path):
        print(f"Warning: {output_json_path} not found. Skipping.")
        return

    with open(output_json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            # Handle cases where it's a JSON string with markdown
            f.seek(0)
            raw_content = f.read()
            # Basic strip of quotes if it's a wrapped string
            if raw_content.startswith('"') and raw_content.endswith('"'):
                raw_content = json.loads(raw_content)
            
            clean_data = raw_content.strip()
            if clean_data.startswith("```"):
                lines = clean_data.split("\n")
                if lines[0].startswith("```"): lines = lines[1:]
                if lines[-1].startswith("```"): lines = lines[:-1]
                clean_data = "\n".join(lines).strip()
            data = json.loads(clean_data)

    if isinstance(data, str):
        # Double encoded case
        data = json.loads(data)

    generated_files = data.get("generated_files", [])
    updated_files = []
    
    # Create a map of existing paths in JSON
    json_files_map = {f["path"]: f for f in generated_files}

    # Walk through project directory
    for root, dirs, files in os.walk(project_dir):
        if any(ignore in root for ignore in ["node_modules", "__pycache__", "dist", ".git"]):
            continue
            
        for file in files:
            if not file.endswith(('.py', '.tsx', '.ts', '.css', '.html', '.json', '.sql')):
                continue
                
            full_path = Path(root) / file
            relative_path = os.path.relpath(full_path, project_dir).replace('\\', '/')
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if relative_path in json_files_map:
                json_files_map[relative_path]["content"] = content
                print(f"Updated in JSON: {relative_path}")
            else:
                updated_files.append({
                    "path": relative_path,
                    "content": content
                })
                print(f"Added to JSON: {relative_path}")

    # Combine updated and new files
    final_files = list(json_files_map.values()) + updated_files
    data["generated_files"] = final_files

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully synced {output_json_path}")

if __name__ == "__main__":
    # Sync Frontend
    update_codegen_json("project/frontend", "outputs/frontend_codegen.json")
    # Sync Backend
    update_codegen_json("project/backend", "outputs/backend_codegen.json")
