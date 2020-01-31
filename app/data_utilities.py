import os
cwd = os.getcwd()

def load_data_file(name):
    print("Data file")
    data_file = cwd + f"/data/{name}"
    print(data_file)
    with open(data_file, 'r') as file:
        data = []
        for file_line in file:
            data.append(file_line.rstrip())
        return data