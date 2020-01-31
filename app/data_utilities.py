import os
cwd = os.getcwd()

def load_data_file(name):
    print("Data file")
    print(cwd+'/data/ks_cities.txt')
    with open(cwd+'/data/ks_cities.txt', 'r') as file:
        data = []
        for file_line in file:
            data.append(file_line.rstrip())
        return data