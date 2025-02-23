import pyperclip
import pyautogui
import random
import time

delay = 5

clipboard_text = pyperclip.paste()

if clipboard_text:
    print("Select the text box to paste to")
    time.sleep(delay)
    for char in clipboard_text:
        pyautogui.write(char)

        # hooman typing
        if random.random() < 0.002:  
            time.sleep(random.uniform(0.15, 0.35))
else:
    print("Clipboard is empty.")

