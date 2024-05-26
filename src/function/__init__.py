import json
import os
import sys

print("start function init")
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

if 'openai_api_key' not in config:
    print(f"配置檔案中缺少必要的資料: openai_api_key")
    sys.exit(1)

# 將配置資料存儲在全域變數中
openai_api_key = config['openai_api_key']

__all__ = ['openai_api_key']