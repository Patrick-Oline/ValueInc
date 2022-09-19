#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:46:45 2022

@author: pat
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

data.info()

#Finding  a Cost per transaction
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']

#Adding column to table
data['CostPerTransaction'] = CostPerItem * NumberofItemsPurchased

#Sales per Transation
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation
data['ProfirperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup
data['Markup'] = (data['ProfirperTransaction']) / data['CostPerTransaction']

roundmarkup = round(data['Markup'],2)

data['Markup'] = roundmarkup

#changing column type and combinding data fields
day = data['Day'].astype(str)
year = data['Year'].astype(str)

data['date'] = day + '-' + data['Month'] + '-' + year

#Observing rows
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows
data.head(5) # first 5 rows

#observing columns
data.iloc[:,2] #all rows in 2nd column
data.iloc[4,2] #4th row 2nd column

#using split to split the client_keywords field
split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Placing split columns into table
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using replace function to remove '[' and']'
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] =data['LengthofContract'].str.replace(']' , '')

#using lowercase fucntion to change items to lowercase
data['ItemDescription'] = data['ItemDescription'] .str.lower()

#merging datasets, bringing in new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on = "Month")

#dropping columns
data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year','Month'], axis = 1)


#Export to a CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)









