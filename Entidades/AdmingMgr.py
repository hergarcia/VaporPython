from Admin import Admin


class AdminMgr:
	def __init__(self):
		self.store = []

	def create_new_admin(self, username, email, password, id):

		admin = Admin(username, email, password, id)
		self.store.append(admin)

	def get_admin(self, id):
		for admin in self.store:
			if admin.id == id:
				return admin
		else:
			print("Admin id is not in the list")

	def update_admin(self, username, email, password, id):
		for admin in self.store:
			if admin.id == id:
				admin.username = username
				admin.email = email
				admin.password = password
				break

			print("Admin id is not in the list")

	def delete_admin(self, id):
		for admin in self.store:
			if admin.id == id:
				self.store.remove(admin)
				break
		else:
			print("Admin id is not in the list")

	def get_admins_stored(self):
		return self.store
