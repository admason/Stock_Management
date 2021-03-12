# Stock_Management
A series of codes designed to automate my job as a Stock Controller 

## 1. Back Order System
### BackOrder_Stock_ordering
##### Back Order Stock Automated Ordering system.
##### With any stock control system there will be times when cutomser demand outweighs the quantity of items in storage.
##### The customer has to wait for their item to arrive in the Warehouse/Distribution Centre.
##### From the perspective of Stock Control this is seen as a negative NET QTY.
##### The purpose of this code is to take an Excel Document and identify the titles and respective quantities which require ordering.
[![Backorderheads.jpg](https://i.postimg.cc/CLCyL4Ss/Backorderheads.jpg)](https://postimg.cc/D8zpxLWS)

##### Also, only titles which have a Purchase Status of IP (In Print) may be ordered. This is based upon book sales.
##### When complete, the code will export an Excel sheet which holds just the id and qty which require orders to be placed. This file may be copied and is well suited for SAP ordering systems.¶
[![newOrds.jpg](https://i.postimg.cc/fbHfNC5L/newOrds.jpg)](https://postimg.cc/NyHH813q)

