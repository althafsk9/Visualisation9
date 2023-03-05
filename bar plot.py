#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:47:13 2023

@author: althafshaik
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a pandas DataFrame
data = pd.DataFrame({
    'Country': ['China', 'India', 'United States', 'Indonesia', 'United Kingdom', 'Brazil', 'Nigeria', 'Bangladesh', 'Mexico'],
    '2016': [1389, 1339, 323, 261, 199, 207, 185, 161, 127],
    '2017': [1394, 1353, 326, 264, 203, 209, 190, 164, 129],
    '2018': [1399, 1366, 329, 268, 208, 211, 195, 167, 131],
    '2019': [1404, 1380, 332, 271, 212, 213, 200, 170, 133],
    '2020': [1409, 1395, 333, 273, 216, 215, 205, 173, 135],
    '2021': [1439, 1380, 331, 274, 221, 212, 206, 165, 130]
})

# Set the 'Country' column as the index
data.set_index('Country', inplace=True)

# Create a bar plot of the data
data.plot(kind='bar')

# Set the x-axis and y-axis labels and title
plt.xlabel('Country')
plt.ylabel('Population (in millions)')
plt.title('Top 9 Countries by Population (2016-2021)')

# Show the plot
plt.show()

