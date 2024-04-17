# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:49:43 2024

@author: routi
"""



# vérifie la condition sur l'orientation des sommets
def count_orientation(couleur1,couleur2,d):
    somme_1=0
    somme_2=0
    # attribue à certains sommets la valeur 1 ou 2 selon la méthode décrite dans le rapport
    liste_pos_1=['L2','F2','R2','B2','L4','F4','R4','B4']
    liste_pos_2=['R1','F1','L1','B1','L3','F3','R3','B3']
    
    for i in liste_pos_1:
        if d[i]==couleur1:
            somme_1+=1
        if d[i]==couleur2:
            somme_2+=1
    for i in liste_pos_2:
        if d[i]==couleur1:
            somme_1+=2
        if d[i]==couleur2:
            somme_2+=2
    
    
    if (somme_1+somme_2)%3!=0:
        # print('somme1')
        return False
   
    return True


def verifier_ordre_sommets(d):
    sommets=[['U4','F1','L2'],['U3','R1','F2'],
             ['F3','R4','D2'],['R4','D2','F3'],
             ['U2','B1','R2'],['U1','L1','B2'],
             ['L4','D4','B3'],['R3','B4','D3']]
    count_sommet_juste=8
    for i in sommets:
        if d[i[0]]=='green' and not ((d[i[1]]=='orange' and d[i[2]]=='white') or 
                                 (d[i[1]]=='yellow' and d[i[2]]=='orange') or 
                                 (d[i[1]]=='white' and d[i[2]]=='red') or
                                 (d[i[1]]=='red' and d[i[2]]=='yellow')):
           
            count_sommet_juste-=1
            
        
        if d[i[0]]=='red' and not ((d[i[1]]=='blue' and d[i[2]]=='yellow') or 
                                 (d[i[1]]=='green' and d[i[2]]=='white') or 
                                 (d[i[1]]=='yellow' and d[i[2]]=='green') or
                                 (d[i[1]]=='white' and d[i[2]]=='blue')):
            count_sommet_juste-=1
           
        
        if d[i[0]]=='yellow' and not ((d[i[1]]=='blue' and d[i[2]]=='orange') or 
                                 (d[i[1]]=='green' and d[i[2]]=='red') or 
                                 (d[i[1]]=='orange' and d[i[2]]=='green') or
                                 (d[i[1]]=='red' and d[i[2]]=='blue')):
        
            count_sommet_juste-=1
            
        if d[i[0]]=='blue' and  not((d[i[1]]=='white' and d[i[2]]=='orange') or 
                                 (d[i[1]]=='red' and d[i[2]]=='white') or 
                                 (d[i[1]]=='yellow' and d[i[2]]=='red') or
                                 (d[i[1]]=='orange' and d[i[2]]=='yellow')):
         
            count_sommet_juste-=1
            
        if d[i[0]]=='white' and not ((d[i[1]]=='green' and d[i[2]]=='orange') or 
                                 (d[i[1]]=='red' and d[i[2]]=='green') or 
                                 (d[i[1]]=='blue' and d[i[2]]=='red') or
                                 (d[i[1]]=='orange' and d[i[2]]=='blue')):
       
            count_sommet_juste-=1
            
        if d[i[0]]=='orange' and not ((d[i[1]]=='blue' and d[i[2]]=='white') or 
                                 (d[i[1]]=='green' and d[i[2]]=='yellow') or 
                                 (d[i[1]]=='white' and d[i[2]]=='green') or
                                 (d[i[1]]=='yellow' and d[i[2]]=='blue')):
       
            count_sommet_juste-=1
        
        if count_sommet_juste!=8:
            return False
    return True
    

def est_resolvable(d):
    liste_noms = ['U1','U2','U3','U4','F1','F2','F3','F4','D1','D2','D3','D4',
           'L1','L2','L3','L4','R1','R2','R3','R4','B1','B2','B3','B4']
    nb_vert=0
    nb_rouge=0
    nb_bleu=0
    nb_jaune=0
    nb_orange=0
    nb_blanc=0
    #compte les couleurs
    for i in range(24):
        if d[liste_noms[i]]=='green':
            nb_vert+=1
        if d[liste_noms[i]]=='red':
            nb_rouge+=1
        if d[liste_noms[i]]=='blue':
            nb_bleu+=1
        if d[liste_noms[i]]=='yellow':
            nb_jaune+=1
        if d[liste_noms[i]]=='orange':
            nb_orange+=1
        if d[liste_noms[i]]=='white':
            nb_blanc+=1
            
    #verifie le bon nombre de couleurs      
    if not nb_vert==nb_rouge==nb_bleu==nb_jaune==nb_orange==nb_blanc==4:
        # print('compte couleur pas bon')
        return False
    
    
    sommets=[['U4','F1','L2'],['U3','R1','F2'],
             ['F3','R4','D2'],['R4','D2','F3'],
             ['U2','B1','R2'],['U1','L1','B2'],
             ['L4','D4','B3'],['R3','B4','D3']]
    couleurs=['blue','white','red','orange','yellow','green']
    for i in sommets:
        #interdit les sommets à 2 couleurs
        if d[i[0]]==d[i[1]] or d[i[2]]==d[i[1]] or d[i[2]]==d[i[0]]:
            
            return False        
        
        for k in range (3):
            if (d[i[0]]==couleurs[k] or d[i[1]]==couleurs[k] or d[i[2]]==couleurs[k]) and (d[i[0]]==couleurs[5-k] or d[i[1]]==couleurs[5-k] or d[i[2]]==couleurs[5-k]):
                
                return False
            if not count_orientation(couleurs[k],couleurs[5-k],d):
                
                return False

    
    if not verifier_ordre_sommets(d):
        
        return False
            
    return True
        