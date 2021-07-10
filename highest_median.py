# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 13:04:51 2021

@author: Ugurhan Uzkal
"""

import pandas as pd
import numpy as np

df = pd.read_csv('country_vaccination_stats_imputation.csv')

filtered_df = df[['country', 'daily_vaccinations']]

country_df = filtered_df[['country']]

arr_country = np.unique(country_df.values)

medians = {}

for country in arr_country:
    temp_df = filtered_df[filtered_df['country']==country]
    temp_series = temp_df.median()
    medians.update({country: temp_series['daily_vaccinations'].tolist()})
    
medians_sorted = sorted(medians, key=medians.get, reverse=True)

top_medians = medians_sorted[:3]

print('Top 3 countries with highest median daily vaccination numbers: ')
print('1.' + top_medians[0] + '\n' + '2.' + top_medians[1] + '\n' + '3.' 
      + top_medians[2] + '\n')

            
        
    