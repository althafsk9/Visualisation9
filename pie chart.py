#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:44:24 2023

@author: althafshaik
"""
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Product Category': ['Clothing', 'Electronics', 'Home Goods', 'Beauty', 'Sports'],
    'Total Sales Revenue (in GBP)': [50000, 35000, 21000, 14000, 10500]
}

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Create the pie chart
plt.pie(df['Total Sales Revenue (in GBP)'], labels=df['Product Category'], autopct='%1.2f%%')

# Add a title to the chart
plt.title('Monthly Sales Revenue by Product Category')

# Show the chart
plt.show()
