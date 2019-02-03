import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    for i in range(8):
        hauteur =[]
        mountain_h = int(input())  # represents the height of one mountain.
        hauteur.append(mountain_h)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    # The index of the mountain to fire on.
    print(hauteur.index(max(hauteur)))
    hauteur[hauteur.index(max(hauteur))]=




hauteur = {}
for i in xrange(8):
    mountain_h = int(input())  # represents the height of one mountain.
    mountain_name = i
    hauteur[i] = mountain_h
classement = sorted(hauteur, key=hauteur.get, reverse=True)
cible = classement[0]
print cible

