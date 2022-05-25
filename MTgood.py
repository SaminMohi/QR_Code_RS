#!/usr/bin/env python
# coding: utf-8

# In[320]:


from PIL import Image, ImageDraw


# In[321]:


#1er code pour faire le QR code, juste en ajoutant les 3 carrés:
couleur = (255,255,255) 
dimensions = (21,21)
img = Image.new("RGB",dimensions , couleur)
draw = ImageDraw.Draw(img)
#1er carré, en haute à gauche
draw.rectangle(((0,0),(6,6)), fill=(0,0,0))   #d'abord on fait un carré et on rempli en noir
draw.rectangle(((1,1),(5,5,)), fill=(255,255,255)) #ensuite on faite un carré blanc
draw.rectangle(((2,2),(4,4)), fill=(0,0,0))   #ensuite le dernier carré noir
#2ème carré en haute à droite
draw.rectangle(((20,0),(14,6)), fill=(0,0,0))
draw.rectangle(((19,1),(15,5,)), fill=(255,255,255))
draw.rectangle(((18,2),(16,4)), fill=(0,0,0))
#3ème carré en bas à gauche
draw.rectangle(((0,20),(6,14)), fill=(0,0,0))
draw.rectangle(((1,19),(5,15,)), fill=(255,255,255))
draw.rectangle(((2,18),(4,16)), fill=(0,0,0))
#img.show()


# In[322]:


def posMdl(image):
    """
    Fonction qui va dessiner les modules de positionnement
    """
    draw = ImageDraw.Draw(image)
    #premier carré en haut à gauche
    draw.rectangle(((0,0),(6,6)), fill=(0,0,0))
    draw.rectangle(((1,1),(5,5,)), fill=(255,255,255))
    draw.rectangle(((2,2),(4,4)), fill=(0,0,0))
    #deuxieme carré en haut à droite
    draw.rectangle(((20,0),(14,6)), fill=(0,0,0))
    draw.rectangle(((19,1),(15,5,)), fill=(255,255,255))
    draw.rectangle(((18,2),(16,4)), fill=(0,0,0))
    #troisieme carré en bas à gauche
    draw.rectangle(((0,20),(6,14)), fill=(0,0,0))
    draw.rectangle(((1,19),(5,15,)), fill=(255,255,255))
    draw.rectangle(((2,18),(4,16)), fill=(0,0,0))


# In[323]:


#Hseg et Vseg fait à l'étape 1
def Hseg(img,ligne, colstart = None , colend = None, color = (255,255,255)):
    """
    Fonction pour les lignes horizontales
    """
    #img, l'image qu'on veut modifier
    #ligne, la hauteur 
    #colstart, colend ; de où à où
    #quand on les spécifie pas, en mettant "None", ça veut dire ça continue jusqu'à la fin de l'image  
    larg, haut = img.size 
    if colstart == None:
        colstart = 0         #si on imagine une image de taille 10x10, ça commence à 0 (le colstart)
    if colend == None:
        colend = larg     # et ici colend = 10, alors que la dernère coordonnée c'est (9,9)
    for x in range(colstart, colend): #ça ne pose pas de problèmes car la fonction range n'inclut pas le dernier élément 
        img.putpixel((x, ligne), color)


# In[324]:


def Vseg(img,colonne, lignestart = None , ligneend = None, color = (255,255,255)):
    """
    Fonction pour les lignes verticales
    """
    larg, haut = img.size 
    if lignestart == None:
        lignestart = 0
    if ligneend == None:
        ligneend = larg
    for x in range(lignestart, ligneend):
        img.putpixel((colonne, x), color)


# In[325]:


#avec les fonctions Hseg et Vseg, on peut créer la fonction separatorMdl pour placer les modules séparateurs
def separatorMdl(img):
    """
    Fonction pour les séparateurs
    """
    #séparateur du carré en haut à gauche.
    Hseg(img,7,0,8)
    Vseg(img,7,0,8)
    #séprateur du carré en haut à droite    
    Hseg(img,7,13,21)
    Vseg(img,13,0,8) 
    #séprateur du carré en bas à gauche    
    Hseg(img,13,0,8)
    Vseg(img,7,13,21)


# In[326]:



