import socket
import threading

serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "localhost"
PORT = 12345

serveur_socket.bind((IP, PORT))
serveur_socket.listen()

# Stocke les connexions des clients
connexions_clients = []


def gerer_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break  # Quitte la boucle si le client se déconnecte
            envoyer_a_tous(message)
        except Exception as e:
            print("Erreur lors de la réception du message :", str(e))
            break
    client_socket.close()


def envoyer_a_tous(message):
    for client_socket in connexions_clients:
        try:
            client_socket.send(message.encode())
        except Exception as e:
            print("Erreur lors de l'envoi au client :", str(e))


print("Serveur en attente de connexions...")
while True:
    client_socket, _ = serveur_socket.accept()
    connexions_clients.append(client_socket)
    print("Nouvelle connexion.")

    # Crée un thread pour gérer la communication avec le client
    client_thread = threading.Thread(target=gerer_client, args=(client_socket,))
    client_thread.daemon = True
    client_thread.start()