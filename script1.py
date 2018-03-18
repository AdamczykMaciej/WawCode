from flask import Flask, render_template
#import googlemaps
#from datetime import datetime
import route_guide_pb2
import route_guide_pb2_grpc
import grpc
import json
from google.protobuf.json_format import MessageToJson

# gmaps = googlemaps.Client(key='AIzaSyBffodETNeaEdS1171Mg9HFDMF7AHUI4SE')
# geocode_result = gmaps.geocode('Lebiodowa, Warsaw')
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
#
# print(geocode_result)
# print(reverse_geocode_result)

channel = grpc.insecure_channel('130.211.231.90:30078') # connects to the service :)
stub = route_guide_pb2_grpc.EventsServiceStub(channel) # gets a class

def run():
    #channel = grpc.insecure_channel('130.211.231.90:30078') # connects to the service :)
    #stub = route_guide_pb2_grpc.EventsServiceStub(channel) # gets a class
    location = route_guide_pb2.Location(Lat = 52.22604, Lon = 20.94154) # returns the location
    request = route_guide_pb2.EventsInDistanceRequest(location = location, distance = 5000)
    res = stub.EventsInDistance(request) # returns an array of events
    with open('data.txt', 'w') as outfile:
        for event in res.events:
            print(event) # returns the an event
            jsonObj = MessageToJson(event)
            print(jsonObj)
            json.dump(jsonObj, outfile)
    #print(jsonObj)

    #print(jsonObj)
    # print("-------------- GetFeature --------------")
    # guide_get_feature(stub)
    # print("-------------- ListFeatures --------------")
    # guide_list_features(stub)
    # print("-------------- RecordRoute --------------")
    # guide_record_route(stub)
    # print("-------------- RouteChat --------------")
    # guide_route_chat(stub)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/about/')
def about():
    return render_template("about.html")
#@app.route('/event/<id>')
#def event(id):


@app.route('/events/<lat_string>/<lon_string>/<dist_string>')
def events(lat_string, lon_string, dist_string):
    lat = float(lat_string)
    lon = float(lon_string)
    dist = int(dist_string)

    location = route_guide_pb2.Location(Lat = lat, Lon = lon) # returns the location
    request = route_guide_pb2.EventsInDistanceRequest(location = location, distance = dist)
    res = stub.EventsInDistance(request)
    jsonObj = MessageToJson(res)
    return json.dumps(jsonObj)

if __name__=="__main__":
    #run()
    app.run(debug=True)
