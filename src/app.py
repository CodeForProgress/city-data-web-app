from flask import Flask, render_template, request
from livereload import Server
from datetime import datetime
from modules.gov_track import *  


import urllib2
import json
import sunlight
import lob
import googlemaps
import tweepy

app = Flask(__name__)
app.debug = True

sunlight.config.API_KEY = "ed9d8054bcca4773a803aa8c9b77e79a"
lob.api_key = "test_32f9cf853c605d272e35567fadb984b4318"
gmaps = googlemaps.Client(key='AIzaSyBuBYoY9OiVXnJnQf3D1jFG_iBOjqJkzw8')

# Tweepy Setup
auth = tweepy.OAuthHandler('09mB3DUJsg9agik4sGw4DJ0jA', 'wM4focfIFuE8Gz3f2EX3dM3EHox4BVRNbedjNdchM24vRlRObL')
auth.set_access_token('1559211414-3ApuTjxIy7Ivr25Vn6GXHUNSEjYa8SE9H6yCbLR', 'FosDpZ9S0pSU0omTfnbpCG8rF14S85VRVJ1wb2ngdNhgc')
api = tweepy.API(auth)

@app.route("/")
def home():

	return render_template("home.html")

@app.route("/search", methods=["POST", "GET"])
def search():
	if request.method == "POST"
		addressLine1 = request.form['addressLine1']
		addressLine2 = request.form["addressLine2"]
		city = request.form['city']
		state = request.form['state']
		zipCode = request.form['zipCode']

	return "The address is: %s, %s %s, %s %s" %(addressLine1,addressLine2,city,state,zipCode)


Server(app.wsgi_app).serve()

