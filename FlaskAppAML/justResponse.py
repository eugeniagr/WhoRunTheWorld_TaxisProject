import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'distance': "1",   
                            'cab_type': "",   
                            'name': "",   
                            'temp': "1",   
                            'rain': "1",   
                            'day': "1",   
                            'hour': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/7f5b50e1d4c747779d1d23d9b3ee6629/services/cf44a1b883de4b94911e4029f2ec804f/execute?api-version=2.0&format=swagger'
api_key = '+xY4jJ2dDpls+QmcIOiulJ91+LizTgJKvNuf3g5G22pVNK5RwnQ1CrIfTfSYlfAxZtkk9p6uJgtLWMVu5s+W6Q==' # Replace this with the API key for the web service
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
