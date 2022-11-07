import tkinter as tk


window = tk.Tk(className="new GUIWindow")


label = tk.Label(text="_________Hello, world!________")
label.pack()
label.config(fg = "green", bg = "grey")

window.minsize(width=500, height=300)
window.mainloop()
# input("Press enter to continue...")