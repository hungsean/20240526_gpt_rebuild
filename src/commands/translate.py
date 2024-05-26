from function import gpt_controller

def index(str_argument: str) -> int:
    text = gpt_controller.translate_jp_tc(str_argument)
    print(text)
    return 0