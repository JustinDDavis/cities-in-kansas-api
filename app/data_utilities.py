import yaml

def load_data_file(name):
    print("Data file")
    data_file = f"{name}"
    print(data_file)
    data = []
    with open(data_file, 'r') as file:
        for file_line in file:
            data.append(file_line.rstrip())
    return data

def load_yaml_data_file(name):
    print("load_yaml_data_file")
    data_file = f"{name}"
    print(data_file)
    data = None
    with open(data_file, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            print()
        except yaml.YAMLError as exc:
            print(exc)
    return data