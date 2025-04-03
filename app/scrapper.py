from bs4 import BeautifulSoup
import requests
from typing import Dict


def valid_links(site: str) -> Dict[str, str]:
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")

    links = {}

    for link in soup.find_all("a"):
        link_address = link.get("href")
        link_text = link.string or "No text"

        if link_address:
            links[link_address] = link_text

    return links
