#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create your objects here.
ev3 = EV3Brick()

moteur_plat =Motor(Port.B, positive_direction=Direction.CLOCKWISE, gears=[12,36])

moteur_bras = Motor(Port.A, positive_direction=Direction.CLOCKWISE)

moteur_scan = Motor(Port.C, positive_direction=Direction.CLOCKWISE, gears=[12,36])

capteur_couleur = ColorSensor(Port.S2)

# Write your program here.

def quart_pos_L():
    #moteur plateforme quart de tour bras relevé
    moteur_plat.run_angle(180, -90, then=Stop.HOLD, wait=True)

def quart_pos_pasL():
    #abbaisse le bras
    #moteur plateforme quart de tour
    #releve le bras
    moteur_bras.run_angle(180, 100, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, -120, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, 50, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, -20, then=Stop.HOLD, wait=True)
    moteur_bras.run_angle(120, -100, then=Stop.HOLD, wait=True)

def quart_neg_L():
    #moteur plateforme quart de tour négatif bras relevé
    moteur_plat.run_angle(180, 90, then=Stop.HOLD, wait=True)

def quart_neg_pasL():
    #abbaisse le bras
    #moteur plateforme quart de tour négatif
    #releve le bras
    moteur_bras.run_angle(180, 100, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, 120, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, -50, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, 20, then=Stop.HOLD, wait=True)
    moteur_bras.run_angle(120, -100, then=Stop.HOLD, wait=True)

def demi_L():
    #moteur plateforme demi tour
    moteur_plat.run_angle(180, 180, then=Stop.HOLD, wait=True)

def demi_pasL():
    #abbaisse le bras
    #moteur plateforme demi de tour
    #releve le bras
    moteur_bras.run_angle(180, 100, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, 210, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, -50, then=Stop.HOLD, wait=True)
    moteur_plat.run_angle(180, 20, then=Stop.HOLD, wait=True)
    moteur_bras.run_angle(120, -100, then=Stop.HOLD, wait=True)

def bascule():
    #abaisse le bras
    #tire sur le cube
    #pousse le cube
    #relève le bras
    moteur_bras.run_angle(180, 190, then=Stop.HOLD, wait=True)
    moteur_bras.run_angle(180, -190, then=Stop.HOLD, wait=True)

def approche_tete_scan():
    #penche la tete pour scanner
    moteur_scan.run_angle(180, -200, then=Stop.HOLD, wait=True)

def releve_tete_scan():
    #releve la tete apres scan
    moteur_scan.run_angle(180, 200, then=Stop.HOLD, wait=True)

def huitieme_tour_pos():
    # 1/8 tour positif
    moteur_plat.run_angle(180, -45, then=Stop.HOLD, wait=True)

def huitieme_tour_neg():
    # 1/8 tour négatif
    moteur_plat.run_angle(180, 45, then=Stop.HOLD, wait=True)

def Urob():
    quart_pos_pasL()
    quart_neg_L()

def U_1rob():
    quart_neg_pasL()
    quart_pos_L()

def U_2rob():
    demi_pasL()
    demi_L()

def Frob():
    bascule()
    quart_pos_pasL()
    bascule()
    bascule()
    bascule()

def F_1rob():
    bascule()
    quart_neg_pasL()
    bascule()
    bascule()
    bascule()

def F_2rob():
    bascule()
    demi_pasL()
    bascule()
    bascule()
    bascule()

def Rrob():
    quart_neg_L()
    bascule()
    quart_pos_pasL()
    bascule()
    bascule()
    bascule()
    quart_pos_L()

def R_2rob():
    quart_neg_L()
    bascule()
    demi_pasL()
    bascule()
    bascule()
    bascule()
    quart_pos_L()

def R_1rob():
    quart_neg_L()
    bascule()
    quart_neg_pasL()
    bascule()
    bascule()
    bascule()
    quart_pos_L()

def scan_face():
    #scan d'une face
    X=[0,0,0,0]

    huitieme_tour_neg()
    approche_tete_scan()

    X[0]=capteur_couleur.color()
    deg = 0
    while (X[0]==Color.BROWN) or (X[0]==None):
        moteur_plat.run_angle(20, 2, then=Stop.HOLD, wait=True)
        deg -= 2
        X[0]=capteur_couleur.color()
    moteur_plat.run_angle(400, deg, then=Stop.HOLD, wait=True)
    quart_neg_L()

    deg = 0
    X[1]=capteur_couleur.color()
    while (X[1]==Color.BROWN) or (X[1]==None):
        moteur_plat.run_angle(20, 2, then=Stop.HOLD, wait=True)
        deg -= 2
        X[1]=capteur_couleur.color()
    moteur_plat.run_angle(400, deg, then=Stop.HOLD, wait=True)
    quart_neg_L()

    deg = 0
    X[2]= capteur_couleur.color()
    while (X[2]==Color.BROWN) or (X[2]==None):
        moteur_plat.run_angle(20, 2, then=Stop.HOLD, wait=True)
        deg -= 2
        X[2]=capteur_couleur.color()
    moteur_plat.run_angle(400, deg, then=Stop.HOLD, wait=True)
    quart_neg_L()

    deg = 0
    X[3]= capteur_couleur.color()
    while (X[3]==Color.BROWN) or (X[3]==None):
        moteur_plat.run_angle(20, 2, then=Stop.HOLD, wait=True)
        deg -= 2
        X[3]=capteur_couleur.color()
    moteur_plat.run_angle(400, deg, then=Stop.HOLD, wait=True)
    releve_tete_scan()
    huitieme_tour_neg()

    for i in range(4):
        if X[i]==Color.BLUE:
            X[i]='blue'
        if X[i]==Color.BLACK:
            X[i]='orange'
        if X[i]==Color.RED:
            X[i]='red'
        if X[i]==Color.GREEN :
            X[i]='green'
        if X[i]==Color.WHITE:
            X[i]='white'
        if X[i]==Color.YELLOW:
            X[i]='yellow'
    print(X)
    return X

