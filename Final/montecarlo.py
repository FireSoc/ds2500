import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load historical data (for demo, simulate)
def simulate(start_gap, sd, future_yrs, mean_change=0):
    np.random.seed(42)
    num_simulations = 1000
    simulations = []

    for i in range(num_simulations):
        gap = [start_gap]
        for _ in range(future_yrs):
            change = np.random.normal(loc=mean_change, scale=sd)
            next_gap = gap[-1] + change
            gap.append(next_gap)
        simulations.append(gap)

    sim_df = pd.DataFrame(simulations).T # Transpose for plotting
    return sim_df

def plot_graph(sim_df, state_name, start_year=2022):
    years = list(range(start_year, start_year + sim_df.shape[0]))
    plt.figure(figsize=(12, 6))
    plt.plot(years, sim_df, color='lightblue', linewidth=0.5, alpha=0.3)
    plt.plot(years, sim_df.mean(axis=1), color='red', label='Average Projection')
    plt.title(f'Monte Carlo Simulation of {state_name} Wage Gap ($) Until 2050')
    plt.xlabel('Year')
    plt.ylabel('Wage Gap ($)')
    plt.grid(True)
    plt.legend()
    plt.show()
