from wind import blow, FixedStrategy as WindFixedStrategy
from dandelion import plant, FixedStrategy as DandelionFixedStrategy
from game import Game

print("DANDELIONS")

dandelion = DandelionFixedStrategy()
wind = WindFixedStrategy()
game = Game(dandelion, wind)
print(game.toString())
while (not game.done()):
    game.step()
    print(game.toString())
print("Wind wins" if game.winner() == wind else "Dandelion wins")
