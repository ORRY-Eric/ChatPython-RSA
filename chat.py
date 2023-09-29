import tkinter as tk

# Fonction pour envoyer un message
def envoyer_message():
    message = message_entry.get()
    if message:
        # Ajoute le nouveau message à la zone d'affichage
        messages_text.config(state=tk.NORMAL)  # Active la modification de la zone de texte
        messages_text.insert(tk.END, "Moi : " + message + "\n")
        messages_text.config(state=tk.DISABLED)  # Désactive la modification de la zone de texte
        message_entry.delete(0, tk.END)  # Efface le champ de saisie après l'envoi

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Chat")

# Zone d'affichage des messages
messages_text = tk.Text(fenetre, width=50, height=20, state=tk.DISABLED)
messages_text.pack()

# Champ de saisie de texte
message_entry = tk.Entry(fenetre, width=50)
message_entry.pack()

# Bouton d'envoi
envoyer_bouton = tk.Button(fenetre, text="Envoyer", command=envoyer_message)
envoyer_bouton.pack()

# Lance la boucle principale de l'interface utilisateur
fenetre.mainloop()
