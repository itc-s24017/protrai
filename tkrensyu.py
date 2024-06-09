# GUIで動くアプリを作ってみるよ

import tkinter as tk # まずはこの行を書く必要があるよ

root = tk.Tk() #始めのおまじない
 
root.geometry("500x400") # ウインドウのサイズを決める
root.title("ハローアプリ") # ウインドウのタイトルを決める
lbl = tk.Label(text="こんにちは世界") # いつもの
lbl.pack() # lblを配置させる必要があるよ



root.mainloop() #終わりのおまじない
