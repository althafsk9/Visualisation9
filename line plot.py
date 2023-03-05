#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:15:49 2023

@author: althafshaik
"""
import matplotlib.pyplot as plt

# Define the data
years = [2017, 2018, 2019, 2020, 2021]
shoreditch_robbery = [100, 110, 120, 130, 140]
camden_burglary = [75, 80, 85, 90, 95]
nottinghill_assault = [50, 55, 60, 65, 70]
brixton_theft = [125, 135, 145, 155, 165]

# Plot the data
plt.plot(years, shoreditch_robbery, label='Shoreditch - Robbery')
plt.plot(years, camden_burglary, label='Camden - Burglary')
plt.plot(years, nottinghill_assault, label='Notting Hill - Assault')
plt.plot(years, brixton_theft, label='Brixton - Theft')

# Customize the plot
plt.title('Reported Crime Rates in London Areas')
plt.xlabel('Year')
plt.ylabel('Number of Reported Crimes')
plt.legend(loc='upper left')

# Show the plot
plt.show()

