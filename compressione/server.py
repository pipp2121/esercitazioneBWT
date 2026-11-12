import socket
from principale import algoritmo_compressione
# Crea un socket TCP (SOCK_STREAM) che usa indirizzi IPv4 (AF_INET).
# Il costrutto with chiude automaticamente il socket al termine del blocco.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    # Associa il socket all'indirizzo IP locale e alla porta 5000.
    server.bind(("127.0.0.1", 5000))

    # Mette il socket in ascolto di richieste di connessione.
    server.listen()

    print("Server in ascolto...")
    print("Socket di ascolto:", server.getsockname())

    # Attende che un client si connetta.
    # accept() restituisce un nuovo socket (conn) per comunicare
    # con il client e il suo indirizzo (addr).
    conn, addr = server.accept()

    with conn:
        print("Client connesso:", addr)

        # Mostra IP e porta locali del socket di connessione:
        # sono gli stessi del socket di ascolto.
        print("Socket di connessione:", conn.getsockname())

        # Riceve fino a 1024 byte dal client.
        # decode() converte i byte ricevuti in una stringa.
        messaggio = conn.recv(1024).decode()
        print("Messaggio ricevuto:", messaggio)
        s=algoritmo_compressione(messaggio)

        # Rimanda al client gli stessi byte ricevuti (echo).
        # sendall() garantisce l'invio di tutti i byte del messaggio,
        # mentre send() potrebbe inviarne solo una parte.
        conn.sendall(s.encode())