# s24017　entry_kadai.py
# エントリーウェジットで受け付けた金額を税込み(10%)価格として出力

import tkinter as tk

def dispLabel():
    #
    a = entry.get()
    print(f"aは{type(a)}")
    lbl.config(text=f"{a}さんこんにちは")


root = tk.Tk()
root.title("エントリーウェジット")
root.geometry("400x200")

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()


tk.mainloop()
