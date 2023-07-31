import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

def run():
    os.system('python main.py --model train.onnx --classes a_kinetics.txt --input dataset1.mp4')

btn = Button(window, text="Video1", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)

def run1():
    os.system('python main.py --model train.onnx --classes a_kinetics.txt --input v.mp4')

btn1 = Button(window, text="Video2", bg="red", fg="white",command=run1)
btn1.grid(column=20, row=0)

def run2():
    os.system('python main.py --model train.onnx --classes a_kinetics.txt --input sk.avi')

btn2 = Button(window, text="Video3", bg="blue", fg="white",command=run2)
btn2.grid(column=30, row=0)


window.mainloop()
