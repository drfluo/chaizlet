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
	db = get_db()
	users = db.query("SELECT *,  UPPER(last_name) as last_name FROM user ORDER BY role_id")
	return render_template('users.html', title=title, users=users)


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
		try:
			passwd_hash = hash_sha1(passwd)
			db = get_db()
			db.add_user(username, passwd_hash, firstname, lastname, email, role)
			msg = 'user was successfully added!'
		except:
			error = 'user already exists'
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
        stored_password = db.get_user_password(username)
        if stored_password != hashed_password:
            error = 'Apprend a te login !'
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
			'mot': 'Cest impossible ... :('
		}
	]
	return render_template('ex2.html', title=title, user=user, messages=messages)

@app.route('/addclass', methods=['POST', 'GET'])
def add_class():
	title="MyApp - Add a new class"
	error = None
	msg = None
	db = get_db()
	'''		'''	
	CLAS = db.query("SELECT * FROM class")
	print(CLAS)
	'''		'''
	languages = db.query("SELECT * FROM language")
	if session['username']:
		if request.method=='POST':
			class_name = request.form['classname']
			language_foreign_id = request.form['foreign']
			language_origin_id = request.form['origin']
			username = session['username']
			if class_name is None or language_foreign_id is None or language_origin_id is None:
				error = 'All fields are mandatory.'
	           	else:
				db.add_class(class_name, language_foreign_id, language_origin_id, username)
				msg = 'Class was successfully added!'
		return render_template('addclass.html', title=title, languages=languages, msg=msg, error=error)
 	else:
		return redirect(url_for('login'))











@app.route('/classes', methods=['POST', 'GET'])
def classes():
	title="Chaizlet - List classes"
	username = "'"+session['username']+"'"
	db = get_db()
	role = db.query("SELECT role_id FROM user WHERE username = "+username)
	print(role)
	if role == [{'role_id': u'Admin'}] :
		classes = db.query("SELECT * FROM class")
	elif role == [{'role_id': u'Professeur'}]:
		classes = db.query("SELECT * from class where prof_id = "+username)
		if classes is None:
			return redirect(url_for('add_class'))
	else:
		classes = db.query("SELECT * from class")
	return render_template('classes.html', title=title, classes=classes)


@app.route('/lol')
def lol():
        title="Chaizlet - List of lists"
        db = get_db()
	lists = db.query("SELECT list_name FROM list, class_list WHERE list_id = list_id_fk_cl AND class_id_fk_cl = 1")
	eleves = db.query("SELECT username FROM user_class WHERE class_id = 1")
	alllist = db.query("SELECT * FROM list")
	print(alllist)
        return render_template('lol.html', title=title, lists=lists, eleves=eleves)


@app.route('/wow', methods=['POST', 'GET'])
def wow():
	if request.method=='GET':
	        _id = request.values.get('nomliste')
		print(_id)
        db = get_db()
	title = db.query("SELECT list_name FROM list WHERE list_id = 1")
	words = db.query("""
				SELECT *
				FROM list, word_list, word, translation_word, translation 
				WHERE list_id = 2
				AND list_id_fk_wl = list_id
				AND translation_id = translation_id_fk_tw
				AND word_id = word_id_fk_wl
				AND word_id = word_id_fk_tw""")
	foreign = db.query("""
                                SELECT language_foreign_id
                                FROM list, class_list, class
				WHERE list_id = 2
                                AND list_id_fk_cl = list_id
                                AND class_id_fk_cl = class_id""")
	origin = db.query("""
                                SELECT language_origin_id
                                FROM list, class_list, class
                                WHERE list_id = 2
                                AND list_id_fk_cl = list_id
                                AND class_id_fk_cl = class_id""")
	print(title)		
	print(words)
	print(origin)
        return render_template('wow.html', title=title, words=words, origin=origin, foreign=foreign)











@app.route('/languages')
def languages():
	title="Chaizlet - List languages"
	db = get_db()
	languages = db.query("SELECT LOWER(name) as name from language ORDER BY name COLLATE NOCASE")
	return render_template('languages.html', title=title, languages=languages)



@app.route('/addlanguages', methods=['POST', 'GET'])
def add_languages():
    title="MyApp - Add a new language"
    error = None
    msg = None
    db = get_db()
    langues = db.query("SELECT * FROM language")
    print(langues)
    if session['username']:
        if request.method=='POST':
            name = request.form['newl']
            if name is None:
               error = 'All fields are mandatory.'
            else:
		try:
	                db.add_language(name)
	                msg = 'Language was successfully added!'
		except:
			error = 'language already exists'
        return render_template('addlanguages.html', title=title, languages=languages, msg=msg, error=error)
    else:
        return redirect(url_for('login'))


@app.route('/addlist', methods=['POST', 'GET'])
def add_list():
	title="MyApp - Add a new list"
	error = None
	msg = None
	db = get_db()
	cl = db.query("SELECT * FROM class_list")	
	print(cl)
	username = "'"+session['username']+"'"
	role = db.query("SELECT role_id FROM user WHERE username = "+username)
	classes = db.query("SELECT * FROM class WHERE prof_id = "+username)
	list = db.query("SELECT * FROM list")
	print(list)
	if session['username']:
		if role == [{'role_id': u'El\xe8ve'}]:
			return redirect(url_for('index'))
		else:
			if request.method=='POST':
				listname = request.form['list']
				classname = "'"+request.form['class_name']+"'"
				if listname is None or classname is None:
					error = 'All fields are mandatory.'
				else:
					try:
						db.add_list(listname)
        		                        class_id_fk_cl = db.query("SELECT class_id FROM class WHERE class_name = "+classname)
						list_id_fk_cl = db.query("SELECT list_id FROM list WHERE list_name ="+"'" +listname +"'")
						cifc = None
						lifc = None
						for row in list_id_fk_cl:
							lifc = row['list_id']
						for row in  class_id_fk_cl: 
							cifc = row['class_id']
						print(lifc)
						print(cifc)
						db.link_cl(lifc, cifc)
						msg = 'List was successfully added!'
					except:
						error = 'list already exists'
			return render_template('addlist.html', title=title, classes=classes, msg=msg, error=error)
	else:
		return redirect(url_for('login'))
