
import geocoder
g = geocoder.ip('me')


def currentCoordinates():
    time = ''
    coordinates = g.laitlng
    payload = {"time": "", "coordinates": coordinates}
    print(payload)
