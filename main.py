# python_version == 3.8.0

import time

from inputimeout import TimeoutOccurred, inputimeout

import shortdoc as sd
from functions import *

#                  ---   INPUTS   ---

def main():
    print(sd.welcome)
    time.sleep(3)
    while True:
        try:
            option = int(inputimeout(sd.inp, 30))
            if option == 1:
                while True:
                    option_sub_a = int(inputimeout(sd.inp1, 30))
                    if option_sub_a == 1:
                        print(city_dict())
                        time.sleep(0.5)
                        break
                    elif option_sub_a == 2:
                        name = str(inputimeout("\nEnter City name: ", 30))
                        where = str(inputimeout(
                            "\nEnter any one of these options [OPTION NAME ONLY]:\n - Coordinates\n - Population\n - Both\n", 30))
                        print(city_by(name.lower(), where.lower()))
                        time.sleep(0.5)
                        break
                    elif option_sub_a == 3:
                        print(cities())
                        time.sleep(0.5)
                        break
                    elif option_sub_a == 4:
                        print("◄ Going back...")
                        time.sleep(2)
                        break
                    else:
                        print("\n --- Invalid Option, Going Back ---")
            elif option == 2:
                while True:
                    option_sub_b = int(inputimeout(sd.inp2, 30))
                    if option_sub_b == 1:
                        option_series_a = int(inputimeout(sd.inp2_a, 30))
                        if option_series_a == 1:
                            print(S1 := city_series("population"))
                            time.sleep(0.5)
                            option_sub_b_1 = str(inputimeout(
                                sd.seriesq1, 30))
                            if option_sub_b_1.lower() == "no":
                                print("◄ Okay, going back...")
                                time.sleep(2)
                                break
                            elif option_sub_b_1.lower() == "yes":
                                what = str(inputimeout(
                                    "\nEnter the name of a city: ", 30))
                                print(
                                    f"The population of {what} is {S1.at[what.lower()]}.")
                                time.sleep(0.5)
                                break
                            else:
                                print("Exiting because wrong option was provided.")
                                time.sleep(1)
                                break
                        if option_series_a == 2:
                            print(S1 := city_series("coordinates"))
                            time.sleep(0.5)
                            option_sub_b_2 = str(inputimeout(
                                sd.seriesq2, 30))
                            if option_sub_b_2.lower() == "no":
                                print("◄ Okay, going back...")
                                time.sleep(2)
                                break
                            elif option_sub_b_2.lower() == "yes":
                                what = str(inputimeout(
                                    "\nEnter the name of a city: ", 30))
                                print(
                                    f"The coordinates of {what} is {S1.at[what.lower()]}.")
                                time.sleep(0.5)
                                break
                            else:
                                print("Exiting because wrong option was provided.")
                                time.sleep(1)
                                break
                        elif option_series_a == 3:
                            print("◄ Going back...")
                            time.sleep(2)
                            break
                        else:
                            print("\n --- Invalid Option, Going Back ---")
                            time.sleep(2)
                    elif option_sub_b == 2:
                        print(DF1 := city_dataframe())
                        time.sleep(0.5)
                        option_dataframe_a = int(inputimeout(sd.inp2_b, 30))
                        if option_dataframe_a == 1:
                            option_sub_b_2 = str(inputimeout(
                                "Enter the name of the city you are interested in: ", 30))
                            print(DF1.loc[option_sub_b_2.lower()])
                            time.sleep(0.5)
                            break
                        if option_dataframe_a == 2:
                            start = time.monotonic()
                            print("\nDataFrame Index: ", DF1.index)
                            print("\nDataFrame Columns:", DF1.columns)
                            print("\nDataFrame DTypes: ", DF1.dtypes)
                            print("\nDataFrame Values: ", DF1.values)
                            print("\nDataFrame Axes: ", DF1.axes)
                            print("\nDataFrame NDim: ", DF1.ndim)
                            print("\nDataFrame Size: ", DF1.size)
                            print("\nDataFrame Shape: ", DF1.shape)
                            print("\nDataFrame Keys: ", DF1.keys())
                            print("\nDataFrame DTypes: ", DF1.dtypes)
                            print(
                                f"\n--- 10 details fetched and printed in {time.monotonic()-start} seconds!")
                            time.sleep(0.5)
                            break
                        if option_dataframe_a == 3:
                            print("◄ Going back...")
                            time.sleep(2)
                            break
                        else:
                            print("\n --- Invalid Option, Going Back ---")
                            time.sleep(2)
                    elif option_sub_b == 3:
                        print("◄ Going back...")
                        time.sleep(2)
                        break
                    else:
                        print("\n --- Invalid Option, Going Back ---")
                        time.sleep(2)
            elif option == 3:
                while True:
                    option_pyplot_1 = int(inputimeout(sd.inp3, 15))
                    if option_pyplot_1 == 1:
                        print(
                            "\nCreating line plot containing population details from year 2000, up until now.")
                        time.sleep(1)
                        hist_line().show()
                        break
                    if option_pyplot_1 == 2:
                        print(
                            "\nCreating pie chart containing population details from year 2000, up until now.")
                        time.sleep(1)
                        hist_pie().show()
                        break
                    if option_pyplot_1 == 3:
                        print(
                            "\nCreating bar graph containing population details from year 2000, up until now.")
                        time.sleep(1)
                        hist_bar().show()
                        break
                    if option_pyplot_1 == 4:
                        print(
                            "\nCreating scatter graph containing population details from year 2000, up until now.")
                        time.sleep(1)
                        hist_scatter().show()
                        break
                    if option_pyplot_1 == 5:
                        print("◄ Going back...")
                        time.sleep(2)
                        break
                    else:
                        print("\n --- Invalid Option, Going Back ---")
                        time.sleep(2)
            else:
                print("PEEPEE POOPOO MAX ULTRA")
        except TimeoutOccurred:
            print("Session Timed Out!")
            break
        except ValueError:
            print("Invalid.")
        except KeyError:
            print("Invalid.")


if __name__ == "__main__":
    main()
