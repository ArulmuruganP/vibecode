from flask import Flask, render_template, jsonify
from dashboard import create_dashboard
from geofencing import monitor_geofencing
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Example dynamic data
    total_entries = 320
    active_employees = 210
    avg_entries_week = 128
    avg_entries_month = 520
    entry_exit_data = [320, 110]
    entry_time_data = [10, 40, 120, 80, 40, 30]
    entries_week_data = [280, 300, 320, 310, 330, 290, 320]

    return render_template(
        'index.html',
        last_update=last_update,
        total_entries=total_entries,
        active_employees=active_employees,
        avg_entries_week=avg_entries_week,
        avg_entries_month=avg_entries_month,
        entry_exit_data=entry_exit_data,
        entry_time_data=entry_time_data,
        entries_week_data=entries_week_data
    )

@app.route('/dashboard')
def dashboard():
    return create_dashboard()

@app.route('/geofencing')
def geofencing():
    return monitor_geofencing()

@app.route('/api/building-entries')
def building_entries():
    # Replace with your real data source
    data = {
        "SDB 1": 45,
        "SDB 2": 38,
        "SDB 3": 52,
        "SDB 4": 41,
        "Cafeteria Block": 120,
        "Open Air Theatre": 16
    }
    return jsonify(data)

if __name__ == '__main__':
    try:
        app.run(debug=True, port=5001)
    except KeyboardInterrupt:
        print("\nServer interrupted. Shutting down gracefully...")
