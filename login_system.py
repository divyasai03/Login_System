from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123",
        database="flask_project"
    )

# 1. Welcome Page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# 2. Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        profile_name = request.form['profile_name']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_data (username, password, profile_name) VALUES (%s, %s, %s)",
                       (username, password, profile_name))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('login'))
    return render_template('register.html')

# 3. Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_data WHERE username=%s ;", (username,))
        user = cursor.fetchone()
         
        if  user[0]==username and  user[1] ==password:
            return render_template("home.html",profile_name=user[2])
        
        
    return render_template('login.html')

# 4. Home Page
@app.route('/home')
def home():
    
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
