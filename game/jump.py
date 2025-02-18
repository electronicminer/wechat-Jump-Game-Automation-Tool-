import pyautogui
import cv2
import numpy as np
import time
import keyboard
while (1):
    if keyboard.is_pressed('1'):
        x1, y1 = pyautogui.position()  # 返回鼠标的坐标
        print(x1, y1)
    if keyboard.is_pressed('2'):
        x2, y2 = pyautogui.position()  # 返回鼠标的坐标
        print(x2, y2)
    if keyboard.is_pressed('q'):
        break

def detect_player():
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 保存截图用于调试
    cv2.imwrite('template.png', screenshot)
    target = cv2.imread('target.png', 0)
    template = cv2.imread('template.png', 0)
    result = cv2.matchTemplate(template, target, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc

    # 获取目标图像的宽度和高度
    h, w = target.shape

    # 计算目标图像的右下角坐标
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 在截图中画出矩形框标记目标图像的位置
    cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
    # print(top_left, bottom_right)
    cv2.circle(screenshot, (top_left[0]+w//2, top_left[1]+h-20), 10, (0, 0, 255), -1)
    # 显示带有矩形框的截图
    # cv2.imshow('Screenshot', screenshot)
    # cv2.waitKey (0)  

    return top_left[0]+w//2, top_left[1]+h-20, top_left[0], top_left[1]

def detect_brick(player_x, player_y):
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1-600))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # 保存截图用于调试
    cv2.imwrite('template.png', screenshot)
    img=cv2.imread('template.png')
    img=cv2.GaussianBlur(img,(5,5),0)
    canny = cv2.Canny(img, 1, 10)
    h, w = canny.shape
    for y_ in range(player_y,y2-y1-600):
        for x_ in range(player_x,player_x+45):
            canny[y_][x_] = 0
    print(h, w)
    center_x, center_y = 0, 0
    max_x = 0
    for y in range(h):
        for x in range(w):
            if canny[y, x] == 255:
                if center_x == 0:
                    center_x = x
                if x > max_x:
                    center_y = y
                    max_x = x
    cv2.imwrite('canny.png', canny)
    
    cv2.circle(screenshot, (center_x, center_y), 10, (0, 0, 255), -1)
    
    # cv2.imshow('Screenshot', screenshot)
    # cv2.waitKey (0) 
    # cv2.imshow('canny', canny)
    # cv2.waitKey (0) 
    return center_x, center_y
x5,y5,x6,y6=detect_player()
detect_brick(x6,y6)
# 639 871

while True:  # 获取鼠标当前位置
    time.sleep(1.5)
    x3, y3 = pyautogui.position()
    x5,y5,x6,y6=detect_player()
    x4, y4 = detect_brick(x5,y5)
    print(f"brick position: ({x4}, {y4})")
    
    dis=((x5-x4)**2+(y5-y4)**2)**0.5
    dalay_time_s=dis/530
    print(f'distance={dis}\nclick_time={dalay_time_s}\n')
    pyautogui.mouseDown(x3, y3, button='left')
    time.sleep(dalay_time_s)
    pyautogui.mouseUp(x3, y3, button='left')
    if keyboard.is_pressed('q'):
        break

# 
