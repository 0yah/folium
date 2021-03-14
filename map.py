import folium

#Create a map object
myMap = folium.Map(location=[42.3601,-71.0589],zoom_start=12)

#Tooltip
tooltip = "Click for more info"

# Create markers
folium.Marker([42.363600,-71.099500],
    popup='<strong>Location One</strong>',
    tooltip=tooltip
    ).add_to(myMap)

folium.Marker([42.333600,-71.109500],
    popup='<strong>Location Two</strong>',
    tooltip=tooltip,
    icon=folium.Icon(icon='cloud')
    ).add_to(myMap)


#Generates a html file with the map
myMap.save('myMap.html')