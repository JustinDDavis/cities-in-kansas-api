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


def find_county(soup):

    # Exception Cities that have trouble:
    #   Andover (17) : Because it was Counties instead of County.
    #   Bern (54): retried and city picked up.
    #   Belpre (49): Picking another County instance before the table.

    county_table_cell = soup.find(text='County')
    # Go to next cell.
    if county_table_cell is None:
        # Try if the term is changed to plural.
        county_table_cell = soup.find(text='Counties')

    if county_table_cell.parent.parent.next_sibling is None:
        county_table_cell = [county for county in soup.findAll(text='County') if "List of counties" in str(county.parent)]
        if len(county_table_cell) != 1:
            return None
        county_table_cell = county_table_cell[0]

    # the majority of counties will be picked up this way:
    table_data = county_table_cell.parent.parent.next_sibling
    county = table_data.text.strip()

    return county


def scrape_county_name_from_page(city_wikipedia_url):
    wikipedia_page = requests.get(city_wikipedia_url)
    webpage = wikipedia_page.content
    soup = BeautifulSoup(webpage, features="html.parser")

    try:
        county = find_county(soup)
        return county
    except Exception as e:
        print(e)

    return None


# List of Cities:
list_of_cities = load_data_file(project_directory() + f"/data/ks_cities.txt")
mapping_of_cities_to_counties = {
    "data": []
}

current_count = 0
list_of_cities_count = len(list_of_cities)

for city in list_of_cities:
    # Wikipedia articles seem to follow this same structure
    wikipedia = f"https://en.wikipedia.org/wiki/{city},_Kansas"
    county_name = scrape_county_name_from_page(wikipedia)

    if county_name is None:
        wait_time = 5
        print(f"Wait to retry city... {wait_time} seconds")
        time.sleep(wait_time)
        county_name = scrape_county_name_from_page(wikipedia)

    if county_name is None:
        print(f"Unable to load {city}")
        continue

    print(f"{current_count} of {list_of_cities_count}",)
    current_count+=1

    mapping_of_cities_to_counties["data"].append({
        'name': city,
        'county': county_name
    })

# Write object to Yaml file.
write_yaml_to_data_folder(mapping_of_cities_to_counties, project_directory() + f"/data/ks_cities_to_county_mappings.yaml")