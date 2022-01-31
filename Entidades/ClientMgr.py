from Client import Client


class ClientMgr:
	def __init__(self):
		self.store = []

	def create_new_client(self, username, email, password, id):

		client = Client(username, email, password, id)
		self.store.append(client)

	def get_client(self, id):
		for client in self.store:
			if client.id == id:
				return client
		else:
			print("Client id is not in the list")

	def update_client(self, username, email, password, id):
		for client in self.store:
			if client.id == id:
				client.username = username
				client.email = email
				client.password = password
				break

			print("Client id is not in the list")

	def delete_client(self, id):
		for client in self.store:
			if client.id == id:
				self.store.remove(client)
				break
		else:
			print("Client id is not in the list")

	def get_clients_stored(self):
		return self.store
