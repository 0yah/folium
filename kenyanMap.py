import folium
import pandas as pd
import os

counties = os.path.join('data','counties.json')
random_unemployment_data = os.path.join('data','random.csv')

counties_data = pd.read_csv(random_unemployment_data)

myMap = folium.Map(location=[-1,36],zoom_start=3)

folium.Choropleth(
    geo_data=counties,
    name="choropleth",
    data=counties_data,
    columns=["County", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(myMap)



folium.LayerControl().add_to(myMap)

myMap.save('unemployment.html')