from Purchase import Purchase


class PurchaseMgr:
	def __init__(self):
		self.store = []

	def create_new_purchase(self, buyer, game, price, date, id):

		purchase = Purchase(buyer, game, price, date, id)
		self.store.append(purchase)

	def get_purchase(self, id):
		for purchase in self.store:
			if purchase.id == id:
				return purchase
		else:
			print("Purchase id is not in the list")

	def update_purchase(self, new_buyer, new_game, new_price, new_date, id):
		for purchase in self.store:
			if purchase.id == id:
				purchase.buyer = new_buyer
				purchase.game = new_game
				purchase.price = new_price
				purchase.date = new_date
				break

			print("Purchase id is not in the list")

	def delete_purchase(self, id):
		for purchase in self.store:
			if purchase.id == id:
				self.store.remove(purchase)
				break
		else:
			print("Purchase id is not in the list")

	def get_purchases_stored(self):
		return self.store