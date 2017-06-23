from flask import Flask, render_template, jsonify, request, session
from datetime import datetime, timedelta
from pytz import timezone
import logging

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    # set configure datas.
    defaults    = app.config['DEFAULTS']
    circuits    = app.config['CIRCUITS']
    time_tables = app.config['TIME_TABLES']

    circuit_id    = session.get('circuit_id', defaults['circuit_id'])
    session['circuit_id'] = circuit_id
    station_id    = session.get('station_id', defaults['station_id'])
    circuit_flickity_index = list(circuits.keys()).index(circuit_id)

    return render_template(
        "index.html",
        circuits=circuits,
        circuit_flickity_index=circuit_flickity_index,
        time_tables=time_tables,
        circuit_id=circuit_id,
        station_id=station_id,
    )

@app.route('/ts')
def timetable():
    defaults    = app.config['DEFAULTS']
    circuits    = app.config['CIRCUITS']
    time_tables = app.config['TIME_TABLES']

    circuit_id = session.get('circuit_id', defaults['circuit_id'])
    circuit_id = request.args.get('circuit_id', circuit_id)
    circuit_id = int(circuit_id)
    station_id = session.get('station_id', defaults['station_id'])
    station_id = request.args.get('station_id', station_id)
    station_id = int(station_id)

    circuit = circuits[circuit_id]
    station = time_tables[circuit_id]['stations'][station_id]
    next_time_tables = get_time_tables(circuit_id, station_id)

    return render_template(
        "timetable.html",
        circuit=circuit,
        next_time_tables=next_time_tables,
        station=station
    )

@app.route('/circuit', methods=['POST'])
def set_circuit():
    circuit_id = request.json['circuit_id']
    session['circuit_id'] = circuit_id
    r = {
        'circuit_id': circuit_id
    }
    # jsonify
    res = jsonify(r)
    res.status_code = 200
    return res

def get_time_tables(circuit_id, station_id):
    # Time Table.
    time_tables = app.config["TIME_TABLES"]
    time_table = time_tables[circuit_id]
    exclude_hours    = time_table['exclude_hours']
    interval_minutes = time_table['interval_minutes']
    stations         = time_table['stations']

    # Station.
    station = stations[station_id]
    start   = station['start']
    s = start.split(':')
    start_hour = int(s[0])
    arrived_at = int(s[1])

    end     = station['end']
    e = end.split(':')
    end_hour   = int(e[0])
    end_minute = int(e[1])

    # current time.
    current_datetime = datetime.now(timezone('Asia/Tokyo'))
    current_year  = current_datetime.year
    current_month = current_datetime.month
    current_day   = current_datetime.day
    current_hour  = int(current_datetime.hour)
    current_min   = int(current_datetime.minute)

    next_hour = current_hour if current_min < arrived_at else current_hour + 1
    if next_hour in exclude_hours:
        next_hour = next_hour + 1

    # 次回候補が 開始時間よりも前の場合、開始時間に設定
    if next_hour < start_hour:
        next_hour = start_hour

    next_datetime = datetime(
        current_year,
        current_month,
        current_day,
        next_hour,
        arrived_at,
        0
    )
    end_datetime = datetime(
        current_year,
        current_month,
        current_day,
        end_hour,
        end_minute,
        0
    )

    # 次にバスがくる時刻
    next_time_tables = []
    while next_datetime <= end_datetime:
        d    = next_datetime.strftime('%Y-%m-%d %H:%M:%S')
        hour = next_datetime.hour
        next_datetime += timedelta(minutes=interval_minutes)
        if hour not in exclude_hours:
            next_time_tables.append(d)


    return next_time_tables

if __name__ == '__main__':
    app.run(host='0.0.0.0')
