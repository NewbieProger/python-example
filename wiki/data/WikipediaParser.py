import requests
from bs4 import BeautifulSoup
import re
from typing import Optional

from wiki.dto.wikipedia.PopularityLanguage import PopularityLanguage


def get_popularity_of_languages() -> list[PopularityLanguage]:
    url: str = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    response: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")

    rows_of_values: list[BeautifulSoup] = (
        soup.select_one("caption:contains('Programming languages used in most popular websites*')").find_parent("table")
        .find_all("tr")[1:])

    if not rows_of_values:
        raise ValueError("No rows_of_values found in the table 'Programming languages used in most popular websites'")

    popularity_languages_list: list[PopularityLanguage] = []
    for row in rows_of_values:
        columns: list[BeautifulSoup] = row.find_all("td")
        name: str = columns[0].text.strip()
        popularity_str: str = columns[1].text.strip().replace(',', '').replace('.', '')

        popularity_match = re.search(r'(\d+)', popularity_str)
        popularity: int = int(popularity_match.group(0)) if popularity_match else None

        if popularity is not None:
            popularity_languages_list.append(PopularityLanguage(name, popularity))

    return popularity_languages_list
