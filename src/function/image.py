import tkinter as tk
print("[function.image] finished import tkinter")
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
    if check_coordination(coordination) == False:
        print("too small")
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

