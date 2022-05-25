import socket
import sys
import time
import os
import signal
import linecache
import datetime

sock = socket.socket()
host = '192.168.1.8'
port = 1006
TIMEOUT = 10
ANSTIMEOUT = 3

file = open("New" , "w+")
pap = open("res" , "w+")
temp = open("temp" , "w+")
final = open("final" , "w+")

sock.connect((host , port))
print("Connection Established!\n")

def interrupted(signum, frame):
    print("\nToo slow!")
    sys.exit()
signal.signal(signal.SIGALRM, interrupted)

def input(num):
    try:
            print("You have " + str(num) + " seconds to type in your stuff...")
            foo = raw_input()
            return foo
    except:
            return

def main():
    for i in range(260):
        data = sock.recv(128)

        if len(data) > 0:
            file.write(str(data))
    
    sock.close()
    file.close()
    fil = open("New" , "r")
    text = fil.readline()
    print(text)

    for i in range(18):
        text = fil.readline()
        print(text)
    
    time.sleep(5)
    text = fil.readline()
    print(text)
    time.sleep(5)

    for i in range(20):
        for j in range(12):
            text = fil.readline()
            print(text)
        
        current_time1 = datetime.datetime.now()
        signal.alarm(TIMEOUT)
        val = input(TIMEOUT)
        signal.alarm(0)
        current_time2 = datetime.datetime.now()
        
        if val == 'b':
            signal.alarm(ANSTIMEOUT)
            sol = input(ANSTIMEOUT)
            signal.alarm(0)
            temp.write(str(sol) + '\n')
            time_diff = current_time2 - current_time1
            pap.write(str(time_diff) + "\n")

        else:
            print("\nInvalid input , Chance over!")
            pap.write(str(1000) + "\n")
            temp.write(str(1000) + "\n")

    count = 261
    temp.close()
    pap.close()
    
    for i in range(20):
        val = linecache.getline("temp" , i + 1)
        ans = linecache.getline("New" , count)
        text = linecache.getline("res" , i + 1)
        check = linecache.getline("check" , 1)
        
        if val == ans:
            final.write(text)

        elif val != ans and val != check:
            final.write(str(-1) + "\n")

        elif val == check:
            final.write(text)
        
        count += 1

main()
final.close()
os.remove("New")
os.remove("temp")
os.remove("res")

points = 0.0

for i in range(20):
    ans = linecache.getline("final" , i + 1)
    check1 = linecache.getline("check" , 1)
    check = linecache.getline("check" , 2)

    if ans == check:
        points -= 0.5
    
    elif ans != check and ans != check1:
        points += 1

print(points)
