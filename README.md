#  en@destael.educanet2.ch ## Useful Commands
```
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user 
pip install virtualenv --user

cd /home/eleve/Documents/
mkdir projet
virtualenv .env
source .env/bin/activate

pip install flask
mkdir app
cd app

vi __init__.py

--
from flask import Flask

app = Flask(__name__)

from app import routes
--

vi routes.py

--
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
--

cd ..

vi myapp.py

--
from app import app
--

export FLASK_APP=myapp.py
flask run
```

### SQL Queries

```
#
source .env/bin/activate			# nos mets dans l'environnement privé
(.ENV)	python					# permet de coder en python 
	import app.db as db			# import les bases de données
	db = db.db_handler()			# classe
	db.query('select * from user')		# extrait tous de la classe user
	




```
