import folium
import pandas
data=pandas.read_csv("map1.csv")
latitude=list(data["latitude"])
longitude=list(data["longitude"])
metrocities=list(data["metrocities"])
color=list(data["color"])
map=folium.Map(location=(12.58,77.48),zoom_start=6)
fg=folium.FeatureGroup(name="bangloremap")
for lati,longi,metro,color in zip(latitude,longitude,metrocities,color):
    fg.add_child(folium.Marker(location=(lati,longi),popup=metro,icon=folium.Icon(color=(color))))
map.add_child(fg)
map.save('bmap1.html')