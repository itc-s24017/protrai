# app2.py バージョン２

import tkinter as tk # tkinterをimportしてtkと略して使う

def dispLabel():
    lbl.config(text="こんにちは")
root = tk.Tk()
 # 画面の大きさを決める
root.geometry("300x200")

# ラベルを作る
lbl = tk.Label(text="LABEL", font=("Helvetion", 20))
# ボタンを作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetion", 20))

# 画面にラベルを配置する
lbl.pack()
# 画面にボタンを配置する
btn.pack()

lbl2 = tk.Label(text="ラベル２", font=("Helvetion", 20)).pack()

btn2 = tk.Button(text="何もしないボタン", command=dispLabel, font=("Helvetion", 20)).pack()

# 作ったウインドを表示する
tk.mainloop()
