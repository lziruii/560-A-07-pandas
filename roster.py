# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

player = {"Last Name":['Bacot', 'Davis', 'Cadeau','High','Ryan','Trimble','Wojcik','Washington','Lebo','Landry'],
          "First Name": ["Armando","RJ","Elliot","Zayden","Cormac","Seth","Paxson","Jalen","Creighton","Rob"],
          "height":[84, 72, 73, 79, 77, 75, 77, 82, 73, 76],
          "weight":[240,180,180,225,195,195,195,230,180,190]
}
data = pd.DataFrame(player)

#bmi  = weight in kg/ height in meters squared
data["bmi"] = (data["weight"]/2.2050)/((data["height"]/39.37)**2)
data_number = round(data, 2)

print(data_number)

data.to_csv("bmi.csv")
