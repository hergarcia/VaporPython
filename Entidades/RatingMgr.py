from Rating import Rating


class RatingMgr:
    def __init__(self):
        self.store = []

    def create_new_rating(self, date, value, id):

        rating = Rating(date, value, id)
        self.store.append(rating)

    def get_rating(self, id):
        for rating in self.store:
            if rating.id == id:
                return rating
        else:
            print("Rating id is not in the list")

    def update_rating(self, date, value, id):
        for rating in self.store:
            if rating.id == id:
                rating.date = date
                rating.value = value
                break

            print("Rating id is not in the list")

    def delete_rating(self, id):
        for rating in self.store:
            if rating.id == id:
                self.store.remove(rating)
                break
        else:
            print("Rating id is not in the list")

    def get_ratings_stored(self):
        return self.store
