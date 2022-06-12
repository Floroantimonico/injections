import socket
import codecs
import time
import sys

argumemto_1 = sys.argv[1]
argumemto_2 = int(sys.argv[2])

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((argumemto_1, argumemto_2))


while True:
    cabecera = input("shell-1 >> ")
    
    if cabecera == "fopen":
        
        clave = "fopen"
        
        nombre = input("nombre del archivo ")
        
        contenido = input("contenido ")
        
        key = clave.encode(encoding="utf-8")
        
        empaquetar_1 = nombre.encode(encoding="utf-8")
        
        empaquetar_2 = contenido.encode(encoding="utf-8")
        
        print("\nenviando clave....")
        
        time.sleep(2.0)
        
        cliente.send(key)
        
        print("\nenviando nombre del archivo....")
        
        time.sleep(3.0)
        
        cliente.send(empaquetar_1)
        
        print("\nenviando contenido....\n")
        
        time.sleep(3.0)
        
        cliente.send(empaquetar_2)
        
    else:
        empaquetar = cabecera.encode(encoding="utf-8")
    
        print("enviando....")
    
        time.sleep(2.0)
    
        cliente.send(empaquetar)
    
        desempaquetar = cliente.recv(4000).decode("utf8")
    
        print(desempaquetar)