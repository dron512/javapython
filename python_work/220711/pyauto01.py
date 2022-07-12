import pyautogui

print(pyautogui.size())
print(pyautogui.position())

# pyautogui.moveTo(x=548,y=19)
# pyautogui.click()
img = pyautogui.locateOnScreen('./python_work/220711/help.png', confidence=0.8)
# pyautogui.click('./python_work/220711/help.png')
pyautogui.click(img)