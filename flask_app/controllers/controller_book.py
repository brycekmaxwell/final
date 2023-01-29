from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import model_book
from flask_app.models import models_users

@app.route("/view_tbr/<int:user_id>")
def view_tbr(user_id):
    return render_template("tbr.html", user_id = user_id, books = model_book.Book.get_all_tbr_books())

@app.route("/view_current/<int:user_id>")
def view_current(user_id):
    return render_template("current.html", user_id = user_id, books=model_book.Book.get_all_current_books())

   
@app.route("/create_book", methods=["POST"])
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
    model_book.Book.save(request_data)
    return redirect("/dashboard")


@app.route("/view_finished/<int:user_id>")
def view_finished(user_id):
    return render_template("finished.html", user_id = user_id)

@app.route("/view_rating/<int:user_id>")
def view_rating(user_id):
    return render_template("rating.html", user_id = user_id)


# @app.route("/move_to_finished", methods=["POST"])
# def move_to_finished(user_id):
#     finished_data = {
#         "title": 'title',
#         "rating": request.form['rating'],
#         "tbr": "no",
#         "current": "no",
#         "finished": "yes",
#         "user_id": session['user_id']
#     }
#     model_book.Book.update_finished(finished_data)
#     return render_template("finished.html", user_id=user_id)


@app.route("/move_current/<int:book_id>", methods=["POST"])
def move_to_current(book_id):
    print("A")
    current_data = {
        "tbr": "no",
        "current": "yes",
        "book_id": book_id
    }
    model_book.Book.update_current(current_data)
    return redirect(f"/view_tbr/{session['user_id']}")