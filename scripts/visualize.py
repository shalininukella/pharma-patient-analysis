#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("../data/cleaned_insurance.csv")


# In[32]:


plt.figure(figsize=(6,4))
sns.barplot(x="smoker", y="charges", data=df)
plt.title("Average Charges: Smokers vs Non-Smokers")
plt.ylabel("Average Charges ($)")
plt.show()


# In[33]:


plt.figure(figsize=(8,4))
sns.barplot(x="region", y="charges", data=df)
plt.title("Average Charges by Region")
plt.ylabel("Average Charges ($)")
plt.show()


# In[34]:


plt.figure(figsize=(8,4))
sns.barplot(x="region", y="charges", data=df)
plt.title("Average Charges by Region")
plt.ylabel("Average Charges ($)")
plt.show()


# In[35]:


plt.figure(figsize=(10,6))
sns.lineplot(x="age", y="charges", data=df, estimator='mean', errorbar=None)
plt.title("Average Charges by Age")
plt.ylabel("Average Charges ($)")
plt.show()


# In[36]:


plt.figure(figsize=(10,6))
sns.scatterplot(x="bmi", y="charges", hue="smoker", data=df, alpha=0.7)
plt.title("BMI vs Charges (Smoker vs Non-Smoker)")
plt.ylabel("Charges ($)")
plt.show()


# In[ ]:




