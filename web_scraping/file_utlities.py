import os
import yaml


def project_directory():
    current_file = __file__  # ../project/app/app.py
    app_folder = os.path.dirname(current_file)  # ../project/app
    project_folder = os.path.dirname(app_folder)  # ../project
    return project_folder

def write_yaml_to_data_folder(dictionary, path):
    with open(path, 'w') as file:
        yaml.dump(dictionary, file)
    print(f"writing to {path}")
    return
