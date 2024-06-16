from function import image
from function.settings import main_setting_manager

def index(str_arguments: str) -> int:
    required_keys = main_setting_manager.valid_area_key
    area_key = str_arguments

    if area_key not in required_keys:
        print("[commands.setting/index]id not valid")
        return -1
    
    selected_area = image.select_area()
    if image.check_coordination(selected_area) == False:
        print("[commands.setting/index] select area too small")
        return -1
    
    return_value = main_setting_manager.update_value_all(area_key, selected_area)
    if return_value == 0:
        print("setting successful saved")

    return return_value