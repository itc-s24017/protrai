# s24017
#実行が確認出来たら時間を表示する「時計アプリ」を作ってみよう
#時計アプリはモジュール名「time_kadai.py」で作成します

import datetime
import tkinter as tk # GUIでアプリを作ることができるモジュール

# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日　%H時%M分%S秒") # 日本語表示
    #
    lbl.config(text=current_time) # 日本語表示した時間を呼び出す
    root.after(1000, update_time) # 自分をもう一回呼び出す

#Tkinterのウインドを作成
root = tk.Tk() # 始めのおまじない

root.title("時計アプリ") # タイトル
#
lbl = tk.Label() # 
lbl.config(text="", font=("Helvetica" , 20))
lbl.pack()

# 関数の呼び出し
update_time()

root.mainloop() # 終わりのおまじない
