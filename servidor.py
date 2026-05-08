import socket
import threading

host = '127.0.0.1'
port = 4447

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

jogadores         = []
bolinha           = []

def usuario(conn):
    while True:
        dados = conn.recv(1024)
        if not dados:
            break
        print(dados)
        
while True:
    con,cli = sock.accept()
    con.send("conectado".encode())
    print(cli)
    usuario(con)
    
