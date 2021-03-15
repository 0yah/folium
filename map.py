import folium
import os
import json

#Initailize a map object
myMap = folium.Map(location=[-1.292155,36.821922],zoom_start=12)

#Tooltip
tooltip = "Click for more info"


# Initialize custom marker icon
customIcon = folium.features.CustomIcon('customMarker.png',icon_size=(50,50))

#Vega data visualization
vis = os.path.join('data','vis.json')

#Geo JSON data
overlayData = os.path.join('data','overlay.json')

# Initialize markers
folium.Marker([-1.298558,36.825382],
    popup='<strong>Location One</strong>',
    tooltip=tooltip
    ).add_to(myMap)

folium.Marker([-1.307466,36.826537],
    popup='<strong>Location Two</strong>',
    tooltip=tooltip,
    icon=folium.Icon(icon='cloud')
    ).add_to(myMap)

folium.Marker([-1.307466,36.826537],
    popup='<strong>Location Three</strong>',
    tooltip=tooltip,
    icon=folium.Icon(icon='cloud',color='red')
    ).add_to(myMap)

folium.Marker([-1.304481,36.823405],
    popup='<strong>Location Four</strong>',
    tooltip=tooltip,
    icon=customIcon
    ).add_to(myMap)

# 1.303683, 36.824670

folium.Marker([-1.303683,36.824670],
    popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),width=450,height=250))
    ).add_to(myMap)


# Encircle a region
folium.CircleMarker(
    location=[-1.311509,36.814945],
    radius=50,
    color='#42bca',
    fill=True,
    popup="Qwetu Wilson View",
    fill_color="#42bca"
).add_to(myMap)


#Load GeoJSON
folium.GeoJson(overlayData,name="Madaraka Regions").add_to(myMap)

#Generates a html file with the map
myMap.save('myMap.html')

# https://youtu.be/4RnU5qKTfYY?t=812