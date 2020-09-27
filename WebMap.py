# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:48:30 2019

@author: PranavM
"""

import numpy
import cv2
import folium
import pandas

import os 
os.getcwd() #getting the current working directory 
#os.chdir('C:\\Users\\PranavM\\')

map = folium.Map(location=[38.58,-99.09],zoom_start=3, tiles = "OpenStreetMap")
fg=folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.58,-99.09], popup='I am marker',icon=folium.Icon(color='green')))
map.add_child(fg)

#fg and map.add are same commands. but fg makes it easier to edit, add feeatures and hence is more organised

map.add_child(folium.Marker(location=[38.58,-99.09], popup='I am marker',icon=folium.Icon(color='green')))
map.save('Mapl.html')



map1 = folium.Map(location=[19.1,73],zoom_start=12, tiles = 'Mapbox Bright')
map1.save('Map1.html')

data= pandas.read_csv('C:\\Users\\PranavM\\OneDrive\\Python\\Volcanoes.txt')

lat=list(data['LAT'])
long=list(data['LON'])
elev=list(data['ELEV'])

fg=folium.FeatureGroup(name='My Map')
for lt,ln,el in zip(lat,long,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],zoom_start=6,tooltip=el,titles='Mapbox Bright'))

#help(folium.Marker)
#help(folium.Icon)

map.add_child(fg)
map.save('Mapl.html')

#To make icon colour green, yellow, red depending on the height of elevation
#Folium does not allow a if condition. hence we need a function to do it 
lat=list(data['LAT'])
long=list(data['LON'])
elev=list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green '
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    

fg=folium.FeatureGroup(name='Volcanoes')
for lt,ln,el in zip(lat,long,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el) + 'm', color=color_producer(el),
                                     fill_color=color_producer(el),fill_opacity=0.7))

fg1=folium.FeatureGroup(name='Population')
fg1.add_child(folium.GeoJson(data=open('C:\\Users\\PranavM\\OneDrive\\Python\\world.json','r',
                                       encoding='utf-8-sig').read(),
    style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] <10000000 
                             else 'black' if 10000000 <=  x['properties']['POP2005'] <100000000
                             else 'red'}))

map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())
map.save('Mapl.html')

help(folium.Map.add_child)

#help(folium.FeatureGroup)

import json

#data1=json.load(open('C:\\Users\\PranavM\\OneDrive\\Python\\world.json'))


