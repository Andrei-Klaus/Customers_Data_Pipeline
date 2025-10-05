#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
df = pd.read_csv("customers-10000.csv")


# In[38]:


df.info()


# In[39]:


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ","_")
)
df.info()


# In[40]:


df.drop_duplicates("customer_id", inplace=True)


# In[41]:


print(df.isna().count())


# In[42]:


df["email_domain"] = "@" + df["email"].str.split("@").str[1]
print(df["email_domain"])


# In[43]:


df["full_name"] = df["first_name"].str.strip() + " " + df["last_name"].str.strip()


# In[44]:


df["subscription_date"] = pd.to_datetime(df["subscription_date"])
df["subscription_year"] = df["subscription_date"].dt.year
df["subscription_month"] = df["subscription_date"].dt.month


# In[45]:


customers_by_country = df.groupby("country")["full_name"].count()
print(customers_by_country)


# In[48]:


df["subscription_age_days"] =( pd.Timestamp.today() - df["subscription_date"]).dt.days


# In[51]:


df.to_excel("cleaned_customers.xlsx", index = True)
customers_by_country.to_excel("customers_by_country.xlsx", index = True)


# In[ ]:




