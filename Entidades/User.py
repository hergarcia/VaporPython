from abc import ABC


class User(ABC):

    def __init__(self, username, email, password, id):
        self.username = username
        self.email = email
        self.password = password
        self.id = id
