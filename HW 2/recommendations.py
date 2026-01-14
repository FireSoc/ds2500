'''
Savir Khanna
HW 2
DS 2500
Spring 2025
'''

# importing libraries and defining constants
import statistics
import matplotlib.pyplot as plt
from food import Food
from utils import *
FILENAME = "food_rankings.csv"

def remove_dup(data):
    """
    :param data: 2D list of dataset
    :return: Checks for duplicates in data and returns data without duplicates
    """
    converted_data = []
    for row in data:
        count = False
        for row2 in converted_data:
            if row[0] == row2[0]:
                count = True
        if not count:
            converted_data.append(row)
    return converted_data

def foods_lst(data):
    """
    :param data: 2D list of dataset
    :return: A list of objects from class Food in file food
    """
    foods = []
    for row in data:
        name = row[0]
        rating = row[1]
        price = row[2]
        wait = row[3]
        proximity = row[4]
        hours = row[5]
        category = row[6]
        features = row[7]

        food = Food(name, hours, category, features,
                    rating, price, wait, proximity)
        foods.append(food)
    return foods

def mean_rating(foods):
    """
    :param foods: List of food class objects for each restaurant in dataset
    :return: The average rating of all restaurants
    """
    total = 0
    for food in foods:
        total += food.get_rating()
    avg = total / len(foods)
    return avg

def median_prices(foods):
    """
    :param foods: List of food class objects for each restaurant in dataset
    :return: The median price of all of the objects in foods
    """
    prices = [food.get_price() for food in foods]
    median = statistics.median(prices)
    return median

def laney_dists(laney, foods):
    """
    :param laney: Food class object defined as laney
    :param foods: List of food class objects for each restaurant in dataset
    :return: the minimum Euclidean distance of all restaurants from laney,
    including that restaurants name
    """
    laney_dist_val = []
    laney_dist_names = []
    min = 100
    for food in foods:
        laney_dist_val.append(laney.distance(food))
        laney_dist_names.append(food.get_name())
    for i in range(len(laney_dist_val)):
        if laney_dist_val[i] < min:
            min = laney_dist_val[i]
            name = laney_dist_names[i]
    return min, name

def wait_score(foods):
    """
    :param foods: List of food class objects for each restaurant in dataset
    :return: Total amount of restaurants with wait score above or equal 3
    """
    total = 0
    for food in foods:
        if food.get_wait_score() >= 3:
            total += 1
    return total

def laney_graph(foods, laney):
    """
    :param foods: List of food class objects for each restaurant in dataset
    :param laney: Food class object defined as laney
    :Does: plots a graph of price vs rating of laney vs all restaurants
    """
    for food in foods:
        food.plot("blue")
    laney.plot("red", "Laney's Restaurant", "+")
    plt.legend()
    plt.title("Price vs Rating for Restaurants")
    plt.xlabel("Price")
    plt.ylabel("Rating")
    plt.show()

def compare_restaurants_graph(foods, restaurant1, restaurant2):
    """
    :param foods: List of food class objects for each restaurant in dataset
    :param restaurant1: string of a restaurant name in dataset
    :param restaurant2: string of a 2nd restaurant name in dataset
    Does: Plots a graph comparing all features of 2 restaurants,
    uses .compare_plot from Food class to plot bar graphs and all labeling happens here
    :return: None
    """
    for food in foods:
        for food2 in foods:
            if restaurant1 == food.get_name() and restaurant2 == food2.get_name():
                food.compare_plot(food2)
                plt.title(f"{food} vs {food2}")
                plt.xticks([1.15,2.15,3.15,4.15], ["Price", "Rating", "Wait", "Proximity"])
                plt.ylim(0, 5)
                plt.xlabel("Restaurant Features")
                plt.ylabel("Score: 1-5")
                plt.legend()
                plt.show()

def euclidean_dist(foods, restaurant1, restaurant2):
    """
    :param foods: List of food class objects for each restaurant in dataset
    :param restaurant1: string of a restaurant name in dataset
    :param restaurant2: string of a 2nd restaurant name in dataset
    :return: the euclidean distance between two restaurants
    """
    for food in foods:
        for food2 in foods:
            if restaurant1 == food.get_name() and restaurant2 == food2.get_name():
                dist = food.distance(food2)
    return dist

def main():
    # reading and converting data + creating lst of food objects
    data = read_csv(FILENAME, 1)
    new_data = name_conversion(data)
    converted_data = remove_dup(new_data)
    foods = foods_lst(converted_data)

    laney = Food("B.good","8am-7pm", "American",
                 "vegan friendly", 5, 2, 4, 1)

    # Solving all respective questions using previously defined functions
    avg_rating = mean_rating(foods)
    print("The mean rating of all restaurants is ", round(avg_rating, 3), ".", sep="")

    median = median_prices(foods)
    print("The median of prices is ", median, ".", sep="")

    restaurants_wait = wait_score(foods)
    print("The number of restaurants wait score of 3 or above is", restaurants_wait, "restaurants.")

    min_dist, min_name = laney_dists(laney, foods)
    print("The minimum distance is ", round(min_dist, 3), " and the name of the place is ",
          min_name, ".", sep="")

    # Asking for input for 2 restaurants to use in Euclidean distance and to compare
    restaurant1 = input("Name a restaurant.")
    restaurant2 = input("Name another restaurant.")

    restaurant_dist = euclidean_dist(foods, restaurant1, restaurant2)
    print("The Euclidean distance between ", restaurant1, " and ",
          restaurant2, " is ", round(restaurant_dist, 3), ".", sep="")

    # Calling graphing functions for the laney comparison graph and 2 restaurants comparison
    laney_graph(foods, laney)
    compare_restaurants_graph(foods, restaurant1, restaurant2)

if __name__ == "__main__":
    main()