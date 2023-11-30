from src.models import Post, db, users
from flask import flash, session

class UserRepository:
    # check if a password meets all requirements
    def validate_input(self, first_name, last_name, username, password):
        if len(first_name) <= 1:
            flash('First name must be greater than 1 character', category='error')
            return False
        elif len(last_name) <= 1:
            flash('Last name must be greater than 1 character', category='error')
            return False
        elif len(username) < 4:
            flash('Username name must be at least 4 characters', category='error')
            return False
        elif (len(password) < 6) or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or any(char.isspace() for char in password):
            flash('Password must contain at least 6 characters, a letter, a number, and no spaces', category='error')
            return False
        return True
    
<<<<<<< HEAD
    def add_user(self, first_name, last_name, username, email, password, profile_picture):
        temp_user = users(first_name, last_name, username, email, password, profile_picture)
        db.session.add(temp_user)
        db.session.commit()

    def login_user(self, username):
        session['username'] = username

    def logout_user(self):
        del session['username']

    def is_logged_in(self):
        return 'username' in session
=======
    # get user by username
    def get_user_by_username(self, username):
        return users.query.filter_by(username=username).first()
>>>>>>> main

# Singleton to be used in other modules
user_repository_singleton = UserRepository()