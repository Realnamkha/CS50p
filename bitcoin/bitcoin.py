import sys
import requests
import json
while True:
    try:
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(json.dumps(response.json(), indent=2))
        break
    except ValueError:
        sys.exit("Input is not a number")