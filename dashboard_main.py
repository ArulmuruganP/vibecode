def create_dashboard():
    # Dashboard with advanced search (Mapbox autocomplete), zoom, home button, drawing tool, and custom marker
    return """
    <html>
        <head>
            <title>Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
            <link rel="stylesheet" href="https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.css" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.css"/>
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            <script src="https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.draw/1.0.4/leaflet.draw.js"></script>
        </head>
        <body>
            <h1>Dashboard Page</h1>
            <div id="map" style="height: 700px;"></div>
            <script>
                var homeCoords = [20.5937, 78.9629]; // Example: India center
                var map = L.map('map').setView(homeCoords, 5);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '© OpenStreetMap'
                }).addTo(map);

                // Add zoom control (default in Leaflet, but you can reposition)
                map.zoomControl.setPosition('topright');

                // Add home button
                var homeControl = L.Control.extend({
                    options: { position: 'topright' },
                    onAdd: function (map) {
                        var container = L.DomUtil.create('button', 'leaflet-bar');
                        container.innerHTML = '🏠';
                        container.title = 'Go Home';
                        container.style.width = '34px';
                        container.style.height = '34px';
                        container.onclick = function(){
                            map.setView(homeCoords, 5);
                        };
                        return container;
                    }
                });
                map.addControl(new homeControl());

                // Add drawing tools
                var drawnItems = new L.FeatureGroup();
                map.addLayer(drawnItems);

                var drawControl = new L.Control.Draw({
                    edit: {
                        featureGroup: drawnItems
                    },
                    draw: {
                        polygon: true,
                        polyline: true,
                        rectangle: true,
                        circle: true,
                        marker: true
                    }
                });
                map.addControl(drawControl);

                map.on('draw:created', function (e) {
                    var layer = e.layer;
                    drawnItems.addLayer(layer);
                    // Optionally, output GeoJSON to console
                    console.log(JSON.stringify(drawnItems.toGeoJSON()));
                });

                // Example: Add a custom marker icon
                var customIcon = L.icon({
                    iconUrl: 'https://cdn-icons-png.flaticon.com/512/684/684908.png', // Example icon
                    iconSize: [32, 32],
                    iconAnchor: [16, 32],
                    popupAnchor: [0, -32]
                });
                L.marker(homeCoords, {icon: customIcon}).addTo(map)
                    .bindPopup('Home Location');

                // Open source search: Leaflet Control Geocoder
                var geocoder = L.Control.geocoder({
                    defaultMarkGeocode: false,
                    placeholder: 'Search for places...'
                })
                .on('markgeocode', function(e) {
                    var bbox = e.geocode.bbox;
                    var poly = L.polygon([
                        bbox.getSouthEast(),
                        bbox.getNorthEast(),
                        bbox.getNorthWest(),
                        bbox.getSouthWest()
                    ]).addTo(map);
                    map.fitBounds(poly.getBounds());
                    L.marker(e.geocode.center).addTo(map)
                        .bindPopup(e.geocode.name)
                        .openPopup();
                })
                .addTo(map);
            </script>
        </body>
    </html>
    """