import requests

#Request for the version
print(requests.__version__)

#get google homepage
print(requests.get("http://google.com/"))

#Print own source code
code = requests.get("https://github.com/JFong5/CMPUT404-LAB/blob/main/lab1.py")
print(code.text)
