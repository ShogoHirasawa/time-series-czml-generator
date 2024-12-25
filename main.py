import json

geojson_path = "./sample_data/sample_data.geojson"  ## input file(.geojson) path
czml_path = "output.czml"  ## output file(.czml) path

with open(geojson_path, "r", encoding="utf-8") as file:
    geojson_data = json.load(file)

czml = [
    {
        "id": "document",
        "name": "CZML from GeoJSON",
        "version": "1.0",
    }
]

for feature in geojson_data.get("features", []):
    properties = feature.get("properties", {})
    geometry = feature.get("geometry", {})
    
    start_time = properties.get("start_time")
    end_time = properties.get("end_time")
    geometry_type = geometry.get("type")
    
    if geometry_type == "GeometryCollection":
        continue
    
    positions = []
    if geometry_type == "Point":
        coordinates = geometry["coordinates"]
        positions.extend([coordinates[0], coordinates[1], 0])

    elif geometry_type == "MultiPoint":
        for coord in geometry["coordinates"]:
            positions.extend([coord[0], coord[1], 0])

    elif geometry_type == "LineString":
        for coord in geometry["coordinates"]:
            positions.extend([coord[0], coord[1], 0])

    elif geometry_type == "MultiLineString":
        for line in geometry["coordinates"]:
            for coord in line:
                positions.extend([coord[0], coord[1], 0])

    elif geometry_type == "Polygon":
        for ring in geometry["coordinates"]:
            for coord in ring:
                positions.extend([coord[0], coord[1], 0])

    elif geometry_type == "MultiPolygon":
        for polygon in geometry["coordinates"]:
            for ring in polygon:
                for coord in ring:
                    positions.extend([coord[0], coord[1], 0])

    if positions:
        entity = {
            "id": str(properties.get("ID", "unknown_id")),
            "name": f"Feature {properties.get('ID', 'unknown')}",
            "availability": f"{start_time}/{end_time}",
            "polygon" if geometry_type in ["Polygon", "MultiPolygon"] else "polyline": {
                "positions": {
                    "cartographicDegrees": positions
                },
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": [255, 0, 0, 128]  
                        }
                    }
                },
                "heightReference": "CLAMP_TO_GROUND"  
            }
        }
        czml.append(entity)

with open(czml_path, "w", encoding="utf-8") as file:
    json.dump(czml, file, indent=2, ensure_ascii=False)
