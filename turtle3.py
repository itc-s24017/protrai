# 「turtle3.py」という名前で保存しましょう
# カラフルな星を描く

from turtle import * 
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    forward(100)
    left(144)
     
done() 
