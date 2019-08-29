# NFL Home Baked Picks
## TODO

## Run Via Docker

Building image will install packages, create database, and expose the app to port 5000 
Running via docker, exposing localhost to the Flask app.

```bash
docker build -t nflpicks:latest .
docker run -d -it --name nfl -p 80:5000 nflpicks
```
Open localhost on your browser. NFL Pick pages awaits.



# Requirements

## Used Packages Python 3.7
```bash
beautifulsoup4            4.7.1
flask                     1.1.1                     
flask-login               0.4.1  
flask-migrate             2.5.2  
flask-sqlalchemy          2.4.0  
flask-wtf                 0.14.2
lxml                      4.3.4
pandas                    0.25.0
requests                  2.21.0
```
# Start DataBase

```bash
# set|export FLASK_APP=app.py to run flask run
# set|export FLASK_DEBUG=1 for debugging

# Set up migration directory
python manager.py -db start
````


# See Data
```python
import sqlite3

with sqlite3.connect('data.sqlite') as f:
    c = f.cursor()
    users = c.excute("SELECT * FROM users")
    print(users.fetchall())
```