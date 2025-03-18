import keyboard
from screen_capture import select_screen_region

def hotkey_listener(toggle_capture):
    keyboard.add_hotkey("ctrl+shift+s", select_screen_region)
    keyboard.add_hotkey("ctrl+shift+d", toggle_capture)
    keyboard.wait()