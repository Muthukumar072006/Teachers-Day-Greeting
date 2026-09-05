from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)

app.secret_key = "teachers-day-secret-key"

DATABASE = "teachers_day.db"


# -----------------------------
# DATABASE CONNECTION
# -----------------------------

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


# -----------------------------
# CREATE DATABASE TABLE
# -----------------------------

def init_database():

    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trainee_name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# -----------------------------
# HOME PAGE
# -----------------------------

@app.route("/")
def home():

    connection = get_db_connection()

    feedback = connection.execute("""
        SELECT *
        FROM feedback
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return render_template(
        "index.html",
        feedback=feedback
    )


# -----------------------------
# ADD FEEDBACK
# -----------------------------

@app.route("/feedback", methods=["POST"])
def add_feedback():

    trainee_name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()

    # Validation

    if not trainee_name or not message:

        flash(
            "Please enter your name and appreciation message.",
            "error"
        )

        return redirect(url_for("home") + "#share")

    if len(trainee_name) > 60:

        flash(
            "Name should not exceed 60 characters.",
            "error"
        )

        return redirect(url_for("home") + "#share")

    if len(message) > 500:

        flash(
            "Message should not exceed 500 characters.",
            "error"
        )

        return redirect(url_for("home") + "#share")


    # Current date and time

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    # Save into database

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO feedback
        (trainee_name, message, created_at)

        VALUES (?, ?, ?)
        """,

        (
            trainee_name,
            message,
            created_at
        )
    )

    connection.commit()
    connection.close()


    flash(
        "Your appreciation message has been added!",
        "success"
    )

    return redirect(url_for("home") + "#wall")


# -----------------------------
# RUN APPLICATION
# -----------------------------

# Initialize database when the application starts
init_database()


if __name__ == "__main__":
    app.run(debug=True)