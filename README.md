# NFL Home Baked Picks
## TODO


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
flask db init
# Set up migration file
flask db migrate -m "moving data"
# Update database with the migration
flask db upgrade
````