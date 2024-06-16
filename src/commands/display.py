from function import image
from function.settings import main_setting_manager

def index(str_arguments: str) -> int:
    required_keys = main_setting_manager.valid_area_key
    area_key = str_arguments

    if area_key not in required_keys:
        print("[commands.setting/index]id not valid")
        return -1
    
    area = main_setting_manager.get_value_all(area_key)

    return_value = image.draw_rectangle(area)

    return return_value