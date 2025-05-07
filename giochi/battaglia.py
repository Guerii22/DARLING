import zmq
import ip
def server():
    if ip.ip()==False:
        return
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Usa REP per rispondere alle richieste
    socket.bind("tcp://*:5555")  # Ascolta su tutte le interfacce e sulla porta 5555
    print("in attesa di un giocatore")
    while True:
        message = socket.recv_string()
        print(f"Ricevuto: {message}")
        if message:
            break
    print("fine comunicazione")
if __name__ == "__main__":
    server()