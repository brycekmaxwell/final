from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import model_book
from flask_app.models import models_users

@app.route("/view_tbr/<int:user_id>")
def view_tbr(user_id):
    return render_template("tbr.html", user_id = user_id)

@app.route("/create_book", methods="POST")
def create_book():
    print(request.form)
    request_data = {
        "title": request.form['title'],
        "rating": 0,
        "tbr": "yes",
        "current": "no",
        "finished": "no",
        "user_id": session['user_id']
    }
    model_book.Book.create(request_data)
    return redirect("/")