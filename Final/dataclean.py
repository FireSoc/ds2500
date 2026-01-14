import pandas as pd
from montecarlo import *
import csv

files = [
    "2023.csv", "2022.csv", "2021.csv", "2019.csv", "2018.csv", "2017.csv",
    "2016.csv", "2015.csv", "2014.csv", "2013.csv", "2012.csv", "2011.csv", "2010.csv"]

# FIPS codes for merging
state_fips = {'Alabama': '01', 'Alaska': '02', 'Arizona': '04', 'Arkansas': '05', 'California': '06',
    'Colorado': '08', 'Connecticut': '09', 'Delaware': '10', 'District of Columbia': '11',
    'Florida': '12', 'Georgia': '13', 'Hawaii': '15', 'Idaho': '16', 'Illinois': '17',
    'Indiana': '18', 'Iowa': '19', 'Kansas': '20', 'Kentucky': '21', 'Louisiana': '22',
    'Maine': '23', 'Maryland': '24', 'Massachusetts': '25', 'Michigan': '26',
    'Minnesota': '27', 'Mississippi': '28', 'Missouri': '29', 'Montana': '30',
    'Nebraska': '31', 'Nevada': '32', 'New Hampshire': '33', 'New Jersey': '34',
    'New Mexico': '35', 'New York': '36', 'North Carolina': '37', 'North Dakota': '38',
    'Ohio': '39', 'Oklahoma': '40', 'Oregon': '41', 'Pennsylvania': '42','Rhode Island': '44', 'South Carolina': '45', 'South Dakota': '46', 'Tennessee': '47',
    'Texas': '48', 'Utah': '49', 'Vermont': '50', 'Virginia': '51', 'Washington': '53',
    'West Virginia': '54', 'Wisconsin': '55', 'Wyoming': '56'}

def extract_income_by_state(filepath):
    df = pd.read_csv(filepath)
    df["Label (Grouping)"] = df["Label (Grouping)"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip()
    states = list(state_fips.keys())
    income_data = {}

    for i, row in df.iterrows():
        label = row["Label (Grouping)"]
        if label in states and i + 10 < len(df):
            total_income = df.iloc[i + 2, 1]
            male_income = df.iloc[i + 6, 1]
            female_income = df.iloc[i + 10, 1]
            income_data[label] = [total_income, male_income, female_income]
            income_df = pd.DataFrame(income_data, index=["Total", "Male", "Female"])

    for col in income_df.columns:
        income_df[col] = income_df[col].map(
            lambda x: pd.to_numeric(str(x).replace(",", "").replace("(X)", ""),
                                    errors='coerce'))
    return income_df

def calculate_wage_gap(df):
    return ((df.loc["Male"] - df.loc["Female"]) / df.loc["Male"]) * 100

def main():
    all_dfs = []
    total_pay_gap = 0
    total_std = 0

    for file in files:
        df = extract_income_by_state(file)
        gap = calculate_wage_gap(df)
        all_dfs.append(gap)

    gap_df = pd.concat(all_dfs, axis = 1)
    mean_avg_gap = gap_df.mean(axis = 1).sort_values(ascending = False)
    std_avg_gap = gap_df.std(axis = 1).sort_values(ascending = False)

    avg_gap_df = mean_avg_gap.reset_index()
    avg_gap_df.columns = ["state_name", "wage_gap"]
    std_avg_gap_df = std_avg_gap.reset_index()
    std_avg_gap_df.columns = ["state_name", "SD_wage_gap"]

    combined_df = pd.merge(avg_gap_df, std_avg_gap_df, on="state_name",  how="left")
    combined_df["fips"] = combined_df["state_name"].map(state_fips)
    '''for i in range(len(combined_df)):
        sim_df = simulate(start_gap=combined_df.loc[i, "wage_gap"], future_yrs=27,
                          sd=combined_df.loc[i, "SD_wage_gap"])
        plot_graph(sim_df, state_name=combined_df.loc[i, "state_name"])'''

    for i in range(len(combined_df)):
        total_pay_gap += combined_df.loc[i, "wage_gap"]
        total_std += combined_df.loc[i, "SD_wage_gap"]

    avg_pay_gap = total_pay_gap / len(combined_df)
    avg_std_gap = total_std / len(combined_df)

    sim_df = simulate(start_gap=avg_pay_gap, future_yrs=27,
                      sd=avg_std_gap)
    plot_graph(sim_df, state_name="USA")

main()
