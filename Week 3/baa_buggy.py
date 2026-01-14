
import matplotlib.pyplot as plt

from utils import read_csv, lst_to_dct

FILENAME = "boston_marathon_2023.csv"
BIB_HEADER = "BibNumber"
AGE_HEADER = "AgeOnRaceDay"
RANK_HEADER = "RankOverall"
GENDER_HEADER = "Gender"
TIME_HEADER = "OfficialTime"


def filter_age(target_age, ages, times):
    ''' given a target age, a list of ages, and a list of times,
        filter and return a list of times for runners who are the given
        age OR OLDER
    '''
    filtered_times = []
    for i in range(len(ages)):
        if ages[i] >= target_age:
            filtered_times.append(times)
    return filtered_times


def main():
    # Gather data - read in the MBTA speed restrictions as a 2d list
    # and then convert to a dictionary where keys come from the header
    data = read_csv(FILENAME, skip = 0)
    dct = lst_to_dct(data)
    print(dct)

    # pull out a list of ages
    ages = dct[AGE_HEADER]
    print(f"Ages before loop {ages}")
    for i in range(len(ages)):
        print(f"Ages inside loop {ages}")
        ages[i] = int(ages[i])
    print(f"Ages of runners in 2023: {ages}")

    # filter to keep everyone older than me
    master_times = filter_age(45, ages, dct[TIME_HEADER])
    print(f"Times of everyone 45 or older: {master_times}")

if __name__ == "__main__":
    main()