import folium

#Initailize a map object
myMap = folium.Map(location=[-1.292155,36.821922],zoom_start=12)

#Tooltip
tooltip = "Click for more info"


# Initialize custom marker icon
customIcon = folium.features.CustomIcon('customMarker.png',icon_size=(50,50))
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


#Generates a html file with the map
myMap.save('myMap.html')