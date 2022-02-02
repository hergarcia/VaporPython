import statistics
from Game import Game
from CategoryMgr import CategoryMgr
from ReviewMgr import ReviewMgr
from Review import Review
from Rating import Rating


class GameMgr:

    def __init__(self, category_mgr, review_mgr):
        self.category_mgr = category_mgr
        self.review_mgr = review_mgr
        self.store = []

    def create_new_game(self, title, image, description, price, category_id, id):
        category = self.category_mgr.get_category(category_id)
        game = Game(title, image, description, price, category, id)
        self.store.append(game)


    def get_game(self, id):
        for game in self.store:
            if game.id == id:
                return game
        else:
            print("Game id is not in the list")


    def update_game(self, new_title, new_image, new_description, new_price, new_category_id, game_id):
        for game in self.store:
            if game.id == game_id:
                game.title = new_title
                game.image = new_image
                game.description = new_description
                game.price = new_price
                game.category = self.category_mgr.get_category(new_category_id)
                break
        else:
            print("Game id is not in the list")


    def delete_game_review(self, game_id, review_id):
        for game in self.store:
            if game.id == game_id:
                for review in game.review:
                    if review.id == review_id:
                        game.review.remove(review)


    def game_category_filter(self, category_id):
        category_game_list = []
        for game in self.store:
            if game.category == category_id:
                category_game_list.append(game)
        return category_game_list


    def delete_game(self, game_id):
        for game in self.store:
            if game.id == game_id:
                self.store.remove(game)
                break
        else:
            print("Game id is not in the list")


    def rate_game(self, game_id, date, value, id):
        rating = Rating(date, value, id)
        for game in self.store:
            if game.id == game_id:
                game.rating.append(rating)
                break


    def review_game(self, game_id, review_title, date, text, id):
        review = Review(review_title, date, text, id)
        for game in self.store:
            if game.id == game_id:
                game.review.append(review)
                break

    def get_game_rating(self, game_id):
        for game in self.store:
            if game.id == game_id:
                return statistics.mean(game.rating)


    def rating_filter(self, rating):    # listar los juegos con valoracion mayor a la proporcionada
        game_list = []
        for game in self.store:
            if GameMgr.get_game_rating(self, game.id) >= rating:
                game_list.append(game)
        return game_list


    def get_games_stored(self):
        return self.store




