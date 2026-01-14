'''
DS2500
Spring 2025
Sample Code from Lecture

Goal:
- Explore 2 numeric variables
- if reasonably well correlated, apply a prediction model
- apply a linear regression and (1) draw the plot and (2) predict a y value for given x
'''

import statistics
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *

ADM_FILE = "data/admission_rate.csv"
TUITION_FILE = "data/tuition.csv"
DATA_COL = 1

def main():
    # gather data - reading tuition and admission data
    adm_lst = read_csv(ADM_FILE)
    tuition_lst = read_csv(TUITION_FILE)

    # pull out column number 1 from each 2D list
    adm_nums = col_to_lst(adm_lst, DATA_COL)
    tuition_nums = col_to_lst(tuition_lst, DATA_COL)

    print(adm_nums)
    print(tuition_nums)

    #convert sstr to floats!
    adm_num = [float(adm) for adm in adm_nums]
    tuition_nums = [clean_currency(tuition) for tuition in tuition_nums]

    # are these variable correlated?
    corr = statistics.correlation(adm_num, tuition_nums)
    print(f"correlation between admission and tuition: {corr}")

    #if admission rates go super low, what's tuition
    lr = stats.linregress(adm_num, tuition_nums)
    predicted_y = 5 * lr.slope + lr.intercept
    print(f"When adm rate is 5%, we predict tuition to be... ${predicted_y}")

    sns.regplot(x=adm_num, y=)


main()