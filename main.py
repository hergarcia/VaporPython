class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Client(User):

    def purchasedGames(self):
        pass

class Admin(User):
    pass

class Purchase:

    # buyer = Client
    # game = Game

    def __init__(self, buyer, game, price, date):
        self.buyer = buyer
        self.game = game
        self.price = price
        self.date = date


class Category:

    def __init__(self, cat_name):
        self.cat_name = cat_name


class Rating:

    def __init__(self, date, value):
        self.date = date
        self.value = value  # (1 - 5)


class Review:

    def __init__(self, review_title, date, text):
        self.review_title = review_title
        self.date = date
        self.text = text


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


# Prueba
g = Game("Rocket League", 50, "Flying car soccer game", 39, "Race", 5, "The best game ever")
print(f"Titulo:" + g.title)
print(f"Imagen numero: {g.image}")
print(f"Descripcion: {g.description}")
print(f"Precio: ${g.price}")
print(f"Categoria: {g.category}")
print(f"Valoracion: {g.rating}")
print(f"Comentarios: {g.review}")
