'''
Savir Khanna
HW 1
DS2500
Spring 2025
'''
import matplotlib.pyplot as plt
class Team:
    def __init__(self, name, x = 0, y = 0, color = "purple"):
        '''
        Does: Instantiating the class with its appropriate parameters, including the name
        of the team, the x and y position of them on the graph, and the color of
        the points on the graph. In addition, every team object has their own
        list of goals.
        '''
        self.goals = []
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.color = color

    def draw(self):
        """
        Does: Plots the markers for goals for each team every game
        """
        plt.scatter(self.x, self.y, color = self.color, marker = ">",
                    label = self.name, s = 200)
        plt.title("Goals Scored over Time 2023-2024")

    def add_goals(self, goals):
        """
        Does: Adds goals to the list attached to the object from before,
        takes in parameter of goal
        """
        self.goals.append(goals)

    def get_total_goals(self):
        """
        Does: uses a for loop to count total goals
        Returns the total goals through for loop usage
        """
        total = 0
        for goal in self.goals:
            total += goal
        return total

    def move_next(self):
        """
        Does: Raises the x value of the marker to signal increase in goals
        Pops the value after adding it to remove from goals list
        """
        self.x += self.goals.pop(0)

    def __str__(self):
        """
        Does: change the called name of variable
        to the self.name instead of address
        Returns: the string representation of the team
        """
        return f"Team {self.name}, Total Goals: {self.get_total_goals()}"