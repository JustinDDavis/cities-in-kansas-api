def load_data_file(name):
    with open('data/ks_cities.txt', 'r') as file:
        data = []
        for file_line in file:
            data.append(file_line.rstrip())
        return data