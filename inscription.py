import tkinter as tk

# Fonction pour afficher un message dans la console
def afficher_message():
    print("Message affiché")

# Fonction pour créer une nouvelle fenêtre d'inscription
def nouvelle_fenetre_inscription():
    fenetre_inscription = tk.Toplevel(root)
    fenetre_inscription.title("Inscription")

    etiquette_prenom = tk.Label(fenetre_inscription, text="Prénom:")
    etiquette_prenom.grid(row=0, column=0, padx=5, pady=5)

    champ_prenom = tk.Entry(fenetre_inscription)
    champ_prenom.grid(row=0, column=1, padx=5, pady=5)

    etiquette_nom = tk.Label(fenetre_inscription, text="Nom:")
    etiquette_nom.grid(row=1, column=0, padx=5, pady=5)

    champ_nom = tk.Entry(fenetre_inscription)
    champ_nom.grid(row=1, column=1, padx=5, pady=5)

    etiquette_email = tk.Label(fenetre_inscription, text="E-mail:")
    etiquette_email.grid(row=2, column=0, padx=5, pady=5)

    champ_email = tk.Entry(fenetre_inscription)
    champ_email.grid(row=2, column=1, padx=5, pady=5)

    etiquette_mot_de_passe_inscription = tk.Label(fenetre_inscription, text="Mot de passe:")
    etiquette_mot_de_passe_inscription.grid(row=3, column=0, padx=5, pady=5)

    champ_mot_de_passe_inscription = tk.Entry(fenetre_inscription, show="*")
    champ_mot_de_passe_inscription.grid(row=3, column=1, padx=5, pady=5)

    bouton_inscription = tk.Button(fenetre_inscription, text="S'inscrire", command=afficher_message)
    bouton_inscription.grid(row=4, column=0, columnspan=2, pady=5)

# Création de la fenêtre principale
root = tk.Tk()
root.title("My Discord")

# Bouton pour ouvrir la fenêtre d'inscription
bouton_inscription = tk.Button(root, text="S'inscrire", command=nouvelle_fenetre_inscription)
bouton_inscription.pack(pady=10)

root.mainloop()
