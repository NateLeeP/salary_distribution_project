# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 05:57:14 2019

@author: Nate P
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

""" This file returns the x and y values needed to plot the lorenz curve """
def lorenz_curve_values(salary_df, league):
    salary = salary_df[salary_df['League'] == league]['Salary'].sort_values(ascending = True).reset_index().drop(columns = 'index')['Salary'].dropna() #Dataframe only containing salary. Salary in ascending order 
    ## Inputs for calculating % of population
    salary = salary[salary > 0] ## Ensuring all salary values are above zero
    n_players = len(salary) # Number of players in the league
    cum_sum = np.cumsum(salary) ## Cumulative sum of league salary 
    total_salary = salary.sum() #### total salary of the league
    p_income = np.linspace(0,1,101) ### percents from 0 to 100
    # For each percent, what percent of players is responsible for that percent of salary? p_players is the percent
    p_players = [len(cum_sum[cum_sum <= (p * total_salary)]) / n_players for p in p_income]
    
    return p_players, p_income

"""What if f(x) only returns player percent? since I already have p_income. Try this tomorrow. Need to get gini coefficient"""