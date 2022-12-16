import folium
import pandas

# To get the Data Required for Volcanoes
data = pandas.read_csv("./data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# To Create dynamic Marker Colors
def color_gen(elevation):
    if elevation <1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'blue'
    else:
        return 'red'

# Create a Map Object to build an actual Map(Layer 0 => Base Layer)
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")


# Looping through the Data to generate Markers using Longitude & Latitude form the dataset(Layer 1)
# Feature Group is necessary because there around 62 Volcanoes in the data, so in order to not create 62 Childs unnecessarily FG is used!!
fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius =6, popup=str(el) +" m", fill_color=color_gen(el), color ='grey', 
     fill_opacity =0.7))

# To add another Geo Layer(Layer 2)
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('./data/world.json','r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties'] ['POP2005'] < 20000000 else 'red'}))


# To add Layers to the Map
map.add_child(fgv)
map.add_child(fgp)

# Folium Layer Control
map.add_child(folium.LayerControl())

# Finally Saving the Map to view on Browser
map.save("map1.html")