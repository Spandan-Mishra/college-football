# COLLEGE FOOTBALL
#### Video Demo: [Video Walkthrough for the College Football Website]https://www.youtube.com/watch?v=oK74ONvYrzM
## Description:

### About the project:
College Football website was designed in order to make the gaming experience of football games more fun, interactive and enjoyable. Players can usually get a bit bored by repititive nature of the game, so to make things more exciting three features were added. 
- The first one was the **Match-Up** feature. Here the user can choose from _David v/s Goliath_, _Heavyweights_ and _Derby_ modes. According to the choice of the user, two random teams will be assigned to two players. This makes the team selection unpredictable and allows the user to try out more teams and different gameplay modes.
- The second feature was **Top-Stars**. Here, the user can get the perfect player according to his needs. The user will provide his player's playing position, his age range and additionally the special qualities which he wants in his player. This can give rise to multiple different combinations of positions, ages and qualities, and the top players that fit into the specified category will be displayed.
- The third and last feature is **Know Your Team**. Users who are new to football or who do not have enough knowledge about the teams will find this feature useful. The user has to select a team from the given pool of teams and a brief description about the selected team will be displayed, describing their history, greatest achievements, the playstyle of the team and also some of the team's best players.

(The functionality of these features will be explained below)

### static folder:
This folder contains all the media which was used in the creation of the website, alongwith the styles.css file and the CSV file which was used to get the information about all the players and the teams.
The CSS file contains hover effects, fonts, and some tags and class related modifications.

### football.db:
The SQL file which stores all the tables storing all of the important and required data.
- **players** table stores the information for about 17,000 players. It contains detailed information about them, like their Name, age, the club for which they play, their nationality, and their stats like attcking, defence etc. This data was taken from the CSV file referred to earlier, which was taken from Kaggle. I designed the stats for the players according to my needs, by combining the data which was present in the CSV file.
> [!NOTE]
> The information for the players is according to the 21-22 football season.

- The **qualities** table stores name of all players, alongwith the qualities which they have. These are the same qualities as referred to in the Top-Stars feature. A player having the quality with have a 'Yes' in that quality's column, while one not having it will have a 'No'.

- The last table is the **teams** table. This table contains close to 30 teams (clubs and national teams) and a description about them. It is used in the Know Your Team feature.
> [!NOTE]
> Some information for the teams may not be accurate as of 2024.

### insert_into_players.py:
Using this python program, I extracted the data from the CSV file into the players table. The inspiration for the code was taken from some online codes, which I read and implemented in my code. The program opens the CSV file and uses a reader to read its data, and then iterates through each row and inserts the corresponding values into the table. Since, the original file had many stats for a single player, I combined them and created new stats which very sufficient and neccessary for my program.

### create_qualities.db:
In this python program the qualities table was created. The columns for this table are the name of the player, and columns representing the player qualities like - Speedster, Hidden Gem, Goal-Scoring Beast, Defensive Wall, Complete Player, and Golden Hands. Initially all players from the players table are inserted into this table, and since the default value of all columns is *'No'*, they are initialized with it.
Then, 6 different SQL SELECT queries are executed and the lists of dictionaries returned by them are stored in 6 variables. The SQL queries are designed in such a manner that the players matching the conditions surely possess the specific quality from the different qualities mentioned above. Then each of the 6 lists are traversed and the quality corresponding to the list is changed to *'Yes'* for each player in the list.
In this way, each player who matches the conditions designed by me is assigned a quality, this adds an additional interesting layer into the player searching mechanism.

### templates:
Templates folder contains all of the html files which are used for this project. I will be explaining each of the html files and their usage one by one.

- #### layout.html:
The first and the most important html file is **layout.html**.
I've kept the default mode of the website to be *dark mode* by using Bootstrap syntax.
For the title I kept it nice and simple by keeping the name of the website and a jinja title tag which can be used by other html files.
Then I proceeded to connecting various resources required for my project. These include - Bootstrap CSS and JS links, link to Google Fonts and the stylesheets for the respective fonts, link to CSS and JS of Select2 using Bootstrap which I found on its website because I wanted to create a custom select element with the ability to search and select, and finally the link to my styles.css file.
Next a navbar, with the links to other pages was created using Bootstrap.
Then a main block was created using jinja, which will contain the contents of each page.
Finally, I added a basic footer which contains the links to my socials.

- #### homepage.html:
This is the first page which the user sees when they enter the website. It is the homepage of College Football.
The first element of this webpage is the carousel. It is a basic carousel taken from Bootstrap. Its first element being a GIF which I made myself. Next there are images of football games and of people playing games.
Next up their is a section for the features of this website, which where discussed earlier. I have used the Cards from Bootstrap to make this section. I also added a hover effect to the card and the text in it to give it a better look.
Lastly, there is an about us section which tells the user the idea behind making this website and what it aims at achieving. 
I have tried to give this website a professional look, and I have also created multiple places where I can work upon later, if I want to expand on this project and create a full-fledged website using this idea.

- #### match-up.html:
This is the website where the user is taken to when the select the Match-Up feature. Here. first they are introduced to the concept of the feature via an introduction. Next up they have to select from three different modes which were mentioned earlier. Two teams get assigned to the players according to their choice.
The select box was made using Select2 which was referred to earlier in *layout.html*

