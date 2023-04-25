from bs4 import BeautifulSoup
import requests
import json
from fake_useragent import UserAgent
import time

start = time.time()
base_url = "https://codingbat.com"


def read_data_file(file_name):
    """Thi function read text from a text file and returns it."""
    file_x = open(file_name, "r")
    file_data = file_x.read()
    file_x.close()
    return file_data


def save_file_to_json(file_name, x_dataset):
    """This function saves dataset like a dict to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(x_dataset, f, indent=4, ensure_ascii=False)


def get_data_from_webpage(base_url):
    """This function is taking a website html content from a specific URL using requests lib."""
    user_agent = UserAgent()
    headers = {"user-agent": user_agent.chrome}
    response = requests.get(url=base_url, headers=headers)
    return response.text


data = get_data_from_webpage("https://codingbat.com/java")
soup = BeautifulSoup(data, "lxml")

table_tags = soup.find_all("table")

table_tags_set_1 = table_tags[2]
table_tags_set_2 = table_tags[3]

all_main_links = []
dataset_dict = {}

for table in table_tags_set_1:
    try:
        link = table.find("a")
        all_main_links.append(base_url + link["href"])
    except TypeError:
        pass

for table in table_tags_set_2:
    try:
        link = table.find("a")
        all_main_links.append(base_url + link["href"])
    except TypeError:
        pass

for x_idx, x_link in enumerate(all_main_links):
    x_idx += 1
    print(f"Fetching data from {x_idx} main website ...")
    time.sleep(1.3)
    data = get_data_from_webpage(x_link)
    soup = BeautifulSoup(data, "lxml")
    table_tags = soup.find_all("table")
    all_secondary_links = []
    table_links_to_tasks = table_tags[2]
    for table in table_links_to_tasks:
        try:
            link = table.find("a")
            all_secondary_links.append(base_url + link["href"])
        except TypeError:
            pass

end = time.time()
print(f"Scraping process finished succesfully in {round(end - start, 2)} seconds!")
