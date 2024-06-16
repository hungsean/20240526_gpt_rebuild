import os
import json

class SettingsManager:
    valid_area_key = ['1', '2', '3']
    AREA_SETTINGS_NAME = "area_settings"

    def __init__(self, directory, filename):
        self.config_dir = directory
        self.config_file = filename
        self.config_path = os.path.join(self.config_dir, self.config_file)
        self.ensure_directory()
        self.ensure_file()
        self.settings = self.load_settings()
        self.ensure_settings_valid()
        self.validate_area_settings()

        # debug ---
        self.print_settings()
        # debug end ---

    def ensure_directory(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
    
    def ensure_file(self):
        if not os.path.exists(self.config_path):
            self.settings = {}
            self.save_settings()  # Create empty settings file if not exists

    def load_settings(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                settings = json.load(f)
                return settings
        else:
            print("[function.settings.load_settings] config_path not exist")
            return {}
        
    def ensure_settings_valid(self):
        if self.AREA_SETTINGS_NAME not in self.settings:
            self.settings[self.AREA_SETTINGS_NAME] = {}
            self.save_settings()

    def validate_area_settings(self):
        required_keys = ['1', '2', '3']
        changes_made = False

        # 確保每個必需的鍵都存在於 area_settings 中
        for key in required_keys:
            if key not in self.settings[self.AREA_SETTINGS_NAME]:
                self.settings[self.AREA_SETTINGS_NAME][key] = [None] * 4
                changes_made = True
            elif len(self.settings[self.AREA_SETTINGS_NAME][key]) != 4:
                self.settings[self.AREA_SETTINGS_NAME][key] = (self.settings[self.AREA_SETTINGS_NAME][key] + [None] * 4)[:4]
                changes_made = True
        
        # 移除 area_settings 中不需要的鍵
        keys_to_remove = [key for key in self.settings[self.AREA_SETTINGS_NAME] if key not in required_keys]
        for key in keys_to_remove:
            del self.settings[self.AREA_SETTINGS_NAME][key]
            changes_made = True

        if changes_made:
            self.save_settings()

    def get_value(self, key, index):
        # 從指定鍵中取得特定索引的值
        # 四個None值: 無效值
        return self.settings.get(key, [None] * 4)[index]
    
    
    def get_value_all(self, key):
        if key not in self.valid_area_key:
            print("[function.settings.SettingsManager/get_value_all] key not valid")
            return None
        # 四個None值: 無效值
        return self.settings[self.AREA_SETTINGS_NAME].get(key)

    def update_value(self, key, index, value):
        # 更新特定鍵的特定索引的值
        if key not in self.settings:
            self.settings[key] = [None] * 4
        if index >= 0 and index < 4:
            self.settings[key][index] = value
            self.save_settings()

    def update_value_all(self, key, value: list):
        # 更新特定鍵的特定索引的值
        if key not in self.valid_area_key:
            print("[function.settings.SettingsManager/update_value_all] key not valid")
            return -1
        if len(value) != 4:
            print("[function.settings.SettingsManager/update_value_all] value len not valid")
            return -1
        self.settings[self.AREA_SETTINGS_NAME][key] = value
        self.save_settings()
        return 0

    def save_settings(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def print_settings(self):
        print(self.settings)

main_setting_manager = SettingsManager("config", "settings.json")

