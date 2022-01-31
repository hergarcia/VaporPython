from builtins import print

from Game import Game


class GameMgr:

    def __init__(self):
        self.store = []

    #	Crear una entidad con los datos que reciba como parámetro. Deberá además asignarle un id y agregarla a la lista store. (create)
    def create_new_game(self, title, id):

        game = Game(title, id)
        self.store.append(game)

    # 	Dado un id, obtener esa entidad desde la lista (read, get)
    def get_game(self, id):
        for game in self.store:
            if game.id == id:
                return game
        else:
            print("Game id is not in the list")

    # 	Dado un id, modificar los datos de esa entidad (update)
    def update_game(self, new_title, id):
        for game in self.store:
            if game.id == id:
                game.title = new_title
                break
        else:
            print("Game id is not in the list")

    # 	Dado un id, borrar esa entidad de la lista.(delete)
    def delete_game(self, id):
        for game in self.store:
            if game.id == id:
                self.store.remove(game)
                break
        else:
            print("Game id is not in the list")

    # 	Obtener la lista de todas las entidades
    def get_games_stored(self):
        return self.store


manager = GameMgr()

manager.create_new_game(21, "RL")
manager.create_new_game(22, "cs")
manager.create_new_game(23, "lol")
manager.create_new_game(24, "pubg")
print(manager.get_games_stored())
print(manager.get_games_stored()[0].id)
manager.delete_game(21)
print(manager.get_games_stored()[0].id)
manager.update_game(22, "tetris")
manager.delete_game(24)
print(manager.get_games_stored()[0].id)
