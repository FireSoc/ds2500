'''
Savir Khanna
HW 2
DS 2500
Spring 2025
'''
import matplotlib.pyplot as plt

class Food:
    def __init__(self, name, hours, category, features,
                 rating, price, wait, proximity):
        '''
        Does: Instantiating the class with its appropriate parameters, name,
        hrs, category, features, rating, price, wait, proximity. The integer ones
        were converted to an int respectively when added to object.
        '''
        self.name = name
        self.hours = str(hours)
        self.category = str(category)
        self.features = features
        self.rating = int(rating)
        self.price = int(price)
        self.wait = int(wait)
        self.proximity = int(proximity)

    def get_rating(self):
        "Returns rating of object"
        return self.rating

    def get_name(self):
        "Returns name of object"
        return self.name

    def get_price(self):
        "Returns price of object"
        return self.price

    def get_wait_score(self):
        "Returns wait score of object"
        return self.wait

    def plot(self, color, label = "", marker = "o"):
        "Does: Plots a scatter point of an objects price vs rating"
        plt.scatter(self.price, self.rating, color = color, label = label, marker = marker)

    def distance(self, other):
        "Returns: The Euclidean distance between 2 objects"
        prox_diff = (other.proximity - self.proximity) ** 2
        rating_diff = (other.rating - self.rating) ** 2
        price_diff = (other.price - self.price) ** 2
        wait_diff = (other.wait - self.wait) ** 2
        total = prox_diff + rating_diff + price_diff + wait_diff
        total = total ** 0.5
        return total

    def compare_plot(self, other):
        "Does: Compares two objects features to each other through a bar graph"
        x = [1,2,3,4]
        y1 = [self.price, self.rating, self.wait, self.proximity]
        y2 = [other.price, other.rating, other.wait, other.proximity]
        plt.bar(x, y1, label = self.name, width = 0.3)
        plt.bar([i+0.3 for i in x], y2, label = other.name, width = 0.3)

    def __str__(self):
        "Does: Returns name of object when called"
        return f"{self.name}"

