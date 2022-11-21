import time
# import cv2
from time import sleep
import sys
import tkinter
from tkinter import * 
from tkinter import messagebox
line_1 = "  Va bo lai sau lung em tat ca"
line_2 = " nhung dieu ngot ngao nhat\n"
line_3 = "  ma doi tay anh nang niu bay lau\n"
line_4 = "  roi thoi gian se\n"
line_5 = "  dan em di qua nhung lo lang ma minh da\n"
h = "  I Love My Girl !"
for l1 in line_1:
    print(l1, end='')
    sys.stdout.flush()
    sleep(0.06)
for l2 in line_2:
    print(l2, end='')
    sys.stdout.flush()
    sleep(0.06)
sleep(0.4)
for l3 in line_3:
    print(l3, end='')
    sys.stdout.flush()
    sleep(0.06)
sleep(0.8)
for l4 in line_4:
    print(l4, end='')
    sys.stdout.flush()
    sleep(0.06)
for l5 in line_5:
    print(l5, end='')
    sys.stdout.flush()
    sleep(0.05)
sleep(0.1)
messagebox.showinfo("i <3 u", "i love my girl <3")