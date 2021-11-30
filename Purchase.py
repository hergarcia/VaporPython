from Client import Client


class Purchase:


    def __init__(self, Client, game, price, date):
        self.Client = Client
        self.game = game
        self.price = price
        self.date = date


