'''
    DS2500
    Spring 2025
    Sample code from lecture 1/21/25 - making a Food class to help Laney figure out
        where to eat lunch now that B.Good has closed

    Attributes:
        * name (nominal)
        * rating (discrete)
        * price (discrete)
        * wait (discrete)
        * hours (nominal)
        * category (nominal)
        * features (nominal)
        * proximity (discrete)

    Open questions:
    1. what do we do about duplicates?
    2. how do know if two objects are the same? If they have the same name

    Adding on for 1/24/25
    * individual attributes for vegan, takeout, quick
    * hamming distance method
'''

class Food:
    def __init__(self, name, price, cat, rating = 1, wait = 1,
                 hours = "", feats = "", prox = 1):
        self.name = name
        self.price = price
        self.category = cat
        self.rating = rating
        self.wait = wait
        self.hours = hours
        self.features = feats
        self.proximity = prox
        self.features = self.features.lower()
        self.create_subfeatures()

    def create_subfeatures(self):
        ''' look for vegan, takeout, quick in self.features and save as 0/1 attributes '''
        self.vegan = 0
        self.takeout = 0
        self.quick = 0
        if "vegan" in self.features or "vegetarian" in self.features:
            self.vegan = 1
        if "takeout" in self.features or "take-out" in self.features or "take out" in self.features:
            self.takeout = 1
        if "quick" in self.features or "fast" in self.features:
            self.quick = 1

    def __str__(self):
        ''' return a pretty string to represent the object '''
        return f"{self.name}, price scale: {self.price}"

    def __eq__(self, other):
        ''' return True if self == other '''
        return self.name == other.name

    def hamming_dst(self, other):
        ''' compute the hamming distance using vegan, takeout, quick attributes (0/1) '''
        dist = abs(self.vegan - other.vegan) + abs(self.takeout - other.takeout) + \
            abs(self.quick - other.quick)
        return dist