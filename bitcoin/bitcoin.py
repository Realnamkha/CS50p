import sys
import requests
import json
while True:
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        for rate in o["bpi"]:
            
        break
    except ValueError:
        sys.exit("Input is not a number")
