#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

# Load CSV
df = pd.read_csv("../data/insurance.csv")

# View first rows
print(df.head())

# Check data info
print(df.info())

# Check summary statistics
print(df.describe())


# In[11]:


# Check for missing values
print(df.isnull().sum())

# Convert categorical columns to category dtype
df['sex'] = df['sex'].astype('category')
df['smoker'] = df['smoker'].astype('category')
df['region'] = df['region'].astype('category')

# Confirm changes
print(df.dtypes)


# In[12]:


# Save cleaned dataset
df.to_csv("../data/cleaned_insurance.csv", index=False)
print("Cleaned dataset saved to ../data/cleaned_insurance.csv")


# In[ ]:




