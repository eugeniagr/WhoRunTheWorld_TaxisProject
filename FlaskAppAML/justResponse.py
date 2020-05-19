import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Column 0': "1",   
                            'distance': "1",   
                            'cab_type': "",   
                            'price': "1",   
                            'surge_multiplier': "1",   
                            'name': "",   
                            'temp': "1",   
                            'clouds': "1",   
                            'pressure': "1",   
                            'rain': "1",   
                            'time_stamp_w': "1",   
                            'humidity': "1",   
                            'wind': "1",   
                            'day': "1",   
                            'hour': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7065fb6f40454835bea030055b531ec5/services/a50b4b7a773d416eb39655241323070c/execute?api-version=2.0&format=swagger'
api_key = 'WfcDYeHh9RYodvvL0B7DJUEaEv3Ar6Bst0/Jb044iEkw7wSyzwo430vB+fXC8Mj8Csl1vXStim0od9geyBXmHg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))