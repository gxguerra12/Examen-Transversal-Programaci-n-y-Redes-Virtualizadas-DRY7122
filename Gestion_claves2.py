import pyotp
import sqlite3
import hashlib
import uuid

from flask import Flask, request, render_template_string

app = Flask(__name__)

db_name = 'accesos.db'

@app.route('/')
def index():
    return 'Item 3 Examen Transversal - Fabiancito'

@app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            HASH      TEXT    NOT NULL);''')
    conn.commit()

    if request.method == 'POST':
        try:
            hash_value = hashlib.sha1(request.form['password'].encode()).hexdigest()
            c.execute("INSERT INTO USER_HASH (USERNAME, HASH) "
                      "VALUES (?, ?)", (request.form['username'], hash_value))
            conn.commit()
            return "signup success"
        except sqlite3.IntegrityError:
            return "username has been registered."
        finally:
            conn.close()

    signup_form = '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Sign Up">
    </form>
    '''
    return render_template_string(signup_form)

def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = ?"
    c.execute(query, (username,))
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == hashlib.sha1(password.encode()).hexdigest()

@app.route('/login/v2', methods=['GET', 'POST'])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'login success'
        else:
            error = 'Invalid username/password'
        return error

    login_form = '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''
    return render_template_string(login_form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)

