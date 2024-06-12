from function import image
print("[function.translate] finished import function.image")
from function.gpt_controller import translate_jp_tc
print("[function.translate] finished import function.gpt_controller.translate_jp_tc")


def start_translate():
    """
    return code:
    0: work successful
    -1: some problem cause it can't work
    """
    coordination = image.select_area()
    # if check_coordination(coordination) == False:
    #     print("too small")
    #     return -1
    screenshot_pillow = image.screenshot_with_pillow(coordination)
    if screenshot_pillow is None:
        return -1
    
    screenshot_numpy = image.pillow_to_numpy(screenshot_pillow)
    screenshot_numpy_preprocessed = image.preprocess(screenshot_numpy)
    screenshot_pillow_preprocessed = image.numpy_to_pillow(screenshot_numpy_preprocessed)
    recognize_text = image.image_recognize_to_jp(screenshot_pillow_preprocessed)

    if recognize_text is None:
        print("text null")
        return -1
    
    print("------")
    print(recognize_text)
    print("------")
    translated_text = translate_jp_tc(recognize_text, confirm= False)
    print("------")
    print(translated_text)
    print("------")
    return 0

def check_coordination(coordination):
    # 確認陣列的長度是否至少為 4
    if len(coordination) != 4:
        raise ValueError("The array must have at least 4 elements")
    
    # 計算差距
    diff_0_2 = abs(coordination[0] - coordination[2])
    diff_1_3 = abs(coordination[1] - coordination[3])

    # 檢查差距是否大於 10
    if diff_0_2 > 10 or diff_1_3 > 10:
        return True
    else:
        return False

