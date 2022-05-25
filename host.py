import socket 
import time
import threading
import sys

all_conn = []
points = []

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    host = "192.168.1.8"
    port = 1006
    
except socket.error as mess:
    print("Socket Creation Error: " + str(mess))

def Binding():
    try:
        sock
        host
        port
        
        print("Binding in progress...\n")
        sock.bind((host , port))
        sock.listen(3)
        print("Binding Succefull!\n")
    
    except socket.error as mess:
        print("Binding failed , Binding error: " + str(mess) + "\n" + "Retrying...\n")
        Binding()
    
# def check(num):
#     data = all_conn[num].recv(1024)

#     print(data)

def game(num):
    fil = open("Questions" , "r")

    play = "Your player Number:" + str(num + 1) + "\n"
    all_conn[num].send(play)

    for i in range(280):
        text = fil.readline()
        all_conn[num].send(text)

    all_conn[num].close()

# def recvi(num):
#     for i in range(20):
#         data = all_conn[num].recv(128)

#         if len(data) > 0:
#             check[num].append(data)

#     all_conn[num].close()

# def re_conn():
#     sock.listen(1)
    
#     for i in range(1):
#         try:
#             conn , address = sock.accept()
#             sock.setblocking(1)
#             print("Connection re-established")

#         except:
#             print("Unable to connect\n")    
    
#     thread1 = threading.Thread(target = recvi , args = (0 , ))
#     thread1.start()

def conn():
    for i in all_conn:
        i.close()

    del all_conn[:]
    
    Num_Players = 0
    
    for i in range(3):
        try:
            conn , address = sock.accept()
            sock.setblocking(1)
            all_conn.append(conn)
            points.append(0)
            Num_Players += 1
            print("Connection Established!\n" + "Number of Players in Lobby: " + str(Num_Players))

        except:
            print("Unable to Connect\n")
        
    thread1 = threading.Thread(target = game , args = (0 , ))
    thread2 = threading.Thread(target = game , args = (1 , ))
    thread3 = threading.Thread(target = game , args = (2 , ))
    thread1.start()
    thread2.start()
    thread3.start()

def main():
    Binding()
    conn()
    # re_conn()

main()
