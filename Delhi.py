import folium
import requests
from google.transit import gtfs_realtime_pb2
import pandas as pd
import datetime
from IPython.display import IFrame

API_KEY = "8WcAOAQxN9pvZ8m4wZyJ3wLk4uMK4lb9"
API_URL = f"https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key={API_KEY}"

def fetch_data():
    response = requests.get(API_URL)
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)

    data = []
    for entity in feed.entity:
        if entity.HasField('vehicle'):
            vehicle = entity.vehicle
            data.append({
                "VehicleID": vehicle.vehicle.id,
                "TripID": vehicle.trip.trip_id,
                "RouteID": vehicle.trip.route_id,
                "Latitude": vehicle.position.latitude,
                "Longitude": vehicle.position.longitude,
                "Timestamp": datetime.datetime.fromtimestamp(vehicle.timestamp) if vehicle.timestamp else None
            })
    return pd.DataFrame(data)

# Initial fetch
df = fetch_data()

# Create base map
m = folium.Map(location=[28.64857, 77.21895], zoom_start=11)

# Add vehicle markers with unique IDs
for _, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"Route: {row['RouteID']}<br>Vehicle: {row['VehicleID']}",
        icon=folium.Icon(color='blue', icon='bus'),
    ).add_to(m)

# Add JavaScript for smooth updates
update_js = """
<script>
let markers = {};
function updateMarkers(data) {
    data.forEach(bus => {
        let id = bus.VehicleID;
        if (markers[id]) {
            markers[id].setLatLng([bus.Latitude, bus.Longitude]);
        } else {
            markers[id] = L.marker([bus.Latitude, bus.Longitude]).addTo(window.map);
            markers[id].bindPopup("Route: " + bus.RouteID + "<br>Vehicle: " + id);
        }
    });
}

// Periodic update
async function fetchData() {
    const response = await fetch('/update');  // needs backend serving JSON
    const buses = await response.json();
    updateMarkers(buses);
    setTimeout(fetchData, 10000); // update every 10s
}
fetchData();
</script>
"""

m.get_root().html.add_child(folium.Element(update_js))

m.save("DelhiTransportLive.html")
IFrame("DelhiTransportLive.html", width=800, height=600)
