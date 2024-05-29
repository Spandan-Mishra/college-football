import csv
import sqlite3
#The idea to convert data from a CSV File into an SQL file, was of my own
#I had to read online documentations and code from other websites to write this code
#Combining stats to create the columns of the SQL table was also my own idea
#The CSV File was taken from Kaggle, https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?select=FIFA22_official_data.csv

conn = sqlite3.connect('football.db')

c = conn.cursor()

with open('./static/FIFA22_official_data.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        c.execute('INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (row['Name'], int(row['Age']), row['Club'], row['Nationality'], row['Best Position'], float(row['Overall']), (float(row['Crossing'])+float(row['Finishing'])+float(row['HeadingAccuracy'])+float(row['ShortPassing'])+float(row['Volleys'])+float(row['Dribbling'])+float(row['LongShots']))/7, (float(row['Interceptions'])+float(row['StandingTackle'])+float(row['SlidingTackle']))/3, (float(row['GKDiving'])+float(row['GKHandling'])+float(row['GKKicking'])+float(row['GKPositioning'])+float(row['GKReflexes']))/5, (float(row['BallControl'])+float(row['Acceleration'])+float(row['SprintSpeed'])+float(row['Agility']))/4, (float(row['ShortPassing'])+float(row['Curve'])+float(row['LongPassing'])+float(row['Vision']))/4, float(row['Potential'])))



conn.commit()

conn.close()