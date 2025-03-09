
import time
import geocoder
g = geocoder.ip('me')


def currentCoordinates():
    current_time = time.asctime()
    coordinates = g.latlng
    payload = {"time": current_time, "coordinates": coordinates}
    return payload
