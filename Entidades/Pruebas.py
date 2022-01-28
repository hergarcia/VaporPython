def delete_game(id):
    for game in store:
        if game == id:
            store.remove(game)


store = ["caca", "pichi", "perro", "gato"]
print(store)
delete_game("perro")
print(store)