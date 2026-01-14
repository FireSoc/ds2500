"""
DS2500
Savir Khanna
HW 4 - Pandas, Numpy, and graphs
March 23rd
"""
import numpy as np
import matplotlib.pyplot as plt
import haversine as hs
from utils import *

# defining constants
STATIONS = "stations.csv"
TEMP = "temp.csv"
stations_header = ["Station ID", "Weather ID", "Lat", "Long"]
temp_header = ["Station ID", "Weather ID", "Month", "Day", "Temp"]
CAPE_CANAVERAL_COORDS = (28.396837, -80.605659)
COLORS = [
    [255, 0, 0],
    [255, 69, 0],
    [255, 140, 0],
    [255, 215, 0],
    [173, 255, 47],
    [0, 255, 0],
    [0, 206, 209],
    [0, 191, 255],
    [30, 144, 255],
    [0, 0, 255]
]


def haversine_dist(lst, loc2):
    """
       Calculate the Haversine distance between a list of coordinates and a given location.
       param: lst: List of coordinates (tuples)
       param: loc2: Tuple representing the target location (latitude, longitude)
       returns: List of Haversine distances for each coordinate in lst
       """
    hs_dist_lst = []
    for val in lst:
        hs_dist = hs.haversine(val, loc2)
        hs_dist_lst.append(hs_dist)
    return hs_dist_lst

def global_coordinates(df):
    """
        param: df: DataFrame containing columns 'Lat' and 'Long'
        returns: coords_lst: list of tuples where each tuple represents coordinates (latitude, longitude)
        does: Converts the 'Lat' and 'Long' columns of the DataFrame into a list of coordinate tuples
        """
    lat = df["Lat"].tolist()
    long = df["Long"].tolist()
    coords_lst = []
    for i in range(len(lat)):
        tup = (float(lat[i]), float(long[i]))
        coords_lst.append(tup)
    return coords_lst

def filter_df(df, col1, val1, num=1, col2="", val2=0):
    """
    Filters dataframes based off values
    :param: dataframe to be filtered, and optional columns and values
    :returns: filtered df
    """
    if num == 1:
        df = df[(df[col1] == val1)]
    if num == 2:
        df = df[(df[col1] == val1) & (df[col2] == val2)]
    return df

def plot_mean_temp_jan(df_station, df_temp):
    """
    param: df_station: DataFrame containing station information
    param: df_temp: DataFrame containing temperature data
    returns: None
    does: Plots the mean temperature per day for all stations in January
    """
    station_ids = [df_station.loc[i, "Station ID"] for i in range(len(df_station))]
    mean_temp_list = []
    df_filtered_temp = pd.DataFrame()

    for val in station_ids:
        df_new_temp = filter_df(df_temp, "Month", 1, 2, "Station ID", val2=val)
        df_filtered_temp = pd.concat([df_filtered_temp, df_new_temp])

    for val in range(len(df_filtered_temp["Day"])):
        df_temp_per_day = filter_df(df_filtered_temp, "Day", val)
        mean_temp_per_day = df_temp_per_day["Temp"].mean()
        if mean_temp_per_day != 0:
            mean_temp_list.append(mean_temp_per_day)
    plt.plot(mean_temp_list)
    plt.ylabel("Temperature (F)")
    plt.xlabel("Day")
    plt.title("Mean Temperature Per Day of all Weather Stations near Cape Canaveral")
    plt.show()

def plot_all_temp(df_temp, df_stations):
    """
        param: df_temp: DataFrame containing temperature data
        param: df_stations: DataFrame containing station information
        returns: None
        does: Creates a grid and assigns colors based on temperature values for stations and plots them
        """
    grid = np.full((100, 150, 3), 245, dtype=int)
    df_stations = df_stations[(df_stations["Lat"] <= 50) & (df_stations["Lat"] >= 25)]
    df_stations = df_stations[(df_stations["Long"] <= -65) & (df_stations["Long"] >= -125)]
    df_temp = df_temp[(df_temp["Day"] == 28) & (df_temp["Month"] == 1)]

    df_stations.reset_index(drop=True, inplace=True)
    df_temp.reset_index(drop=True, inplace=True)
    df_filtered_temps = df_stations.merge(df_temp, on='Station ID', how='inner')
    df_filtered_temps.reset_index(drop=True, inplace=True)

    for i in range(len(df_filtered_temps)):
        lat = df_stations.loc[i, "Lat"]
        long = df_stations.loc[i, "Long"]
        col = (long - -125) / (-65 - (-125)) * 150
        row = (lat - 25) / (50 - 25) * 100
        row = 100 - row
        temp = df_filtered_temps.loc[i, "Temp"]
        if temp >= 90:
            grid[round(row), round(col)] = COLORS[0]
        elif 80 <= temp < 90:
            grid[round(row), round(col)] = COLORS[1]
        elif temp >= 70 and temp < 80:
            grid[round(row), round(col)] = COLORS[2]
        elif temp >= 60 and temp < 70:
            grid[round(row), round(col)] = COLORS[3]
        elif temp >= 50 and temp < 60:
            grid[round(row), round(col)] = COLORS[4]
        elif temp >= 40 and temp < 50:
            grid[round(row), round(col)] = COLORS[5]
        elif temp >= 30 and temp < 40:
            grid[round(row), round(col)] = COLORS[6]
        elif temp >= 20 and temp < 30:
            grid[round(row), round(col)] = COLORS[7]
        elif temp >= 10 and temp < 20:
            grid[round(row), round(col)] = COLORS[8]
        elif temp >= 0 and temp < 10:
            grid[round(row), round(col)] = COLORS[9]

    plt.imshow(grid)
    plt.title("All Temperatures on January 28 in USA")
    plt.show()

def main():
    df_stations = read_file(STATIONS, stations_header)
    df_temp = read_file(TEMP, temp_header)

    print("The shape of stations.csv is", df_stations.shape)

    df_stations = df_stations.dropna()
    df_stations = df_stations.drop(0).reset_index(drop=True)
    df_temp = df_temp.dropna()

    stations_coords_lst = global_coordinates(df_stations)
    haversine_dist_lst = haversine_dist(stations_coords_lst, CAPE_CANAVERAL_COORDS)
    df_stations["Haversine Dist_Cape"] = haversine_dist_lst

    df_filtered_temp = filter_df(df_temp, "Month", 1, 2, "Station ID", 722040)
    min_temp_jan = df_filtered_temp["Temp"].min()
    print("The mininum at Weather Station 722040 throughout January is",
          round(min_temp_jan,3), "Fahrenheit.")

    df_jan_28_temp = filter_df(df_temp, "Month", 1, 2, "Day", 28)
    mean_temp_jan_28 = df_jan_28_temp["Temp"].mean()
    print("The mean temperature throughout all weather stations on January 28th is",
          round(mean_temp_jan_28,3), "Fahrenheit.")

    df_km_100_cape_stations = df_stations[df_stations["Haversine Dist_Cape"] <= 100]
    stations_within_100 = len(df_km_100_cape_stations["Haversine Dist_Cape"])
    print("The number of stations within 100 km of Cape Canaveral is",
          stations_within_100, "stations.")

    df_km_100_cape_stations = df_km_100_cape_stations.reset_index(drop=True)
    plot_mean_temp_jan(df_km_100_cape_stations, df_temp)

    plot_all_temp(df_temp, df_stations)

main()