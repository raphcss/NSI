'''
Code créer par Raphaël LEROU--LEMOINE, terminé le 15/02/2023.

Ce code permet tout d'abord d'afficher une première fenêtre dite "launcher" qui aura pour but de nous laisser le choix entre deux possibilitées, créer ou charger un partie de puissance 4,
le reste du code permet tout simplement le bon déroulement de la partie
'''

# Import des modules nécessaires pour le programme
import csv
import datetime as time
import json
import os
import sys
import asyncio
import tkinter as tk
from tkinter import filedialog, messagebox


# Définition de la classe StartPage qui hérite de tk.Tk
class StartPage(tk.Tk):
    # Initialisation de la classe
    def __init__(self, *args, **kwargs):
        # Appel du constructeur de la classe parente tk.Tk
        tk.Tk.__init__(self, *args, **kwargs)

        config = { 
                "start_from_old_path": "null",
                "start_from_old_check" : "False"
        }
        with open("config/config.json", "w") as f:
            json.dump(config, f, indent=4)

        with open("config/count.json", 'r') as f:
            data = json.loads(f.read().replace("\n", ""))
            count = data["game_count"]
            # Définition du titre de la fenêtre
            self.title(f"Launcher - Puissance 4 - Parties totales: {count}")
        # Définition des dimensions de la fenêtre
        self.geometry("500x400")
        # Désactive la possibilité de redimensionner la fenêtre
        self.resizable(width=False, height=False)

        # Création d'un cadre pour contenir le cadre
        self.frame_of_frame = tk.Frame(self, bg="#4285F4")
        self.frame_of_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

        # Création d'un cadre pour contenir les widgets
        self.frame = tk.Frame(self, bg="#80c1ff")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=490, height=390)

        # Création d'une étiquette avec un titre pour l'application
        self.title_label = tk.Label(self.frame, text="Puissance 4", font=("Helvetica", 30), bg="#80c1ff", fg="white")
        self.title_label.pack(pady=10)

        # Création d'un titre afin d'accompagner le bouton
        self.new_label = tk.Label(self.frame, text="Créer une nouvelle partie", font=("Helvetica", 18), bg="#80c1ff", fg="white")
        self.new_label.pack(pady=10)

        # Création du bouton "Charger"
        self.start_button = tk.Button(self.frame, text="Créer", font=("Helvetica", 16), bg="#00bfff", fg="white", command=self.start_new)
        self.start_button.pack(pady=10)

        # Création d'un titre afin d'accompagner le bouton
        # Initialiser un compteur
        count = 0

        # Boucler sur les fichiers du répertoire
        for file in os.listdir("saves"):
            # Vérifier si le fichier se termine par l'extension .csv
            if file.endswith(".csv"):
                # Incrémenter le compteur
                count += 1
        self.charger_label = tk.Label(self.frame, text=f"Charger une partie (Dispo: {count})", font=("Helvetica", 18), bg="#80c1ff", fg="white")
        self.charger_label.pack(pady=10)

        # Création du bouton "Charger"
        self.start_button = tk.Button(self.frame, text="Charger", font=("Helvetica", 16), bg="#00bfff", fg="white", command=self.start_old)
        self.start_button.pack(pady=10)

        # Création d'un titre afin de mentionner le créateur
        self.charger_label = tk.Label(self.frame, text="Made by Raphaël L.", font=("Helvetica", 10), bg="#80c1ff", fg="#6290bf")
        self.charger_label.pack(pady=10)

        self.menu_bar = tk.Menu(self.master)
        self.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Outils", menu=self.file_menu)
        self.file_menu.add_command(label="Visionneur", command=self.visio)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Comming soon..", command=self.force_pass)
        def force_quit():
            quit = tk.messagebox.askquestion("Puissance 4", 'Es-tu sur de vouloir quitter le launcher ?',icon = "info")
            if quit == 'yes':
                sys.exit()
            return
        # Faire en sorte de demander aux joueurs si il souhaites sauvgarder avant de quitter
        self.wm_protocol ("WM_DELETE_WINDOW", force_quit)
    #Définition de la fonction force_pass qui ne fait rien
    def force_pass(self):
        pass
    #Définition de la fonction visio qui permet d'ouvrir un fichier texte, de l'afficher dans une zone de texte
    #et de proposer un menu pour fermer l'application
    def visio(self):
        # Définition de la fonction open_file pour ouvrir un fichier et l'afficher dans la zone de texte
        def open_file():
            # Ouverture de la boîte de dialogue pour choisir un fichier
            file_path = filedialog.askopenfilename(initialdir="logs/", filetypes=[("Fichiers texte", "*.txt")])
            if file_path:
                # Si un fichier a été choisi, ouverture du fichier et affichage dans la zone de texte
                with open(file_path, "r") as file:
                    content = file.read()
                    text.config(state='normal')
                    text.delete(1.0, tk.END)
                    text.insert(tk.END, content)
                    text.config(state='disabled')
        # Définition de la fonction quit_app pour fermer l'application
        def quit_app():
            visionneur.quit()

        # Création de la fenêtre principale de l'application
        visionneur = tk.Tk()
        visionneur.title("Puissance 4 - Visionneur de logs")

        # Création de la zone de texte pour afficher le contenu des fichiers
        text = tk.Text(visionneur, wrap="word")
        text.pack(fill="both", expand=True)
        text.insert(1.0, "Aucun fichier LOG ouvert")
        text.config(state='disabled')

        # Création du menu pour ouvrir un fichier et fermer l'application
        menu_bar = tk.Menu(visionneur)
        visionneur.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Ouvrir", command=open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=quit_app)

        # Lancement de la boucle principale de l'application
        visionneur.mainloop()
    #Définition de la fonction counter pour compter le nombre de parties jouées
    def counter(self):
        count = 0
        with open("config/count.json", 'r') as f:
            data = json.loads(f.read().replace("\n", ""))
            count = data["game_count"] + 1
        with open("config/count.json", 'w') as f:
            data = { 
                "game_count": count
            }
            json.dump(data, f, indent=4)
    # Méthode déclenchée lorsque le bouton "Créer" est cliqué
    def start_new(self):
        self.counter()
        self.destroy()


    # Méthode déclenchée lorsque le bouton "Charger" est cliqué
    def start_old(self):
        # Ouverture d'une boîte de dialogue "Ouvrir" pour sélectionner un fichier CSV
        file_path = filedialog.askopenfilename(initialdir="saves/", defaultextension=".csv", filetypes=[("Fichier CSV (P4 Logs)", "*.csv")])
        # Destruction de la fenêtre actuelle
        # Vérifier si un fichier a été sélectionné
        if file_path:
            # Traitement du fichier CSV sélectionné ici
            data = { 
                "start_from_old_path": file_path,
                "start_from_old_check" : 'True'
            }
            with open("config/config.json", "w") as f:
                json.dump(data, f, indent=4)
                self.counter()
            

        else:
            return
        self.destroy()
