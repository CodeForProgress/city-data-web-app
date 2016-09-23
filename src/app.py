from flask import Flask, render_template, request, redirect, session
from livereload import Server
from datetime import datetime
from modules.gov_track import * 
from modules.functions.funct import *
from random import randint

import urllib2
import json
import sunlight
import lob
import googlemaps
import tweepy

app = Flask(__name__)
app.debug = True
app.secret_key = 'wou029092101983i32wop823'

sunlight.config.API_KEY = "ed9d8054bcca4773a803aa8c9b77e79a"
lob.api_key = "test_32f9cf853c605d272e35567fadb984b4318"
gmaps = googlemaps.Client(key='AIzaSyBuBYoY9OiVXnJnQf3D1jFG_iBOjqJkzw8')

# Tweepy Setup
auth = tweepy.OAuthHandler('09mB3DUJsg9agik4sGw4DJ0jA', 'wM4focfIFuE8Gz3f2EX3dM3EHox4BVRNbedjNdchM24vRlRObL')
auth.set_access_token('1559211414-3ApuTjxIy7Ivr25Vn6GXHUNSEjYa8SE9H6yCbLR', 'FosDpZ9S0pSU0omTfnbpCG8rF14S85VRVJ1wb2ngdNhgc')
api = tweepy.API(auth)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method=="POST":
		addressLine1 = request.form["addressLine1"]
		addressLine2 = request.form["addressLine2"]
		city = request.form["city"]
		state = request.form["state"]
		zipCode = request.form['zipCode']
		try:
			verifiedAddress = lob.Verification.create(
				address_line1=addressLine1,
				address_line2=addressLine2,
				address_city=city,
				address_state=state,
				address_zip=zipCode, 
				)

			session['address'] = verifiedAddress['address']
			return redirect('/%s' %session['address']['address_city'])

		except lob.error.InvalidRequestError:
			error_message = "Invalid address. Please try again."
			return render_template('home.html', error_message=error_message)

@app.route("/<city_name>")
def city_info(city_name):
	address = session['address']['address_line1'] + ',' + session['address']['address_city'] + ',' + session['address']['address_state']
	city = session['address']['address_city']
	state = session['address']['address_state']
	geocode_results = gmaps.geocode(address)

	latitude = geocode_results[0]['geometry']['location']['lat']
	longitude = geocode_results[0]['geometry']['location']['lng']

	weatherFile = weather(city, state)
	
	try: 
		weatherAlert = {"description": weatherFile["alerts"][0]["description"], "message": weatherFile["alerts"][0]["message"]}
	except IndexError:
		weatherAlert = False


	currentTemp = weatherFile["current_observation"]["temperature_string"]

	dailyForecast = weatherFile["forecast"]["simpleforecast"]["forecastday"]

	# airQuality = breezometer(latitude, longitude)

	image = cityImage(city)[randint(0,3)]


	return render_template('city.html', cityName = city, weatherAlert = weatherAlert, dailyForecast = dailyForecast, currentTemp = currentTemp, cityImage = image)




Server(app.wsgi_app).serve()

