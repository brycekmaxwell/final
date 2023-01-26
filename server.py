from flask_app import app
from flask_app.controllers import controllers_users
from flask_app.controllers import controller_book

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)