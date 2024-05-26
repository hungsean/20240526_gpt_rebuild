from function import gpt_controller

def index(str_argument: str) -> int:
    token = gpt_controller.token_len(str_argument)
    print("token: ", token)
    return 0