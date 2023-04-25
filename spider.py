from bs4 import BeautifulSoup
import requests
import json
from fake_useragent import UserAgent
import time

start = time.time()
base_url = "https://codingbat.com"

end = time.time()
print(f"Scraping process finished succesfully in {round(end - start, 2)} seconds!")