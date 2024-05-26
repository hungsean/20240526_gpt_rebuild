from commands import test

commands = {
    "test": test.index
}

def exec_commands(command_name: str, str_arguments: str):
    for key, value in commands.items():
        if key == command_name:
            value(str_arguments)
            return 0
    print("[exec_commands] no command found")
    return -1
    

def get_commands():
    return commands