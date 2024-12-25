import json

geojson_path = "./sample_data/sample_data.geojson"  # GeoJSON file path
czml_path = "output.czml"  # output file(CZML) path

with open(geojson_path, "r", encoding="utf-8") as file:
    geojson_data = json.load(file)

# make CZML header
czml = [
    {
        "id": "document",
        "name": "CZML from GeoJSON",
        "version": "1.0",
    }
]

# Convert each GeoJSON feature to a CZML entity
for feature in geojson_data.get("features", []):
    properties = feature.get("properties", {})
    geometry = feature.get("geometry", {})
    
    start_time = properties.get("start_time")
    end_time = properties.get("end_time")
    
    if start_time and end_time and geometry.get("type") == "MultiPolygon":
        positions = []
        for polygon in geometry["coordinates"]:
            for ring in polygon:
                for coord in ring:
                    positions.extend([coord[0], coord[1], 0])  

        entity = {
            "id": str(properties.get("ID", "unknown_id")),
            "name": f"Feature {properties.get('ID', 'unknown')}",
            "availability": f"{start_time}/{end_time}",
            "polygon": {
                "positions": {
                    "cartographicDegrees": positions
                },
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": [255, 0, 0, 128]  # set a color
                        }
                    }
                },
                "heightReference": "CLAMP_TO_GROUND" 
            }
        }
        czml.append(entity)

with open(czml_path, "w", encoding="utf-8") as file:
    json.dump(czml, file, indent=2, ensure_ascii=False)