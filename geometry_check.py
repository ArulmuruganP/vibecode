from shapely.geometry import shape

def verify_blocks_within_campus(campus_geojson, blocks_geojson):
    campus_polygon = shape(campus_geojson['features'][0]['geometry'])
    results = []
    for feature in blocks_geojson['features']:
        block_polygon = shape(feature['geometry'])
        results.append(campus_polygon.contains(block_polygon))
    return results