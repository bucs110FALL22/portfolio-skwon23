import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
  
class Alcohol:
  def __init__(self):
    self.url = "http://www.thecocktaildb.com/api/json/v1/1/search.php?i=%i"
    self.search = ""
    
 
    

  def main(self):
    
    response = requests.get(self.url + self.search)
    jprint(response.json())