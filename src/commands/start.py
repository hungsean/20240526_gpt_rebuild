import keyboard
print("[commands.start] finished import keyboard")
import time
print("[commands.start] finished import time")
from function import translate
print("[commands.start] finished import function.translate")

key_function_map = {
        't': translate.start_translate
    }
stop_combination = 'p'



def index(str_arguments: str) -> int:
    """
    監測按鍵資訊並觸發對應的函數。
    """

    global key_function_map

    def on_key_event(event):
        if event.name in key_function_map:
            key_function_map[event.name]()

    keyboard.on_press(on_key_event)
    
    # 停止監測組合鍵
    global stop_combination
    keyboard.add_hotkey(stop_combination, lambda: print("停止監測組合鍵被按下"))
    print("開始監測，按下 {} 終止監測".format(stop_combination))

    # 等待停止監測的組合鍵被按下
    keyboard.wait(stop_combination)
    time.sleep(0.5)
    
    # 清除所有鍵位檢測
    keyboard.unhook_all()

    return 0

