"""
DS2500
1/14
"""
import matplotlib.pyplot as plt

class HockeyTeam:
    def __init__(self, city, w, l):
        self.city = city
        self.wins = int(w)
        self.losses = int(l)

    def plot_team(self):
        '''plot wins vs losses'''
        plt.bar(1, self.wins, color = "pink")
        plt.bar(2, self.losses, color = "magenta")
        plt.title(f"{self.city} Wins vs Losses 2023-2024")
        # xticks takes: list of positions, list of labels
        plt.xticks([1,2], ['Wins', 'Losses'])
        plt.show()

    def is_better(self, other):
        # is current team better than other team
        if self.wins/self.losses > other.wins / other.losses:
            return True
        return False

    def __str__(self):
        return self.city + "!"
