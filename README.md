# time-series-czml-generator

### What is this tool for
This is a Python script to convert GeoJSON with timestamps to CZML for time series data.
<img src="src/gif001.gif" width="400">   
<img src="src/gif002.gif" width="400">  


### What you shold do
1. **Prepare a Geojson data**   
This script can only input GeoJSON. it does not support Shp or CSV. GeoJSON must have the properties "start_time" and "end_time" The "start_time" property describes the start time the data is displayed, and the "end_time" property describes the end time the data is displayed."start_time" and "end_time" must be written according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).
GeoJSON samples are available and can be checked [here](./sample_GeoJSON).

Example:
```
"type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "start_time": "2024-12-24T01:00:00Z", ## it must include in properties
        "end_time": "2024-12-24T01:00:05Z" ## it must include in properties
      },
      "geometry": {
        "coordinates": [
          [
            [0.46465215814495764, 30.42367752416716],
            [0.46465215814495764, 18.04236535131379],
            [8.852847616359526, 18.04236535131379],
            [8.852847616359526, 30.42367752416716],
            [0.46465215814495764, 30.42367752416716]
          ]
        ],
        "type": "Polygon" 
      },
      "id": 0
    },
```


2. **Check the geometry type**      
To run this script, the geometry type must be Point, MultiPoint, LineString, MultiLineString, Polygon, or MultiPolygon. Other types are not supported.   

Example:
```
"type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "start_time": "2024-12-24T01:00:00Z",
        "end_time": "2024-12-24T01:00:05Z"
      },
      "geometry": {
        "coordinates": [
          [
            [0.46465215814495764, 30.42367752416716],
            [0.46465215814495764, 18.04236535131379],
            [8.852847616359526, 18.04236535131379],
            [8.852847616359526, 30.42367752416716],
            [0.46465215814495764, 30.42367752416716]
          ]
        ],
        "type": "Polygon" ## Check here if type is suitable or not
      },
      "id": 0
    },
```

3. **Run the Script**   
Run the script locally. When the script is executed, a file selection screen will appear as shown in the image below, select GeoJSON, and when processing is complete, "output.czml" will be created in the same hierarchy as the executed script.Sample CZML files can be found [here](./sample_output_CZML).
<img src="src/img001.png" width="400">