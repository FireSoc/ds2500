'''
    Ds2500
    Spring 2025
    Sample code from lecture 1/24/25

    Driver to create food objects and compute Hamming distance

    our goal today:
    - read in CSV file to a 2d list
    - create 5-10 Food objects
    - compute the Hamming distance from those objects to B.Good
    - just print them out
'''
from utils import *
from food import Food
import csv

FOOD_FILE = "food_rankings.csv"

def main():
    # create a Food object to represent B.Good :(
    # name, price, category are required in the constructor
    bgood = Food("B.Good", 2, "American", feats = "vegan options and good for takeout")

    # read in from the CSV file into a 2d list
    lst = read_csv(FOOD_FILE)
    print(lst)

    # Iterate over SOME of my 2d list and compute distances to B.Good
    for i in range(5):
        row = lst[i]
        food = Food(row[0], row[2], row[-2], feats = row[-1])
        dist = food.hamming_dst(bgood)
        print(f"Distance from {food} to {bgood} is..... {dist}")

if __name__ == "__main__":
    main()