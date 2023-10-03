import tkinter as tk
import socket
import threading

IP = "localhost"
PORT = 12345


def envoyer_message():
    message = message_entry.get()
    if message:
        message_entrant("Moi : " + message)
        client_socket.send(message.encode())
        message_entry.delete(0, tk.END)  # Efface le champ de saisie après l'envoi


def recevoir_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                messages_text.config(state=tk.NORMAL)
                messages_text.insert(tk.END, "Utilisateur : " + message + "\n")
                messages_text.config(state=tk.DISABLED)
        except Exception as e:
            print("Erreur lors de la réception du message :", str(e))
            break


def se_connecter():
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        message_entrant("Serveur : Connecté au serveur.")
        
        # Thread permet de recevoir les messages du serveur
        recevoir_thread = threading.Thread(target=recevoir_messages)
        recevoir_thread.daemon = True
        recevoir_thread.start()
    except Exception as e:
        print("Erreur lors de la connexion au serveur :", str(e))


# Teste afficher message dans la fenetre
def message_entrant(message):
    messages_text.config(state=tk.NORMAL)
    messages_text.insert(tk.END, message + "\n")
    messages_text.config(state=tk.DISABLED)


# Tkinter

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Chat Sécurisé")

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
se_connecter() # Permet de se connecter directement lors du lancement du programme
fenetre.mainloop()