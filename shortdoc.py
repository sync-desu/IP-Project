welcome = """
Welcome to this awesome data representation program. All the data in this program is scraped from "https://worldpopulationreview.com/countries/cities/india", which shows the population of all cities in India as of now, along with the latitudes and longitudes of that city.
In a few seconds, you will be prompted with a few options to choose from."""

inp = """
You can choose any one of these options given below to play around with the data!
1. Display raw city data in list/dictionary format.
2. Display raw city data in a series/dataframe.
3. Display raw population data from 2000 up until today in the form of a bar/line/pie/scatter chart.
4. Exit.
--- Enter your choice ---
"""

inp1 = """
You have chosen option 1, Display raw data in list/dictionary format.
You now have the following options to choose from:
1. Display raw city data, with indent {DICT}.
2. Display city name along with "x" where x can be coordinates, population or both, with indent {DICT}.
3. Display only the names of the cities [LIST].
4. Go back.
--- Enter your choice ---
"""

inp2 = """
You have chosen option 2, Display raw data in a series/dataframe.
You now have the following options to choose from:
1. Make a Series Object.
2. Make a DataFrame Object containing all city names, coordinates and population.
3. Go back.
--- Enter your choice ---
"""

inp2_a = """
- You have chosen to make a Series Object. You now have the following options:
1. Make a Series Object from city names and their population.
2. Make a Series Object from city names and their coordinates.
3. Go back.
--- Enter your choice ---
"""

seriesq1 = """
Series object created successfully! Do you want to display population of a city using Series attribute?
 - Yes
 - No
"""

seriesq2 = """
Series object created successfully! Do you want to display coordinates of a city using Series attribute?
 - Yes
 - No
"""

inp2_b = """
DataFrame object created successfully! Which of the following actions would you like to perform on the DataFrame?
1. Display coordinates and population details from city name.
2. Display DataFrame details.
3. Do nothing, go back.
--- Enter your choice ---
"""

inp3 = """
You have chosen option 3, Display population data from 2000 in the form of a bar/line/pie/scatter chart.
You now have the following options to choose from:
1. Make a line plot showing population from year 2000, up until now.
2. Make a pie chart showing population from year 2000, up until now.
3. Make a bar graph showing population from year 2000, up until now.
4. Make a scatter chart showing population from year 2000, up until now.
5. Go back.
--- Enter your choice ---
"""
