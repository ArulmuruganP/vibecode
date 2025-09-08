def load_geojson(file_path):
    import json

    with open(file_path, 'r') as file:
        data = json.load(file)

    return data

def validate_geojson(data):
    if 'type' in data and data['type'] == 'FeatureCollection':
        return True
    return False

def extract_boundaries(data):
    if validate_geojson(data):
        return [feature['geometry'] for feature in data['features']]
    return []