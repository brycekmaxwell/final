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
        self.user_id = data['user_id']
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

    @classmethod 
    def get_all_tbr_books(cls, user_id):
        query= """
            SELECT 
                *
            FROM 
                books
            WHERE 
                books.tbr = 'yes'
                AND
                user_id = "%(id)s";
        """
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        all_books = []
        for book in results:
            all_books.append(cls(book))
        return all_books

    @classmethod 
    def get_current_book(cls, user_id):
        query="""
                SELECT 
                    *
                FROM 
                    books 
                WHERE 
                    books.current = 'yes'
                AND
                    user_id = "%(id)s";
        """
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        all_books = []
        for book in results:
            all_books.append( cls(book) )
        return all_books

    @classmethod 
    def get_all_finished_books(cls, user_id):
        query="""
                SELECT 
                    *
                FROM 
                    books 
                WHERE 
                    books.finished = 'yes'
                AND
                    user_id = "%(id)s";
        """
        results = connectToMySQL(cls.DB).query_db(query, user_id)
        all_books = []
        for book in results:
            all_books.append( cls(book) )
        return all_books

    @classmethod 
    def save(cls, request_data):
        query="INSERT INTO books (rating, title, tbr, current, finished, user_id) VALUES (%(rating)s, %(title)s, %(tbr)s, %(current)s, %(finished)s, %(user_id)s);"
        return connectToMySQL(cls.DB).query_db(query, request_data)

    @classmethod
    def update_current(cls, current_data):
        query="UPDATE books SET tbr = %(tbr)s, current = %(current)s WHERE id = %(book_id)s"
        return connectToMySQL(cls.DB).query_db(query, current_data)

    @classmethod
    def update_finished(cls, finished_data):
        query="UPDATE books SET rating = %(rating)s, current = %(current)s, finished = %(finished)s WHERE id = %(book_id)s"
        return connectToMySQL(cls.DB).query_db(query, finished_data)

    @classmethod
    def delete(cls, book_id):
        query="DELETE from books WHERE books.id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, book_id)
