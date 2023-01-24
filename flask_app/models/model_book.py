from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_users
from flask_app import app
from flask import flash

class Book:
    DB="final"
    def __init__(self,data):
        self.id=data["id"]
        self.title=data["title"]
        self.rating=data["rating"]
        self.tbr=data["tbr"]
        self.current=data["current"]
        self.finished=data["finished"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.posted_by='temp'

    @classmethod 
    def get_all_books(cls):
        query="SELECT * FROM books;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_books = []
        for book in results:
            all_books.append( cls(book) )
        return all_books