import cv2
import matplotlib
import numpy
import tkinter

root = tkinter.Tk()
#設定
root.option_add("*font", ["MS Pゴシック", 22])

#ウィンドウ設定
root.title("KMDさんぐるぐる")
root.geometry("640x480+100+100")

text1 = tkinter.Label(text="ぐるぐるさせたい", bg="white")
text1.place(x=10, y=10)

# メインループ
root.mainloop()

