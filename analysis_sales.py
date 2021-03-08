# By Julio Daniel, 11 July 2020
# I reproduced this experiment from https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import pandas as pd
import os

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


files = [file for file in os.listdir('./Sales_Data')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Sales_Data/" + file)
    all_months_data = pd.concat([all_months_data, df])


all_months_data.to_csv("all_data.csv", index=False)

all_data = pd.read_csv("all_data.csv")

    # Clean up the data
    # Drop rows on NaN

nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
all_data['Month'] = all_data['Order Date'].str[0:2]

    # Find and delete the 'Or's
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data['Month'] = all_data['Month'].astype('int32')

    # Convert columns to correct type
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


    # Task 3: add a sales column

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

print(all_data.groupby('Month').sum())

# .groupby('Month').head(80)
# augment data with additional columns

    # Task 2: add month column. take first two characters in the date string and make that the month column
all_data['Month'] = all_data['Order Date'].str[0:2]

    # after running this, we get an error
# ValueError: invalid literal for int() with base 10: 'Or' so we go back to the cleaning process eliminate the 'Or's



nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()

all_data = all_data.dropna(how='all')
all_data.head()


# Find 'Or' and delete it
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
# Convert columns to correct type
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) # Make int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) # Make float

    # Task 3: add a sales column
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

all_data.groupby('Month').sum()

print(all_data.head(10))

# What was the best month for sales? How much was earned that month?

# Some ways to find NaNs in a df

# import pandas as pd
# import numpy as np

df = pd.DataFrame(np.random.randn(10,6))
# Make a few areas have NaN values
df.iloc[1:3,1] = np.nan
df.iloc[5,3] = np.nan
df.iloc[7:9,5] = np.nan
# Option 1: df.isnull().any().any() - This returns a boolean value
# If you make it df.isnull().any(), you can find just the columns that have NaN values:


# Option 2: df.isnull().sum().sum() - This returns an integer of the total number of NaN values:

#  Finally, to get the total number of NaN values in the DataFrame:

df.isnull().sum().sum()

# to find out which rows have NaNs in a specific column:

nan_rows = df[df['name column'].isnull()



















