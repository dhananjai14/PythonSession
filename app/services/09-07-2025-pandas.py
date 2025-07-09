
"""
# Pandas 
    -> Panel Data

Datastructure 
    -> Series (1-D)  
    -> Dataframe (2-D)

Why Pandas?
    -> Data Cleaning and Preparation
    -> Data Exploration and Analysis
    -> Integration
    -> Performance
"""

import pandas as pd

pd_series = pd.Series([1,2,3,4,5], name = "FirstFiveNum")
# print(type(pd_series))
# print(pd_series)

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                  index=['falcon', 'dog', 'spider', 'fish'])

# print(type(df))
# print(df)

#### loc and iloc

# print(df.loc['falcon'])
# print(df.loc[['falcon', 'fish']])
# print(df.loc[['falcon', 'fish'],['num_legs']])
# print(df.loc[['falcon', 'fish'],['num_legs', 'num_specimen_seen']])

# print(df.iloc[1])
# print(df.iloc[[1,3])
# print(df.iloc[[1,3],[1]])
# print(df.iloc[[1,3],[1,2]])



df = pd.read_csv(r"C:\Users\DhananjaiSingh\Downloads\Monthly_Rates_of_Laboratory-Confirmed_COVID-19_Hospitalizations_from_the_COVID-NET_Surveillance_System.csv")
# print(type(df))

# print(df.head())

# print("############")
# print(df.tail(10))

# print(df.shape)

# print(df.info())

# print("===========================================")
# print(df.describe())

# Filtering data 

print(df[(df['_YearMonth'] > 202181) or () or ()])
