import sys 
import requests
import socket
import json

if len(sys.argv) < 2: print("Usage: " + sys.argv[0] + " """) 
sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

ip = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + ip + "\n")

req2 = requests.get("https://ipinfo.io/" + ip + "/json") 
resp = json.loads(req2.text)

print("Location: " + resp["loc"])
print("City: " + resp["city"])
print("Region: " + resp["region"]) 
print("Country: " + resp["country"])