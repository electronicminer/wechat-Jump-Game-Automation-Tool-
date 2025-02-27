# 跳一跳脚本实现原理
## 一、鼠标标记位置原理
在脚本运行过程中，用户可通过按键1和2来标记屏幕上的两个位置。程序运用`pyautogui.position()`获取鼠标当前坐标，并将其存储为全局变量`x1`、`y1`和`x2`、`y2`。这两个位置主要用于定义后续截图区域，确保图片获取范围与游戏窗口对应。
该方法主要目的在于让用户能依据实际游戏窗口的位置和大小灵活调整截图区域，进而提高角色和砖块检测的准确性。

## 二、角色检测原理
角色检测主要依赖图像处理库OpenCV的模板匹配功能，具体步骤如下：
1. **截图获取**：利用`pyautogui.screenshot`获取游戏窗口截图，并通过`cv2.cvtColor`将截图转换为BGR格式。
2. **模板匹配**：运用`cv2.matchTemplate`将截取的屏幕图像与预先准备的模板图片（`target.png`）进行匹配。模板匹配通过计算输入模板与目标图像的相关性来识别游戏角色的位置，返回值为一个相似度矩阵。
3. **位置定位**：借助`cv2.minMaxLoc`函数找到相似度矩阵中的最大值位置，该位置即为角色在游戏截图中的坐标。此外，函数还会返回角色的宽度和高度，用于后续计算角色的中心位置。

## 三、砖块检测原理
砖块检测采用边缘检测技术，具体步骤如下：
1. **截图处理**：同样通过`pyautogui.screenshot`获取游戏窗口截图，但鉴于砖块通常位于游戏窗口上方，会对截图区域进行一定裁剪（`region=(x1, y1, x2 - x1, y2 - y1 - 600)`）。
2. **图像预处理**：
    - **高斯模糊**：使用`cv2.GaussianBlur`对截图进行高斯模糊处理，以减少图像噪声，提高边缘检测的准确性。
    - **Canny边缘检测**：运用`cv2.Canny`对模糊后的图像进行边缘检测，生成一张二值化边缘图像。
3. **位置搜索**：在生成的边缘图像中，通过遍历像素值为255（即边缘）的区域，找到砖块的中心位置。为确保检测准确性，还会屏蔽角色所在区域可能干扰检测的部分。

## 四、自动跳跃原理
自动跳跃功能基于游戏角色与砖块之间的距离来模拟鼠标点击，具体原理如下：
1. **距离计算**：使用欧几里得距离公式`distance = ((player_x - brick_x)**2 + (player_y - brick_y)**2)**0.5`计算游戏角色与砖块之间的距离。其中`player_x`和`player_y`是角色的位置坐标，`brick_x`和`brick_y`是砖块的位置坐标。
2. **时间转换**：根据距离计算合适的鼠标点击持续时间。通过公式`delay_time_s = distance / 530`将距离转换为时间，其中530是一个预设的比例因子，用于调整时间和距离之间的关系，确保跳跃的精准度与游戏中的实际表现相符。
3. **鼠标模拟**：使用`pyautogui.mouseDown`和`pyautogui.mouseUp`模拟鼠标按钮的按下和释放。通过设置合理的鼠标点击位置和持续时间，实现游戏角色的自动跳跃。
自动跳跃原理如图所示：[自动跳跃原理](自动跳跃原理的具体链接)

整个脚本的实现原理可总结为以下流程：
1. 通过鼠标标记位置确定游戏窗口截图的区域。
2. 使用模板匹配技术检测游戏角色的位置。
3. 应用边缘检测技术检测砖块的位置。
4. 基于游戏角色与砖块的距离计算鼠标点击时间，模拟鼠标点击实现自动跳跃。 
