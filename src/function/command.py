from commands import test, token_len, translate

def menu(str_argument: str):
    for key in commands.keys():
        print("- ", key)
    return 0

commands = {
    "test": test.index,
    "token_len": token_len.index,
    "translate": translate.index,
    "menu": menu
}

def exec_commands(command_name: str, str_arguments: str):
    # if command_name == "menu":
    #     menu()
    #     return 0

    for key, value in commands.items():
        if key == command_name:
            value(str_arguments)
            return 0
    print("[exec_commands] no command found")
    return -1
    

def get_commands():
    return commands

