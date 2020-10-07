from tkinter import *
import time
savan = Tk()
savan.geometry("1000x500")
savan.resizable(0,0)
savan.title("Loading Animation By -Savan Vaghela")
savan.configure(bg = "yellow")

bb = IntVar()
aa = 0

global li1
li1 = [".     " , ". .  " , ". . ."]

global li2
li2 = ["  . ." , "    ." , "     "]

def sav() :
     global aa , bb
     for i in range(3) :
          time.sleep(0.1)
          a.set(li1[i])
          l.update()
     aa += 0.3
     if aa < bb.get() - bb.get() / 10 :
          saav()
     else :
          bb.set(0)


def saav() :
     global aa , bb
     for i in range(3) :
          time.sleep(0.1)
          a.set(li2[i])
          l.update()
     aa += 0.3
     if aa < bb.get() - bb.get() / 10 :
          sav()
     else :
          bb.set(0)

def kav() :
     if bb.get() > 0 :
          saav()



a = StringVar()
a.set(". . .")

l4 = Label(text = "How Many Seconds Would You Like To Show Loading Animation :" , bg = "lightgrey").place(x = 100 , y = 0)
e = Entry(savan ,relief = FLAT ,bg = "light grey" , textvariable = bb).place(x = 675 , y = 0 , height = 34)

l = Label(textvariable = a , font = "lucida 70 " , bg = "yellow", fg = "blue")
l.place( x = 430 , y = 140)

b = Button(text = "start" , fg = "blue" , bg = "grey" , font = "comicsansms 18 bold" , command = kav)
b.pack(side = "bottom" , fill = X)

savan.mainloop()
