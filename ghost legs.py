# Objectif
# Ghost Legs is a kind of lottery game common in Asia. It starts with a number of vertical lines. 
# Between the lines there are random horizontal connectors binding all lines into a connected diagram, like the one below.
# 
# A  B  C
# |  |  |
# |--|  |
# |  |--|
# |  |--|
# |  |  |
# 1  2  3
# 
# 
# To play the game, a player chooses a line in the top and follow it downwards. 
When a horizontal connector is encountered, he must follow the connector to turn to another vertical line and continue downwards. 
Repeat this until reaching the bottom of the diagram.
# 
# In the example diagram, when you start from A, you will end up in 2. 
# Starting from B will end up in 1. Starting from C will end up in 3. It is guaranteed that every top label will map to a unique bottom label.
# 
# Given a Ghost Legs diagram, find out which top label is connected with which bottom label. List all connected pairs.
# 
# 
# Entrée
# Line 1: Integer W and H for width and height of the diagram below.
# Next H lines: Containing a Ghost Legs diagram as your input.
# 
# The diagram itself is composed of characters: '|' and '-', (and space).
# The top line in the diagram has a number of labels T.
# The bottom line contains labels B.
# 
# Each T and B is a single ascii character that can be of any random value. Do not assume they will always be ABC or 123.
# 
# As a rule of the game, left and right horizontal connectors  will never appear at the same point.
# 
# All diagrams are having the same style as the test cases.
# Sortie
# List all connected pairs between top and bottom labels, TB, in the order of the top labels from Left to Right. Write each pair in a separate line.
# Contraintes
# 3 < W, H ≤ 100

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()

# le nombre de valeurs a trouver = 1+(w-1)/3
# transformer les lignes en ligne de valeur 0 +1 -1
# pour additionner les lignes :
# from operator import add
# list( map(add, list1, list2))
# le total final donne la colonne d'arrivée des valeurs à trouver



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")