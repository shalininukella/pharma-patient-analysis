#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("../data/cleaned_insurance.csv")

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Load the DataFrame into SQL
df.to_sql("insurance", conn, index=False, if_exists="replace")

# Sample SQL queries
query1 = "SELECT smoker, AVG(charges) as avg_charge FROM insurance GROUP BY smoker;"
query2 = "SELECT region, AVG(charges) as avg_charge FROM insurance GROUP BY region;"
query3 = "SELECT age, AVG(charges) as avg_charge FROM insurance GROUP BY age ORDER BY age;"

# Run and print results
print(pd.read_sql(query1, conn))
print(pd.read_sql(query2, conn))
print(pd.read_sql(query3, conn).head(10))  # First 10 rows only


# In[ ]:




