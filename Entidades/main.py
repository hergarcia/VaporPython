from User import User
from Client import Client
from Admin import Admin
from Game import Game
from Category import Category
from Purchase import Purchase
from Rating import Rating
from Review import Review



# Prueba
g = Game("Rocket League", 50, "Flying car soccer game", 39, "Race", 5, "The best game ever", 2)
print(f"Titulo:" + g.title)
print(f"Imagen numero: {g.image}")
print(f"Descripcion: {g.description}")
print(f"Precio: ${g.price}")
print(f"Categoria: {g.category}")
print(f"Valoracion: {g.rating}")
print(f"Comentarios: {g.review}")
print(type(g.title))