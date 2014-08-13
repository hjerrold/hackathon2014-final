#############Find ISE Username#########
def findISEUser(macAddress):
	url = 'https://iseipaddress/ise/mnt/ers/config/endpoint?filter=mac.EQ.bc:cf:cc:a3:6d:d3'
	headers = {'application/vnd.com.cisco.ise.identity.internaluser.1.0+xml'}
	response = requests.get(url, verify=False, auth=('team2','Password2'), headers=headers)
	xmldoc = minidom.parse(response.xml)
	username = xmldoc.getElementsByTagName(‘user_name’)
	print username
#############Move Camera#############
def movePTZCamera():
	url = 'https://VSMServer/ums/ManagedDevices/CameraControls/2dc27113-dd74-41fa-aa7d-b4fe66d47017/gotoPreset?index=1&priority=100&token=c77bc5bf-4d6a-49a0-984f-5dc6f28a61a2^LVEAMO^50^0^0^1350881423^275e8c4a3380118bdb8b3fd532255f1bd718ddf7'
	response = requests.get(url, verify=False, auth=('team2','Password2'))
	
#############Trigger Extension Pilot##############
#url='http://172.30.228.70:8081/EXHEALTH/fall/location%longitude%20:%s%20Latitude%20%s' %(long,lat)
#fall message is a precanned message
#variable of location%longitude%20:%s%20Latitude%20%s is the location of the fall
#requests.post(url, verify=False, auth=('Team2','Password2', headers=headers)

#############Jenkins#####################
#url='jenkinsurl/job/hackathon/build?token=adkjfiao7fi7oiji7oipj9ou2joi7'
#requests.post(url, verify=False, auth=('Team2','Password2', headers=headers)