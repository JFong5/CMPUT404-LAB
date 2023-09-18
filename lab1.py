import requests

#Request for the version
print(requests.__version__)

#get google homepage
print("Status Code:", requests.get("http://google.com/"))

#Print own source code
code = requests.get("https://github.com/JFong5/CMPUT404-LAB/blob/main/lab1.py")
print("Source Code:", code.text)
