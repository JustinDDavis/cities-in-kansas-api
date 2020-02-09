from web_scraping.file_utlities import project_directory

def load_data_file(name):
    print("Data file")
    data_file = f"{name}"
    print(data_file)
    data = []
    with open(data_file, 'r') as file:
        for file_line in file:
            data.append(file_line.rstrip())
    return data

# List of Cities:
list_of_cities = load_data_file(project_directory() + f"/data/ks_cities.txt")
mapping_of_cities_to_counties = {
    "data" : []
}

for city in list_of_cities[:5]:
    print(city)