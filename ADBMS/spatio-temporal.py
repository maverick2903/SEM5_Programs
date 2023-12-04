
import geojson
from datetime import datetime
import matplotlib.pyplot as plt

path_to_file = "sampledata.json"
with open(path_to_file) as f:
    gj = geojson.load(f)

features = gj['features']

for feature in features:
    temporal_info = feature["properties"]["time"]
    parsed_time = datetime.fromisoformat(temporal_info.rstrip('Z'))
    print("Feature Geometry: ", feature['geometry']['type'])
    print("Parsed Temporal Information:", parsed_time)

for feature in features:
    if feature["geometry"]["type"] == "Point":
        coordinates = feature["geometry"]["coordinates"]
        x, y = coordinates
        plt.scatter(x, y, label=f"Point ({x}, {y})")
    elif feature["geometry"]["type"] == "LineString":
        coordinates = feature["geometry"]["coordinates"]
        x, y = zip(*coordinates)
        plt.plot(x, y, label="LineString")
    elif feature["geometry"]["type"] == "Polygon":
        coordinates = feature["geometry"]["coordinates"][0]  # Only the exterior ring
        x, y = zip(*coordinates)
        plt.fill(x, y, label="Polygon")

# Set labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("GeoJSON Data Coordinates")

# Add a legend
plt.legend()

# Show the plot
plt.show()
