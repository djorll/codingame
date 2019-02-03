import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

bin_repr = lambda s, coding="ascii": ''.join('{0:08b}'.format(c) for c in s.encode(coding))
message_bin = bin_repr(message)

# pour memoriser le caractere précédent
caractere_precedent = ''
# pour compter la répétition de caractères identiques
rang = 0
answer = ''

caractere_pour_0 = '00 '
caractere_pour_1 = '0 '
caractere_supplementaire = '0'


for caractere in message_bin:

    # si le caractere est égal au précédent incrémenter le rang
    if caractere is caractere_precedent:
        rang += 1
    else:
        if caractere_precedent is '0':
            answer += caractere_pour_0
        elif caractere_precedent is '1':
            answer += caractere_pour_1
            for i in range(rang):
                answer += caractere_supplementaire
        if rang > 0:
            answer += ' '

        caractere_precedent = caractere
        rang = 1

if caractere_precedent is '0':
    answer += caractere_pour_0
elif caractere_precedent is '1':
    answer += caractere_pour_1
for j in range(rang):
    answer += caractere_supplementaire

print(answer)
