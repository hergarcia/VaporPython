from User import User


class UserMgr:
    def __init__(self):
        self.store = []

    def create_new_user(self, username, email, password, id):

        user = User(username, email, password, id)
        self.store.append(user)

    def get_user(self, id):
        for user in self.store:
            if user.id == id:
                return user
        else:
            print("User id is not in the list")

    def update_user(self, username, email, password, id):
        for user in self.store:
            if user.id == id:
                user.username = username
                user.email = email
                user.password = password
                break

            print("User id is not in the list")

    def delete_user(self, id):
        for user in self.store:
            if user.id == id:
                self.store.remove(user)
                break
        else:
            print("User id is not in the list")

    def get_users_stored(self):
        return self.store
