#---------------------------------------------------------------------------------------------------------
# Copyright (c) Momowawa. All rights reserved.
# Licensed under the GNU General Public License. See LICENSE in the project root for license information.
#---------------------------------------------------------------------------------------------------------

from config_vars import home_dir, config_dir, rules_file, conf_file, readme_file

import subprocess
import os
import tkinter as tk
from tkinter import Menu

# Fonction associée à l'option "Initialiser" dans le menu "Fichier"
def init_file():
    # Insérez ici le code pour initialiser l'application
    pass

# Fonction associée à l'option "Nouveau" dans le menu "Fichier"
def new_file():
    # Insérez ici le code pour créer un nouveau fichier
    pass

# Fonction associée à l'option "Ouvrir" dans le menu "Fichier"
def open_file():
    # Insérez ici le code pour ouvrir un fichier existant
    pass

# Fonction associée à l'option "Enregistrer" dans le menu "Fichier"
def save_file():
    # Insérez ici le code pour enregistrer le fichier actuel
    pass

# Fonction associée à l'option "Copier" dans le menu "Édition"
def copy():
    # Insérez ici le code pour copier du texte ou des données
    pass

# Fonction associée à l'option "Coller" dans le menu "Édition"
def paste():
    # Insérez ici le code pour coller du texte ou des données
    pass

# Fonction associée à l'option "A propos" dans le menu "Aide"
def about():

    if os.path.exists(readme_file):
        try:
            subprocess.run(["xdg-open", readme_file], check=True)
        except FileNotFoundError:
            # xdg-open n'est pas disponible, affichez le contenu du fichier dans un terminal
            try:
                subprocess.run(["cat", readme_file], check=True)
            except FileNotFoundError:
                # "cat" n'est pas disponible, vous pouvez personnaliser le comportement ici
                print("Impossible d'afficher le contenu du fichier README.")
    else:
        # Gérez le cas où le fichier readme_file n'existe pas
        print("Le fichier readme_file n'existe pas.")
    pass

# Création de la fenêtre principale
root = tk.Tk()
root.title("Mon Application")

# Création d'une barre de menus
menu_bar = Menu(root)

# Menu "Fichier"
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Initialiser", command=init_file)
file_menu.add_command(label="Nouveau", command=new_file)
file_menu.add_command(label="Ouvrir", command=open_file)
file_menu.add_command(label="Enregistrer", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Menu "Édition"
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Copier", command=copy)
edit_menu.add_command(label="Coller", command=paste)
menu_bar.add_cascade(label="Édition", menu=edit_menu)

# Menu "Aide"
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="A propos", command=about)
menu_bar.add_cascade(label="Aide", menu=help_menu)

# Configuration de la barre de menus comme le menu principal
root.config(menu=menu_bar)

# Démarrage de la boucle principale de l'interface graphique
root.mainloop()
