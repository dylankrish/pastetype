import pyperclip
import pyautogui
import time

delay = 3

clipboard_text = pyperclip.paste()

if clipboard_text:
    print("Select the text box to paste to")
    time.sleep(delay)
    pyautogui.write(clipboard_text)
else:
    print("Clipboard is empty.")

