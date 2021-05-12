# Stock_Management
A series of codes designed to automate my job as a Stock Controller 

## 1. Back Order System
### BackOrder_Stock_ordering
##### Back Order Stock Automated Ordering system.
##### With any stock control system there will be times when customer demand outweighs the quantity of items in storage.
##### The customer has to wait for their item to arrive in the Warehouse/Distribution Centre.
##### From the perspective of Stock Control this is seen as a negative NET QTY.
##### The purpose of this code is to take an Excel Document and identify the titles and respective quantities which require ordering.
[![Backorderheads.jpg](https://i.postimg.cc/CLCyL4Ss/Backorderheads.jpg)](https://postimg.cc/D8zpxLWS)

##### Also, only titles which have a Purchase Status of IP (In Print) may be ordered. This is based upon book sales.
##### When complete, the code will export an Excel sheet which holds just the id and qty which require orders to be placed. This file may be copied and is well suited for SAP ordering systems.¶
[![newOrds.jpg](https://i.postimg.cc/fbHfNC5L/newOrds.jpg)](https://postimg.cc/NyHH813q)

## 2. ETA Calculator 
### This code will produce an Estimated Time of Arrival (ETA) for consignments.
### Simply enter the shipment quantity and then the Source, either UK, India, Australia and the code output the ETA for you.

```
## ETA Calculator
## Deliveries are sent every Wednesday, the code will accomodate for this

import datetime as dt
from datetime import date, timedelta

# Lead times as list:
days =[14,42,70,100]

# Input funation:
q = int(input("Quantity: "))
s = str(input("Source: "))

# To set ETA starting from nearest subsequent Wednesday
dt = datetime.datetime.now()
daynum = int(dt.strftime("%w"))
extra_days = 7-daynum%3


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
```

#### An example output being:

```Source: aus
100  copies due on  2021-07-28 shipped from aus
```
