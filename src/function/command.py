
from commands import test
print("[function.command] finished import commands.test")
# from commands import token_len
# print("[function.command] finished import commands.token_len")
from commands import translate
print("[function.command] finished import commands.translate")
from commands import start
print("[function.command] finished import commands.start")
from commands import setting
print("[function.command] finished import commands.setting")
from commands import display
print("[function.command] finished import commands.display")

def menu(str_argument: str):
    for key in commands.keys():
        print("- ", key)
    return 0

def exit_program(str_argument: str):
    print("程式即將結束...")
    return 1

commands = {
    "test": test.index,
    # "token_len": token_len.index,
    "translate": translate.index,
    "menu": menu,
    "start": start.index,
    "exit": exit_program,
    "setting": setting.index,
    "display": display.index
}

def exec_commands(command_name: str, str_arguments: str):
    # if command_name == "menu":
    #     menu()
    #     return 0

    for key, value in commands.items():
        if key == command_name:
            return_code = value(str_arguments)
            if return_code == 1:
                return 1
            return 0
    print("[exec_commands] no command found")
    return -1
    

def get_commands():
    return commands

