class User:

    def __init__(self, name, password):

        self.name = name

        self.password = password

        self.logged_in = False

    def get_name(self):

        return self.name

    def get_password(self):

        return self.password

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

        user = User(name, password)

        self.users.append(user)

        self.save_users()

        return user

    def login(self, name, password):

        for user in self.users:

            if user.get_name() == name and user.get_password() == password:

                user.logged_in = True

                self.save_users()

                return user

        return None

    def load_users(self):

        try:

            with open(self.filename, "r") as f:

                for line in f:

                    name, password = line.strip().split(": ")

                    user = User(name, password)

                    self.users.append(user)

        except FileNotFoundError:

            pass

    def save_users(self):

        with open(self.filename, "w") as f:

            for user in self.users:

                f.write(f"{user.get_name()}: {user.get_password()}\n")
