Group Members: 
	Matthew Guo and Richard Chen 
Instructions:
	1. Run the server.py file on Raspberry Pi. Please note, IP address coded in the client.py file may need to be changed in accordance with your setup. 
	2. Run the client.py file on Mac.
	3. Have a phone with the 'sonic' app ready, with the frequency audible
	4. Press enter and place the frequency source near the microphone of the local machine for 	   about a second.
	5. If the frequency is correct, then type the message you want to send. If the frequency is 	   wrong, then the program would automatically stop.
	6. The message should appear on the LCD screen
	7. After 5 seconds, the LCD screen will be reset
Libraries: 
	client.py: 
		import requests
		import pprint
		import pyaudio
		import wave
		import json 
		import numpy as np
		from scipy.io import wavfile
		import matplotlib.pyplot as plt
		import time
	server.py:
		from flask import Flask, request, jsonify
		from grove_rgb_lcd import *
		import grovepi