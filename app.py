import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    if cursor.fetchone():
        return "Login successful"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run(debug=True) 
