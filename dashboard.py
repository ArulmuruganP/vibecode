from flask import render_template

def create_dashboard():
    # Example data, replace with your actual logic
    entry_time_distribution = [1, 2, 3, 4]
    entries_last_7_days = [10, 12, 8, 15, 9, 11, 13]
    geospatial_data = [
        {"lat": 12.9716, "lon": 77.5946},
        {"lat": 28.7041, "lon": 77.1025}
    ]
    return render_template(
        'dashboard.html',
        entry_time_distribution=entry_time_distribution,
        entries_last_7_days=entries_last_7_days,
        geospatial_data=geospatial_data
    )