# Création de l'objet StartPage
app = StartPage()
# Boucle principale de l'application
app.mainloop()

# Classe pour créer une fenêtre d'application pour un jeu de puissance 4
class Power4(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initialiser la classe parente Tk
        tk.Tk.__init__(self, *args, **kwargs)

        if os.path.exists("logs/latest.txt"):
            self.log("\n[ERROR] The last party didn't save properly. Force save allowed\n")
            self.save_logs()

        # Définir le titre de la fenêtre
        self.title("Puissance 4")

        # Définir la taille de la fenêtre
        self.geometry("525x450")

        # Désactiver la redimensionnabilité de la fenêtre
        self.resizable(width=False, height=False)

        # Créer un canvas pour dessiner les éléments du jeu
        self.canvas = tk.Canvas(self, bg="#80c1ff", height=450, width=650)
        self.canvas.pack()

        # Définir le nombre de colonnes et de lignes pour le jeu
        self.columns = 7
        self.rows = 6

        # Créer la grille pour le jeu
        self.create_grid()

        # Définir les couleurs pour les joueurs
        self.player_colors = ["firebrick1", "goldenrod1"]
        self.preview_colors = ["coral2", "LightGoldenrod1"]
        self.border_colors = ["brown3", "gold"]
        self.team_colors = ["rouge", "jaune"]
        # Définir le joueur actuel (0 pour le premier joueur, 1 pour le second joueur)
        self.player = 0
        # Stocker le gagnant (None par défaut)
        self.winner = None
        # Stocker le nombres de cases utilisées
        self.check_used_places = 0
        # Définir la valeur afin de savoir si une partie a été importer
        self.imported = False
        # Définir le chemin d'accès vers le fichier dit save soit un fichier csv
        self.imported_path = "null"

        # Stocker les valeurs de chaque case dans un tableau
        self.squares = []
        self.grid = []
        self.start_game_from_old_check()

        # Initialiser le tableau avec des zéros
        if len(self.squares) == 0:
            self.log("[INFO] Save method initiated")
            for i in range(self.columns):
                self.squares.append([0] * self.rows)

        # Lier l'événement de clic de souris à la méthode "click"
        self.canvas.bind("<Button-1>", self.click)
        # Lier l'événement de mouvement de souris à la méthode "preview"
        self.canvas.bind("<Motion>", self.preview)
        # Lier l'événement de sortie de souris a la méthode "remove_preview"
        self.canvas.bind("<Leave>", self.remove_preview)

        def force_quit():
            quit = tk.messagebox.askquestion("Puissance 4", 'Es-tu sur de vouloir quitter cette partie ?',icon = "info")
            if quit == 'yes':
                self.save_party()
                self.log("[INFO] The current party was closed during the game. Saving logs and data..")
                self.save_logs()
                sys.exit()
            return
        # Faire en sorte de demander aux joueurs si il souhaites sauvgarder avant de quitter
        self.wm_protocol ("WM_DELETE_WINDOW", force_quit)
    #Fonction permettant d'écrire les fichier dit "logs"
    def log(self, line):
        with open('logs/latest.txt', 'a') as file:
            file.write(f"\n{str(line)}")

    #Fonction permettant de sauvegarder les fichier dit "logs"
    def save_logs(self):
        with open('logs/latest.txt', 'a') as file:
            file.write("\n[INFO] Game saved and closed correctly")
        date = time.date.today()
        hour = time.datetime.now()
        hour = hour.strftime("%Hh%Mm%Ss")
        os.rename("logs/latest.txt", f"logs/{date}_{hour}.txt")

    # Fonction permettant de savoir si une partie a été importée et non créer
    def start_game_from_old_check(self):
        with open("config/config.json", 'r') as file:
            data = json.loads(file.read().replace("\n", ""))
            if data["start_from_old_check"] == "True":
                self.imported = True
                self.imported_path = data["start_from_old_path"]
                self.log(f"[INFO] Game started from an old game save. ({self.imported_path})\n")
                self.open_party()
            else:
                self.log(f"[INFO] New game started\n")

    # Méthode pour créer la grille du jeu
    def create_grid(self):
        self.log("[INFO] Creating grid...")
        for i in range(self.columns):
            for j in range(self.rows):
                x1 = i * 75
                y1 = j * 75
                x2 = x1 + 75
                y2 = y1 + 75
                # Dessiner les rectangles pour chaque case de la grille
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#4285F4", fill="#80c1ff")

    def draw_pieces(self):
        # Affiche un message de journalisation pour indiquer que les pions de la partie sauvegardée sont dessinés
        self.log("[INFO] Drawing the pawns of the imported saved game")
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == 1:
                    # Affiche un message de journalisation pour indiquer le placement d'un pion rouge
                    self.log(f"[PUISSANCE 4] Red pawn placed at {i+1}x{j+1} by the import method")
                    # Incrémente le nombre de places utilisées
                    self.check_used_places = self.check_used_places + 1
                    # Définit les couleurs du pion rouge
                    color = "firebrick1"
                    border_color = "brown3"
                    # Calcule les coordonnées du cercle représentant le pion rouge
                    x1 = j * 75 
                    y1 = i * 75 
                    x2 = x1 + 75
                    y2 = y1 + 75
                    # Dessine le cercle représentant le pion rouge
                    self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=border_color)
                if self.grid[i][j] == 2:
                    # Affiche un message de journalisation pour indiquer le placement d'un pion jaune
                    self.log(f"[PUISSANCE 4] Yellow pawn placed at {i+1}x{j+1} by the import method")
                    # Incrémente le nombre de places utilisées
                    self.check_used_places = self.check_used_places + 1
                    # Définit les couleurs du pion jaune
                    color = "goldenrod1"
                    border_color = "gold"
                    # Calcule les coordonnées du cercle représentant le pion jaune
                    x1 = j * 75 
                    y1 = i * 75 
                    x2 = x1 + 75
                    y2 = y1 + 75
                    # Dessine le cercle représentant le pion jaune
                    self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=border_color)
    # Fonction permettant de lancer une partie depuis un fichier csv dit save
    def open_party(self):
            # Ouverture du fichier .csv contenant la grille sauvegardée précédemment
            with open(self.imported_path, newline='') as file:
                reader = csv.reader(file)
                grid = list(reader)

                # Conversion de la grille en liste d'entiers
                grid = [[int(grid[j][i]) for j in range(len(grid))] for i in range(len(grid[0]))]

                # Enregistrement de la grille
                self.squares = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
                self.grid = grid
            
            # Dessin des pions sur le canvas
            self.draw_pieces()

            # Détermination du joueur courant
            self.player = (self.check_used_places) % 2

            # Configuration par défaut
            config = { 
                    "start_from_old_path": "null",
                    "start_from_old_check" : "False"
                }

            # Sauvegarde de la configuration par défaut dans le fichier config.json
            with open("config/config.json", "w") as f:
                json.dump(config, f, indent=4)

            if self.check_used_places == 42:
                self.winner = "draw"
                self.show_winner()

            # vérifier s'il y a un gagnant en utilisant la fonction check_winner()
            self.winner = self.check_winner()

            # si un gagnant a été trouvé, afficher le message de gagnant et désactiver les clics sur le canvas
            if self.winner is not None:
                # Retirer les liasons
                self.canvas.unbind("<Button-1>")

                self.title(f"Puissance 4 - Bravo au joueur {self.team_colors[self.player]} pour sa victoire !")
                self.log(f"[PUISSANCE 4] Player {self.team_colors[self.player]} winned the game")
                self.show_winner()

    # Fonction pour afficher un aperçu de l'emplacement où le joueur pose son pion
    def preview(self, event):
        # Supprimer tout cercle précédemment dessiné
        self.canvas.delete("preview")

        # déterminer la colonne en utilisant la position x de l'événement de mouvement de souris
        column = event.x // 75
        # initialiser la ligne à 5
        row = 5

        # boucle pour trouver la première case vide dans la colonne
        while row >= 0:
            # si la case est vide, quitter la boucle
            if self.squares[column][row] == 0:
                break
            # décrémenter la ligne pour vérifier la case suivante
            row -= 1

        # si aucune case vide n'a été trouvée, retourner sans faire quoi que ce soit
        if row < 0:
            return

        # calculer les coordonnées du cercle à dessiner sur le canvas
        x1 = column * 75
        y1 = row * 75
        x2 = x1 + 75
        y2 = y1 + 75

        self.title(f"Puissance 4 - C'est au tour du joueur {self.team_colors[self.player]} - {row+1}x{column+1}")

        # dessiner un cercle temporaire sur le canvas en utilisant les coordonnées et la couleur correspondant au joueur courant
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.preview_colors[self.player], fill=self.preview_colors[self.player], tags="preview")
    # Fonction permetant de supprimé la preview des pions sur le plateau
    def remove_preview(self, event):
        self.canvas.delete("preview")

    # fonction qui gère les clics de la souris sur le canvas
    def click(self, event):
        # déterminer la colonne en utilisant la position x de l'événement de clic
        column = event.x // 75
        # initialiser la ligne à 5
        row = 5

        # boucle pour trouver la première case vide dans la colonne
        while row >= 0:
            # si la case est vide, quitter la boucle
            if self.squares[column][row] == 0:
                break
            # décrémenter la ligne pour vérifier la case suivante
            row -= 1

        # si aucune case vide n'a été trouvée, retourner sans faire quoi que ce soit
        if row < 0:
            return

        # définir la valeur de la case trouvée à 1 pour le joueur 1 ou 2 pour le joueur 2
        self.squares[column][row] = self.player + 1

        # calculer les coordonnées du cercle à dessiner sur le canvas
        x1 = column * 75
        y1 = row * 75
        x2 = x1 + 75
        y2 = y1 + 75

        # dessiner un cercle sur le canvas en utilisant les coordonnées et la couleur correspondant au joueur courant
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.border_colors[self.player], fill=self.player_colors[self.player], tags="pawns")
        self.log(f"[PUISSANCE 4] Pawn placed at {row+1}x{column+1} by {self.team_colors[self.player]}")

        
        # Ajouter 1 a la valuer pour check si toutes les cases sont utilisées
        self.check_used_places = self.check_used_places + 1
        if self.check_used_places == 42:
            self.winner = "draw"
            self.show_winner()

        # vérifier s'il y a un gagnant en utilisant la fonction check_winner()
        self.winner = self.check_winner()

        # si un gagnant a été trouvé, afficher le message de gagnant et désactiver les clics sur le canvas
        if self.winner is not None:
            # Retirer les liasons
            self.canvas.unbind("<Button-1>")

            self.title(f"Puissance 4 - Bravo au joueur {self.team_colors[self.player]} pour sa victoire !")
            self.log(f"[PUISSANCE 4] Player {self.team_colors[self.player]} winned the game")
            self.show_winner()
        # sinon, passer au joueur suivant en utilisant un modulo 2
        else:
            self.player = (self.player + 1) % 2
            self.title(f"Puissance 4 - C'est au tour du joueur {self.team_colors[self.player]}")


    # fonction qui vérifie s'il y a un gagnant dans le jeu
    def check_winner(self):
        # Boucle pour vérifier s'il y a une combinaison gagnante de 4 pions alignés horizontalement
        for i in range(self.columns - 3):
            for j in range(self.rows):
                if self.squares[i][j] != 0 and self.squares[i][j] == self.squares[i + 1][j] == self.squares[i + 2][j] == self.squares[i + 3][j]:
                    return self.squares[i][j]

        # Boucle pour vérifier s'il y a une combinaison gagnante de 4 pions alignés verticalement
        for i in range(self.columns):
            for j in range(self.rows - 3):
                if self.squares[i][j] != 0 and self.squares[i][j] == self.squares[i][j + 1] == self.squares[i][j + 2] == self.squares[i][j + 3]:
                    return self.squares[i][j]

        # Boucle pour vérifier s'il y a une combinaison gagnante de 4 pions alignés en diagonale (en haut à gauche vers le bas à droite)
        for i in range(self.columns - 3):
            for j in range(3, self.rows):
                if self.squares[i][j] != 0 and self.squares[i][j] == self.squares[i + 1][j - 1] == self.squares[i + 2][j - 2] == self.squares[i + 3][j - 3]:
                    return self.squares[i][j]

        # Boucle pour vérifier s'il y a une combinaison gagnante de 4 pions alignés en diagonale (en bas à gauche vers le haut à droite)
        for i in range(self.columns - 3):
            for j in range(self.rows - 3):
                if self.squares[i][j] != 0 and self.squares[i][j] == self.squares[i + 1][j + 1] == self.squares[i + 2][j + 2] == self.squares[i + 3][j + 3]:
                    return self.squares[i][j]

        return None

    def restart_game(self):
        # Réinitialiser les valeurs par défaut
        self.player = 0
        self.winner = None
        self.check_used_places = 0
        self.squares = []
        self.grid = []

        # Initialiser le tableau avec des zéros
        self.log("[INFO] Save method initiated")
        for i in range(self.columns):
            self.squares.append([0] * self.rows)

        # Effacer les cercles sur le canvas
        self.canvas.delete("all")
        # Recréer le tableau
        self.create_grid()
        # Ré-activer les clics sur le canvas
        # Lier l'événement de clic de souris à la méthode "click"
        self.canvas.bind("<Button-1>", self.click)

        config = { 
                "start_from_old_path": "null",
                "start_from_old_check" : "False"
        }
        with open("config/config.json", "w") as f:
            json.dump(config, f, indent=4)


    def save_party(self):
        date = time.date.today()
        hour = time.datetime.now()
        hour = hour.strftime("%Hh%Mm%Ss")
        with open(f"saves/{date}_{hour}.csv",'w', encoding='UTF8', newline='' ) as f:
            writter = csv.writer(f)
            for i in self.squares:
                writter.writerow(i)
                #writter.writerow([self.player,self.winner])

    #Définition d'une méthode pour afficher le gagnant
    def show_winner(self):
        if self.winner == "draw":
            # Si la partie est nulle, afficher un message et demander à l'utilisateur s'il veut quitter ou rejouer
            message_draw = "C'est une égalité ! Personne n'a gagné."
            finie_draw = tk.messagebox.askquestion(message_draw,'La partie est finie, souhaite-tu quitter le jeu ?',icon = 'info')
            if finie_draw == 'yes':
                # Si l'utilisateur veut quitter, demander s'il veut sauvegarder la partie et quitter
                savemessage_draw = "C'est une égalité ! Personne n'a gagné."
                save_draw = tk.messagebox.askquestion(savemessage_draw, 'Souhaites-tu sauvegarder ta partie ?',icon = "info")
                if save_draw == 'yes':
                    # Si l'utilisateur veut sauvegarder la partie et quitter, enregistrer les informations de la partie et quitter
                    self.save_party()
                    self.save_logs()
                    sys.exit()
                # Quitter le jeu
                self.save_logs()
                sys.exit()
            else:
                # Si l'utilisateur veut rejouer, demander s'il veut sauvegarder la partie et rejouer, sinon quitter
                save_draw = tk.messagebox.askquestion('Puissance 4','Souhaites-tu sauvegarder ta partie ?',icon = 'info')
                if save_draw == 'yes':
                    # Si l'utilisateur veut sauvegarder la partie et rejouer, enregistrer les informations de la partie et redémarrer la partie
                    self.save_party()
                    self.save_logs()
                    replay_draw = tk.messagebox.askquestion('Puissance 4','Souhaites-tu rejouer ?',icon = 'info')
                    if replay_draw == "yes":
                        self.restart_game()
                    else: 
                        # Si l'utilisateur ne veut pas rejouer, enregistrer les informations de la partie et quitter
                        self.save_logs()
                        sys.exit()
                else:
                    # Si l'utilisateur ne veut pas sauvegarder la partie, demander s'il veut rejouer, sinon quitter
                    self.save_logs()
                    replay_draw = tk.messagebox.askquestion('Puissance 4','Souhaites-tu rejouer ?',icon = 'info')
                    if replay_draw == "yes":
                        self.restart_game()
                    else: 
                        # Si l'utilisateur ne veut pas rejouer, quitter
                        sys.exit()
        
        # Si un joueur a gagné, afficher un message avec la couleur du joueur gagnant et demander à l'utilisateur s'il veut quitter ou rejouer
        message = f"Le joueur {self.team_colors[self.winner-1]} a gagné !"
        finie = tk.messagebox.askquestion(message,'La partie est finie, souhaites-tu quitter le jeu ?',icon = 'info')
        if finie == 'yes':
            savemessage_draw = f"Le joueur {self.team_colors[self.winner-1]} a gagné !"
            save_draw = tk.messagebox.askquestion(savemessage_draw, 'Souhaites-tu sauvegarder ta partie ?',icon = "info")
            if save_draw == 'yes':
                # Si l'utilisateur veut sauvegarder la partie et quitter, enregistrer les informations de la partie et quitter
                self.save_party()
                self.save_logs()
                sys.exit()
            # Quitter le jeu
            self.save_logs()
            sys.exit()
        else:
            save_draw = tk.messagebox.askquestion('Puissance 4','Souhaites-tu sauvegarder ta partie ?',icon = 'info')
            if save_draw == 'yes':
                self.save_party()
                self.save_logs()
                replay_draw = tk.messagebox.askquestion('Puissance 4','Souhaites-tu rejouer ?',icon = 'info')
                if replay_draw == "yes":
                    self.restart_game()
                else: 
                    self.save_logs()
                    sys.exit()
            else:
                self.save_logs()
                replay_draw = tk.messagebox.askquestion('Puissance 4','Souhaites-tu rejouer ?',icon = 'info')
                if replay_draw == "yes":
                    self.restart_game()
                else: 
                    sys.exit()

# Vérification pour exécuter le jeu uniquement si ce fichier est le fichier principal
if __name__ == "__main__":
    # Instanciation de l'objet Power4
    app = Power4()
    # Boucle principale de l'application
    app.mainloop()