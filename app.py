import folium


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


m.save("index.html");