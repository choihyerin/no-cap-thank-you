import os
import pytz
from datetime import datetime
import random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "your_secret_key"

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///gratitude.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Ensure the database tables exist
def initialize_db():
    db.execute("""
        CREATE TABLE IF NOT EXISTS good_deeds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            deed TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS gratitude (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gratitude_text TEXT NOT NULL,
            entry_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt_text TEXT NOT NULL
        )
    """)

    # Populate prompts table if empty
    if not db.execute("SELECT 1 FROM prompts LIMIT 1"):
        print("Populating prompts table...")
        prompts = [
            "What made you smile today?",
            "Who has helped you recently, and how?",
            "What is something in nature you’re grateful for?",
            "Describe a happy memory from your past.",
            "What is your favorite place to relax, and why?",
            # Add the rest of the prompts here
        ]
        for prompt in prompts:
            db.execute("INSERT INTO prompts (prompt_text) VALUES (?)", prompt)
        print("Prompts table populated.")

    print("Database initialized and tables created (if not already present).")

initialize_db()

# Helper function to convert UTC to local timezone
def convert_utc_to_local(utc_time_str, timezone="America/Toronto"):
    """Convert a UTC timestamp to the user's local timezone."""
    utc_time = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S")
    utc_time = pytz.utc.localize(utc_time)
    local_time = utc_time.astimezone(pytz.timezone(timezone))
    return local_time.strftime("%Y-%m-%d %H:%M:%S")

@app.route("/", methods=["GET", "POST"])
def gratitude_journal():
    if request.method == "POST":
        gratitude_text = request.form.get("gratitude_text")
        if not gratitude_text:
            flash("Gratitude entry cannot be empty!")
            return redirect("/")
        db.execute("INSERT INTO gratitude (gratitude_text) VALUES (?)", gratitude_text)
        flash("Gratitude entry added successfully!")
        return redirect("/")
    gratitude = db.execute("SELECT * FROM gratitude ORDER BY entry_timestamp DESC")
    timezone = "America/Toronto"  # Replace with the user's timezone if dynamic detection is implemented
    for entry in gratitude:
        entry["entry_timestamp"] = convert_utc_to_local(entry["entry_timestamp"], timezone)
    return render_template(
        "gratitude_journal.html",
        title="No Cap, Thank You - Gratitude Journal",
        GRATITUDE=gratitude
    )

@app.route("/good_deeds", methods=["GET", "POST"])
def good_deeds():
    if request.method == "POST":
        # Fetch the deed from the form
        deed = request.form.get("deed")

        # Validate input
        if not deed:
            flash("Good deed cannot be empty!")
            return redirect("/good_deeds")

        # Insert into database
        db.execute("INSERT INTO good_deeds (deed) VALUES (?)", deed)

        # Flash success message and redirect
        flash("Good deed added successfully!")
        return redirect("/good_deeds")  # Redirect clears the form submission context

    # For GET requests, fetch deeds
    deeds = db.execute("SELECT * FROM good_deeds ORDER BY timestamp DESC")
    return render_template("good_deeds.html", DEEDS=deeds)

@app.route("/daily_prompt", methods=["GET"])
def daily_prompt():
    prompt = db.execute("SELECT prompt_text FROM prompts ORDER BY RANDOM() LIMIT 1")
    if prompt:
        prompt_text = prompt[0]["prompt_text"]
    else:
        prompt_text = "No prompts available. Please add some prompts!"
    return render_template(
        "daily_prompt.html",
        title="No Cap, Thank You - Daily Prompt",
        prompt=prompt_text
    )

if __name__ == "__main__":
    app.run(debug=True)
