import time
from datetime import datetime, timedelta
import json


def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def getBusData(filename, origin_id, lat, lon, dest_id):
    trip_id = ""
    origin_time = 0
    current_time = f'{datetime.now().strftime("%H:%M:%S")}'
    #find origin_id time closest to current time
    with open(filename) as input_file:
        for i, line in enumerate(input_file):
            content = line.split(',')[3]
            if (content == origin_id):
                if (get_sec(current_time) > get_sec(line.split(',')[1])):  
                    if (origin_time > get_sec(current_time) - get_sec(line.split(',')[1]) or origin_time == 0): 
                        origin_time = get_sec(current_time) -  get_sec(line.split(',')[1])
                        origin_departure = line.split(',')[1]
                        trip_id = line.split(',')[0]
                else:
                    if (origin_time > get_sec(line.split(',')[1]) - get_sec(current_time) or origin_time == 0):
                        origin_time = get_sec(line.split(',')[1]) - get_sec(current_time)
                        origin_departure = line.split(',')[1]
                        trip_id = line.split(',')[0]

    #use origin_time to find closest dest time
    print(origin_time)
    with open(filename) as input_file:
        for i, line in enumerate(input_file):
            content = line.split(',')[0]
            if (line.split(',')[3] == dest_id and content == trip_id):
                if (get_sec(origin_departure) > get_sec(line.split(',')[1])):
                    time = get_sec(origin_departure) - get_sec(line.split(',')[1])
                    dest_arrival = str(timedelta(seconds=time) + timedelta(seconds=get_sec(origin_departure)))
                else:
                    dest_arrival = str(timedelta(seconds=get_sec(line.split(',')[1])))
                    
    try:
        dest_arrival
    except NameError:
        return {
            "statusCode": 500,
            "message": "Invalid. Please check origin ID or Destination ID"
        }
    else:
        return {
            "next_schedule": [
                {
                    "transit_mode": "Bus", 
                    "departure_time": origin_departure,
                    "arrival_time": dest_arrival
                }
            ]
        }


def getRailData(filename, origin_id, lat, lon, dest_id):
    if int(origin_id) > 161:
        transit_method = "Light Rail"
    else:
        transit_method = "Rail"
    trip_id = ""
    origin_time = 0
    current_time = f'{datetime.now().strftime("%H:%M:%S")}'
    #find origin_id time closest to current time
    with open(filename) as input_file:
        for i, line in enumerate(input_file):
            content = line.split(',')[3]
            if (content == origin_id):
                if (get_sec(current_time) > get_sec(line.split(',')[1])):  
                    if (origin_time > get_sec(current_time) - get_sec(line.split(',')[1]) or origin_time == 0): 
                        origin_time = get_sec(current_time) -  get_sec(line.split(',')[1])
                        origin_departure = line.split(',')[1]
                        trip_id = line.split(',')[0]
                else:
                    if (origin_time > get_sec(line.split(',')[1]) - get_sec(current_time) or origin_time == 0):
                        origin_time = get_sec(line.split(',')[1]) - get_sec(current_time)
                        origin_departure = line.split(',')[1]
                        trip_id = line.split(',')[0]
    #use origin_time to find closest dest time
    with open(filename) as input_file:
        for i, line in enumerate(input_file):
            content = line.split(',')[0]
            if (line.split(',')[3] == dest_id and content == trip_id):
                if (get_sec(origin_departure) > get_sec(line.split(',')[1])):
                    time = get_sec(origin_departure) - get_sec(line.split(',')[1])
                    dest_arrival = str(timedelta(seconds=time) + timedelta(seconds=get_sec(origin_departure)))
                else:
                    dest_arrival = str(timedelta(seconds=get_sec(line.split(',')[1])))
                    
    try:
        dest_arrival
    except NameError:
        return {
            "statusCode": 500,
            "message": "Invalid. Please check origin ID or Destination ID"
        }
    else:
        return {
            "next_schedule": [
                {
                    "transit_mode": transit_method, 
                    "departure_time": origin_departure,
                    "arrival_time": dest_arrival
                }
            ]
        }


# print(getRailData("stop_times_rail.txt", origin_id, 0, 0, dest_id))
