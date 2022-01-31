from Category import Category

class CategoryMgr:
	def __init__(self):
		self.store = []

	def create_new_game(self, cat_name, id):

		category = Category(cat_name, id)
		self.store.append(category)

	def get_category(self, id):
		for category in self.store:
			if category.id == id:
				return category
		else:
			print("Category id is not in the list")

	def update_category(self, id, cat_name):
		for category in self.store:
			if category.id == id:
				category.cat_name = cat_name
				break
		else:
			print("Category id is not in the list")

	def delete_category(self, id):
		for category in self.store:
			if category.id == id:
				self.store.remove(category)
				break
		else:
			print("Category id is not in the list")

	def get_categories_stored(self):
		return self.store
