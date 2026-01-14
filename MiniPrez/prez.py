"""
DS2500
Mini Presentation
Savir Khanna and Melvin Cheng
"""
import csv
import matplotlib.pyplot as plt

DATAFILE = "Carbon_(CO2)_Emissions_by_Country.csv"
COUNTRY_COL = 0
REGION_COL = 1
DATES_COL = 2
KILOTONS_COL = 3
CAPITA_COL = 4

FIRST_YR = 1990
LAST_YR = 2020
TOP_N = 10

AFRICA = "Africa"
EU = "Europe"
AMERICA = "Americas"
ASIA = "Asia"
OCEANIA = "Oceania"

SALMON = "salmon"
SKYBLUE = "skyblue"

def readfile(filename):
    """ Parameters: filename (string)
        Returns: list of lists
        Description: Reads the data from a CSV file and stores it as a list of lists.
                 Skips the header row.
    """
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)  # using csv library to read data
        next(csvfile)  # skipping headers
        data = []  # creating empty list
        for line in csvfile:
            data.append(line)  # appending data from the csv file to a list
    return data

def converting_data(data, column_index_date, column_index_kilotons,
                    column_index_capita):
    """ Parameters: data (list of lists), column_index_date (int),
        column_index_kilotons (int), column_index_capita (int)
        Returns: list of lists
        Description: Converts the data in specified columns:
                 - Extracts the year from a full date string in the date column
                 - Converts the year to an integer
                 - Converts the kilotons and per capita emissions values to floats
    """
    for row in data:
        full_date = row[column_index_date]
        row[column_index_date] = (full_date.split("-")[2])
        row[column_index_date] = int(row[column_index_date])
        row[column_index_kilotons] = float(row[column_index_kilotons])
        row[column_index_capita] = float(row[column_index_capita])
    return data

def aggregate_data_per_year(data, region, value_col):
    """ Parameters:
        data (list of lists)
        region (string)
        Returns: dictionary
        Description: Creates a dictionary with years (1990-2019) as keys and
                 the total CO2 emissions (in kilotons) for the given region as values.
    """
    dct = {year: 0 for year in range(FIRST_YR, LAST_YR)}  # creating a dictionary
    for row in data:
        if row[REGION_COL] == region:  # checks if the region in the cell is the
            year = row[DATES_COL]  # same as parameter
            if FIRST_YR <= year < LAST_YR:
                dct[year] += row[value_col]  # appends the value of the
                # corresponding kiloton emissions to the dictionary
        elif region == "ALL":
            year = row[DATES_COL]  # same as parameter
            if FIRST_YR <= year < LAST_YR:
                dct[year] += row[value_col]
    return dct

def aggregate_data_per_country(data, value_col):
    """ Parameters: data (list of lists), value_col (int)
        Returns: dictionary
        Description: Aggregates the total emissions or per capita emissions for
                    each country. Creates a dictionary with country names as
                    keys and aggregated values as values.
    """
    lst = {}  # creating a dictionary
    for row in data:
        country = row[COUNTRY_COL]
        values = row[value_col]
        if country in lst:
            lst[country] += values
        else:
            lst[country] = values
    return lst

def axes_plt(xlst, ylst_1, ylst_2, color1, color2):
    """ Parameters:
        xlst (list)
        ylst_1 (list)
        ylst_2 (list)
        color1 (string)
        color2 (string)
        Returns: None
        Description: Creates a dual-axis plot showing total emissions and
                     emissions per capita over time. Labels the axes and
                     adds a title.
    """
    fig, ax1 = plt.subplots()

    ax1.plot(xlst, ylst_1, label="Total Emissions", color=color1)
    ax1.set_xlabel('Time (yr)')
    ax1.set_ylabel('Co2 Emissions (kT)')
    ax1.set_ylim(0, 35000000)
    plt.legend()

    ax2 = ax1.twinx()
    ax2.plot(xlst, ylst_2, label="Emissions per Capita", color=color2)
    ax2.set_ylabel('Co2 Emissions per Capita (kT)')
    ax2.set_ylim(0, 1000)
    fig.tight_layout()

    plt.title("Total Co2 Emissions vs Emissions per Capita")
    plt.legend()
    plt.show()

def main():
    years = [year for year in range(FIRST_YR, LAST_YR)]
    total_emissions = []
    total_emissions_capita = []

    # calling functions and storing values in variables
    data = readfile(DATAFILE)
    converted_data = converting_data(data, DATES_COL, KILOTONS_COL, CAPITA_COL)

    # calling functions to create axes plot
    dct_yearly_kilotons = aggregate_data_per_year(data, "ALL", KILOTONS_COL)
    dct_yearly_capita = aggregate_data_per_year(data, "ALL", CAPITA_COL)
    
    for keys in dct_yearly_kilotons:
        total_emissions.append(dct_yearly_kilotons[keys])

    for keys in dct_yearly_capita:
        total_emissions_capita.append(dct_yearly_capita[keys])

    axes_plt(years, total_emissions, total_emissions_capita, SKYBLUE, SALMON)

main()