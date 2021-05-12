#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Incorporate a list
# Nearest wednesday

import datetime as dt
from datetime import date, timedelta

days =[14,42,70,100]

q = int(input("Quantity: "))
s = str(input("Source: "))

dt = datetime.datetime.now()

daynum = int(dt.strftime("%w"))
#print(daynum)
type(daynum)
extra_days = 7-daynum%3
print("extra",extra_days, "days")

def eta(q,s):
    if s == "UK" or s=="uk":
        n = days[0]+extra_days
    elif s == "INDIA" or s=="india":
        n = days[1]+extra_days
    elif s == "AUS" or "aus":
        n = days[2]+extra_days
    else:
        n = days[3]+extra_days
    eta = (date.today()+timedelta(days=n)).isoformat()
    #eta = int((date.today()+timedelta(days=n))+int(extra_days)).isoformat()
    return eta

print(q," copies due on ",eta(q,s), "shipped from",s)


# In[5]:


daynum = int(dt.strftime("%w"))


# In[ ]:




