from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '@Gmuthoni001'

# MySQL Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Gmuthoni001'
app.config['MYSQL_DB'] = 'attractionsites'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SITES')
def about():
    return render_template('SITES.html')


@app.route('/contact')
def contacts():
    return render_template('contact.html')

@app.route('/signup')
def services():
    return render_template('signup.html')

@app.route('/general')
def general():
    return render_template('general.html')




@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')  # Use .get()
        email = request.form.get('email')
        password = request.form.get('password')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO signupsites (Name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        cur.close()

        return redirect('/')





if __name__=="__main__":
    app.run(debug=True)