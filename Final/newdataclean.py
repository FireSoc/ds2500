import pandas as pd
import csv
import numpy as np
from newmontecarlo import *

FILES = ["2022.csv", "2021.csv", "2019.csv", "2018.csv", "2017.csv",
    "2016.csv", "2015.csv", "2014.csv", "2013.csv", "2012.csv", "2011.csv", "2010.csv"
    ]
FILES_WITH_DIFF = ["2022.csv", "2021.csv", "2019.csv", "2018.csv", "2017.csv"]

STATE_NAMES = ["Alaska", "Alabama", "Arkansas", "Arizona", "California",
               "Colorado", "Connecticut", "Delaware",
               "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana",
               "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan",
               "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota",
               "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio",
               "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
               "South Dakota", "Tennessee", "Texas",
               "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

def clean_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header if necessary
        data = list(reader)
        rows = []
        for i in range(0, len(data)):
            try:
                state_name = data[i][0].strip()
                if state_name in STATE_NAMES:
                    if filename in FILES_WITH_DIFF:
                        male_income = data[i + 6][14].replace(',', '').strip()
                        female_income = data[i + 10][14].replace(',', '').strip()
                        i = i + 13
                    else:
                        male_income = data[i + 4][14].replace(',', '').strip()
                        female_income = data[i + 6][14].replace(',', '').strip()
                        i = i + 6

                    # Ensure numeric conversion
                    male_income = float(male_income)
                    female_income = float(female_income)

                    rows.append({
                        "Year": filename[:4],
                        "State": state_name,
                        "Male_Income": male_income,
                        "Female_Income": female_income
                    })
            except IndexError:
                print(f"Skipping malformed block in {filename} at index {i}")

        return pd.DataFrame(rows)

def calculate_wage_gap(df):
    return ((df["Male_Income"] - df["Female_Income"]) / df["Male_Income"]) * 100

def main():
    all_years = []
    all_wage_gap_dfs = []
    all_avg_gap = []
    all_std_gap = []

    for file in FILES:
        df = clean_data(file)
        year = int(file[:4])
        df["wage_gap"] = calculate_wage_gap(df)
        df["Year"] = year
        all_years.append(year)
        all_wage_gap_dfs.append(df[["State", "Year", "wage_gap"]])

    # Combine all yearly data into one DataFrame
    full_df = pd.concat(all_wage_gap_dfs, ignore_index=True)

    for df in all_wage_gap_dfs:
        if df.loc[0, "Year"] == 2010:
            start_df = df

    for name in STATE_NAMES:
        all_gaps = []
        for i in range(len(full_df)):
            if name == full_df.loc[i, "State"]:
                all_gaps.append(full_df.loc[i, "wage_gap"])
        avg_gap = np.mean(all_gaps)
        std_gap = np.std(all_gaps)
        all_avg_gap.append(float(avg_gap))
        all_std_gap.append(float(std_gap))

    # Pivot so rows are states, columns are years
    wage_gap_matrix = full_df.pivot(index="State", columns="Year", values="wage_gap")

    # Sort years in correct order (ascending)
    wage_gap_matrix = wage_gap_matrix[sorted(wage_gap_matrix.columns)]

    # Calculate year-to-year difference per state
    year_diff = wage_gap_matrix.diff(axis=1)

    # Calculate average yearly increase per state (ignoring NaNs)
    wage_gap_matrix["avg_yearly_increase"] = year_diff.mean(axis=1)
    wage_gap_matrix["avg_yearly_increase"] = wage_gap_matrix["avg_yearly_increase"].round(2)

    # Display result
    print(wage_gap_matrix[["avg_yearly_increase"]])

    '''for i, state in enumerate(wage_gap_matrix.index):
        avg_increase = wage_gap_matrix.loc[state, "avg_yearly_increase"]
        std_dev = all_std_gap[i]
        start_gap = start_df.loc[i, "wage_gap"]

        sim_df = simulate(
            start_gap=start_gap,
            future_yrs=28,
            sd=std_dev,
            mean_change=avg_increase
        )

        plot_graph(sim_df, state_name=state)'''

    # --- National level simulation ---
    national_start_gap = start_df["wage_gap"].mean()
    national_std = np.mean(all_std_gap)
    national_mean_change = wage_gap_matrix["avg_yearly_increase"].mean()

    national_sim_df = simulate(
        start_gap=national_start_gap,
        future_yrs=28,
        sd=national_std,
        mean_change=national_mean_change
    )

    plot_graph(national_sim_df, state_name="United States")

main()