- #### apology.html:
apology.html is rendered whenever the user fails to input all of the required fields. It gives them an error message and asks them to return back and fill out all information.

- #### matched.html:
After choosing their gamemode in match-up.html, the user gets two teams assigned to two players. Using jinja, the two teams are displayed as table body content. A paragraph element is used to display to the user the gamemode which they chose as well as both of the teams' names.

- #### top-stars.html:
This particular feature was the most fun as well as the most difficult to implement (implementation explained in ***app.py***).
The webpage starts off with an introduction to the idea behind this featuere. Bascially, by taking some inputs from the user, we will be able to predict the best players that macth their needs. 
Again, Select2 was used to create the select elements in this page. The user selects the position, qualities (None, one or more) from three different selection options and finally an age range. After submitting this info, they will get output based on it.

- #### no-star.html:
When the input given by the user is posted, and no player matching their choices exists, this page is showed to the user, telling them that no player profile matched their needs and that they should try out some other combination of inputs.

- #### found-stars.html:
If there exists atleast one player who matches the input given by the user, this page is showed to them.
It consists of a table listing the name, afe, overall, club, nationality and position of all the players who match the combination of inputs.
A hover effect is added to the tr tags in order to give the website a modern and gamer-like look.

- #### know.html:
The last feature of the website is Know Your Team, and this is the page where the visitor is redirected to if they want to use this feature.
It has a very simple layout, consisting an introduction to the feature and a select tag which displays the names of all the available teams, and this is where Select2 becomes most useful. Instead of scrolling through the list of teams, the user can also type in few initial letters of the team, and if it is present in the list of the teams, it will automatically get selected.

- #### team-desc.html:
This page displays a 6-7 line description about the team which was selected by the user in *know.html*.

### app.py:
app.py is the most important file in this project as the complete flask application runs with the help of it.
First, all important functions are imported from various libraries, flask is set up, and the connection to football.db is made.
Now I will discuss what the response of app.py is for various different app routes.

- #### app route *"/"*:
This app route renders **homepage.html** which takes the user to the homepage of the website.

- #### app route *"/match-up"*:

    - ##### GET:
    When the request method of /match-up is **GET**, app.py simply renders **match-up.html**

    - ##### POST:
    Here, the input from the select tag named "match" is requested first. If it is empty, **apology.html** gets rendered.
    If not, a condtional block gets executed.

    If the user selected the *David v/s Goliath* mode, two SQL SELECT queries get executed on the players table and the result is stored in two variables.
    The first query returns a team which is considered very good in the world of football, and the second one returns a team which not so strong infront of the first team. To get the second team I used the random library of python in order to randomly select a team within a given range of overall.
    The SQL queries are executed until both variables are not empty.
    When the condition is satisfied, **matched.html** gets rendered, and names of the first team, the second team and the variable containing the value of "match" are passed for jinja to use.

- #### app route *"/top-stars"*:

    - ##### GET:
    In the **GET** method of /top-stars, a first a variable stores all possible playing positions of players. Next I created a list which stores all of the qualities which was mentioned earlier.
    **top-stars.html** gets rendered, and the above mentioned variables are passed into it for jinja to use in the select tag of top-stars.html

    - ##### POST:
    The form in top-stars.html returns 5 values which are stored in 5 variables, namely - position, age, quality1, quality2, and quality3. A check is made for position and age, if either of them is found empty, **apology.html** gets rendered.

    Based on the user input for age, a new numeric value is assigned to it (if age = 'less than 20' is selected, the age variable will be set to 20, for age = 'less than 30', age = 30 will be set). This is done in order to make the SQL query easier to execute (Since the age column in *players* table is INT type).

    A list called *qualities* was created, and all qualities were stored in them (even if they are empty)
    Another variable called *query* was created. A part of an SQL SELECT query was written in it. It contained the columns which were required to display to the user and it was written upto a WHERE condition which matches the position and age entered by the user with the rows of *players* table.

    A list named Qualities was made and all qualities were stored in it. And a list called placeholders was made, which stored the position and age variables.

    Now, we iterate *qualities* and for each element, we check if this value exists in Qualities a condition is added to query like : 
        `query += f" AND {quality} = 'Yes'"`

    After that additional conditions were added to the query.

    This might seem a bit confusing at first, since I am using placeholders for column names, as it is not common practice. I took the help of GitHub Copilot and CS50.ai to implement this feature. This took a lot of debugging and re-writing of the code. The columns of the *qualities* table are the qualities, and based on the qualities given by the user, the SQL query is updated (for null quality variables, the query doesn't get updated). 

    A variable called ***players*** stores the result generated by the SQL query, where we pass the *query* variable and the placeholders list as positional arguments into the execute() function.

    If no player matches the condition given by the user, **no-star.html** is rendered.
    Else, **found-stars.html** is rendered, and the ***players, query and placeholders*** variables are passed into it for jinja to use.

- #### app route *"/know-your-team"*

    - ##### GET:
    When the page is requested via the **GET** method, a list of all teams present in the *teams* table is passed into the rendering of **know.html**.

    - ##### POST:
    The working of this route is quite simple as compared to the others route.
    We request the input from the select tag named "know". If found empty, we render **apology.html** as usual.

    Otherwise, an SQL SELECT query is executed to get the name of the team and also their description.
    Then the **team-desc.html** file is executed and the values received above are passed into it so that jinja can use it to display the name and a short description about the team.
