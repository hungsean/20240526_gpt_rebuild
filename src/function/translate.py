from function import image
print("[function.translate] finished import function.image")
from function.gpt_controller import translate_jp_tc
print("[function.translate] finished import function.gpt_controller.translate_jp_tc")
from function.settings import main_setting_manager
print("[function.translate] finished import function.settings")
import re
print("[function.translate] finished import re")

def start_translate():
    """
    return code:
    0: work successful
    -1: some problem cause it can't work
    """
    coordination = image.select_area()
    return coords_translate(coordination)
    # if check_coordination(coordination) == False:
    #     print("too small")
    #     return -1
    # screenshot_pillow = image.screenshot_with_pillow(coordination)
    # if screenshot_pillow is None:
    #     return -1
    
    # screenshot_numpy = image.pillow_to_numpy(screenshot_pillow)
    # screenshot_numpy_preprocessed = image.preprocess(screenshot_numpy)
    # screenshot_pillow_preprocessed = image.numpy_to_pillow(screenshot_numpy_preprocessed)
    # recognize_text = image.image_recognize_to_jp(screenshot_pillow_preprocessed)

    # if recognize_text is None:
    #     print("text null")
    #     return -1
    
    # print("------")
    # print(recognize_text)
    # print("------")
    # translated_text = translate_jp_tc(recognize_text, confirm= False)
    # print("------")
    # print(translated_text)
    # print("------")
    # return 0

def settings_translate(id: str) -> int:
    coords = main_setting_manager.get_value_all(id)
    if coords is None:
        print("[function.translate/settings_translate] coords is None")
        return -1
    
    if any(element is None for element in coords):
        print("[function.translate/settings_translate] coords have None")
        return -1
    
    return_value = coords_translate(coords)
    return return_value

def coords_translate(coords: list) -> int:
    if coords is None:
        print("[function.translate/coords_translate] coords is None")
        return -1

    screenshot_pillow = image.screenshot_with_pillow(coords)
    if screenshot_pillow is None:
        print("[function.translate/coords_translate] screenshot_pillow is None")
        return -1
    
    # screenshot_numpy = image.pillow_to_numpy(screenshot_pillow)
    # screenshot_numpy_preprocessed = image.preprocess(screenshot_numpy)
    # screenshot_pillow_preprocessed = image.numpy_to_pillow(screenshot_numpy_preprocessed)
    # recognize_text = image.image_recognize_to_jp(screenshot_pillow_preprocessed)

    recognize_text = image.image_recognize_to_jp(screenshot_pillow)

    filtered_text = re.sub(r'^[^\u3000-\u303F\u3040-\u309F\u30A0-\u30FF]+$', '', recognize_text, flags=re.MULTILINE)

    filtered_text = re.sub(r'目\s*\n\s*坦', '', filtered_text)

    # 進行後處理字串清理
    # 移除任何意外的換行符或多於空格
    cleaned_text = re.sub(r'\n+', '\n', filtered_text).strip()

    if cleaned_text is None:
        print("text null")
        return -1
    
    print("------")
    print(cleaned_text)
    print("------")
    translated_text = translate_jp_tc(cleaned_text, confirm= False)
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