def timingMdl(img):
    """
    Fonction pour les modules de cadencement
        - 1 segment verticale
        - 1 segment horizontale
    """
    #segment horizontale
    img.putpixel((8,6), (0,0,0))
    img.putpixel((9,6), (255,255,255))
    img.putpixel((10,6), (0,0,0))
    img.putpixel((11,6), (255,255,255))
    img.putpixel((12,6), (0,0,0))
    #segment verticale
    img.putpixel((6,8), (0,0,0))
    img.putpixel((6,9), (255,255,255))
    img.putpixel((6,10), (0,0,0))
    img.putpixel((6,11), (255,255,255))
    img.putpixel((6,12), (0,0,0))
    


# In[327]:


#Code pour faire le QR code avec le fond gris:
couleur = (128,128,128)
dimensions = (21,21)
img = Image.new("RGB",dimensions , couleur)
draw = ImageDraw.Draw(img)
#premier carré en haut à gauche
draw.rectangle(((0,0),(6,6)), fill=(0,0,0))
draw.rectangle(((1,1),(5,5,)), fill=(255,255,255))
draw.rectangle(((2,2),(4,4)), fill=(0,0,0))
#deuxieme carré en haut à droite
draw.rectangle(((20,0),(14,6)), fill=(0,0,0))
draw.rectangle(((19,1),(15,5,)), fill=(255,255,255))
draw.rectangle(((18,2),(16,4)), fill=(0,0,0))
#troisieme carré en bas à gauche
draw.rectangle(((0,20),(6,14)), fill=(0,0,0))
draw.rectangle(((1,19),(5,15,)), fill=(255,255,255))
draw.rectangle(((2,18),(4,16)), fill=(0,0,0))

separatorMdl(img)
timingMdl(img)
img.putpixel((8,13),(0,0,0))
#img.show()


# In[328]:


#exercice de l'étape 3
def formatMdl(img):
    """
    Fonction qui va mettre les modules de format sur notre image 
        - Il y aura 1 ligne verticale
        - Et 1 ligne horizontale
    """    
    #partie verticale
    img.putpixel((8,0), (0,0,0))
    img.putpixel((8,1), (255,255,255))
    img.putpixel((8,2), (0,0,0))
    img.putpixel((8,3), (0,0,0))
    img.putpixel((8,4), (0,0,0))
    img.putpixel((8,5), (255,255,255))
    img.putpixel((8,7), (255,255,255))
    img.putpixel((8,8), (0,0,0))
    img.putpixel((8,13),(0,0,0))
    img.putpixel((8,14), (255,255,255))
    img.putpixel((8,15), (255,255,255))
    img.putpixel((8,16), (255,255,255))
    img.putpixel((8,17), (0,0,0))
    img.putpixel((8,18), (0,0,0))
    img.putpixel((8,19), (0,0,0))
    img.putpixel((8,20), (0,0,0)) 
    
    #partie horizontale
    img.putpixel((20,8), (0,0,0))
    img.putpixel((19,8), (255,255,255))
    img.putpixel((18,8), (0,0,0))
    img.putpixel((17,8), (0,0,0))
    img.putpixel((16,8), (0,0,0))
    img.putpixel((15,8), (255,255,255))
    img.putpixel((14,8), (255,255,255))
    img.putpixel((13,8), (0,0,0))
    img.putpixel((8,8), (0,0,0))
    img.putpixel((7,8), (255,255,255))
    img.putpixel((5,8), (255,255,255))
    img.putpixel((4,8), (255,255,255))
    img.putpixel((3,8), (0,0,0))
    img.putpixel((2,8), (0,0,0))
    img.putpixel((1,8), (0,0,0))
    img.putpixel((0,8), (0,0,0))


# In[329]:


#Code pour faire le QR code avec le module de format:
couleur = (128,128,128)
dimensions = (21,21)
img = Image.new("RGB",dimensions , couleur)
draw = ImageDraw.Draw(img)
#premier carré en haut à gauche
draw.rectangle(((0,0),(6,6)), fill=(0,0,0))
draw.rectangle(((1,1),(5,5,)), fill=(255,255,255))
draw.rectangle(((2,2),(4,4)), fill=(0,0,0))
#deuxieme carré en haut à droite
draw.rectangle(((20,0),(14,6)), fill=(0,0,0))
draw.rectangle(((19,1),(15,5,)), fill=(255,255,255))
draw.rectangle(((18,2),(16,4)), fill=(0,0,0))
#troisieme carré en bas à gauche
draw.rectangle(((0,20),(6,14)), fill=(0,0,0))
draw.rectangle(((1,19),(5,15,)), fill=(255,255,255))
draw.rectangle(((2,18),(4,16)), fill=(0,0,0))

