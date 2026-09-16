# First, we making default window with Tkinter
# If you dont know how see my other project how_to_window.py)
import tkinter as tk
window = tk.Tk()
window.title("text")
window.geometry("500x400")
# Now create text
label = tk.Label(window, text="Hello!")

# Put the label inside the window
label.pack()

# MainLoop 
window.mainloop()