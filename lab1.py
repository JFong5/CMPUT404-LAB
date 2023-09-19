import requests

#Request for the version
print(requests.__version__)

#get google homepage
print("Status Code:", requests.get("http://google.com/"))

#Print own source code
code = requests.get("https://raw.githubusercontent.com/JFong5/CMPUT404-LAB/main/lab1.py")
print("Source Code:", code.text)
