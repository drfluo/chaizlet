from app import app
from flask import g, render_template, redirect, url_for, request, session
from app.db import db_handler
from app.utils import hash_sha1

def get_db():
    if 'db' not in g:
        g.db = db_handler()
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/index')
def index():
    title="MyApp - Welcome!"
    return render_template('index.html', title=title)

@app.route('/users')
def users():
    title="MyApp - List users"
    if session['username']:
        db = get_db()
        users = db.query("SELECT * from user")
        return render_template('users.html', title=title, users=users)
    else:
        return redirect(url_for('login'))

@app.route('/adduser', methods=['POST', 'GET'])
def add_user():
    title="MyApp - Add a new user"
    error = None
    msg = None
    if session['username']:
        if request.method=='POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            username = request.form['username']
            passwd = request.form['password']
	    role = request.form['role']
            if firstname is None or lastname is None or email is None or username is None or passwd is None or role is None:
                error = 'All fields are mandatory.'
            else:
                passwd_hash = hash_sha1(passwd) 
                db = get_db()
                db.add_user(username, passwd_hash, firstname, lastname, email, role)
                msg = 'User was successfully added!'
        return render_template('adduser.html', title=title, msg=msg, error=error)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    title="MyApp - Login"
    error = None
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_sha1(password) 
        db = get_db()
	# custom query
        stored_password = db.get_user_password(username)
        if stored_password != hashed_password:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html', title=title, error=error)

@app.route('/logout')
def logout():
    title="MyApp - Logout"
    g.username = None
    session['username'] = None
    return render_template('logout.html', title=title)

@app.route('/ex1')
def ex1():
    title = "My App - Example 1"
    user = {'username': 'Test'}
    posts = [
        {
            'author': {'username': 'Rambo'},
            'body': 'Beautiful day in Geneva!'
        },
      {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Zuliette'},
            'body': 'Stop being so CHILDISH!'
        },
        {
            'author': {'username': 'Damien'},
            'body': 'Tu vois Laureline, y en a qui travaille :)'
        }
    ]
    return render_template('ex1.html', title=title, user=user, posts=posts)
    
@app.route('/ex2')
def ex2():
	title = "My App - Example 2"
	user ={'username': 'Test'}
	messages = [
		{
			'parleur': {'username': 'Laureline'},
			'mot': 'On galere avec heroku x)'
		},
		{
			'parleur': {'username': 'Damien'},
			'mot': 'C est impossible ... :('
		}
	]
	return render_template('ex2.html', title=title, user=user, messages=messages)

@app.route('/addclass', methods=['POST', 'GET'])
def add_class():
    title="MyApp - Add a new class"
    error = None
    msg = None
    db = get_db()
    if session['username']:
        if request.method=='POST':
            class_name = request.form['classname']
            language_foreign_id = request.form['foreign']
            language_origin_id = request.form['origin']
            if class_name is None or language_foreign_id is None or language_origin_id is None:
               error = 'All fields are mandatory.'
            else:
                db.add_class(class_name, language_foreign_id, language_origin_id)
                msg = 'Class was successfully added!'
	languages = db.query("SELECT * FROM language")
        return render_template('addclass.html', title=title, languages=languages, msg=msg, error=error)
    else:
        return redirect(url_for('login'))


@app.route('/classes')
def classes():
    title="Chaizlet - List classes"
    if session['username']:
        db = get_db()
        classes = db.query("SELECT * from class")
        return render_template('classes.html', title=title, classes=classes)
    else:
        return redirect(url_for('login'))


@app.route('/languages')
def languages():
    title="Chaizlet - List languages"
    if session['username']:
        db = get_db()
        languages = db.query("SELECT * from language")
        return render_template('languages.html', title=title, languages=languages)
    else:
        return redirect(url_for('login'))




@app.route('/addlanguages', methods=['POST', 'GET'])
def add_languages():
    title="MyApp - Add a new language"
    error = None
    msg = None
    db = get_db()
    if session['username']:
        if request.method=='POST':
            name = request.form['newl']
            if name is None:
               error = 'All fields are mandatory.'
            else:
                db.add_language(name)
                msg = 'Language was successfully added!'
        languages = db.query("SELECT * FROM language")
        return render_template('addlanguages.html', title=title, languages=languages, msg=msg, error=error)
    else:
        return redirect(url_for('login'))
	
