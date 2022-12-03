# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:08:03 2022

@author: black
"""

import pandas as pd
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemPurchased = 6

#Working with Calculation

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem

CostPerTransaction = NumberOfItemsPurchased*CostPerItem

SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

CostPerTransaction = CostPerItem * NumberOfItemPurchased

#Adding new column to dataframe

CostPerItem = data['CostPerItem']

NumberOfItemsPurchased = data['NumberOfItemsPurchased']

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Calculating profit (Profit = sales - cost)

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

#Rounding up

data['Markup'] = round(data['Markup'], 2)

#changing column type

day = data['Day'].astype(str)

year = data['Year'].astype(str)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific column

data.iloc[0]

#Using split to split client keyword field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' ,expand = True)

#creating a new column for the client keywords

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LenghtOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')

data['LenghtOfContract'] = data['LenghtOfContract'].str.replace(']', '')

#how to merge files
#briging in new data set

import pandas as pd

Seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merg_df = pd.merge(df_old, df.new, on 'key')

data = pd.merge(data, Seasons, on = 'Month')

#dropping column

data =data.drop('ClientKeywords', axis = 1)

data = data.drop('LentthOfContract', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)

data['ItemDescription'] = data['ItemDescription'].str.lower()

#export to csv

data.to_csv('Cleaned_Value_Inc.csv', index = False)
