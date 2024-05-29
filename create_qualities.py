import os
from cs50 import SQL

db = SQL("sqlite:///football.db")

db.execute("CREATE TABLE qualities (Playername TEXT NOT NULL, Hidden_Gem TEXT DEFAULT 'No', Speedster TEXT DEFAULT 'No', Defensive_Wall TEXT DEFAULT 'No', Goal_Scoring_Beast TEXT DEFAULT 'No', Complete_Player TEXT DEFAULT 'No', Golden_Hands TEXT DEFAULT 'No')")

db.execute("INSERT INTO qualities (Playername) SELECT Name FROM players")


hidden = db.execute("SELECT name FROM players WHERE POT - OVR > 20")
speed = db.execute("SELECT name FROM players WHERE SPD > 86")
wall = db.execute("SELECT name FROM players WHERE DEF > 85")
beast = db.execute("SELECT name FROM players WHERE ATK > 83")
complete = db.execute("SELECT name FROM players WHERE(ATK+DEF+SPD+PASS)/4 > 80")
hands = db.execute("SELECT name FROM players WHERE GK > 83")

for i in range(len(hidden)):
    db.execute("UPDATE qualities SET Hidden_Gem = 'Yes' WHERE Playername = ?", hidden[i]['Name'])

for i in range(len(speed)):
    db.execute("UPDATE qualities SET Speedster = 'Yes' WHERE Playername = ?", speed[i]['Name'])
    
for i in range(len(wall)):
    db.execute("UPDATE qualities SET Defensive_Wall = 'Yes' WHERE Playername = ?", wall[i]['Name'])

for i in range(len(beast)):
    db.execute("UPDATE qualities SET Goal_Scoring_Beast = 'Yes' WHERE Playername = ?", beast[i]['Name'])

for i in range(len(complete)):
    db.execute("UPDATE qualities SET Complete_Player = 'Yes' WHERE Playername = ?", complete[i]['Name'])

for i in range(len(hands)):
    db.execute("UPDATE qualities SET Golden_Hands = 'Yes' WHERE Playername = ?", hands[i]['Name'])