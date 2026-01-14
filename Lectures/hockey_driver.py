from hockeyteam import HockeyTeam

def main():
    fleet = HockeyTeam("Boston", 8, 9)
    sirens = HockeyTeam("New York", 5, 12)

    # plot the boston team!
    fleet.plot_team()
    sirens.plot_team()

    if fleet.is_better(sirens):
        print(f"{fleet} is better obviously")
    else:
        print(f"{sirens} cheated")


main()