from Client import Client
from PurchaseMgr import PurchaseMgr


class ClientMgr:
	def __init__(self, purchase_mgr):
		self.purchase_mgr = purchase_mgr
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

	def update_client(self, new_username, new_email, new_password, id):
		for client in self.store:
			if client.id == id:
				client.username = new_username
				client.email = new_email
				client.password = new_password
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

	def purchased_games(self, client_id):
		purchased_game_list = []
		for purchase in self.purchase_mgr.get_purchases_stored():
			if purchase.buyer == client_id:
				purchased_game_list.append(purchase.game)
		return purchased_game_list