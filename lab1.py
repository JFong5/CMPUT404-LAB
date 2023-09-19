import requests

#Request for the version
print(requests.__version__)

#get google homepage
google = requests.get("https://www.google.com/")
print("Google Homepage:", google.text)

#Print own source code
code = requests.get("https://raw.githubusercontent.com/JFong5/CMPUT404-LAB/main/lab1.py")
print("Source Code:", code.text)
