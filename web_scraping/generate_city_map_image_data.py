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


def find_image(soup):
        image_section = soup.findAll('img', alt=True)
        all_links = [image for image in image_section if "Incorporated" in str(image)]
        print()
        if len(all_links) == 1:
            return "https:" + all_links[0]["src"]
        else:
            return ''


def scrape_image_link_from_page(city_wikipedia_url):
    wikipedia_page = requests.get(city_wikipedia_url)
    webpage = wikipedia_page.content
    soup = BeautifulSoup(webpage, features="html.parser")

    try:
        image = find_image(soup)
        return image
    except Exception as e:
        print(e)

    return None


# List of Cities:
list_of_cities = load_data_file(project_directory() + f"/data/ks_cities.txt")
mapping_of_cities_to_map_image = {
    "data": []
}

current_count = 0
list_of_cities_count = len(list_of_cities)

for city in list_of_cities:
    # Wikipedia articles seem to follow this same structure
    wikipedia = f"https://en.wikipedia.org/wiki/{city},_Kansas"
    image_url = scrape_image_link_from_page(wikipedia)

    if image_url is None:
        wait_time = 5
        print(f"Wait to retry city... {wait_time} seconds")
        time.sleep(wait_time)
        image_url = scrape_image_link_from_page(wikipedia)

    if image_url is None:
        print(f"Unable to load {city}")
        continue

    print(f"{current_count} of {list_of_cities_count}",)
    current_count+=1

    mapping_of_cities_to_map_image["data"].append({
        'name': city,
        'image_url': image_url
    })
    print(image_url)

# Write object to Yaml file.
write_yaml_to_data_folder(mapping_of_cities_to_map_image, project_directory() + f"/data/ks_cities_to_image_mappings.yaml")