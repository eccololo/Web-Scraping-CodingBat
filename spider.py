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


end = time.time()
print(f"Scraping process finished succesfully in {round(end - start, 2)} seconds!")
