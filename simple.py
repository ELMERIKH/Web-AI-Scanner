import sys 
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <URL>")
    sys.exit(1)
url = sys.argv[1]
if url.startswith("https://"):
    url = url.replace("https://", "", 1)
if url.startswith("http://"):
    url = url.replace("http://", "", 1)

ip = socket.gethostbyname(url)
print("[+] location scan :\n  The IP address of " + url + " is: " + ip + "\n")

req2 = requests.get("https://ipinfo.io/" + ip + "/json")
resp = json.loads(req2.text)

print("Location: " + resp["loc"])
print("City: " + resp["city"])
print("Region: " + resp["region"]) 
print("Country: " + resp["country"])