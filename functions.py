import json

import matplotlib.pyplot as plt
import pandas as pd


from dataparse import city_data, history_data

#          --- CITY DATA FUNCTIONS ---

def city_dict():
    return json.dumps(city_data, indent=4, ensure_ascii=False)


def city_by(name: str, what: str):
    if what.lower() == "both":
        return json.dumps({f"{name.lower()}": city_data[name.lower()]}, indent=4, ensure_ascii=False)
    return json.dumps({f"{name.lower()}": {f"{what.lower()}": f"{city_data[name.lower()][what.lower()]}"}}, indent=4, ensure_ascii=False)


def cities():
    return [x for x in city_data]


def city_series(what: str):
    tuples = [(x, city_data[x][what]) for x in city_data]
    return pd.Series(data=[item[1] for item in tuples], index=[item[0] for item in tuples])


def city_dataframe():
    reconstructed_data = {
        "coordinates": [city_data[x]["coordinates"] for x in city_data],
        "population": [city_data[x]["population"] for x in city_data]
    }
    DF1 = pd.DataFrame(data=reconstructed_data, index=city_data.keys())
    return DF1


#          --- HISTORY DATA FUNCTIONS ---

def hist_line():
    plt.plot([x for x in history_data], [history_data[x]
             for x in history_data])
    plt.xlabel("Year")
    plt.ylabel("Population (in billions)")
    plt.grid()
    return plt


def hist_pie():
    plt.pie([history_data[x] for x in history_data],
            labels=[x for x in history_data])
    return plt


def hist_bar():
    plt.bar([x for x in history_data], [history_data[x] for x in history_data])
    plt.xlabel("Year")
    plt.ylabel("Population (in billions)")
    return plt


def hist_scatter():
    plt.scatter([x for x in history_data], [history_data[x]
                for x in history_data], color="r")
    plt.xlabel("Year")
    plt.ylabel("Population (in billions)")
    return plt
