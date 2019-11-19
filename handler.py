import json
import parse
from datetime import datetime


def codingChallenge(event, context):
    params = event["queryStringParameters"]

    filename = "rail_info.json"
    # Read JSON data into the datastore variable
    if filename:
        with open(filename, "r") as f:
            datastore = json.load(f)

    if params["origin_station_id"] in datastore:
        # go through rails data
        respBody = parse.getRailData(
            "stop_times_rail.txt",
            params["origin_station_id"],
            0,
            0,
            params["destination_station_id"],
        )
    else:
        respBody = parse.getBusData(
            "stop_times_bus.txt",
            params["origin_station_id"],
            0,
            0,
            params["destination_station_id"],
        )
        # go through bus data
    return {"statusCode": 200, "body": json.dumps(respBody)}
