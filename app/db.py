import sqlite3

DATABASE = 'database.db'
SCHEMA = './conf/schema.sql'

class db_handler:
    """
        Handle connection and queries to SQLite
    """
    
    def __init__(self):
        """
            Constructor
        """
        try:
            # connect to the DB
            self.conn = sqlite3.connect(DATABASE)
            self.conn.row_factory = sqlite3.Row
        except (Exception) as error:
            print(error)

    def query(self, query, args=(), one=False):
        """
            Query the DB
        """
        cur = self.conn.execute(query, args)
	rd = None
        if one:
	    row = cur.fetchone()
	    if row:
	    	rd = dict(zip(zip(*cur.description)[0], row)) 
        else:
	    rows = cur.fetchall()
	    if rows:
	    	rd = [dict(zip(zip(*cur.description)[0], row)) for row in rows]
	return rd if rd else None
    
    def edit(self, query, args=()):
        """
            Insert in the DB
        """
        self.conn.execute(query, args)
        self.conn.commit()

    def init(self):
        """
            Init DB schema
        """
        with open(SCHEMA, 'r') as f:
            self.conn.cursor().executescript(f.read())
        self.conn.commit()

    def close(self):
        """
            Close DB connection
        """
        if self.conn is not None:
            self.conn.close()
    
    def get_user_password(self, username):
	"""
	    Get user password
	"""
        rd = self.query('SELECT passwd_hash FROM user WHERE username=?', (username,), one=True)
        return rd['passwd_hash'] if rd else None

    def get_user_role_id(self, username):
        """
            Get user role_id
        """
        rd = self.query('SELECT role_id FROM user WHERE username=?', (username,), one=True)
        return rd['role_id'] if rd else None


    def add_user(self, username, passwd_hash, firstname, lastname, email, role_id):
        """
            Add a new user
        """
        self.edit('INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) VALUES (?,?,?,?,?,?)', (username, passwd_hash, firstname, lastname, email, role_id,))
    
    def add_class(self, class_name, language_foreign_id, language_origin_id, prof_id):
        """
            Add a new class
        """
        self.edit('INSERT INTO class (class_name, language_foreign_id, language_origin_id, prof_id) VALUES (?,?,?,?)', (class_name, language_foreign_id, language_origin_id, prof_id,))

    def add_language(self, name):
		
        self.edit('INSERT INTO language (name) VALUES (?)', (name,))


    def add_list(self, list_name):
	self.edit('INSERT INTO list (list_name) VALUES (?)', (list_name,))


    def link_cl(self, list_id_fk_cl, class_id_fk_cl):
	self.edit('INSERT INTO class_list (list_id_fk_cl, class_id_fk_cl) VALUES (?,?)', (list_id_fk_cl, class_id_fk_cl,))


    def awo(self, word_origin):
	self.edit('INSERT INTO word (word_origin) VALUES (?)', (word_origin,))

    def awf(self, word_foreign):
        self.edit('INSERT INTO translation (word_foreign) VALUES (?)', (word_foreign,))

    def link_wl(self, word_id_fk_wl, list_id_fk_wl):
        self.edit('INSERT INTO word_list (word_id_fk_wl, list_id_fk_wl) VALUES (?,?)', (word_id_fk_wl, list_id_fk_wl,))

    def link_tw(self, translation_id_fk_tw, word_id_fk_tw):
        self.edit('INSERT INTO translation_word (translation_id_fk_tw, word_id_fk_tw) VALUES (?,?)', (translation_id_fk_tw, word_id_fk_tw,))

    def link_uc(self, username_fk_uc, class_id_fk_uc):
        self.edit('INSERT INTO user_class (username_fk_uc, class_id_fk_uc) VALUES (?,?)', (username_fk_uc, class_id_fk_uc,))


