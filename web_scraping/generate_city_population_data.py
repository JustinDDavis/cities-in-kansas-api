import requests
import time
from bs4 import BeautifulSoup

from web_scraping.file_utlities import project_directory, write_yaml_to_data_folder


def load_data_file(name):
    print("Data file")
    data_file = f"{name}"
    print(data_file)
    data = []
    with open(data_file, 'r') as file:
        for file_line in file:
            data.append(file_line.rstrip())
    return data


def find_population(soup):
    population_table_cell = soup.find(text='Population')
    # Go to next cell.
    table_data = population_table_cell.parent.parent.next_sibling
    # for node in table_data.children:
    #     print(node)
    population = table_data.contents[1].text.strip()
    return population


def scrape_population_from_page(city_wikipedia_url):
    wikipedia_page = requests.get(city_wikipedia_url)
    webpage = wikipedia_page.content
    soup = BeautifulSoup(webpage, features="html.parser")

    try:
        population = find_population(soup)
        return population
    except Exception as e:
        print(e)

    return None


# List of Cities:
list_of_cities = load_data_file(project_directory() + f"/data/ks_cities.txt")
mapping_of_cities_to_population= {
    "data": []
}

current_count = 0
list_of_cities_count = len(list_of_cities)

for city in list_of_cities:
    # Wikipedia articles seem to follow this same structure
    wikipedia = f"https://en.wikipedia.org/wiki/{city},_Kansas"
    population = scrape_population_from_page(wikipedia)

    if population is None:
        wait_time = 5
        print(f"Wait to retry city... {wait_time} seconds")
        time.sleep(wait_time)
        population = scrape_population_from_page(wikipedia)

    if population is None:
        print(f"Unable to load {city}")
        continue

    print(f"{current_count} of {list_of_cities_count}",)
    current_count+=1

    mapping_of_cities_to_population["data"].append({
        'name': city,
        'population': population
    })

# Write object to Yaml file.
write_yaml_to_data_folder(mapping_of_cities_to_population, project_directory() + f"/data/ks_cities_to_population_mappings.yaml")