def scan_tot():
    #scan de toutes les faces
    liste_U=[]
    liste_D=[]
    liste_F=[]
    liste_R=[]
    liste_B=[]
    liste_L=[]
    d = {'U1' : 'yellow', 'U2' : 'yellow', 'U3' : 'yellow', 'U4' : 'yellow','F1' : 'orange', 'F2' : 'orange', 'F3' : 'orange', 'F4' : 'orange','B1' : 'red', 'B2' : 'red', 'B3' : 'red', 'B4' : 'red','L1' : 'green', 'L2' : 'green', 'L3' : 'green', 'L4' : 'green','D1' : 'white', 'D2' : 'white', 'D3' : 'white', 'D4' : 'white','R1' : 'blue', 'R2' : 'blue', 'R3' : 'blue', 'R4' : 'blue'}
    print(d)
    print("U")
    liste_U=scan_face()
    d['U1'],d['U2'],d['U3'],d['U4'] = liste_U[0],liste_U[3],liste_U[2],liste_U[1]
    print(d['U1'],d['U2'],d['U3'],d['U4'] )
    print(d)
    bascule()


    print("\n")
    print("B")
    liste_B=scan_face()
    d['B1'],d['B2'],d['B3'],d['B4'] = liste_B[2],liste_B[1],liste_B[0],liste_B[3]
    print(d['B1'],d['B2'],d['B3'],d['B4'])
    bascule()


    print("\n")
    print("D")
    liste_D=scan_face()
    d['D1'],d['D2'],d['D3'],d['D4'] = liste_D[0],liste_D[3],liste_D[2],liste_D[1]
    print(d['D1'],d['D2'],d['D3'],d['D4'])
    bascule()


    print("\n")
    print("F")
    liste_F=scan_face()
    d['F1'],d['F2'],d['F3'],d['F4'] = liste_F[0],liste_F[3],liste_F[2],liste_F[1]
    print(d['F1'],d['F2'],d['F3'],d['F4'] )
    quart_pos_L()
    bascule()


    print("\n")
    print("R")
    liste_R=scan_face()
    d['R1'],d['R2'],d['R3'],d['R4'] = liste_R[1],liste_R[0],liste_R[3],liste_R[2]
    print(d['R1'],d['R2'],d['R3'],d['R4'])
    bascule()
    bascule()


    print("\n")
    print("L")
    liste_L=scan_face()
    d['L1'],d['L2'],d['L3'],d['L4'] = liste_L[1],liste_L[0],liste_L[3],liste_L[2]
    print(d['L1'],d['L2'],d['L3'],d['L4'] )
    quart_neg_L()
    bascule()
    quart_neg_L()
    print(d)
    return d

def execute_mouvements(mouvements):
    #execute les mouvements d'une liste
    for i in mouvements:
        if i=='U':
            Urob()
        if i=='U_1':
            U_1rob()
        if i=='U2':
            U_2rob()
        if i=='R':
            Rrob()
        if i=='R_1':
            R_1rob()
        if i=='R2':
            R_2rob()
        if i=='F':
            Frob()
        if i=='F_1':
            F_1rob()
        if i=='F2':
            F_2rob()

def resolution(liste):
    # Exécute les mouvements pour résoudre un cube selon le résultat fournies par l'algorithme de résolution.
    execute_mouvements(liste[1:-1])



#Utilisation du script :

#1. Exécuter `scan_tot()` pour obtenir les données initiales.
#2. Copier le résultat de `scan_tot()` pour usage ultérieur.
#3. Déterminer un chemin de résolution basé sur ce résultat.
#4. Commenter l'appel à `scan_tot()` et décommenter `resolution()` avec le chemin trouvé.
#5. Exécuter à nouveau le script pour appliquer la résolution.


scan_tot()  # Exécuter puis commenter après usage
#resolution("chemin_de_resolution")  # Décommenter et remplacer avec le chemin exact





