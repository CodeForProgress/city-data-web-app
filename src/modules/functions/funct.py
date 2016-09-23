import urllib2, cStringIO, urllib
import json
import pprint
from random import randint
import os, sys

# -*- coding: utf-8 -*- 

def breezometer(latitude, longitude):
    
    f = urllib2.urlopen("https://api.breezometer.com/baqi/?lat=" + str(latitude) + "&lon=" + str(longitude) + "&key=ecf323791dbc458da50f98712afa89f3")
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    
    air_quality_dict = {"Air Quality": parsed_json["breezometer_description"], "Main Pollutant": parsed_json["dominant_pollutant_description"], "Pollutant Causes": parsed_json["dominant_pollutant_text"]["causes"], "Health Damage from Pollutant": parsed_json["dominant_pollutant_text"]["effects"], "Precausions for Parents": parsed_json["random_recommendations"]["children"], "Health Precausions": parsed_json["random_recommendations"]["health"], "Indoor Air Quality": parsed_json["random_recommendations"]["inside"], "Outside Air Quality": parsed_json["random_recommendations"]["outside"], "Recommendations While Sporting": parsed_json["random_recommendations"]["sport"]}
    airQuality = air_quality_dict
    return airQuality


def weather(city, state):
    weather = urllib2.urlopen('http://api.wunderground.com/api/d13977cb92663c84/alerts/conditions/forecast/forecast10day/q/' + state + "/" + city.replace(" ", "_") + '.json')
    json_string = weather.read()
    weatherFile = json.loads(json_string)
    weather.close()

    return weatherFile

def cityImage(city):
    imageFile = urllib2.urlopen('https://api.unsplash.com/search/photos?&query=' + city.replace(" ", "%20") + '&client_id=7c2701f5c05bf660ca41c6fd0e792994c7375c54d0c64e06c3997f7d82980b02')
    json_string = imageFile.read()
    images = json.loads(json_string)
    imageFile.close()

    x = images["results"][:4]

    imageList = []

    for image in x:
        imageList.append(image["urls"]["regular"])
    return imageList

def geo_images(lat,lng):
    api_key = "AIzaSyDPJuBOQjOllMxsNBkVTPLIJFevlRA7x2w"
    imageFile = urllib2.urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+ str(lat) + "," + str(lng) + "&radius=200&key="  + api_key)
    json_string = imageFile.read()
    images = json.loads(json_string)
    imageFile.close()

    place_id = images["results"][0]["place_id"]

    imageFile = urllib2.urlopen("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + place_id + "&key=" + api_key)
    json_string = imageFile.read()
    images = json.loads(json_string)
    imageFile.close()
    image_id_list = []

    for image in images["result"]["photos"]:
        image_id_list.append(image["photo_reference"])

    photo_reference = image_id_list[randint(0,(len(image_id_list)-1))]

    return photo_reference



