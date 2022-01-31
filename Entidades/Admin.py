from User import User


class Admin(User):
    def __init__(self, username, email, password, id):
        User.__init__(self, username, email, password, id)
