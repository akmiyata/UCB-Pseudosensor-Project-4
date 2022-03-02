import requests
response = requests.get("https://dvmjby15r5.execute-api.us-east-2.amazonaws.com/default/Gate_Send")
print(response.text)