# Agilis Coding Challenge

### Dependencies

- Python 3.6
- Docker

This repo contains the code for an AWS Lambda written in python to take data feeds obtained from NJ Transit. The resulting output will be the soonest departure time for the nearest origin station with the ETA which is also provided by NJ Transit.

### Example Inputs

The lambda endpoint will accept the following inputs as url parameters:

`origin_station_id` Ex: `38938` <br/>
`coordinates` Ex: `24.125, -74,010` <br/>
`destination_station_id` Ex: `1089`

### Example Output:

`{"next_schedule": [
      {
        "transit_mode": "Rail",
        "departure_time": "22:36:00",
        "arrival_time": "23:31:00"
      }
    ]
  }
}`

### Process

There will an initial lookup of times on the corresponding data feed (Bus or Rails), which will compare the current time to the closest and next available departure time. Afterwards, there will be a second lookup using the corresponding `Trip_ID`. If the Trip_ID is not valid for the origin station, an error will be thrown. The same is true for an invalid origin or destination.

Destination times are printed as is, unless the origin time is prior to the destination time. If this is the case, the destination time is subracted from the origin time, and the difference is added to the origin time.

### Containerization

This repo has been containerized using <a href="https://github.com/lambci/docker-lambda">docker-lambda</a> which containerizes the lambda in an environment that is almost identical to the AWS Lambda environment. The image can be found  <a href="https://hub.docker.com/repository/docker/gferrer807/agilis">here</a>

### Future Additions

Lat/Lon integration to find the closest station without an `origin_station_id`. One possible integration could be to use Elasticsearch which offers a ranking based on Lat/Lon coordinates.

Unit testing using PyUnit