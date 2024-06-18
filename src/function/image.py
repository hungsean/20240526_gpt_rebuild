import tkinter as tk
print("[function.image] finished import tkinter")
from tkinter import Toplevel
print("[function.image] finished import tkinter.Toplevel")
from PIL.ImageGrab import grab
print("[function.image] finished import PIL.ImageGrab.grab")
from PIL import Image
print("[function.image] finished import PIL.Image")
import numpy as np
print("[function.image] finished import numpy")
import cv2
print("[function.image] finished import cv2")
import pytesseract
print("[function.image] finished import pytesseract")
import time
print("[function.image] finished import time")
from function import tesseract_path
print("[function.image] finished import function.tesseract_path")


root = None

def select_area():
    def on_click(event):
        canvas.delete("rectangle")
        global start_x, start_y
        start_x, start_y = event.x, event.y

    def on_drag(event):
        # global rectangle
        global end_x, end_y
        end_x, end_y = event.x, event.y
        canvas.delete("rectangle")
        canvas.create_rectangle(start_x, start_y, end_x, end_y, outline='red', tag="rectangle")

    def on_release(event):
        global end_x, end_y
        end_x, end_y = event.x, event.y
        # print(f"Start coordinates: ({start_x}, {start_y})")
        # print(f"End coordinates: ({end_x}, {end_y})")
        root.quit()

    global root
    root = tk.Tk()
    
    root.attributes('-fullscreen', True)
    root.attributes('-alpha', 0.3)  # 半透明窗口
    root.wait_visibility(root)
    root.wm_attributes('-topmost', 1)
    
    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.bind("<Button-1>", on_click)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    root.mainloop()
    root.destroy()
    return [start_x, start_y, end_x, end_y]


def screenshot_with_pillow(coordination: list):
    if check_coordination(coordination) != True:
        print("[function.image/screenshot_with_pillow] coordination check not true")
        return None

    # 定義截圖區域 (left, top, right, bottom)
    # 確保座標是正確的（左上角和右下角）
    left = min(coordination[0], coordination[2])
    top = min(coordination[1], coordination[3])
    right = max(coordination[0], coordination[2])
    bottom = max(coordination[1], coordination[3])
    
    # 截圖指定區域
    screenshot = grab(bbox=(left, top, right, bottom))
    
    
    return screenshot

def pillow_to_numpy(pillow_image):
    """
    將 Pillow 圖片轉換為 NumPy 陣列

    參數:
    pillow_image (PIL.Image.Image): Pillow 圖片對象

    返回:
    numpy.ndarray: NumPy 陣列表示的圖片
    """
    return np.array(pillow_image, dtype=np.uint8)

def numpy_to_pillow(numpy_array):
    """
    將 NumPy 陣列轉換為 Pillow 圖片

    參數:
    numpy_array (numpy.ndarray): NumPy 陣列表示的圖片

    返回:
    PIL.Image.Image: Pillow 圖片對象
    """
    return Image.fromarray(numpy_array.astype('uint8'))

def preprocess(image):
    # 灰度化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 降噪（中值濾波）
    denoised_image = cv2.medianBlur(binary_image, 1)

    return denoised_image
    
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def image_recognize_to_jp(image: Image):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image,config=custom_config, lang= 'jpn')
    if all(char.isspace() for char in text):
        # image.show()
        return None
    return text

def check_coordination(coordination: list) -> bool:
    if coordination is None:
        print("[function.image/check_coordination] coordination is None")
        return None

    # 確認陣列的長度是否至少為 4
    if len(coordination) != 4:
        print("[function.image/check_coordination] The array must have at least 4 elements")
        return None
    
    if not all(isinstance(i, (int, float)) for i in coordination):
        print("[function.image/check_coordination] All elements must be numbers")
        return None
    
    temp_start_x, temp_start_y,temp_end_x,temp_end_y = coordination
    
    # 計算差距
    diff_0_2 = abs(temp_start_x - temp_end_x)
    diff_1_3 = abs(temp_start_y - temp_end_y)

    # 檢查差距是否大於 10
    if diff_0_2 > 10 or diff_1_3 > 10:
        return True
    else:
        return False
    
def draw_rectangle(coords: list):
    # 檢查輸入是否為四個元素的列表
    if len(coords) != 4:
        print("[function.image/draw_rectangle] coords len not valid")
        return -1
    
    # 檢查每個座標是否為數字且不為None
    for coord in coords:
        if coord is None or not isinstance(coord, (int, float)):
            print("[function.image/draw_rectangle] coords value not valid")
            return -1

    # 將座標轉換為整數
    x1, y1, x2, y2 = map(int, coords)

    # 創建主Tkinter窗口
    root = tk.Tk()

    root.attributes('-fullscreen', True)
    root.attributes('-alpha', 0.3)  # 半透明窗口
    root.wait_visibility(root)
    root.wm_attributes('-topmost', 1)

    # 創建畫布以繪製矩形
    canvas = tk.Canvas(root, cursor="cross")
    canvas.pack(fill=tk.BOTH, expand=True)

    # 獲取螢幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 繪製矩形
    # x1, y1, x2, y2 = coords
    canvas.create_rectangle(x1, y1, x2, y2, outline='red', width=3)

    # 啟動視窗
    root.update()
    
    # 設定一定時間後關閉視窗
    time.sleep(1.5)
    root.destroy()