separatorMdl(img)
timingMdl(img)
formatMdl(img)
#img.show()


# In[330]:


#Raccourci pour ne pas reécrire à chaque fois
def QRCode(img):
    """
    Fonction pour crée notre QR code avec les 3 carrés
    """
    couleur = (255,255,255)
    dimensions = (21,21)
    img = Image.new("RGB",dimensions , couleur)
    draw = ImageDraw.Draw(img)
    #1er carré, en haute à gauche
    draw.rectangle(((0,0),(6,6)), fill=(0,0,0))   #d'abord on fait un carré et on rempli en noir
    draw.rectangle(((1,1),(5,5,)), fill=(255,255,255)) #ensuite on faite un carré blanc
    draw.rectangle(((2,2),(4,4)), fill=(0,0,0))   #ensuite le dernier carré noir
    #2ème carré en haute à droite
    draw.rectangle(((20,0),(14,6)), fill=(0,0,0))
    draw.rectangle(((19,1),(15,5,)), fill=(255,255,255))
    draw.rectangle(((18,2),(16,4)), fill=(0,0,0))
    #3ème carré en bas à gauche
    draw.rectangle(((0,20),(6,14)), fill=(0,0,0))
    draw.rectangle(((1,19),(5,15,)), fill=(255,255,255))
    draw.rectangle(((2,18),(4,16)), fill=(0,0,0))


# In[ ]:





# In[331]:


#Finale(img) #juste pour voir ce que ça donne en ayant raccourci 


# # Tout ce qui y a avant c'est jusqu'au placement de module à l'étape 3

# ## Maintenant on va créer le code finale pour que le qr code ait notre message

# In[332]:


#Fonction donné par le prof à l'étape 3
def masque(x,y,bit):
    if (x+y) %3 == 0:
        if bit == '0':
            return '1'
        else:
            return '0'
    else:
        return bit


# In[333]:


import qr


# In[334]:


#Exemple de tranches d'éléments
#a = "000010100111"        
#a.split()
#for i in range(2):  #au total il y aura 2 fois montée-descente
#    print("Colonne qui monte n°{0}".format(i+1))#indicateur de colonne 
#    for j in a[0+6*i:3+6*i]:
#        print(j)
#    print("Colonne qui descent n°{0}".format(i+1))#indicateur de colonne 
#    for j in a[3+6*i:6+6*i]:
#        print(j)


# In[335]:


def montee(img,x,y,tranche):
    """
    La fonction pour les colonnes montantes 
    """
    for i in tranche:
        i = masque(x,y,i)#fonction donner par le prof à l'étape 3
        if x>=7:  #à partir de la colonne 7, c'est "normal": puisqu'on commence tout en bas à droite (20,20)
            a = 0 
        else:     #mais après avoir atteint la colonne 7 (depuis la droite), la parité va changer
            a = 1  # -> c'est pour ça on met a = 1, pour décaler
        if (x+a)%2 == 0:  #SI c'est pair
            if i == "0": #et si le bit est 0
                z = (255,255,255)   #la couleur est blanc
                img.putpixel((x,y),z)  #et on met un pixel blanc
            elif i == "1":  #sinon si le bit est 1
                z = (0,0,0)  #la couleur est noir
                img.putpixel((x,y),z) 
            x = x - 1    #et aussi, si c'est pair, en décale d'une colonne à gauche
        
        elif (x+a)%2 != 0:    #Ensuite si c'est impair
            if i == "0":    #la couleur, et le chiffre reste pareil, la fonction masque a aussi été pris en compte au début 
                z = (255,255,255)
                img.putpixel((x,y),z)
            elif i == "1":
                z = (0,0,0)
                img.putpixel((x,y),z)
            x = x + 1   #si c'est impair, on écale d'une colonne à droite
            y = y - 1   #et on monte d'une ligne


# In[336]:


