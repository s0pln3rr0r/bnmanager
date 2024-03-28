import sqlite3
from termcolor import cprint


def edit_Selected_Bot(bot_index):
    conn = sqlite3.connect('bnmanager.sqlite')
    query = "SELECT * FROM bind WHERE ID=" + str(bot_index)
    try:
        cursor = conn.execute(query)
        lcursor = list(cursor)
        cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
        cprint("Following are the details of your selected bot", attrs=["bold"])

        tup = (
            "ID",
            "Payload Name",
            "Payload",
            "Host",
            "Port",
            "Persistance Command",
            "TimeStamp",
        )
        for i in range(len(tup)):
            cprint(tup[i] + ": ", attrs=["bold"], end="")
            print(lcursor[0][i])
        cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
        cprint("Do you want to edit name of the bot, Y/N", attrs=["bold"])
        cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
        user_input = input().lower()
        if user_input == 'y':
            cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
            cprint("Enter New Name", attrs=["bold"])
            cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
            user_input = input()
            query = (
                "UPDATE bind SET pay_name=\'"
                + str(user_input)
                + "\' WHERE ID="
                + str(bot_index)
            )
            conn.execute(query)
            cprint(
                "[+] Name Updated Successfully. Here are the new details of the bot.",
                "green",
                attrs=["bold"],
            )
        elif user_input == 'n':
            cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
            cprint("Redirecting to main menu.", attrs=["bold"])
            return 0
        else:
            cprint(
                "Invalid option, redirecting to main menu.", "yellow", attrs=["bold"]
            )
            return 1

        query = "SELECT * FROM bind WHERE ID=" + str(bot_index)
        print(query)
        cursor = conn.execute(query)
        lcursor = list(cursor)
        cprint("view[or]editBot> ", "green", attrs=["bold"], end="")
        cprint("Following are the details of your selected bot", attrs=["bold"])

        tup = (
            "ID",
            "Payload Name",
            "Payload",
            "Host",
            "Port",
            "Persistance Command",
            "TimeStamp",
        )
        for i in range(len(tup)):
            cprint(tup[i] + ": ", attrs=["bold"], end="")
            print(lcursor[0][i])
    except KeyboardInterrupt:
        cprint("Exiting 'View or Edit Bot' mode...", "yellow")
        return 1

