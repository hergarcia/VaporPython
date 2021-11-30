from abc import ABC


class User(ABC):

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
