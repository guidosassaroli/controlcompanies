import os
import json

def read_json_files(folder_path):
    json_data = {}
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".json") and filename != "_data_structure.json" and filename != "all_data.json":
            with open(os.path.join(folder_path, filename), 'r') as f:
                json_data[filename] = json.load(f)
    return json_data

def create_table_from_json(json_data):
    table_header = "| Name | Headquarter | Short Description | Tags |\n| ----- | ----------- | ----------------- | ---- |\n"
    table_content = ""
    for data in json_data.values():
        name = data.get("name", "N/A")
        if name == "":
            continue
        url = data.get("url", "N/A")
        headquarter = data.get("headquarter", "N/A")
        short_description = data.get("short_description", "N/A")
        tags = data.get("tags", [])
        tags_str = " - ".join(tags)
        
        table_content += f"| [{name}]({url}) | {headquarter} | {short_description} | {tags_str} |\n"
        
    return table_header + table_content

def update_readme(json_data):
    readme_content = """
[//]: # (DO NOT EDIT THIS FILE MANUALLY, USE THE GENERATOR AND DATA FOLDER)
# Awesome Control Companies

A list of high-tech control companies, with a focus on autonomous driving.

### Built and maintained by
* [Giulio Vaccari](https://github.com/giuliovv)
* [Guido Sassaroli](https://github.com/guidosassaroli)

### Control companies"""

    # Update the README.md content based on the json_data
    new_content = create_table_from_json(json_data)

    # Replace a specific section or append to the README. This example appends.
    updated_readme_content = readme_content + "\n" + new_content

    with open("README.md", "w") as f:
        f.write(updated_readme_content)

def generate_all_files(json_data, output_filename="data/all_data.json"):
    """Writes combined JSON data to a single file."""
    with open(output_filename, "w") as outfile:
        json.dump(json_data, outfile, indent=4)


if __name__ == "__main__":
    folder_path = "data"
    json_data = read_json_files(folder_path)
    update_readme(json_data)
    generate_all_files(json_data)
