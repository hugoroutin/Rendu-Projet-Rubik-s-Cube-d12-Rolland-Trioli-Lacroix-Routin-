# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:29:49 2024

@author: vaian
"""

import tkinter.font as tkFont #pour la police soulignée

from random import* #pour la fonction generate_cube

import tkinter as tk 
It=True

import est_resolvable

import resolution_angle


    
#%% initialisation de toutes les variables

#definition d'un dico initial valable
d = {'U1' : 'yellow', 'U2' : 'yellow', 'U3' : 'yellow', 'U4' : 'yellow',
      'F1' : 'orange', 'F2' : 'orange', 'F3' : 'orange', 'F4' : 'orange',
      'B1' : 'red', 'B2' : 'red', 'B3' : 'red', 'B4' : 'red',
      'L1' : 'green', 'L2' : 'green', 'L3' : 'green', 'L4' : 'green',
      'D1' : 'white', 'D2' : 'white', 'D3' : 'white', 'D4' : 'white',
      'R1' : 'blue', 'R2' : 'blue', 'R3' : 'blue', 'R4' : 'blue',}

#Variable qui indique si on est en mode remplissage manuel
remplissage_manuel_active=0

#Variable qui indique à quelle case on en est dans le remplissage manuel
c=0

#Pareil avec l_c 
l_c = ['U1','U2','U3','U4','F1','F2','F3','F4','D1','D2','D3','D4',
        'L1','L2','L3','L4','R1','R2','R3','R4','B1','B2','B3','B4']

#creation d'une pile pour la fonction retour de l'interface
pile=[] #contient toutes les actions qu'on peut faire sur l'interface
pile_gen=[] #contient les dico precedents lorsqu'on fait appel à generate cube

#Initialise la sequence de mouvement de resolution 
mouvements=''




#%%

#Fonction de résolution

def resoudre():
    global mouvements
    global d
    #vérifie que le cube est résolvable
    if est_resolvable.est_resolvable(d):
        mouvements = resolution_angle.resolution_arbre2(d)
        if type(mouvements) != bool:
            del(mouvements[0])
            del(mouvements[-1])
        else :
            mouvements= ['Le cube est résolu !']
    else:
        mouvements= "Ce cube n'est pas resolvable"
    #on actualise le canva
    dessin(d,mouvements)

#%% generer un cube aleatoire

def generate_cube():
    global d
    global pile
    pile.append('gen_cub')
    pile_gen.append(d.copy())
    global c
    global mouvements
    global remplissage_manuel_active
    
    remplissage_manuel_active=False
    c=0
    # depart resolu donc possible
    d = {'U1' : 'yellow', 'U2' : 'yellow', 'U3' : 'yellow', 'U4' : 'yellow',
         'F1' : 'orange', 'F2' : 'orange', 'F3' : 'orange', 'F4' : 'orange',
         'B1' : 'red', 'B2' : 'red', 'B3' : 'red', 'B4' : 'red',
         'L1' : 'green', 'L2' : 'green', 'L3' : 'green', 'L4' : 'green',
         'D1' : 'white', 'D2' : 'white', 'D3' : 'white', 'D4' : 'white',
         'R1' : 'blue', 'R2' : 'blue', 'R3' : 'blue', 'R4' : 'blue',}
    #effectue 20 mouvements en aléatoire parmi U, R , F
    for i in range (20):
        n=randint(0,3)
        if n==0:
            # equivalent à U
            d['U2'],d['U3'],d['U4'],d['U1'] = d['U1'],d['U2'],d['U3'],d['U4'] 
            d['L1'],d['B1'],d['R1'],d['F1'] = d['F1'],d['L1'],d['B1'],d['R1'] 
            d['L2'],d['B2'],d['R2'],d['F2'] = d['F2'],d['L2'],d['B2'],d['R2']
        if n==1:
            # equivalent à R
            d['R2'],d['R3'],d['R4'],d['R1'] = d['R1'],d['R2'],d['R3'],d['R4'] 
            d['U2'],d['B4'],d['D2'],d['F2'] = d['F2'],d['U2'],d['B4'],d['D2'] 
            d['U3'],d['B1'],d['D3'],d['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
        if n==2:
            # equivalent à F
            d['F2'],d['F3'],d['F4'],d['F1'] = d['F1'],d['F2'],d['F3'],d['F4'] 
            d['D1'],d['L2'],d['U3'],d['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
            d['R1'],d['D2'],d['L3'],d['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
    resoudre()
    dessin(d,mouvements)
    return d

    
#%% dessin du patron du cube    

def dessin(d, mouvements) :
    #remet a zero le canva
    canvas.delete('all')
    #dessine le nouveau canva
    l = ['L1', 'L2', 'F1', 'F2', 'R1', 'R2', 'B1', 'B2']
    T = 0
    for i in range(2, 8*tcarre+2, tcarre):
        canvas.create_rectangle(i, 100+2*tcarre, i+tcarre, 100+3*tcarre, fill = d[l[T]])
        T += 1
    l = ['L4', 'L3', 'F4', 'F3', 'R4', 'R3', 'B4', 'B3']
    T = 0
    for i in range(2, 8*tcarre+2, tcarre):
        canvas.create_rectangle(i, 100+3*tcarre, i+tcarre, 100+4*tcarre, fill = d[l[T]])
        T += 1
    l = ['U1', 'U4', 'F1', 'F4', 'D1', 'D4']
    T = 0
    for j in range(100, 6*tcarre+100, tcarre) :
        canvas.create_rectangle(2*tcarre+2, j, 3*tcarre+2, j+tcarre, fill = d[l[T]])
        T += 1
    l = ['U2', 'U3', 'F2', 'F3', 'D2', 'D3']
    T = 0
    for j in range(100, 6*tcarre+100, tcarre) :
        canvas.create_rectangle(3*tcarre+2, j, 4*tcarre+2, j+tcarre, fill = d[l[T]])
        T += 1
    #affiche le texte a afficher
    if type(mouvements) != bool:
        texte_solution= canvas.create_text(200, 80, text=mouvements, fill="black", font=("Helvetica 15 bold"))

#%% Definitions du remplissage manuel des cases  

def bleu() : 
    global d
    global c
    global remplissage_manuel_active
    global l_c
    global pile
    global mouvements

    #verifie que l'on est bien en train de remplir manuellement

    if remplissage_manuel_active==True:
        #modifie le dictionnaire des couleurs
        d[l_c[c]] = 'blue'
        pile.append('blu') #pour la fonction retour
        # vérifie que l'on est pas en fin du remplissage
        if c < 23 :
            c += 1
            d[l_c[c]] = 'black'
            dessin(d,'')
        else:
            #desactive le remplissage
            remplissage_manuel_active=False
            #reset le compte pour la prochaine fois
            c=0
            dessin(d,mouvements)
            resoudre()
            

def orange() : 
    global d
    global c
    global mouvements
    global remplissage_manuel_active
    global l_c
    global pile
    if remplissage_manuel_active==True:
        d[l_c[c]] = 'orange'
        pile.append('ora')
        if c < 23 :
            c += 1
            d[l_c[c]] = 'black'
            dessin(d,'')
        else:
            remplissage_manuel_active=False
            c=0
            dessin(d,mouvements)
            resoudre()
            

def jaune() : 
    global d
    global c
    global mouvements
    global remplissage_manuel_active
    global l_c
    global pile
    if remplissage_manuel_active==True:
        d[l_c[c]] = 'yellow'
        pile.append('yel')
        if c < 23 :
            c += 1
            d[l_c[c]] = 'black'
            dessin(d,'')
        else:
            remplissage_manuel_active=False
            c=0
            dessin(d,mouvements)
            resoudre()
            

def vert() : 
    global d
    global c
    global mouvements
    global remplissage_manuel_active
    global l_c
    global pile
    if remplissage_manuel_active==True:
        d[l_c[c]] = 'green'
        pile.append('gre')
        if c < 23 :
            c += 1
            d[l_c[c]] = 'black'
            dessin(d,'')
        else:
            remplissage_manuel_active=False
            c=0
            dessin(d,mouvements)
            resoudre()
            

def blanc() : 
    global d
    global c
    global mouvements
    global remplissage_manuel_active
    global l_c
    global pile
    if remplissage_manuel_active==True:
        d[l_c[c]] = 'white'
        pile.append('whi')
        if c < 23 :
            c += 1
            d[l_c[c]] = 'black' 
            dessin(d,'')
        else:
            remplissage_manuel_active=False
            c=0
            dessin(d,mouvements)
            resoudre()
    
    
def rouge() : 
    global d
    global c
    global mouvements
    global remplissage_manuel_active
    global l_c
    global pile
    if remplissage_manuel_active==True:
        d[l_c[c]] = 'red'
        pile.append('red')
        if c < 23 :
            c += 1
            d[l_c[c]] = 'black' 
            dessin(d,'')
        else:
            remplissage_manuel_active=False
            c=0
            dessin(d,mouvements)
            resoudre()
            


def remplissage_manuel():
    global remplissage_manuel_active
    #active le remplissage
    remplissage_manuel_active=True
    global d
    global mouvements
    global c
    
    d = {'U1' : 'black', 'U2' : 'lightgray', 'U3' : 'lightgray', 'U4' : 'lightgray',
        'F1' : 'lightgray', 'F2' : 'lightgray', 'F3' : 'lightgray', 'F4' : 'lightgray',
        'B1' : 'lightgray', 'B2' : 'lightgray', 'B3' : 'lightgray', 'B4' : 'lightgray',
        'L1' : 'lightgray', 'L2' : 'lightgray', 'L3' : 'lightgray', 'L4' : 'lightgray',
        'D1' : 'lightgray', 'D2' : 'lightgray', 'D3' : 'lightgray', 'D4' : 'lightgray',
        'R1' : 'lightgray', 'R2' : 'lightgray', 'R3' : 'lightgray', 'R4' : 'lightgray',}
    l_c = ['U1','U2','U3','U4','F1','F2','F3','F4','D1','D2','D3','D4',
           'L1','L2','L3','L4','R1','R2','R3','R4','B1','B2','B3','B4']
    c = 0
    
    dessin(d,'')


#%% fonction commande pour config initiale du cube

def remettre_au_debut():
    global c
    global remplissage_manuel_active
    global d
    global mouvements
    #désactive le remplisssage manuel
    remplissage_manuel_active=False
    global pile
    pile.append('restart')
    c=0
    #dictionnaire initial
    d = {'U1' : 'yellow', 'U2' : 'yellow', 'U3' : 'yellow', 'U4' : 'yellow',
         'F1' : 'orange', 'F2' : 'orange', 'F3' : 'orange', 'F4' : 'orange',
         'B1' : 'red', 'B2' : 'red', 'B3' : 'red', 'B4' : 'red',
         'L1' : 'green', 'L2' : 'green', 'L3' : 'green', 'L4' : 'green',
         'D1' : 'white', 'D2' : 'white', 'D3' : 'white', 'D4' : 'white',
         'R1' : 'blue', 'R2' : 'blue', 'R3' : 'blue', 'R4' : 'blue',}
    mouvements=''
    dessin (d,mouvements)

#%% definiton de tous les mouvements autorises (9 en tout en fixant un sommet)

def U() :
    # vérifie que l'on est pas en config remplissage manuel
    if remplissage_manuel_active==False:
        global d
        global mouvements
        #altère le dictionnaire pour tenir compte du mouvement
        d['U2'],d['U3'],d['U4'],d['U1'] = d['U1'],d['U2'],d['U3'],d['U4'] 
        d['L1'],d['B1'],d['R1'],d['F1'] = d['F1'],d['L1'],d['B1'],d['R1'] 
        d['L2'],d['B2'],d['R2'],d['F2'] = d['F2'],d['L2'],d['B2'],d['R2'] 
        #on prend en mémoire le mouvement
        pile.append(U)
        # vérifie si on a bien suivi le chemin de résolution prescrit si il existe
        if mouvements:
            if str(mouvements[0])=="U":
                del(mouvements[0])
            else:
                resoudre()
        else:
            resoudre()
        
        dessin(d,mouvements)
        
    

def U_1():
    if remplissage_manuel_active==False:
        global d
        global mouvements
        d['U1'],d['U2'],d['U3'],d['U4']=d['U2'],d['U3'],d['U4'],d['U1']
        d['F1'],d['L1'],d['B1'],d['R1']=d['L1'],d['B1'],d['R1'],d['F1']
        d['F2'],d['L2'],d['B2'],d['R2'] =d['L2'],d['B2'],d['R2'],d['F2']
        pile.append(U_1)
        if mouvements:
            if str(mouvements[0])=="U_1":
                del(mouvements[0])
            else:
                resoudre()
        else:
            resoudre()
            
        dessin(d,mouvements)
    
    

def U_2():
    global pile
    global mouvements
    if remplissage_manuel_active==False:
        d['U2'],d['U3'],d['U4'],d['U1'] = d['U1'],d['U2'],d['U3'],d['U4'] 
        d['L1'],d['B1'],d['R1'],d['F1'] = d['F1'],d['L1'],d['B1'],d['R1'] 
        d['L2'],d['B2'],d['R2'],d['F2'] = d['F2'],d['L2'],d['B2'],d['R2']
        d['U2'],d['U3'],d['U4'],d['U1'] = d['U1'],d['U2'],d['U3'],d['U4'] 
        d['L1'],d['B1'],d['R1'],d['F1'] = d['F1'],d['L1'],d['B1'],d['R1'] 
        d['L2'],d['B2'],d['R2'],d['F2'] = d['F2'],d['L2'],d['B2'],d['R2']
        pile.append(U_2)
        if mouvements:
            if str(mouvements[0])=="U2":
                del(mouvements[0])
                dessin(d,mouvements)
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)

def R():
    if remplissage_manuel_active==False:
        global d
        global mouvements
        d['R2'],d['R3'],d['R4'],d['R1'] = d['R1'],d['R2'],d['R3'],d['R4'] 
        d['U2'],d['B4'],d['D2'],d['F2'] = d['F2'],d['U2'],d['B4'],d['D2'] 
        d['U3'],d['B1'],d['D3'],d['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
        pile.append(R)
        if mouvements:
            if str(mouvements[0])=="R":
                del(mouvements[0])
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)
        


def R_1():
    if remplissage_manuel_active==False:
        global d
        global mouvements
        d['R1'],d['R2'],d['R3'],d['R4']=d['R2'],d['R3'],d['R4'],d['R1']
        d['F2'],d['U2'],d['B4'],d['D2']=d['U2'],d['B4'],d['D2'],d['F2']
        d['F3'],d['U3'],d['B1'],d['D3']=d['U3'],d['B1'],d['D3'],d['F3']
        pile.append(R_1)
        if mouvements:
            if str(mouvements[0])=="R_1":
                del(mouvements[0])
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)
        
    

def R_2():
    global pile
    global mouvements
    if remplissage_manuel_active==False:
        d['R2'],d['R3'],d['R4'],d['R1'] = d['R1'],d['R2'],d['R3'],d['R4'] 
        d['U2'],d['B4'],d['D2'],d['F2'] = d['F2'],d['U2'],d['B4'],d['D2'] 
        d['U3'],d['B1'],d['D3'],d['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
        d['R2'],d['R3'],d['R4'],d['R1'] = d['R1'],d['R2'],d['R3'],d['R4'] 
        d['U2'],d['B4'],d['D2'],d['F2'] = d['F2'],d['U2'],d['B4'],d['D2'] 
        d['U3'],d['B1'],d['D3'],d['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
        
        pile.append(R_2)
        if mouvements:
            if str(mouvements[0])=="R2":
                del(mouvements[0])
                dessin(d,mouvements)
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)
    

def F() :
    if remplissage_manuel_active==False:
        global d
        global mouvements
        d['F2'],d['F3'],d['F4'],d['F1'] = d['F1'],d['F2'],d['F3'],d['F4'] 
        d['D1'],d['L2'],d['U3'],d['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
        d['R1'],d['D2'],d['L3'],d['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
        pile.append(F)
        if mouvements:
            if str(mouvements[0])=="F":
                del(mouvements[0])
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)
    
    
def F_1() :
    if remplissage_manuel_active==False:
        global d
        global mouvements
        d['F1'],d['F2'],d['F3'],d['F4'] = d['F2'],d['F3'],d['F4'],d['F1']
        d['R4'],d['D1'],d['L2'],d['U3'] = d['D1'],d['L2'],d['U3'],d['R4'] 
        d['U4'],d['R1'],d['D2'],d['L3'] = d['R1'],d['D2'],d['L3'],d['U4']
        pile.append(F_1)
        if mouvements:
            if str(mouvements[0])=="F_1":
                del(mouvements[0])
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)
    

def F_2():
    global pile
    global mouvements
    if remplissage_manuel_active==False:
        d['F2'],d['F3'],d['F4'],d['F1'] = d['F1'],d['F2'],d['F3'],d['F4'] 
        d['D1'],d['L2'],d['U3'],d['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
        d['R1'],d['D2'],d['L3'],d['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
        d['F2'],d['F3'],d['F4'],d['F1'] = d['F1'],d['F2'],d['F3'],d['F4'] 
        d['D1'],d['L2'],d['U3'],d['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
        d['R1'],d['D2'],d['L3'],d['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
        pile.append(F_2)
        if mouvements:
            if str(mouvements[0])=="F2":
                del(mouvements[0])
                dessin(d,mouvements)
            else:
                resoudre()
        else:
            resoudre()
        dessin(d,mouvements)
 
#%% fonction pour revenir en arrière sur l'interface

def retour():
    global d
    global c
    global remplissage_manuel_active
    global l_c
    global pile
    global mouvements
            
    if remplissage_manuel_active==True:
        if pile:
            x=pile.pop()
            #cas du replissage des cases, sauf la dernière
            if x=='blu' or x=='whi' or x=='ora' or x=='red' or x=='gre'or x=='yel':
                d[l_c[c]] = 'lightgray'
                d[l_c[c-1]] = 'black'
                c-=1
                dessin(d,'')

    if remplissage_manuel_active==False:
        if pile:
            x=pile.pop()
            #cas des mouvements
            if x==U:
                U_1()
                pile.pop()
            if x==F:
                F_1()
                pile.pop()
            if x==R:
                R_1()
                pile.pop()
            if x==U_1:
                U()
                pile.pop()
            if x==F_1:
                F()
                pile.pop()
            if x==R_1:
                R()
                pile.pop()
            if x==U_2:
                U_2()
                pile.pop()
            if x==F_2:
                F_2()
                pile.pop()
            if x==R_2:
                R_2()
                pile.pop()
            #cas de la dernière case du remplissage
            if x=='blu' or x=='whi' or x=='ora' or x=='red' or x=='gre'or x=='yel':
                c=23
                d[l_c[c]] = 'black'
                remplissage_manuel_active=True
                dessin(d,'')
            #cas du cube aléatoire généré
            if  x=='gen_cub':
                d=pile_gen.pop()
                dessin(d,'')
            #pour ne pas revenir en arrière après appui sur bouton restart
            if x=='restart':
                pile.append(x)
        
#%% creation de l'interface graphique

fenetre = tk.Tk()
fenetre.config(bg='ivory')

# mesure taille écran pour adapter taille du canva
h_ecran = fenetre.winfo_screenheight()
tcarre = int(((h_ecran/2)-100)/6)

canvas = tk.Canvas(fenetre, width=8*tcarre+1, height=h_ecran/2,bg='ivory')
fenetre.title("Resolution de mon rubik's cube 2 X 2") # titre de la fenetre

#definition de 2 types de police d'écriture
police_soulignee= tkFont.Font(family="Gabriola", size=20, weight="normal", slant="roman", underline=True)
police_normale= tkFont.Font(family="Gabriola", size=15, weight="normal", slant="roman", underline=False)

#tracé du canva
l = ['L1', 'L2', 'F1', 'F2', 'R1', 'R2', 'B1', 'B2']
T = 0
for i in range(2, 8*tcarre+2, tcarre):
    canvas.create_rectangle(i, 100+2*tcarre, i+tcarre, 100+3*tcarre, fill = d[l[T]])
    T += 1
l = ['L4', 'L3', 'F4', 'F3', 'R4', 'R3', 'B4', 'B3']
T = 0
for i in range(2, 8*tcarre+2, tcarre):
    canvas.create_rectangle(i, 100+3*tcarre, i+tcarre, 100+4*tcarre, fill = d[l[T]])
    T += 1
l = ['U1', 'U4', 'F1', 'F4', 'D1', 'D4']
T = 0
for j in range(100, 6*tcarre+100, tcarre) :
    canvas.create_rectangle(2*tcarre+2, j, 3*tcarre+2, j+tcarre, fill = d[l[T]])
    T += 1
l = ['U2', 'U3', 'F2', 'F3', 'D2', 'D3']
T = 0
for j in range(100, 6*tcarre+100, tcarre) :
    canvas.create_rectangle(3*tcarre+2, j, 4*tcarre+2, j+tcarre, fill = d[l[T]])
    T += 1
    
canvas.grid(row=2,column=4, columnspan=3, rowspan=7, padx=10, pady=10)
texte_solution= canvas.create_text(200, 80, text=mouvements, fill="black", font=("Helvetica 15 bold"))


#creation de tous les boutons mouvements

tex1=tk.Label(fenetre, text='Faire tourner mon cube :',bg='ivory')
tex1.grid(row=2,column=7,padx=10, columnspan=3)
tex1.configure(font=police_soulignee)


button1 = tk.Button(fenetre, text="U", command=U, bg='dark goldenrod')
button1.grid(row=3,column=7,pady=10)


button2 = tk.Button(fenetre, text="U_1", command=U_1, bg='dark goldenrod')
button2.grid(row=3,column=8,pady=10)
button3 = tk.Button(fenetre, text="U2", command=U_2, bg='dark goldenrod')
button3.grid(row=3,column=9,pady=10)
button4 = tk.Button(fenetre, text="R", command=R,bg='dark goldenrod')
button4.grid(row=4,column=7,pady=10)
button5 = tk.Button(fenetre, text="F", command=F,bg='dark goldenrod')
button5.grid(row=5,column=7,pady=10)
button6 = tk.Button(fenetre, text="R_1", command=R_1,bg='dark goldenrod')
button6.grid(row=4,column=8,pady=10)
button7 = tk.Button(fenetre, text="F_1", command=F_1,bg='dark goldenrod')
button7.grid(row=5,column=8,pady=10)
button8 = tk.Button(fenetre, text="R2", command=R_2,bg='dark goldenrod')
button8.grid(row=4,column=9,pady=10)
button9 = tk.Button(fenetre, text="F2", command=F_2,bg='dark goldenrod')
button9.grid(row=5,column=9,pady=10)

#Boutons ayant trait au remplissage manuel par l'utilisateur
button10=tk.Button(fenetre,text='Remplissage manuel',command=remplissage_manuel,bg='dark goldenrod')
button10.grid(row=2,column=1)
bou11 = tk.Button(fenetre, bg='red',text="Rouge", height=1, width=5, command=rouge)
bou11.grid(row=2,column=2)
bou12 = tk.Button(fenetre, bg='blue',text="Bleu", height=1, width=5, command=bleu)
bou12.grid(row=2,column=3)
bou13 = tk.Button(fenetre, bg='yellow',text="jaune", height=1, width=5, command=jaune)
bou13.grid(row=3,column=2)
bou14 = tk.Button(fenetre, bg='orange',text="orange", height=1, width=5, command=orange)
bou14.grid(row=3,column=3)
bou15 = tk.Button(fenetre, bg='green',text="vert", height=1, width=5, command=vert)
bou15.grid(row=4,column=2)


bou17 = tk.Button(fenetre, bg='white',text="blanc", height=1, width=5, command=blanc)
bou17.grid(row=4,column=3)


#Boutons pour plus de facilites de manipulations de l'interface
button20 = tk.Button(fenetre, text="cube aleatoire", command=generate_cube,bg='dark goldenrod')
button20.grid(row=9,column=6,padx=10)

button21 = tk.Button(fenetre, text="Restart", command=remettre_au_debut,bg='dark goldenrod')
button21.grid(row=9,column=5,padx=10)

button22 = tk.Button(fenetre, text="Retour", command=retour,bg='dark goldenrod')
button22.grid(row=9,column=4,padx=10)

button23= tk.Button(fenetre, text="Resoudre", command=resoudre,bg='dark goldenrod')
button23.grid(row=5,column=1)

button30=tk.Button(fenetre, text="Quitter", command=fenetre.destroy, fg='red4',bg='dark goldenrod')
button30.grid(row=10,column=1,padx=10)

#Les textes sur l'interface
rubi=tk.Label(fenetre, text="Rubik's cube 2x2", fg='black',bg='ivory')
rubi.config(font=("Algerian", 45)) 
rubi.grid(row=1,column=3, padx=10, pady=10, columnspan=5)


demarche=tk.Label(fenetre, text="Démarche pour résoudre votre rubik's cube :",bg='ivory')
etape1=tk.Label(fenetre, text='1- Cliquez sur Remplissage manuel.'+'\n'+'La case à remplir apparait en noir.'+'\n'+'2- Cliquez sur la couleur correspondant au carré noir.'+'\n'+"3- Continuez jusqu'au remplissage complet de tout le rubik's cube."+'\n'+'4- La suite des mouvements à effectuer apparait au dessus.',bg='ivory')

demarche.configure(font=police_soulignee)
demarche.grid(row=6, column=1, columnspan=3, pady=10)
etape1.configure(font=police_normale)
etape1.grid(row=6, column=1,columnspan=3, rowspan=4, padx=10)


expli0=tk.Label(fenetre, text='Convention de notations : Mouvements des faces:',bg='ivory')
expli1=tk.Label(fenetre,text='U=haut'+'\n'+'R=droite'+'\n'+'F=devant',bg='ivory')
expli2=tk.Label(fenetre,text='Sens de rotation (ce qui suit la lettre X) :',bg='ivory')
expli3=tk.Label(fenetre,text='X = 1/4 de tour dans sens horaire'+'\n'+'X_1 = 1/4 de tour dans sens anti-horaire'+'\n'+"X2 = 1/2 tour", fg='black',bg='ivory')

expli0.configure(font=police_soulignee)
expli0.grid(row=6, column=7,columnspan=4)
expli1.configure(font=police_normale)
expli1.grid(row=7, column=7,columnspan=3)
expli2.configure(font=police_soulignee)
expli2.grid(row=8, column=7,columnspan=3)
expli3.configure(font=police_normale)
expli3.grid(row=9, column=7,columnspan=3, rowspan=2)


fenetre.mainloop()