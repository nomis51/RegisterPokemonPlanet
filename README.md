# RegisterPokemonPlanet
 
 APP base on Python to register an account with pokemon-planet.com. 
 
 How to use ? 
 we need  2 file to run 
 1 . input.json file
 2. RegisterPokemonPlanet.exe file 
 
 Step :
 1 . Fill information into input.json file
 
 name , password , email are string (Ex : "name" : "pokemasterrrr")
 
 If you want to use proxy to register :
 
 Keep httpproxy , host , port 
 
 port is a number (Ex : "port" : 8080)
 
 
 If you dont want to use proxy to register  :
 
 Delete httpproxy , host , port  , i will be like this  :
 
 {
 
  "name": "abc",
  
  "password": "abc",
  
  "email" : "abc",
  
  }
  
 2. Then run RegisterPokemonPlanet.exe file or Build code with Python 3.x and SublimeText, Pycharm ,...
 After  the coded  run succesfully  it will export json file for you that you can use for PPORise bot or for managing . Enjoy !
