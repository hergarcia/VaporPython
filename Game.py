from Category import Category
from Rating import Rating
from Review import Review


class Game:

    def __init__(self, title, image, description, price, category, rating, review):
        self.title = title
        self.image = image
        self.description = description
        self.price = price
        self.category = category
        self.rating = rating
        self.review = review

    def getRating(self):
        pass

    def getReviews(self):
        pass