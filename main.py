import hashlib

import os

class User:

    def __init__(self, name, password_hash, salt):

        self.name = name

        self.password_hash = password_hash

        self.salt = salt

        self.logged_in = False

    def get_name(self):

        return self.name

    def get_password_hash(self):

        return self.password_hash

    def get_salt(self):

        return self.salt

    def is_logged_in(self):

        return self.logged_in

    def autologout(self):

        self.logged_in = False

class Verb:

    def __init__(self, filename):

        self.users = []

        self.filename = filename

        self.load_users()

    def signup(self, name, password):

        salt = os.urandom(32)

        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

        user = User(name, password_hash, salt)

        self.users.append(user)

        self.save_users()

        return user

    def login(self, name, password):

        for user in self.users:

            if user.get_name() == name:

                salt = user.get_salt()

                password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

                if password_hash == user.get_password_hash():

                    user.logged_in = True

                    self.save_users()

                    return user

        return None

    def load_users(self):

        try:

            with open(self.filename, "r") as f:

                for line in f:

                    name, password_hash, salt = line.strip().split(": ")

                    user = User(name, bytes.fromhex(password_hash), bytes.fromhex(salt))

                    self.users.append(user)

        except FileNotFoundError:

            pass

    def save_users(self):

        with open(self.filename, "w") as f:

            for user in self.users:

                f.write(f"{user.get_name()}: {user.get_password_hash().hex()}: {user.get_salt().hex()}\n")


