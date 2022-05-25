# QR Code - Projet OC Informatique
Gymnase de Chamblandes - 2022

## Auteurs

Samin & Romain
## Fichiers

La liste des fichiers faisant partie du projet

 * README.md
 * LICENSE
 * MTgood.py
 * Journal de Bord_RS.ipynb
 * qr.py

## Démarrage du QR Code

Comment ça fonctionne:

- Avec tous ces fichiers, import le fichier "MTgood.py" de la manière suivante: "import MTgood"
- Ensuite on va vous demander d'entrer votre message, de 17 caractères max.
- La deuxième fois pour reéssayer il faut entrer les données suivantes:
	
	"from PIL import Image, ImageDraw" (sur une nouvelle cellule
	
	couleur = (155,155,155) 
	dimensions = (21,21)
	img = Image.new("RGB",dimensions , couleur)
	draw = ImageDraw.Draw(img)   (ces 4 lignes ensemble sur une autre cellule aussi)
    
    "MTgood.Final(img)" (sur une nouvelle cellule)

- Et on va vous redemander d'écrire votre message

