# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:32:31 2024

@author: leand
"""

######
# La fonction de résolution à appeller est resolution_arbre2(d)
######




#création des dictionnaire global
dictio = {}
dictio5 = {}
d_parf = {}


def ordre(d) :
    n_d = {} 
    l = ['U1','U2','U3','U4','F1','F2','F3','F4','B1','B2','B3','B4',
         'L1','L2','L3','L4','D1','D2','D3','D4','R1','R2','R3','R4']
    for f in l :
        n_d[f] = d[f]
    return n_d


#céation du dictionnaire parfait
def parfait(d):
    newd = {}
    
    # Utilisez des noms de variables distincts pour éviter les écrasements
    b_value = d['B3']
    d_value = d['D4']
    l_value = d['L4']
    # print(b_value,d_value,l_value)
    # print(comp(b_value),comp(d_value),comp(l_value))
    
    newd['U1'] = newd['U2'] = newd['U3'] = newd['U4'] = comp(d_value)
    newd['F1'] = newd['F2'] = newd['F3'] = newd['F4'] = comp(b_value)
    newd['B1'] = newd['B2'] = newd['B3'] = newd['B4'] = b_value
    newd['L1'] = newd['L2'] = newd['L3'] = newd['L4'] = l_value
    newd['D1'] = newd['D2'] = newd['D3'] = newd['D4'] = d_value
    newd['R1'] = newd['R2'] = newd['R3'] = newd['R4'] = comp(l_value)
    
    return newd


def comp(couleur):
    c = ''
    if couleur == 'red':
        c = 'orange'
    elif couleur == 'orange':
        c = 'red'
    elif couleur == 'blue':
        c = 'green'
    elif couleur == 'green':
        c = 'blue'
    elif couleur == 'white':
        c = 'yellow'
    elif couleur == 'yellow':
        c = 'white'
    return c
        


# Renvoie une liste de tous les mouvements possibles à partir de la position donnée.
# Chaque élément de la liste est un tuple contenant deux éléments:
#   1. La position future après le mouvement
#   2. Le mouvement nécessaire pour atteindre cette nouvelle position
def mouvement(d):
    r = []

    #U
    d1=d.copy()
    d1['U2'],d1['U3'],d1['U4'],d1['U1'] = d['U1'],d['U2'],d['U3'],d['U4']
    d1['L1'],d1['B1'],d1['R1'],d1['F1'] = d['F1'],d['L1'],d['B1'],d['R1']
    d1['L2'],d1['B2'],d1['R2'],d1['F2'] = d['F2'],d['L2'],d['B2'],d['R2']
    r.append((d1,"U"))

    #U2
    d1=d.copy()
    d1['U2'],d1['U3'],d1['U4'],d1['U1'] = d['U1'],d['U2'],d['U3'],d['U4']
    d1['L1'],d1['B1'],d1['R1'],d1['F1'] = d['F1'],d['L1'],d['B1'],d['R1']
    d1['L2'],d1['B2'],d1['R2'],d1['F2'] = d['F2'],d['L2'],d['B2'],d['R2']
    d1['U2'],d1['U3'],d1['U4'],d1['U1'] = d1['U1'],d1['U2'],d1['U3'],d1['U4']
    d1['L1'],d1['B1'],d1['R1'],d1['F1'] = d1['F1'],d1['L1'],d1['B1'],d1['R1']
    d1['L2'],d1['B2'],d1['R2'],d1['F2'] = d1['F2'],d1['L2'],d1['B2'],d1['R2']
    r.append((d1,"U2"))
    
    #U_1
    d1=d.copy()
    d1['U1'],d1['U2'],d1['U3'],d1['U4']=d['U2'],d['U3'],d['U4'],d['U1']
    d1['F1'],d1['L1'],d1['B1'],d1['R1']=d['L1'],d['B1'],d['R1'],d['F1']
    d1['F2'],d1['L2'],d1['B2'],d1['R2'] =d['L2'],d['B2'],d['R2'],d['F2']
    r.append((d1,"U_1"))
    d1=d.copy()

    #R
    d1=d.copy()
    d1['R2'],d1['R3'],d1['R4'],d1['R1'] = d['R1'],d['R2'],d['R3'],d['R4']
    d1['U2'],d1['B4'],d1['D2'],d1['F2'] = d['F2'],d['U2'],d['B4'],d['D2']
    d1['U3'],d1['B1'],d1['D3'],d1['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
    r.append((d1,"R"))

    #R2
    d1=d.copy()
    d1['R2'],d1['R3'],d1['R4'],d1['R1'] = d['R1'],d['R2'],d['R3'],d['R4']
    d1['U2'],d1['B4'],d1['D2'],d1['F2'] = d['F2'],d['U2'],d['B4'],d['D2']
    d1['U3'],d1['B1'],d1['D3'],d1['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
    d1['R2'],d1['R3'],d1['R4'],d1['R1'] = d1['R1'],d1['R2'],d1['R3'],d1['R4']
    d1['U2'],d1['B4'],d1['D2'],d1['F2'] = d1['F2'],d1['U2'],d1['B4'],d1['D2']
    d1['U3'],d1['B1'],d1['D3'],d1['F3'] = d1['F3'],d1['U3'],d1['B1'],d1['D3']
    r.append((d1,"R2"))

    #R_1
    d1=d.copy()
    d1['R1'],d1['R2'],d1['R3'],d1['R4']=d['R2'],d['R3'],d['R4'],d['R1']
    d1['F2'],d1['U2'],d1['B4'],d1['D2']=d['U2'],d['B4'],d['D2'],d['F2']
    d1['F3'],d1['U3'],d1['B1'],d1['D3']=d['U3'],d['B1'],d['D3'],d['F3']
    r.append((d1,"R_1"))

    #F
    d1=d.copy()
    d1['F2'],d1['F3'],d1['F4'],d1['F1'] = d['F1'],d['F2'],d['F3'],d['F4']
    d1['D1'],d1['L2'],d1['U3'],d1['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
    d1['R1'],d1['D2'],d1['L3'],d1['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
    r.append((d1,"F"))

    #F2
    d1=d.copy()
    d1['F2'],d1['F3'],d1['F4'],d1['F1'] = d['F1'],d['F2'],d['F3'],d['F4']
    d1['D1'],d1['L2'],d1['U3'],d1['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
    d1['R1'],d1['D2'],d1['L3'],d1['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
    d1['F2'],d1['F3'],d1['F4'],d1['F1'] = d1['F1'],d1['F2'],d1['F3'],d1['F4']
    d1['D1'],d1['L2'],d1['U3'],d1['R4'] = d1['R4'],d1['D1'],d1['L2'],d1['U3']
    d1['R1'],d1['D2'],d1['L3'],d1['U4'] = d1['U4'],d1['R1'],d1['D2'],d1['L3']
    r.append((d1,"F2"))

    #F_1
    d1=d.copy()
    d1['F1'],d1['F2'],d1['F3'],d1['F4'] = d['F2'],d['F3'],d['F4'],d['F1']
    d1['R4'],d1['D1'],d1['L2'],d1['U3'] = d['D1'],d['L2'],d['U3'],d['R4']
    d1['U4'],d1['R1'],d1['D2'],d1['L3'] = d['R1'],d['D2'],d['L3'],d['U4']
    r.append((d1,"F_1"))

    return r



#génère récursivement une liste de positions possibles atteignables à partir
#d'une position donnée (liste_position) en effectuant des mouvements spécifiques
#définis par la fonction mouvement. Elle enregistre également les mouvements
#effectués (liste_position_mouv). Si la longueur de la liste des positions
#dépasse i, elle enregistre les mouvements dans le dictionnaire global dictio
def resolution_arbre1_aux(liste_position, liste_position_mouv, i):
    global dictio

    if len(liste_position) > i:
        l = []
        for i in liste_position_mouv:
            l.append(i[1])
        dictio[str(liste_position[-1])] = l
        return False

    for x in mouvement(liste_position[-1]):
        if x[0] not in liste_position:
            liste_position.append(x[0])
            liste_position_mouv.append(x)
            resolution_arbre1_aux(liste_position,liste_position_mouv,i)
            liste_position.pop()
            liste_position_mouv.pop()



#initialise le processus de résolution en appelant resolution_arbre1_aux avec
#une position initiale du cub parfait et une liste vide de mouvements. Elle explore les
#différentes positions possibles du cube, enregistre les mouvements nécessaires
#pour les atteindre dans le dictionnaire global dictio, puis écrit ce dictionnaire
#dans un fichier texte appelé 'solution_arbre_1.txt'.
def resolution_arbre1():
    global dictio
    global d_parf

    d = d_parf
    liste_position = [d]
    liste_position_mouv = [(d,"final")]
    
#5 pour crée 5mv 
    for i in range(5,0,-1):
        resolution_arbre1_aux(liste_position,liste_position_mouv,i)

    with open('solution_arbre_1.txt', 'w') as fichier_1:
        fichier_1.write(str(dictio))

    return



#prend un chemin de mouvements et renvoie son inverse en remplaçant chaque
#mouvement par son opposé
def chemin_inverse(chemin):
    nouveau_chemin = []

    for i in chemin:
        if i == "U":
            nouveau_chemin.append("U_1")
        elif i == "U_1":
            nouveau_chemin.append("U")
        elif i == "R":
            nouveau_chemin.append("R_1")
        elif i == "R_1":
            nouveau_chemin.append("R")
        elif i == "F":
            nouveau_chemin.append("F_1")
        elif i == "F_1":
            nouveau_chemin.append("F")
        else:
            nouveau_chemin.append(i)

    nouveau_chemin.reverse()
    return nouveau_chemin



#La fonction trie_dictio organise les informations du dictionnaire global dictio
#en plusieurs sous-dictionnaires (dictio1, dictio2, ..., dictio6) en fonction de
#la longueur des mouvements. Ensuite, elle enregistre chaque sous-dictionnaire
#dans un fichier texte correspondant à la couche correspondante
def trie_dictio():
    global dictio
    global dictio5

    for cle, valeur in dictio.items():
        if len(valeur) == 6:
            dictio5[cle] = valeur
            
    with open('solution_arbre_1_couche5.txt', 'w') as fichier_c5:
        fichier_c5.write(str(dictio5))


    return



#La fonction resolution_arbre2_aux tente de résoudre le cube en explorant les
#différentes positions possibles. Elle utilise une approche récursive, vérifie
#la présence de la position actuelle dans des dictionnaires spécifiques à chaque
#couche, et retourne la liste des mouvements nécessaires pour atteindre la solution
#si elle est trouvée. Sinon, elle renvoie False.
def resolution_arbre2_aux(liste_position,liste_position_mouv,i):
    global d_parf
    if (i == 1):
        if liste_position[-1] == d_parf:
            return True
        if str(liste_position[-1]) in dictio:
            return True
    if (i > 1):
        if str(liste_position[-1]) in dictio5:
            return True


    if len(liste_position) > i:
        return False

    for x in mouvement(liste_position[-1]):
        if x[0] not in liste_position:
            liste_position.append(x[0])
            liste_position_mouv.append(x)
            if resolution_arbre2_aux(liste_position,liste_position_mouv,i):
                return liste_position_mouv
            liste_position.pop()
            liste_position_mouv.pop()

    return False



#initialise la résolution du cube en appelant la fonction auxiliaire
#resolution_arbre2_aux
#La fonction tente de résoudre le cube en autorisant un nombre croissant de
#mouvements pour trouver la solution optimale.
def resolution_arbre2(d):
    global d_parf
    d = ordre(d)
    d_parf = parfait(d)
    # print(d_parf)
    
    
    if d == d_parf:
        return True

    resolution_arbre1()
    trie_dictio()
    liste_position = [d]
    liste_position_mouv = [(d,"initial")]
    reponse = False
    mouv = []
    pos = []
    #7 pour 5 mv
    for i in range(1,7):
        reponse = resolution_arbre2_aux(liste_position,liste_position_mouv,i)
        # print(reponse)
        if not reponse:
            continue
        else:
            break

    if reponse == True:
        mouv = dictio[str(d)]
        solu = chemin_inverse(mouv)
        solu.insert(0,'initial')
    elif not reponse:
        solu = "le programme n'a pas trouvé de solution"
    else:
        for i in reponse:
            mouv.append(i[1])
            pos.append(i[0])
        mouv2 = dictio[str(pos[-1])]
        mouv3 = chemin_inverse(mouv2)
        solu = mouv+mouv3
    return solu

        

teste = {'U1': 'yellow', 'U2': 'yellow', 'U3': 'yellow', 'U4': 'yellow', 'F1': 'blue', 'F2': 'blue', 'F3': 'blue', 'F4': 'blue', 'B1': 'green', 'B2': 'green', 'B3': 'green', 'B4': 'green', 'L1': 'orange', 'L2': 'orange', 'L3': 'orange', 'L4': 'orange', 'D1': 'white', 'D2': 'white', 'D3': 'white', 'D4': 'white', 'R1': 'red', 'R2': 'red', 'R3': 'red', 'R4': 'red'}

teste2 = {'U1': 'red', 'U2': 'blue', 'U3': 'orange', 'U4': 'yellow', 'F1': 'blue', 'F2': 'white', 'F3': 'white', 'F4': 'orange', 'B1': 'yellow', 'B2': 'green', 'B3': 'red', 'B4': 'yellow', 'L1': 'orange', 'L2': 'orange', 'L3': 'green', 'L4': 'green', 'D1': 'white', 'D2': 'red', 'D3': 'green', 'D4': 'white', 'R1': 'blue', 'R2': 'red', 'R3': 'red', 'R4': 'blue'}

teste3 = {'U1': 'green', 'U2': 'blue', 'U3': 'orange', 'U4': 'red', 'F1': 'white', 'F2': 'blue', 'F3': 'green', 'F4': 'green', 'B1': 'yellow', 'B2': 'white', 'B3': 'red', 'B4': 'orange', 'L1': 'orange', 'L2': 'blue', 'L3': 'orange', 'L4': 'green', 'D1': 'yellow', 'D2': 'yellow', 'D3': 'blue', 'D4': 'white', 'R1': 'yellow', 'R2': 'red', 'R3': 'white', 'R4': 'red'}

teste4 = {'U1': 'green', 'U2': 'blue', 'U3': 'orange', 'U4': 'red', 'F1': 'white', 'F2': 'blue', 'F3': 'green', 'F4': 'green', 'B1': 'yellow', 'B2': 'white', 'B3': 'red', 'B4': 'orange', 'L1': 'orange', 'L2': 'blue', 'L3': 'orange', 'L4': 'green', 'D1': 'yellow', 'D2': 'yellow', 'D3': 'blue', 'D4': 'white', 'R1': 'yellow', 'R2': 'red', 'R3': 'white', 'R4': 'red'}

teste5 = {'U1': 'yellow', 'U2': 'blue', 'U3': 'red', 'U4': 'yellow', 'F1': 'orange', 'F2': 'yellow', 'F3': 'orange', 'F4': 'blue', 'B1': 'white', 'B2': 'red', 'B3': 'red', 'B4': 'red', 'L1': 'green', 'L2': 'green', 'L3': 'yellow', 'L4': 'green', 'D1': 'orange', 'D2': 'green', 'D3': 'white', 'D4': 'white', 'R1': 'blue', 'R2': 'orange', 'R3': 'blue', 'R4': 'white'}

teste6 = {'U1': 'yellow', 'U2': 'green', 'U3': 'white', 'U4': 'red', 'F1': 'white', 'F2': 'blue', 'F3': 'orange', 'F4': 'yellow', 'B1': 'orange', 'B2': 'blue', 'B3': 'red', 'B4': 'yellow', 'L1': 'red', 'L2': 'blue', 'L3': 'green', 'L4': 'green', 'D1': 'orange', 'D2': 'blue', 'D3': 'green', 'D4': 'white', 'R1': 'orange', 'R2': 'white', 'R3': 'red', 'R4': 'yellow'}

teste7 = {'U1': 'yellow', 'U2': 'red', 'U3': 'red', 'U4': 'red', 'F1': 'yellow', 'F2': 'yellow', 'F3': 'orange', 'F4': 'blue', 'B1': 'white', 'B2': 'green', 'B3': 'red', 'B4': 'white', 'L1': 'orange', 'L2': 'green', 'L3': 'yellow', 'L4': 'green', 'D1': 'orange', 'D2': 'green', 'D3': 'orange', 'D4': 'white', 'R1': 'blue', 'R2': 'blue', 'R3': 'blue', 'R4': 'white'}

teste8 = {'U1': 'white', 'U2': 'yellow', 'U3': 'yellow', 'U4': 'white', 'F1': 'orange', 'F2': 'red', 'F3': 'orange', 'F4': 'red', 'B1': 'red', 'B2': 'orange', 'B3': 'red', 'B4': 'orange', 'L1': 'green', 'L2': 'blue', 'L3': 'blue', 'L4': 'green', 'D1': 'white', 'D2': 'yellow', 'D3': 'yellow', 'D4': 'white', 'R1': 'green', 'R2': 'blue', 'R3': 'blue', 'R4': 'green'}

teste9 = {'U1': 'yellow', 'U2': 'blue', 'U3': 'orange', 'U4': 'white', 'F1': 'orange', 'F2': 'green', 'F3': 'yellow', 'F4': 'orange', 'B1': 'red', 'B2': 'blue', 'B3': 'red', 'B4': 'yellow', 'L1': 'red', 'L2': 'blue', 'L3': 'blue', 'L4': 'green', 'D1': 'yellow', 'D2': 'red', 'D3': 'orange', 'D4': 'white', 'R1': 'white', 'R2': 'white', 'R3': 'green', 'R4': 'green'}

teste10 = {'U1': 'white', 'U2': 'yellow', 'U3': 'blue', 'U4': 'yellow', 'F1': 'orange', 'F2': 'white', 'F3': 'orange', 'F4': 'red', 'B1': 'red', 'B2': 'orange', 'B3': 'red', 'B4': 'blue', 'L1': 'green', 'L2': 'green', 'L3': 'green', 'L4': 'green', 'D1': 'yellow', 'D2': 'white', 'D3': 'orange', 'D4': 'white', 'R1': 'red', 'R2': 'blue', 'R3': 'yellow', 'R4': 'blue'}

testeF = {'U1': 'blue', 'U2': 'yellow', 'U3': 'yellow', 'U4': 'yellow', 'F1': 'blue', 'F2': 'blue', 'F3': 'orange', 'F4': 'orange', 'B1': 'green', 'B2': 'green', 'B3': 'red', 'B4': 'red', 'L1': 'orange', 'L2': 'orange', 'L3': 'green', 'L4': 'green', 'D1': 'white', 'D2': 'white', 'D3': 'white', 'D4': 'white', 'R1': 'red', 'R2': 'red', 'R3': 'blue', 'R4': 'blue'}

testeT = {'U1': 'blue', 'U2': 'white', 'U3': 'yellow', 'U4': 'green', 'F1': 'orange', 'F2': 'green', 'F3': 'orange', 'F4': 'green', 'B1': 'red', 'B2': 'orange', 'B3': 'blue', 'B4': 'blue', 'L1': 'white', 'L2': 'white', 'L3': 'yellow', 'L4': 'yellow', 'D1': 'red', 'D2': 'blue', 'D3': 'red', 'D4': 'red', 'R1': 'orange', 'R2': 'green', 'R3': 'white', 'R4': 'yellow'}