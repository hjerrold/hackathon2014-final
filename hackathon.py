
#from xml.dom.minidom import parse, parseString
from hummingbird import Hummingbird
from time import sleep
import tweepy
import requests
import json
import math
from collections import Counter
from collections import OrderedDict


humm = Hummingbird()
knob = humm.get_knob_value(1)

# Loop until knob is 255 away detected
while knob < 255:
    knob = humm.get_knob_value(1)
    print(knob)
    sleep(0.2)


#############turn on light
humm.set_single_led(1, 255)


############Get coordinates of static object

url = 'https://10.87.103.20:443/api/contextaware/v1/maps/'
headers = {'Accept': 'application/json'}

response = requests.get(url, verify=False, auth=('team2','Password2'), headers=headers)
binary = response.content
data = json.loads(binary)

mydata = data['Maps']['Campus'][0]['Building'][0]['Floor'][0]['GPSMarker'][1]['GeoCoordinate']

lat = mydata.get('lattitude')
long = mydata.get('longitude')
#print "the mac address is located on", buildingZone, "x coordinate", xCoord, "y coordinate", yCoord
#print "lattitude is: ", lat
#print "long is: ", long
#print mydata


#############Trigger Extension Pilot##############
#url='http://172.30.228.70:8081/EXHEALTH/fall/location%longitude%20:%s%20Latitude%20%s' %(long,lat)
#fall message is a precanned message
#variable of location%longitude%20:%s%20Latitude%20%s is the location of the fall
#requests.post(url, verify=False, auth=('Team2','Password2', headers=headers)

#############Jenkins#####################
#url='jenkinsurl/job/hackathon/build?token=adkjfiao7fi7oiji7oipj9ou2joi7'
#requests.post(url, verify=False, auth=('Team2','Password2', headers=headers)




#############Send TWEET of static object#################
#Login
consumer_key="POTbokML3BP1Q0qvclxh7Rp5S"
consumer_secret="xbBmWnbOrcyUO1WCO2ABIQbeWDXFzfToWgSkxigiHuiV4x6i7X"
access_token="2717225706-CuFQswi3jNv5szoRKrzehq7cnxFnguTAtHbJwXM"
access_token_secret="JBYjpXysiJXriuzLCaLrwFduS4KfodBHrQlhWdYxuJPEw"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

tweet = tweepy.API(auth)

#send a direct message
googleStaticMap = 'http://maps.google.com/?q=%s,%s' %(lat,long)
tweet.send_direct_message(user='jtfish4', text=('Static Object', googleStaticMap))




#############Get coordinates of phone
url = 'https://10.87.103.20:443/api/contextaware/v1/location/clients/bc:cf:cc:a3:6d:d3'
headers = {'Accept': 'application/json'}

response = requests.get(url, verify=False, auth=('team2','Password2'), headers=headers)
binary = response.content
data = json.loads(binary)

mydata = data['WirelessClientLocation']['GeoCoordinate']
#print mydata
latPhone = mydata.get('lattitude')
longPhone = mydata.get('longitude')

myXY = data['WirelessClientLocation']['MapCoordinate']

myX = myXY.get('x')
myY = myXY.get('y')
#print latPhone
#print longPhone

#############Send TWEET of phone object#################
#Login
consumer_key="POTbokML3BP1Q0qvclxh7Rp5S"
consumer_secret="xbBmWnbOrcyUO1WCO2ABIQbeWDXFzfToWgSkxigiHuiV4x6i7X"
access_token="2717225706-CuFQswi3jNv5szoRKrzehq7cnxFnguTAtHbJwXM"
access_token_secret="JBYjpXysiJXriuzLCaLrwFduS4KfodBHrQlhWdYxuJPEw"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

tweet = tweepy.API(auth)

#send a direct message
googleStaticMapPhone = 'http://maps.google.com/?q=%s,%s'% (latPhone,longPhone)
tweet.send_direct_message(user='jtufail', text=('Moving Object', googleStaticMapPhone))

##############Find Closest wireless devices
url = 'https://10.87.103.20:443/api/contextaware/v1/location/clients'
headers = {'Accept': 'application/json'}

response = requests.get(url, verify=False, auth=('team2','Password2'), headers=headers)
binary = response.content
data = json.loads(binary)


myRealX = myX
myRealY = myY


mymac = data['Locations']['entries']
newdict = {}
userid = 1

newdict2 = {}
for thismac in mymac:
	mac= thismac['macAddress']
	tempx= thismac['MapCoordinate']['x']
	tempy= thismac['MapCoordinate']['y']
	trueX = math.fabs(tempx-myRealX)
	trueY = math.fabs(tempy-myRealY)
	dist = math.sqrt(pow(trueX,2)+pow(trueY,2))
	newdict2[mac]=dist

sortedDict=Counter(newdict2).most_common()[::-1]
print '\n\n\n\n\n\n\n\n'
print '-' * 8
for k,v in sortedDict:
	print("{} : {}".format (k,v))

##############Close hummingbird
# Loop until knob is 255 away detected
while knob > 1:
    knob = humm.get_knob_value(1)
    #print(knob)
    sleep(0.2)
