import plotly.express as px
import pandas as pd
import numpy as np
import plotly
import matplotlib.pyplot as plt


data = pd.read_csv('src/listings_summary_dec18.csv')
data = data.values
pos = []
position = []
for row in data:
    lat = row[6]
    lon = row[7]
    position = [lat,lon]
    pos.append(position)

print('pos',len(pos))

latt = []
lonn = []

for cor in pos:
    if -33.695 > cor[0] > -34.005 and 151.323 > cor[1] > 150.631:
        latt.append(cor[0])
        lonn.append(cor[1])
    else:
        pass




#------------- plot -------------------
img = plt.imread('src/map_2.png')
fig, ax = plt.subplots()
# [151,151,35] , [-34.15, -33.5]


ax.imshow(img, extent=[150.6310, 151.3258,-34.0088, -33.6950])
ax.scatter(lonn, latt, s=0.1, alpha=0.5)

plt.show()


#fig = px.density_mapbox(data, lat = '')


