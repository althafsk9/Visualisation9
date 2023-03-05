#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 12:44:07 2023

@author: althafshaik
"""
import pandas as pd

# Define the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    '2018 Revenue': [50000, 55000, 60000, 70000, 75000, 80000, 85000, 90000, 95000, 100000, 105000, 110000],
    '2022 Revenue': [75000, 80000, 90000, 95000, 105000, 110000, 115000, 120000, 125000, 130000, 135000, 140000]
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Set the "Month" column as the index
df.set_index('Month', inplace=True)

# Print the DataFrame
print(df)

