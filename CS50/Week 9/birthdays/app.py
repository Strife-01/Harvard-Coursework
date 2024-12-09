import os

import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect to the database
con = sqlite3.connect("birthdays.db", check_same_thread=False)

# Create the cursor
cur = con.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Get the data from the form
        name = request.form["name"]
        month = request.form["month"]
        day = request.form["day"]

        # Server-side validation of data
        if not name or not month or not day:
            return redirect("/")
        elif not 1 <= int(month) <= 12 or not 1 <= int(day) < 31:
            return redirect("/")

        # Submit data to the database
        cur.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", (name, month, day))
        con.commit()

        return redirect("/")

    else:

        # Get the data from the database
        res = cur.execute("SELECT name, month, day FROM birthdays ORDER BY id DESC")
        users = res.fetchall()

        # Send the data to the UI
        return render_template("index.html", users=users)