# s24017
# おみくじGUIで動かすプログラム
import tkinter as tk

root = tk.Tk()

root.geometry("300x300")
root.title("おみくじGUI")
import random
kuji= ["大吉","中吉","小吉"]
print(random.choice(kuji))
lbl=tk.Label(text=kuji("大吉","中吉","小吉"))
lbl.pack()

root.mainloop()
