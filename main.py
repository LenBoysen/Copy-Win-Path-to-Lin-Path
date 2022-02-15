import keyboard
import win32clipboard
import time
import re



regex = r"(.)"

test_str = ""

subst = "\g<1>,"

result = ""

def copy():
    global test_str
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    input = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    test_str = input
    print(test_str )

def paste():
    global test_str
    global result
    result = re.sub(r"^Z:", "/media/usb-drive", re.sub(r"\\", "/", test_str, 0, re.MULTILINE), 0, re.MULTILINE).replace('[', '\[').replace(']', '\]').replace(' ', '\ ').replace('(', '\(').replace(')', '\)')
    keyboard.press_and_release('backspace')
    keyboard.write(result)


keyboard.add_hotkey('ctrl+c', copy)
keyboard.add_hotkey('ü', paste)
keyboard.add_hotkey('esc', quit)

keyboard.wait()


