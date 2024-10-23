# app.py

from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Load configurations
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
USERNAME = os.getenv('USERNAME', 'admin')

@app.route('/')
def home():
    return render_template_string('''
        <h1>Login</h1>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == SECRET_KEY:
        return f"<h1>Welcome, {username}!</h1>"
    else:
        return "<h1>Login Failed!</h1>", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
