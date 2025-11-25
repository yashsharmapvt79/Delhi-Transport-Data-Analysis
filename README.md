# Delhi-Transport-Data-Analysis

## 🗺️ Delhi Transport Live Tracking System

A real-time map visualization of Delhi’s bus & metro vehicle positions using **GTFS-Realtime**, **Folium**, and **Leaflet**.

This project fetches live transit data from the **Delhi Government Open Transit Data API**, processes it, and plots active vehicles on interactive maps. The maps can be hosted locally or deployed on a server.

---

## 🚀 Features

### 1. ✅ Real-Time Vehicle Tracking
- Fetches **GTFS-Realtime VehiclePositions.pb** feed from the Delhi Govt API  
- Extracts **latitude, longitude, route ID, vehicle ID, timestamp**  
- Displays vehicles using:
  - **Folium** (static map)
  - **Leaflet + JavaScript** (auto-updating map)

### 2. 🌍 Interactive Maps
Includes two fully generated HTML maps:

- `Delhi Transport Mapping.html` → Folium Static Map  
- `DelhiTransportLive.html` → Live Updating Map (Leaflet + JS)

### 3. 🚌 Metro & Bus Marker Visualization
- Blue markers for buses/metro  
- Popup details:
  - Route Number  
  - Vehicle Number  
  - Timestamp  

### 4. 🧭 Backend Data Processing
Using Python (`Delhi.py`):
- Fetches GTFS-Realtime feed  
- Parses protobuf data  
- Converts to a clean DataFrame  
- Generates interactive maps  

---

## 📁 Project Structure

📦 Delhi-Transport-Live

- Delhi.py # Main script to fetch data & generate the map
- Delhi metro.csv # Metro route dataset
- DELHI.ipynb # Jupyter analysis notebook
- DelhiMetro.ipynb # Metro mapping notebook
- Delhi Transport Mapping.html # Folium map (static)
- DelhiTransportLive.html # Dynamic updating map (Leaflet JS)
- README.md # Documentation


---

## ⚙️ How It Works

---

### 🔗 Data Source  
Delhi Government Open Transit Data API:

https://otd.delhi.gov.in/api/realtime/VehiclePositions.pb?key=YOUR_API_KEY

---

### 🔧 Data Pipeline
1. Download protobuf GTFS-Realtime feed  
2. Parse using `gtfs_realtime_pb2`  
3. Convert to DataFrame:  
   - Vehicle ID  
   - Route ID  
   - Latitude  
   - Longitude  
   - Timestamp  
4. Add markers to Folium Map  
5. Add JavaScript for auto-updating Leaflet map (`DelhiTransportLive.html`)  

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install folium pandas requests protobuf
```
### 2️⃣ Add Your API Key
```
API_KEY = "YOUR_KEY"
```
### 3️⃣ Run the Script
```
python Delhi.py
```
### 4️⃣ View the Maps
Open generated HTML files:

1.Static Version:
  - Delhi Transport Mapping.html

2.Live Updating Version:
  - DelhiTransportLive.html

3.🖼️ Screenshots (Maps Included)
  a.Static Map
    - File: Delhi Transport Mapping.html

(Open the file to view the generated map.)

4.Live Map
  - File: DelhiTransportLive.html

(Shows moving bus markers updated every 10 seconds.)

5.📊 Dataset
The repository includes:
- Delhi metro.csv
Contains station coordinates
Useful for:

- Plotting metro network

- Graph analysis

- Heatmaps

- Route planning

🔥 Advanced Features (Optional)
🔄 Auto-Updating Vehicle Markers
- DelhiTransportLive.html updates positions every 10 seconds:

js
```
setTimeout(fetchData, 10000);
```

🧭 Backend Endpoint Support
- If hosted, the /update endpoint should return JSON formatted vehicle data.

### `📌 Future Enhancements`
- Metro route visualization

- ETA predictions using ML

- Traffic density heatmaps

- Flask dashboard integration

- Real-time clustering of vehicle movement

📝 License
This project is available under the MIT License.
