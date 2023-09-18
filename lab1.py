import requests

#Request for the version
print(requests.__version__)

#get google homepage
print(requests.get("http://google.com/"))
