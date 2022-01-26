import sys
import requests

#Change webhook here
webhookurl = "https://discordapp.com/api/webhooks/935853838819274792/UGeUh9ph6Lq8Cp89YhpZt6-K468ahlU7mz5n1Cvj1fZfIJV6nsj6zFH3W3s7gajafdTf"
data = {"content": str(sys.argv[1])}
response = requests.post(webhookurl, json=data)
print(response.status_code)
print(response.content)
