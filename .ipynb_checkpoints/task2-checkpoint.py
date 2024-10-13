import numpy as np
import pandas as pd

# creating the array with income values for 10 months
income = np.array([500,1000,2500,3300,4700,15600,13000,9000,27000, 30900])

# multiplying every value in the array by 0.7 to get the amount before tax
income_without_tax = income*0.7

# creating the array with expense values for 10 months
expenses = np.array([500,500,600,900,3000,5000,3400,900,7000,15000])


# creating a data frame based on expenses and income

# first, making a list with all the months names
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]

# second, creating the dictionary as the foundation for the data frame
dict = {'Month': months, 'Income without tax': income_without_tax, 'Expenses':expenses}

# data frame itself
df = pd.DataFrame(dict)
print()
# now, outputting it; using to_string to get rid of the index column
print("Income/Expenses Data Frame:")
print("-----------------------------------")
print(df.to_string(index=False))

# selecting the first 3 months (indexes 0,1,2)
quarter = df.iloc[0:3]      
print()
print()
# outputting the data for the first quarter
print("First Quarter Only:")
print("-----------------------------------")
print(quarter.to_string(index=False))
      