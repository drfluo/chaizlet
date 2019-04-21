### Useful Commands
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
rm database.db			// AVANT TOUTE UTILISATION 
python app/init_db.py 	// AVANT TOUTE UTILISATION et no such user table

export FLASK_APP=myapp.py
flask run
```

### SQL Queries

```
#
source .env/bin/activate			# nos mets dans l'environnement priv√©
(.ENV)	python					# permet de coder en python 
	import app.db as db			# import les bases de donn√©es
	db = db.db_handler()			# classe
	db.query('select * from user')		# extrait tous de la classe user
	




```
### cr√©e une nouvelle page
```
virtualenv. env				# new pc
source .env/bin/activate		# new pc
pip install flask			# new pc


python app/init_db.py
flask run 

vi app/route.py





JE L'AI MODIFI… !!!


```
### Heroku comment le run sur windows
```

download Heroku CIL en WIndows 64

installÈ Heroku CIL

ouvert cmd

$ heroku login 			# ouvre une fenetre firefox et log in

$ heroku git clone https://github.com/drfluo/chaizlet.git

$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

$ get-pip.py --user

$ cd C:\Users\drupp\git\chaizlet

$ 

```

### unchecked update
```

- routes.py ('/ex2')
- app/templates/ex2.html
- base.html (ex2) l.12

```
