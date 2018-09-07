import requests
import json
import io


data = {}
http_proxy = ""
proxy = False
proxyDict = { 
              "http"  : http_proxy, 
            }
_email = ""
_password = ""
_username = ""
_host = ""
_port = 0

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
try  :
 with open('input.json') as data_file:
    data_loaded = json.load(data_file)
    _username  = data_loaded["name"]
    _password  = data_loaded["password"]
    _email = data_loaded["email"]
    if('httpProxy' in data_loaded) :
      proxy = True
      data_loaded2 = data_loaded["httpProxy"]
      try  :
       _port  =data_loaded2["port"]
       _host = data_loaded2["host"]
       n = str(data_loaded2["port"])
       http_proxy = "https://"+data_loaded2["host"]+":"+n
      except :
       print("something wrong when extract host and port variables please check!")
 params  = {
  "email": _email,
  "password": _password,
  "passwordCheck": _password,
  "username": _username
 }
 if len(_username) < 3 or len(_username) > 25 : 
  print("username requires > 2 characters and < 26")
 else :
   json_data = json.dumps(params)
   if proxy == True :
    r  = requests.post("http://pokemon-planet.com/index.php" , data  = params ,proxies=proxyDict )
   else :
    r  = requests.post("http://pokemon-planet.com/index.php" , data  = params  )
   if "Account successfully created. You may now log in." in r.text :
     print("your account register successfully")
     with io.open(_username+".json", 'w', encoding='utf8') as outfile:
      if proxy == False :
       dataoutput ={
         "name": _username,
         "password": _password
       }
      else :
        dataoutput ={
         "name": _username,
         "password": _password,
         "httpProxy" :{
               "host": _host,
               "port": _port
          }
       }
      str_ = json.dumps(dataoutput,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
      outfile.write(to_unicode(str_))
   elif  "his name is already in use by another member" in r.text:
    print("username is already taken")
   elif "is being used by a registered member already" in r.text :
    print("email is already taken")
   elif "Passwords aren't the same." in r.text :
    print("Password and passwordCheck are different")
   else :
    print(r.text)
except  :
  print("no file input found please put in same folder")

input("Press the <Enter> key on the keyboard to exit.")
