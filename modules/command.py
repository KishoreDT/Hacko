import os
import sys
sys.path.append("modules/")
import helper
import filescan
import urlscan
import ipscan

def Commands(message):

	try:
		if message[0] == "!help":
			helper.Features() # Write all features of the bot
			
		elif message[0] == "!filescan":
			if message[1]:
				try:	
					filescan.Filescan1(message[1])
				except:
					print("Check file path please")
			else:
				print("Bad syntax")	

		elif message[0] == "!urlscan":
			if message[1]:
				try:
					urlscan.Urlscan1(message[1])
				except:
					print("Check url please")
			else:
				print("Bad syntax")

		elif message[0] == "!ipscan":
			if message[1]:
				try:
					ipscan.Ipscan1(message[1])
				except:
					print("Check IP please")

		else:
			print("I dont know this command")

	except:
		print("**Try again, check your syntax. You can use !help command")
