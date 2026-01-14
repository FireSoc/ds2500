'''
Savir Khanna
HW 1
DS2500
Spring 2025
'''
import matplotlib.pyplot as plt
from team import Team
from utils import *

# defining constants of FILENAME and colors
FILENAME = "PWHL_goals_2023.csv"
COLORS = ["green", "aqua", "maroon", "blue", "purple", "red"]

def most_goals(total_goals, team_names):
    """
    :param total_goals: list of total goals from all teams
    :param team_names: list of team names
    Does: uses a for loop to find the max total goals scored
    and which team did it.
    :return: returns the name of the team with the max goals,
    and the max goals in question
    """
    max = -1
    for i in range(len(total_goals)):
        if total_goals[i] > max:
            max = total_goals[i]
            max_goals_name = team_names[i]
    return max_goals_name, max

def least_goals(total_goals, team_names):
    """
        :param total_goals: list of total goals from all teams
        :param team_names: list of team names
        Does: uses a for loop to find the minimum total goals scored
        and which team did it.
        :return: returns the name of the team with the min goals,
        and the min goals in question
        """
    min = 1000
    for i in range(len(total_goals)):
        if total_goals[i] < min:
            min = total_goals[i]
            min_goals_name = team_names[i]
    return min_goals_name, min

def find_avg(total_goals):
    """
    :param total_goals: list of total goals scored by each team
    :return: returns the average total goals scored as an int
    """
    total = 0
    for goal in total_goals:
        total += goal
    avg = total / len(total_goals) # grabs the length of the list for # of teams
    return int(avg)

def total_zero_goals(data):
    """
    :param data: 2D ist of the data of FILENAME
    :return: returns the total number of games with 0 goals scored
    """
    count = 0
    for row in data:
        for val in row[2:]: # row[2:] removes the team name and first blank that's unintentional
            if val == 0:
                count += 1
    return count

def plot_season(teams):
    """
    :param teams: a list of all the team objects: Boston, Toronto, etc.
    Does: Plots the graph of team's goals over the course of a season
    :return: Nothing
    """
    plt.figure()
    """
    we want to move the marker for every goal, so I use a for 
    loop to iterate through goals for each value in goals, add 
    to the x value and plot
    """
    for i in range(len(teams[0].goals)):
        for val in teams:
            val.move_next()
            val.draw()
        plt.legend()
        # setting limits and labels to plot
        plt.xlim(0,80)
        plt.ylim(0, 7)
        plt.yticks([])
        plt.xlabel("Total Goals")
        plt.ylabel("Teams")
        plt.pause(0.1)
        plt.show()

def create_teams(team_names, data):
    """
    :param team_names: A list of all the team names
    :param data: 2D list of all the data from FILENAME
    :return: returns a list of team objects and a list of total_goals
    """
    # defining the lists to be used and later returned
    teams = []
    total_goals = []
    split_team_names = []

    # splitting team names to use the first or second word
    for j in range(len(team_names)):
        split_team_names.append(team_names[j].split())
        if len(split_team_names[j]) == 3: # for New York to concatenate into one string
            split_team_names[j][0] = split_team_names[j][0] + " " + split_team_names[j][1]
    for i in range(len(team_names)):
        # using a for loop to create each team with appropriate names, y values, and color
        team = Team(name = split_team_names[i][0], y = i + 1, color = COLORS[i])
        goals = data[i][2:]
        for goal in goals:
            team.add_goals(int(goal)) # appending the goals from data into goals list
        total_goals.append(team.get_total_goals()) # adding all total goals into a list for later use
        teams.append(team)
    return teams, total_goals

def main():
    """
    Calling the read_csv func to read the data from utils.py
    Creating 3 lists of team_names, the teams, and the total_goals
    All of these lists are used in the subsequent functions to answer questions
    """

    data = read_csv(FILENAME, 1)
    team_names = find_team_names(data)
    teams, total_goals = create_teams(team_names, data)

    """
    Answering all questions through calling the functions:
    most_goals, least_goals, total_zero_goals, avg_goals
    Assigned one or two variables to their func return and printed
    """
    max_goals_name, max_goals = most_goals(total_goals, team_names)
    print("The team that scored the most goals in 2023 is the ", max_goals_name, ".", sep = "")

    min_goals_name, min_goals = least_goals(total_goals, team_names)
    print("The fewest number of total goals scored was", min_goals, "goals.")

    zero_goals_total = total_zero_goals(data)
    print("A team scored zero total points in", zero_goals_total, "games.")

    avg_goals = find_avg(total_goals)
    print("The average number of total goals scored by all teams is", avg_goals, "goals.")

    # Calling the plot_season function with parameter teams list
    plot_season(teams)

if __name__ == "__main__":
    main()