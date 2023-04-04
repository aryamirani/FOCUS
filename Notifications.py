# Import the following modules
import requests
import json
from functions import OpenPorts

# Function to send Push Notification


def pushbullet_noti(title, body):

	TOKEN = 'o.AXywoKPih45dKCjhY0ZyTwJ8ePGBkbW2' # Pass your Access Token here
	# Make a dictionary that includes, title and body
	msg = {"type": "note", "title": title, "body": body}
	# Sent a posts request
	resp = requests.post('https://api.pushbullet.com/v2/pushes',
						data=json.dumps(msg),
						headers={'Authorization': 'Bearer ' + TOKEN,
								'Content-Type': 'application/json'})
	if resp.status_code != 200: # Check if fort message send with the help of status code
		raise Exception('Error', resp.status_code)
	else:
		print('Message sent')

message = ''
for port in OpenPorts:
	message = '\n' + message + str(port) + '\n'

pushbullet_noti('Open Ports Detected:', message)