def descente(img,x,y,tranche): 
    """ 
    La fonction pour les colonnes descendantes 
    """
    for i in tranche:
        i = masque(x,y,i)#fonction donner par le prof à l'étape 3
        if x >=7:   #même chose qu'avant
            a=0
        else:
            a=1
        if (x+a)%2 == 0:  #SI c'est pair
            if i == "0": #et si le bit est 0
                z = (255,255,255)   #la couleur est blanc
                img.putpixel((x,y),z)  #et on met un pixel blanc
            elif i == "1":  #sinon si le bit est 1
                z = (0,0,0)  #la couleur est noir
                img.putpixel((x,y),z) 
            x = x -1    #et aussi, si c'est pair, en décale d'une colonne à gauche
        
        elif (x+a)%2 != 0:    #Ensuite si c'est impair
            if i == "0":    #la couleur, et le chiffre reste pareil, la fonction masque a aussi été pris en compte au début 
                z = (255,255,255)
                img.putpixel((x,y),z)
            elif i == "1":
                z = (0,0,0)
                img.putpixel((x,y),z)
            x = x + 1   #si c'est impair, on décale d'une colonne à droite
            y = y + 1   #et on descend d'une ligne
   


# In[364]:


def code(img,message): 
    """
    La fonction finale qui va placer les bits du message codé dans le QR code
        - Elle va codé notre message en bit, chaîne de caractère composé de 0 et 1
        - Elle va mettre les bits uniquement dans les zones grises 
        - Elle va le faire en plusieurs tranches 
        - 208 bits au total
        
    """
    QRCode(img)
    separatorMdl(img)
    timingMdl(img)
    formatMdl(img)
    
    message = input("Entrez-votre message (max 17 caractères) :  ")
    msg = qr.message2bits(message) #le code qui va crypté notre message en bit, donné par le prof aussi
    msg.split()#sépare tous les bits: important pour faire les tranches de bits

    
    tranche_bit = msg[0:24]    #1ers 24 bits, du premier point (20,20), on va remplir les 2 premières colonnes
    montee(img,20,20, tranche_bit)  #donc ça commence à (20,20) et s'arrête à (19,9)
    
    tranche_bit = msg[24:48]   #les 24 prochains bits seront pout les colonnes descendantes
    descente(img,18,9, tranche_bit) #de la coordonnée (18,9) à (17,20)
    
    tranche_bit = msg[48:72]   #à nouveau montante
    montee(img,16,20, tranche_bit) #de (16,20) à (15,9)
    
    tranche_bit = msg[72:96] 
    descente(img,14,9, tranche_bit) #de (14,9) à 13(20)
    #On a fini la 1ère "tranche", un rectangle de taille 8x12 : 
    # colonnes 13-20 et lignes 9-20
    
    
    #Prochaine tranche
    tranche_bit = msg[96:124]#on continue avec les bits de 96 à 124, cette fois 28 bits, colonnes montantes
    montee(img,12,20, tranche_bit) #de (12,20) à (11,7)
    
    #ici il y aura une séparation: le segment verticale fait avec la fonction timingMdl
    tranche_bit = msg[124:136] #on continue donc avec une colonne montante mais de 12 bits
    montee(img,12,5, tranche_bit) #de (12,5) à (11,0)
    
    tranche_bit = msg[136:148] #ensuite on passe à la colonne descendante, depuis le haut, avec 12 bits
    descente(img,10,0, tranche_bit) #de (10,0) à (9,5)
    
    tranche_bit = msg[148:176] #et on retombe sur la longue colonne (descendante) de 28 bits
    descente(img,10,7, tranche_bit) #de (10,7) à (9,20)
    #on a ainsi fini la 2ème tranche (composé de 2 rectangles) de taille 4x21
    
    
    #dernière tranche
    tranche_bit = msg[176:184] #cette fois seulement 8 bits, colonne montante
    montee(img,8,12, tranche_bit) #de (8,12) à (7,9)
    
    #une autre séparation: cette fois un segment verticale
    tranche_bit = msg[184:192] #8 bits, colonne descendante
    descente(img,5,9, tranche_bit) #de (5,9) à (4,12)
    
    tranche_bit = msg[192:200] #dernière colonne montante, 8 bits
    montee(img,3,12, tranche_bit) #de (3,12) à (2,9)
    
    tranche_bit = msg[200:208] #dernière colonne descendante, 8 bits
    descente(img,1,9, tranche_bit) #de (1,9) à (0,12)        


# In[365]:


def Final(img):
    posMdl(img)
    timingMdl(img)
    separatorMdl(img)
    formatMdl(img)
    code(img, "")
    img.show()


# In[366]:


Final(img)


# In[ ]:




