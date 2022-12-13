import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
  
class Meal:
  def __init__(self):
    self.url = "http://www.themealdb.com/api/json/v1/1/search.php?s=%s"
    self.search = ""
    
 
    

  def main(self):
    
    response = requests.get(self.url + self.search)
    jprint(response.json())