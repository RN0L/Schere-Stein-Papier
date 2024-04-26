import socket

def entscheide_gewinner(wahl1, wahl2):
    gewinnt_gegen = {'Schere': 'Papier', 'Papier': 'Stein', 'Stein': 'Schere'}
    if wahl1 == wahl2:
        return "Unentschieden!"
    elif gewinnt_gegen[wahl1] == wahl2:
        return "Spieler 1 gewinnt!"
    else:
        return "Spieler 2 gewinnt!"

def main():
    host = '127.0.0.1'
    port = 12345

    server_verbindung = socket.socket()
    server_verbindung.bind((host, port))

    server_verbindung.listen(2) 
    print("Warte auf Spieler...")
    spieler1, ip_spieler1 = server_verbindung.accept()  
    print(f"Verbunden mit {ip_spieler1}")
    spieler2, ip_spieler2 = server_verbindung.accept()  
    print(f"Verbunden mit {ip_spieler2}")

    while True:
        wahl1 = spieler1.recv(1024).decode()  
        wahl2 = spieler2.recv(1024).decode()  

        spieler1.send(wahl2.encode())
        spieler2.send(wahl1.encode())

        if not wahl1 or not wahl2:
            print("Spiel beendet")
            break

        ergebnis = entscheide_gewinner(wahl1, wahl2)
        spieler1.sendall(ergebnis.encode())
        spieler2.sendall(ergebnis.encode())

    spieler1.close()
    spieler2.close()

if __name__ == '__main__':
    main()
