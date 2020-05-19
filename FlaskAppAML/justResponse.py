 
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Column 0': "0",   
                            'distance': "0.44",   
                            'cab_type': "Lyft",   
                            'price': "5",   
                            'surge_multiplier': "1",   
                            'name': "Shared",   
                            'temp': "38.46",   
                            'clouds': "0.29",   
                            'pressure': "1022.25",   
                            'rain': "0",   
                            'time_stamp_w': "1544953501",   
                            'humidity': "0.76",   
                            'wind': "7.68",   
                            'day': "6",   
                            'hour': "9",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7065fb6f40454835bea030055b531ec5/services/faabf68e26524eae81063780e2d0f823/execute?api-version=2.0&format=swagger'
api_key = 'abc123' # Replace this with the API key for the web service
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
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Column 0': "0",   
                            'distance': "0.44",   
                            'cab_type': "Lyft",   
                            'price': "5",   
                            'surge_multiplier': "1",   
                            'name': "Shared",   
                            'temp': "38.46",   
                            'clouds': "0.29",   
                            'pressure': "1022.25",   
                            'rain': "0",   
                            'time_stamp_w': "1544953501",   
                            'humidity': "0.76",   
                            'wind': "7.68",   
                            'day': "6",   
                            'hour': "9",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7065fb6f40454835bea030055b531ec5/services/faabf68e26524eae81063780e2d0f823/execute?api-version=2.0&format=swagger'
api_key = 'niVoiBEitkNPMB9nxWC97cHc33jqphpImgETjO8r+D1zH1KvWnA+5d0lq8KUa/csUoxNXZvWNe7HeiCxnBbGuA==' # Replace this with the API key for the web service
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
