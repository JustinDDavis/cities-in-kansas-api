import yaml
import os

def join_images_to_city_name(city_payload, image_mappings):
    for city in city_payload:
        # Get the county value from the list.
        print(city)
        image = [image for image in image_mappings if image["name"] == city["name"]][0]
        print(image)
        image_data = {
            "image_url": image["image_url"]
        }
        city.update(image_data)
    return city_payload

def join_population_to_city_name(city_payload, population_mappings):
    for city in city_payload:
        # Get the county value from the list.
        print(city)
        population = [population for population in population_mappings if population["name"] == city["name"]][0]
        print(population)
        population_data = {
            "population": population["population"].replace(',', '')
        }
        city.update(population_data)
    return city_payload

def join_county_to_city_name(county_mappings, list_of_cities):
    city_payload = []
    # Loop through all the cities add and their respective county mapping to the list.
    for city in list_of_cities:
        # Get the county value from the list.
        print(county_mappings)
        county = [county for county in county_mappings if county["name"] == city][0]
        print(county)
        test = {
            "name": city,
            "county": county["county"].split(",")[0]
        }
        city_payload.append(test)
    return city_payload

def _project_directory():
    current_file = __file__  # ../project/app/app.py
    app_folder = os.path.dirname(current_file)  # ../project/app
    project_folder = os.path.dirname(app_folder)  # ../project
    return project_folder

def _join_city_and_county_mapping(city_data, county_mappings):
    city_data = city_data['data']
    county_mappings = county_mappings['data']

    for city in city_data:
        county_mapping_valune = county_mappings[city['county']]
        city.update(county_mapping_valune)

    data = {
        "data": city_data
    }
    return data


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

#
project_folder = _project_directory()
list_of_cities = load_yaml_data_file(f"{project_folder}/data/ks_cities.yaml")["data"]

# Join list of cities and add Counties
county_mappings = load_yaml_data_file(f"{project_folder}/data/ks_cities_to_county_mappings.yaml")["data"]
city_payload = join_county_to_city_name(county_mappings, list_of_cities)

# Join list with population
population_mappings = load_yaml_data_file(f"{project_folder}/data/ks_cities_to_population_mappings.yaml")["data"]
city_payload = join_population_to_city_name(city_payload, population_mappings)

# Join list with image
image_mappings = load_yaml_data_file(f"{project_folder}/data/ks_cities_to_image_mappings.yaml")["data"]
city_payload = join_images_to_city_name(city_payload, image_mappings)

# Join list with county Region
region_mappings = load_yaml_data_file(f"{project_folder}/data/ks_cities_to_county_region_mapping.yaml")["data"]

# Add the Region
for city in city_payload:
    city.update(region_mappings[city["county"]])

# Add Wikipedia Link
for city in city_payload:
    wikipedia = {
        "wikipedia": f"https://en.wikipedia.org/wiki/{city['name']},_Kansas"
    }

    city.update(wikipedia)

def merged_city_data():
    return city_payload

