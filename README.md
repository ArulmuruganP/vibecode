# Geospatial Dashboard

This project is a geospatial dashboard designed to monitor the presence of resources (e.g., staff, devices) within defined office premises and blocks using mobile network-based geofencing. The dashboard utilizes Folium for visualization and GeoJSON for defining geographical boundaries.

## Project Structure

```
geospatial-dashboard
├── src
│   ├── app.py                # Main entry point of the application
│   ├── dashboard
│   │   └── __init__.py       # Logic for rendering the geospatial dashboard
│   ├── geofencing
│   │   └── __init__.py       # Implements geofencing logic
│   ├── utils
│   │   └── geojson_loader.py  # Utility functions for loading GeoJSON data
│   └── data
│       └── boundaries.geojson  # GeoJSON data defining boundaries
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd geospatial-dashboard
   ```

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Execute the following command to start the Flask application:
   ```
   python src/app.py
   ```

4. **Access the dashboard:**
   Open your web browser and navigate to `http://127.0.0.1:5000` to view the geospatial dashboard.

## Features

- **Geospatial Visualization:** Interactive maps displaying resource locations within defined boundaries.
- **Geofencing Monitoring:** Real-time tracking of resources entering or exiting specified geofenced areas.
- **User Interaction:** Users can interact with the dashboard to view details about resources and their locations.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.