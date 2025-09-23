import folium
import itertools


# 30.3435275097896, -97.97418129729917
m = folium.Map(
    tiles='https://tile.openstreetmap.de/{z}/{x}/{y}.png',
    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    location=(30.3435275097896, -97.97418129729917), 
    zoom_start=13)


# LKWY
folium.Marker(
    location=[30.3435275097896, -97.97418129729917],
    tooltip="Lake Travis Community Library - LKWY",
    popup="Lake Travis Community Library - LKWY",
    icon=folium.Icon(icon="home"),
).add_to(m)


# WEST
folium.Marker(
    location=[30.353050237852162, -98.06523183857625],
    tooltip="Lake Travis Community Library - WEST",
    popup="Lake Travis Community Library - WEST",
    icon=folium.Icon(icon="home"),
).add_to(m)


# DISTRICT BOUNDARY
boundary_coords = []

with open("./data/district_coordinates.txt", "r") as file:
    for line in file:
        coord = line.split(",")
        x = float(coord[0])
        y = float(coord[1])
        boundary_coords.append([x, y])
        
# remove potential duplicate coordinates
boundary = list(coord for coord,_ in itertools.groupby(boundary_coords))
print(boundary)

folium.Polygon(
    locations=boundary,
    color="blue",
    weight=6,
    fill_color="green",
    fill_opacity=0.25,
    no_clip=True,
    fill=True,
    popup="Lake Travis Community Library District",
    tooltip="Library District Boundary",
).add_to(m)

m.save("index.html")