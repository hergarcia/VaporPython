from Review import Review
from PurchaseMgr import PurchaseMgr


class ReviewMgr:
	def __init__(self, PurchaseMgr):
		self.store = []
		self.PurchaseMgr = PurchaseMgr

	# CRUD
	def create_new_rating(self, review_title, date, text, id):

		review = Review(review_title, date, text, id)
		self.store.append(review)

	def get_review(self, id):
		for review in self.store:
			if review.id == id:
				return review
		else:
			print("Review id is not in the list")

	def update_review(self, new_review_title, new_date, new_text, id):
		for review in self.store:
			if review.id == id:
				review.review_title = new_review_title
				review.date = new_date
				review.text = new_text
				break

			print("Review id is not in the list")

	def delete_review(self, id):
		for review in self.store:
			if review.id == id:
				self.store.remove(review)
				break
		else:
			print("Review id is not in the list")

	def get_reviews_stored(self):
		return self.store



	def create_review_game(self, user, game, review):
		pass
