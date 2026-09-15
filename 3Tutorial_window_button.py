# How to make button inside a window with Tkinter
import tkinter as tk
window = tk.Tk()
window.geometry("500x300")
window.title("ButtonTest")

# Button command
button = tk.Button(window, text="click👆")

# Packing button
button.pack()

# MainLoop
window.mainloop()