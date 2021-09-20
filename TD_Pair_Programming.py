# -*- coding:Utf-8 -*-
""" Fichier rendu du TD PairProgramming Hannotte & Richaudeau """

# gestion de la matrice
import numpy as np


def verify_win(tableau_gagnant, morpion):
    for combinaison in tableau_gagnant:
        #test= combinaison[0]
        #print(test)
        #print(morpion[test[0],test[1]])
        #print(morpion[0,0])
        if morpion[combinaison[0][0],combinaison[0][1]] == morpion[combinaison[1][0],combinaison[1][1]] and  morpion[combinaison[0][0],combinaison[0][1]] == morpion[combinaison[2][0],combinaison[2][1]] :
            if morpion[combinaison[0][0],combinaison[0][1]] == "N":
                return False
            else:
                print(morpion[combinaison[0][0], combinaison[0][1]])
                print(morpion[combinaison[1][0], combinaison[1][1]])
                print(morpion[combinaison[2][0], combinaison[2][1]])
                print(f"Le joueur {morpion[combinaison[0][0],combinaison[0][1]]} à gagner !")
                return True
    return False







def new_game(morpion):
    morpion = np.matrix([['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']])
    return morpion


def choix_du_joueur(state):
    j = input("Signe du joeur O ou X= ")
    l = input("numero ligne= ")
    c = input("colonne= ")
    l = int(l)
    c = int(c)

    if j != 'X':
        if j =='O':
            pass
        else:
            print("Seul les joueurs X et O peuvent jouer ")
            (j, l, c) = choix_du_joueur(state)
            l = int(l)
            c = int(c)
            return j, l, c

    if j != 'O':
        if j == 'X':
            pass
        else:
            print("Seul les joueurs X et O peuvent jouer ")
            (j, l, c) = choix_du_joueur(state)
            l = int(l)
            c = int(c)
            return j, l, c

    if l < 0:
        print("Merci de rentrer un un numéro de ligne entre 0 et 2 ")
        (j,l,c) = choix_du_joueur(state)
        l = int(l)
        c = int(c)
        return j, l, c

    if l > 2:
        print("Merci de rentrer un un numéro de ligne entre 0 et 2 ")
        (j,l,c) = choix_du_joueur(state)
        l = int(l)
        c = int(c)
        return j, l, c

    if c < 0 :
        print("Merci de rentrer un un numéro de colonne entre 0 et 2 ")
        (j,l,c) = choix_du_joueur(state)
        l = int(l)
        c = int(c)
        return j, l, c
    if  c > 2:
        print("Merci de rentrer un un numéro de colonne entre 0 et 2 ")
        (j,l,c) = choix_du_joueur(state)
        l = int(l)
        c = int(c)
        return j, l, c

    return j, l, c




def match_nul(morpion):
    var=True
    for i in range(0, 3):
        for j in range(0, 3):
            if morpion[i, j] == "N":
                var = False
                return var
    return var


def tour(morpion,state):
    (j, l, c) = choix_du_joueur(state)
    l=int(l)
    c=int(c)


    if morpion[l, c] != 'N':
        print("Cette case est deja jouer merci de ressaisir une case")
        (j, l, c) = choix_du_joueur(state)
        l = int(l)
        c = int(c)
    else:
        morpion[l, c] = j
    return morpion


if __name__ == '__main__':
    tableau_gagnant = [[[0, 0], [0, 1], [0, 2]],
                       [[1, 0], [1, 1], [1, 2]],
                       [[2, 0], [2, 0], [2, 0]],
                       [[0, 0], [1, 0], [2, 0]],
                       [[0, 1], [1, 1], [2, 1]],
                       [[0, 2], [1, 2], [2, 2]],
                       [[0, 0], [1, 1], [2, 2]],
                       [[0, 2], [1, 1], [2, 0]]]
    state = ""
    boolean=True

    #morpion = np.matrix([['O', 'O', 'O'], ['N', 'N', 'N'], ['N', 'N', 'N']])
    morpion = np.matrix([['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']])# MATRICE DE BASE NULL
    #verify_win(tableau_gagnant,morpion)

    while boolean:
        tour(morpion,state)
        print(morpion)
        if verify_win(tableau_gagnant,morpion):
            verify_win(tableau_gagnant,morpion)
            u = input("Voulez vous rejouer y or n ?")
            if u=="y":
                morpion = new_game(morpion)
            else:
                print("fin du jeu")
                boolean = False

        if match_nul(morpion) :
            u=input("Voulez vous rejouer y or n ?")
            if u=="y":
                morpion = new_game(morpion)
            else:
                print("fin du jeu")
                boolean = False




