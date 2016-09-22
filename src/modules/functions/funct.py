import urllib2
import json

def breezometer(latitude, longitude):
    
    f = urllib2.urlopen("https://api.breezometer.com/baqi/?lat=" + str(latitude) + "&lon=" + str(longitude) + "&key=ecf323791dbc458da50f98712afa89f3")
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    
    air_quality_dict = {"Air Quality": parsed_json["breezometer_description"], "Main Pollutant": parsed_json["dominant_pollutant_description"], "Pollutant Causes": parsed_json["dominant_pollutant_text"]["causes"], "Health Damage from Pollutant": parsed_json["dominant_pollutant_text"]["effects"], "Precausions for Parents": parsed_json["random_recommendations"]["children"], "Health Precausions": parsed_json["random_recommendations"]["health"], "Indoor Air Quality": parsed_json["random_recommendations"]["inside"], "Outside Air Quality": parsed_json["random_recommendations"]["outside"], "Recommendations While Sporting": parsed_json["random_recommendations"]["sport"]}
    airQuality = air_quality_dict
    return airQuality


