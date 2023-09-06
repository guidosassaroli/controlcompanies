import os
import json

def read_json_files(folder_path):
    json_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), 'r') as f:
                json_data[filename] = json.load(f)
    return json_data

def create_table_from_json(json_data):
    table_header = "| Key | Value |\n| --- | ----- |\n"
    table_content = ""
    for key, value in json_data.items():
        if isinstance(value, list):
            value = ", ".join(value)
        table_content += f"| {key} | {value} |\n"
    return table_header + table_content

def update_readme(json_data):
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Update the README.md content based on the json_data
    new_content = "## Updated Data\n\n"
    for filename, data in json_data.items():
        table = create_table_from_json(data)
        new_content += f"### {filename}\n\n{table}\n"

    # Replace a specific section or append to the README. This example appends.
    updated_readme_content = readme_content + "\n" + new_content

    with open("README.md", "w") as f:
        f.write(updated_readme_content)

if __name__ == "__main__":
    folder_path = "data"
    json_data = read_json_files(folder_path)
    update_readme(json_data)
