import socket

def main():
    host = '127.0.0.1'  
    port = 12345        # Der gleiche Port wie der Server

    server_verbindung = socket.socket()
    server_verbindung.connect((host, port)) 

    message = input("Wähle Schere, Stein oder Papier: ")
    while message.lower() not in ['schere', 'stein', 'papier']:
        message = input("Ungültige Eingabe, wähle Schere, Stein oder Papier: ")

    server_verbindung.send(message.encode()) 
    eingabe = server_verbindung.recv(1024).decode() 

    print('Die andere Wahl war: ' + eingabe)

    ergebnis = server_verbindung.recv(1024).decode()
    print('Ergebnis: ' + ergebnis)

    server_verbindung.close()

if __name__ == '__main__':
    main()
