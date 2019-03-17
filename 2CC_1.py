#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:42:19 2019

@author: aryaman
"""

import requests
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.animation as animation


res_1 = requests.get('http://api.open-notify.org/astros.json')
data_ISS = dict(res_1.json())
people = []
        
for i in data_ISS['people']:
    people.append(i['name'])


      
res_2 = requests.get('http://api.open-notify.org/iss-now.json')
data_ISS_pos = dict(res_2.json())
        
iss_pos_lat = data_ISS_pos['iss_position']['latitude']
iss_pos_long = data_ISS_pos['iss_position']['longitude']
        
fig = plt.figure()
ax = plt.axes(projection=ccrs.Mollweide())
ax.stock_img()

ax.plot([iss_pos_lat, iss_pos_long],color='blue', linewidth=2, marker='o',transform=ccrs.Geodetic())
        
plt.show()


print("The ISS Heroes are:-")
for i in people:
        print(i)
        