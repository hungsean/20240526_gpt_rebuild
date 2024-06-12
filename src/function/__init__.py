import json
print("[function.__init__] finished import json")
import os
print("[function.__init__] finished import os")
import sys
print("[function.__init__] finished import sys")

# 確定配置檔案的路徑
config_path = os.path.join('config', 'config.json')

# 確認配置檔案是否存在
if not os.path.exists(config_path):
    print(f"配置檔案 {config_path} 不存在，請創建該檔案並提供必要的配置。")
    sys.exit(1)

# 讀取配置檔案
with open(config_path, 'r') as config_file:
    try:
        config = json.load(config_file)
    except json.JSONDecodeError:
        print(f"配置檔案 {config_path} 格式不正確，請檢查檔案內容。")
        sys.exit(1)

# 要檢查的必要項目
required_keys = ['openai_api_key', 'tesseract_path']

# 檢查每個必要項目是否存在於配置檔案中
for key in required_keys:
    if key not in config:
        print(f"配置檔案中缺少必要的資料: {key}")
        sys.exit(1)

# 將配置資料存儲在全域變數中
openai_api_key = config['openai_api_key']
tesseract_path = config['tesseract_path']

# __all__ = ['openai_api_key']
__all__ = required_keys

print("[function.__init__] finished init")