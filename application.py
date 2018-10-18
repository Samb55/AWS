from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
import bcrypt

application=app = Flask(__name__ , static_url_path='/static')
app.secret_key = '^A%DJAJU^JJ123'
#app.config['SESSION_TYPE'] = 'filesystem'
app.config['MYSQL_DATABASE_HOST'] = 'introcloud.cr1uwcxbg0if.us-east-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'cloudintro'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rootroot'
app.config['MYSQL_DATABASE_DB'] = 'db'
#app.config['MYSQL_DATABASE_PORT'] = '3306'

# app.config['MYSQL_DATABASE_PORT'] = '5005'
# app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hash_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)", (name, email, hash_password,))
        cur.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('home'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        cur = mysql.get_db().cursor()
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cur.fetchone()

        print(user)
        cur.close()

        if user and len(user) > 0:
            if bcrypt.checkpw(password, user[3].encode('utf-8')):
                session['name'] = user[1]
                session['email'] = user[2]
                return render_template("schd.html")
            else:
                return "Error password and email not match"
        else:
            return render_template("register.html")
    else:
        return render_template("login.html")


@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("login.html")
@app.route('/finalschd')
def finalschd():
    return render_template("finalschd.html")
@app.route('/schd')
def schd():
        return render_template("schd.html")
@app.route('/programs')
def programs():
    return render_template("programs.html")

if __name__ == "__main__":
    app.run(debug=True, port="5001")
