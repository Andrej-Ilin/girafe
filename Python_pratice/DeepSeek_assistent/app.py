import tkinter as tk
from tkinter import scrolledtext
import threading
from screen_capture import capture_screen, region
from text_processing import extract_text
from deepseek_api import ask_deepseek
from tts import speak
from hotkeys import hotkey_listener

capture_enabled = False

def toggle_capture():
    global capture_enabled
    capture_enabled = not capture_enabled
    status = "Включен" if capture_enabled else "Выключен"
    chat_window.insert(tk.END, f"\n[INFO] Захват экрана: {status}\n", "info")

def process_text():
    global capture_enabled
    if capture_enabled:
        screen_img = capture_screen(region)
        text = extract_text(screen_img)
        if text:
            chat_window.insert(tk.END, f"\nВы: {text}\n", "user")
            response = ask_deepseek(text)
            chat_window.insert(tk.END, f"DeepSeek-R1: {response}\n", "bot")
            threading.Thread(target=speak, args=(response,), daemon=True).start()
    root.after(5000, process_text)

root = tk.Tk()
root.title("AI Assistant (DeepSeek-R1)")
root.geometry("600x400")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

chat_window.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="green", font=("Arial", 12))
chat_window.tag_configure("info", foreground="orange", font=("Arial", 10, "italic"))

threading.Thread(target=hotkey_listener, args=(toggle_capture,), daemon=True).start()
process_text()

root.mainloop()