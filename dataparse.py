import json

import requests
from bs4 import BeautifulSoup


def make_request():
    res = requests.get(
        "https://worldpopulationreview.com/countries/india-population")
    return res.content.decode()


def parse_data():
    data = make_request()
    soup = BeautifulSoup(data, "html.parser")
    soup_data = soup.find("script", {"id": "__NEXT_DATA__"})
    soup_data = soup_data.find(text=True)
    soup_data = soup_data.strip()
    soup_data = json.loads(soup_data)
    return soup_data["props"]["pageProps"]


city_data = {}
for item in parse_data()["cities"]["cities"]:
    city_data[item["name"].lower()] = {
        "coordinates": f"{item['latitude']}°N, {item['longitude']}°E",
        "population": f"{item['2022']}"
    }

history_data = {}
for item in parse_data()["history"]:
    if item["Year"] < 2000:
        continue
    history_data[item["Year"]] = round(item['TotalPopulation']*1000)
