import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg, username):
    message = f"{username}: {msg}".encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            if not message: 
                print("[SERVER DISCONNECTED] Server disconnected.")
                break
            print(message)
        except:
            print("[ERROR] An error occurred!")
            break
    client.close()

receive_thread = threading.Thread(target=receive)
receive_thread.start()


print("[CONNECTED] Conectado ao servidor. Você pode começar a enviar mensagens.")

username = input("Digite seu nome de usuário: ")

while True:
    msg = input()
    send(msg, username)
    if msg == DISCONNECT_MESSAGE:
        print("[CLIENT DISCONNECTED] Desconectado do servidor.")
        break

client.close()
