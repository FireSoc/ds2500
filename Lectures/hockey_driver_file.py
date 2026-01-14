'''
DS2500
Spring 2025
'''
import matplotlib.pyplot as plt
from hockeyteam import HockeyTeam
from utils import *

FILENAME = "pwhl_small.csv"

def plot_teams(teams):
    wins = [team.wins for team in teams]
    losses = [team.losses for team in teams]
    plt.scatter(wins, losses)
    plt.show()

def main():
    lst = read_csv(FILENAME)
    print(lst)

    # keeps the header
    lst2 = read_csv(FILENAME, skip = 0)
    print(lst2, "\n")

    teams = []
    for row in lst:
        team = HockeyTeam(row[0], row[2], row[3])
        print(team)
        teams.append(team)

if __name__ == "__main__":
    main()
