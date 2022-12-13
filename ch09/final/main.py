import requests
import json
import meal
import alcohol

alcohol = alcohol.Alcohol()
meal = meal.Meal()
   
def main():
  #when using meal.search = input("What meal do you want to eat?"), it causes a error that only prints out null results.
  print("What meal do you want to eat?")
  input(meal.search)
  print("What alcohol drink do you want to drink?")
  input(alcohol.search)
  meal.main()
  alcohol.main()
  

main()