import os
import random
from cs50 import SQL
from flask import Flask, render_template, request
#this part was taken from The Birthday Problem Question

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///football.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    
    return render_template("homepage.html")

@app.route("/match-up", methods=["GET", "POST"])
def matchup():

    if request.method == "POST":
        
        match = request.form.get("match")
        team1, team2 = "", ""
        
        if not match:
            return render_template("apology.html")
        elif match == "David v/s Goliath":
            while(True):
                team1 = db.execute("SELECT Club FROM players WHERE OVR > 83 ORDER BY RANDOM() LIMIT 1")
                team2 = db.execute("SELECT club FROM players WHERE OVR <= 75  AND OVR >= 70 ORDER BY RANDOM() LIMIT 1")
                if not team1 or not team2:
                    continue
                else:
                    break
            return render_template("matched.html", team1=team1, team2=team2, type=match)
        elif match == "Heavyweights":
            while(True):
                team1 = db.execute("SELECT club FROM players WHERE OVR > 86 ORDER BY RANDOM() LIMIT 1")
                team2 = db.execute("SELECT club FROM players WHERE OVR > 86 ORDER BY RANDOM() LIMIT 1")
                if team1 == team2:
                    continue
                else:
                    break
            return render_template("matched.html", team1=team1, team2=team2, type=match)
        elif match == "Derby":
            derbies = [["AC Milan", "Inter Milan"], ["Roma", "Lazio"], ["Liverpool ", "Everton"], ["Benfica", "Porto"], ["PSG", "Marseille"], ["Ajax", "Feyenoord"], ["Real Madrid", "Barcelona"], ["Borussia Dortmund", "FC Bayern Munich"], ["Celtic", "Rangers"], ["Fenerbahce", "Galatasaray"], ["Manchester United", "Manchester City"], ["Liverpool", "Manchester United"], ["Benfica", "Sporting Lisbon"], ["Arsenal", "Tottenham Hotspur"], ["East Bengal FC", "Mohun Bagan Super Giant"], ]
            i = random.randint(0,14)
            team1 = derbies[i][0]
            team2 = derbies[i][1]
            return render_template("matched.html", team1=[{'Club':team1}], team2=[{'Club':team2}], type=match)
        
    else:
        return render_template("match-up.html")
    

@app.route("/top-stars", methods=["GET", "POST"])
def topstars():

    if request.method == "POST":

        position = request.form.get("position")
        if not position:
            return render_template("apology.html")
        
        
        age = request.form.get("age")
        if not age:
            return render_template("apology.html")
        elif age == "less than 20":
            age = 20
        elif age == "less than 30":
            age = 30
        elif age == "less than 40":
            age = 40
        else:
            return render_template("apology.html")
        
        quality1 = request.form.get("quality1")
        quality2 = request.form.get("quality2")
        quality3 = request.form.get("quality3")

        #Only in this part of the code I had to take help from GitHub Copilot and CS50.ai
        #Whenever I submitted the form it showed me that the number of placeholders was more than the number of values provided.
        #I thought this might have happened because I was using placeholders foe column names, because it was required by my code.
        #I gave this part of the code to both GitHub Copilot and CS50.ai to debug it and to check for possible errors
        #Finally, I can to know that the problem was not in the placeholders, but rather in the execute() function
        #So, I read the CS50 Docs, but still couldn't fully understand the problem, but later I found out that the compiler maybe couldn't understand the difference between positional and named arguments
        #So, I just put an '*' before and the positional arguments and the code seemed to work
        query = "SELECT DISTINCT Name, OVR AS Overall, Age, Club, Nationality, Position FROM players INNER JOIN qualities ON players.Name = qualities.Playername WHERE players.Position = ? AND players.Age < ?"

        placeholders = [position, age]

        qualities = [quality1, quality2, quality3]
        Qualities = ['Hidden_Gem', 'Speedster', 'Defensive_Wall', 'Goal_Scoring_Beast', 'Complete_Player', 'Golden_Hands']
        for quality in qualities:
            if quality in Qualities:
                query += f" AND {quality} = 'Yes'"
                
        query +=  " ORDER BY OVR DESC LIMIT 10"

        players = db.execute(query, *placeholders)

        if len(players) == 0:
            return render_template("no-star.html")
        else:
            return render_template("found-stars.html", players=players, query=query, placeholders=placeholders)
    else:
        Positions = db.execute("SELECT DISTINCT position FROM players ORDER BY ATK DESC")
        Qualities = ['Hidden_Gem', 'Speedster', 'Defensive_Wall', 'Goal_Scoring_Beast', 'Complete_Player', 'Golden_Hands']
        return render_template("top-stars.html", positions=Positions, qualities=Qualities)
    
@app.route("/know-your-team", methods=["GET", "POST"])
def knowyourteam():
    if request.method == "POST":
        know = request.form.get("know")
        if not know:
            return render_template("apology.html")
        
        team = db.execute("SELECT * FROM teams WHERE Team = ?", know)
        return render_template("team-desc.html", team=team)
    else:
        teams = db.execute("SELECT Team FROM teams ORDER BY Team;")
        return render_template("know.html", teams=teams)