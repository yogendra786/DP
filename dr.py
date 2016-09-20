import Tkinter
from  Tkinter import *
import tkMessageBox
#from gtts import gTTS
import os
import subprocess
import thread
#from autocorrect import spell
from ScrolledText import ScrolledText
#from urllib2
#import requests


top = Tkinter.Tk()

total_label_text = StringVar()
global text1
text1=StringVar()
text1=""
global k
k=StringVar()
k=""
global q
q=IntVar()
q=0
global a
a=IntVar()
a=0
global s
#s=StringVar()
s=""
global sa
sa=StringVar()
sa=" "
global r
r=StringVar()
r=""
global n
n=StringVar()
global m
m=IntVar()
m=1
global i
i=IntVar()
i=0
global j
j=IntVar()
j=0
global g
g=IntVar()
g=0
global h
h=IntVar()
h=0
global row1
row1=IntVar()
row1=0
global word
word=StringVar()
global flag
flag=IntVar()
global flag1
flag1=IntVar()
flag1=0
global flag3
flag3=IntVar()
flag3=0
def space1():
    global m
    global k
    global s
    global r
    global n
    n=""
    r=""
    #r=E1.get("1.0",END)
    r=s
    #print r
    """f1=m.split()  
    n=spell(f1[-1])
    del f1[-1]
    if len(f1)!=0:
        s=' '.join(f1)
        r=s+" "+n
    else :
        r=n
    #r=m"""
    r=r+" "
    #print r
    s=r
    #m=m+" "
    #k=r
    E1.delete("1.0",END)
    E1.insert(INSERT,r)

def backspace1():
   """global text1
   text1=E1.get("1.0",END)[:-1]
   if text1 == "":
        text1="0"
   E1.current=text1"""
   global s
   s=s[:-1]
   E1.delete("1.0",END)
   E1.insert(INSERT,s)

def clear2():
    global k
    global m
    global s
    m=1
    k=""
    s=""
    E1.delete("1.0",END)

def say():
    #import urllib
    global m
    global k
    global sa
    sa=E1.get("1.0",END)
    #sa=urllib.quote("'"+sa+"'")
    sa="'%s'"%sa
    #print sa 
    #tts = gTTS(text=sa,lang='en')
    #tts.save("hello.mp3")
    #os.system("mpg321 hello.mp3")
    subprocess.call('espeak -ven+f4 -s180 '+sa,shell=True)
       

def hello1(k):  
    E1.insert(INSERT,k)


def alarm1():
    global q
    global a
    os.system("mplayer -endpos 5 siren.mp3")
    q=q+1
    

def helloCallBack1(word):
            global flag3
            if flag3==0:
            	clear2()
                flag3=1
                
            global k
            global s
            global sa
            sa=word
            #tts = gTTS(text=word,lang='en')
            #tts.save("hello1.mp3")
            #os.system("mpg321 hello1.mp3")
            subprocess.call('espeak -ven+f4 -s180 '+sa,shell=True)               
            s=s+sa
            k=word
            hello1(k)
"""def take():
    f = open('text.txt','r')
    line = f.readline()
    la1,la2,la3 = line.split()
    l.config(text=la1)
    l2.config(text=la2)
    l3.config(text=la3)
    f.close()
"""
def save():
    text = E1.get("1.0",END)
    k=text.split()

    with open(k[-1], "a") as f:
        del k[-1]
        text=' '.join(k)
        f.write(text)

#photo=PhotoImage(file="img.jpg")
top.option_add("*Font", "Helvetica 10 ")
top.config(background="gold")
top.option_add("*Background", "gold")

L1 = Label(top, text="EYE BLINK WRITER",fg="black")
L1.grid(columnspan=20)
E1 = ScrolledText(top,relief="solid",bg="white",height=9, bd =4,width=110)
E1.grid(columnspan=20)

E1.insert(INSERT,"YOUR TEXT APPEARS HERE...")

r1=Tkinter.Button(top,text="1",width="1",command=lambda: ROW1())
r1.grid(row=4,column=0)
alarm=Tkinter.Button(top,text="ALARM",width="24",bg="RED",command= lambda:alarm1())
alarm.grid(row=4,column=1,columnspan=2)
water=Tkinter.Button(top,text="WATER",width="24",command= lambda:helloCallBack1("WATER"))
water.grid(row=4,column=3,columnspan=2)
food=Tkinter.Button(top,text="FOOD",width="24",command= lambda:helloCallBack1("FOOD"))
food.grid(row=4,column=5,columnspan=2)
washroom=Tkinter.Button(top,text="WASHROOM",width="24",command= lambda:helloCallBack1("WASHROOM"))
washroom.grid(row=4,column=7,columnspan=2)

r2=Tkinter.Button(top,text="2",width="1")
r2.grid(row=5,column=0)
read=Tkinter.Button(top,text="SPEAK",width="24",command= lambda:say())
read.grid(row=5,column=1,columnspan=2)
space=Tkinter.Button(top,text="SPACE",width="24",relief=RAISED,command= lambda:space1())
space.grid(row=5,column=3,columnspan=2)
clear1=Tkinter.Button(top,text="CLEAR",width="24",command= lambda:clear2())
clear1.grid(row=5,column=5,columnspan=2)
backspace=Tkinter.Button(top,text="BACKSPACE",width="24",command= lambda:backspace1())
backspace.grid(row=5,column=7,columnspan=2)

r3=Tkinter.Button(top,text="3",width="1")
r3.grid(row=6,column=0)
E=Tkinter.Button(top,text="E",width="10",command= lambda:helloCallBack1("E"))
E.grid(row=6,column=1)
A=Tkinter.Button(top,text="A",width="10",command= lambda:helloCallBack1("A"))
A.grid(row=6,column=2)
S=Tkinter.Button(top,text="S",width="10",command= lambda:helloCallBack1("S"))
S.grid(row=6,column=3)
F=Tkinter.Button(top,text="F",width="10",command= lambda:helloCallBack1("F"))
F.grid(row=6,column=4)
Q=Tkinter.Button(top,text="Q",width="10",command= lambda:helloCallBack1("Q"))
Q.grid(row=6,column=5)
C=Tkinter.Button(top,text="C",width="10",command= lambda:helloCallBack1("C"))
C.grid(row=6,column=6)
J=Tkinter.Button(top,text="J",width="10",command= lambda:helloCallBack1("J"))
J.grid(row=6,column=7)
M=Tkinter.Button(top,text="M",width="10",command= lambda:helloCallBack1("M"))
M.grid(row=6,column=8)

r4=Tkinter.Button(top,text="4",width="1")
r4.grid(row=7,column=0)
T=Tkinter.Button(top,text="T",width="10",command= lambda:helloCallBack1("T"))
T.grid(row=7,column=1)
I=Tkinter.Button(top,text="I",width="10",command= lambda:helloCallBack1("I"))
I.grid(row=7,column=2)
D=Tkinter.Button(top,text="D",width="10",command= lambda:helloCallBack1("D"))
D.grid(row=7,column=3)
G=Tkinter.Button(top,text="G",width="10",command= lambda:helloCallBack1("G"))
G.grid(row=7,column=4)
K=Tkinter.Button(top,text="K",width="10",command= lambda:helloCallBack1("K"))
K.grid(row=7,column=5)
W=Tkinter.Button(top,text="W",width="10",command= lambda:helloCallBack1("W"))
W.grid(row=7,column=6)
Z=Tkinter.Button(top,text="Z",width="10",command= lambda:helloCallBack1("Z"))
Z.grid(row=7,column=7)
V=Tkinter.Button(top,text="V",width="10",command= lambda:helloCallBack1("V"))
V.grid(row=7,column=8)

r5=Tkinter.Button(top,text="5",width="1")
r5.grid(row=8,column=0)
N=Tkinter.Button(top,text="N",width="10",command= lambda:helloCallBack1("N"))
N.grid(row=8,column=1)

O=Tkinter.Button(top,text="O",width="10",command= lambda:helloCallBack1("O"))
O.grid(row=8,column=2)
L=Tkinter.Button(top,text="L",width="10",command= lambda:helloCallBack1("L"))
L.grid(row=8,column=3)
P=Tkinter.Button(top,text="P",width="10",command= lambda:helloCallBack1("P"))
P.grid(row=8,column=4)
R=Tkinter.Button(top,text="R",width="10",command= lambda:helloCallBack1("R"))
R.grid(row=8,column=5)
U=Tkinter.Button(top,text="U",width="10",command= lambda:helloCallBack1("U"))
U.grid(row=8,column=6)
Y=Tkinter.Button(top,text="Y",width="10",command= lambda:helloCallBack1("Y"))
Y.grid(row=8,column=7)
X=Tkinter.Button(top,text="X",width="10",command= lambda:helloCallBack1("X"))
X.grid(row=8,column=8)

r6=Tkinter.Button(top,text="6",width="1")
r6.grid(row=9,column=0)
H=Tkinter.Button(top,text="H",width="10",command= lambda:helloCallBack1("H"))
H.grid(row=9,column=1)
flstp=Tkinter.Button(top,text=".",width="10",command= lambda:helloCallBack1("."))
flstp.grid(row=9,column=2)
que=Tkinter.Button(top,text="?",width="10",command= lambda:helloCallBack1("?"))
que.grid(row=9,column=3)
d0=Tkinter.Button(top,text="0",width="10",command= lambda:helloCallBack1("0"))
d0.grid(row=9,column=4)
d1=Tkinter.Button(top,text="1",width="10",command= lambda:helloCallBack1("1"))
d1.grid(row=9,column=5)
d2=Tkinter.Button(top,text="2",width="10",command= lambda:helloCallBack1("2"))
d2.grid(row=9,column=6)
d3=Tkinter.Button(top,text="3",width="10",command= lambda:helloCallBack1("3"))
d3.grid(row=9,column=7)
d4=Tkinter.Button(top,text="4",width="10",command= lambda:helloCallBack1("4"))
d4.grid(row=9,column=8)

r7=Tkinter.Button(top,text="7",width="1")
r7.grid(row=10,column=0)
d5=Tkinter.Button(top,text="5",width="10",command= lambda:helloCallBack1("5"))
d5.grid(row=10,column=1)
d6=Tkinter.Button(top,text="6",width="10",command= lambda:helloCallBack1("6"))
d6.grid(row=10,column=2)
d7=Tkinter.Button(top,text="7",width="10",command= lambda:helloCallBack1("7"))
d7.grid(row=10,column=3)
d8=Tkinter.Button(top,text="8",width="10",command= lambda:helloCallBack1("8"))
d8.grid(row=10,column=4)
d9=Tkinter.Button(top,text="9",width="10",command= lambda:helloCallBack1("9"))
d9.grid(row=10,column=5)
song3=Tkinter.Button(top,text="SAVE",width="10",command= lambda:save())
song3.grid(row=10,column=6)
song4=Tkinter.Button(top,text="READ",width="10",command= lambda:myfileOpen())
song4.grid(row=10,column=7)
song5=Tkinter.Button(top,text="QUIT",width="10",command= lambda:Shut_Down())

song5.grid(row=10,column=8)

def Shut_Down():
    #os.system("sudo poweroff")
    print "Yogendra"
lo=True;
def stop(a):
    global lo
    lo=False
    

"""f = open("hars.txt", 'r')
while(1):
    # line = f.readline()
    if line.find("1") != -1:
        top.after(6000, stop,0)
with open("hars.txt") as f:
l=0
while 1 
	c=f.read(l)
	
	if c=='1':
	top.after(0, stop,0)

	


print c
if c=='1':
	top.after(0, stop,0)"""


def stopw():
	i=flag
	if flag1==0:
		stop(a)
		return
	if i==2:

		 stop2(a)
	if i==3: 
		 stop3(a)
	if i==4: 
		 stop4(a)
	if i==5: 
		 stop5(a)
	if i==6:
		 stop6(a)
	if i==0: 
		 stop7(a)
	if i==1: 
		 stop1(a)




# E2.bind('<i>', stopw)
"""E10=Entry()
E10.grid(columnspan=10)
E10.bind('<i>', stopw)"""


def blink(i, j):
    global lo
    global flag
    global flag1
    if lo :
        
        
        top.after(2000, blink, (i+1) % 7, j+1)
    else:
        flag=i
        flag1=1
        lo=True
        white1(i);
        if i==2:
            top.after(2000, blink2, 0, 0)
        if i==3:
            top.after(2000,blink3,0,0)
        if i==4:
            top.after(2000,blink4,0,0)
        if i==5:
            top.after(2000,blink5,0,0)
        if i==6:
            top.after(2000,blink6,0,0)
        if i==0:
            top.after(2000,blink7,0,0)

        if i==1:
            top.after(2000, blink1, 0, 0)
        
        print i;
        return
    if i == 0:
        r1.config(fg="red",bg="black")
        if j > 0:
            r7.config(fg="black",bg=top["bg"])
    elif i == 1:
        r1.config(fg="black",bg=top["bg"])
        r2.config(fg="red",bg="black")
    elif i == 2:
        r2.config(fg="black",bg=top["bg"])
        r3.config(fg="red",bg="black")
    elif i == 3:
        r3.config(fg="black",bg=top["bg"])
        r4.config(fg="red",bg="black")
    elif i == 4:
        r4.config(fg="black",bg=top["bg"])
        r5.config(fg="red",bg="black")
    elif i == 5:
        r5.config(fg="black",bg=top["bg"])
        r6.config(fg="red",bg="black")
    elif i == 6:
        r6.config(fg="black",bg=top["bg"])
        r7.config(fg="red",bg="black")
    



def white1(i):
    if i==1:
        r1.config(fg="black",bg=top["bg"]) 
    if i==2:
        r2.config(fg="black",bg=top["bg"]) 
    if i==3:
        r3.config(fg="black",bg=top["bg"]) 
    if i==4:
        r4.config(fg="black",bg=top["bg"]) 
    if i==5:
        r5.config(fg="black",bg=top["bg"]) 
    if i==6:
        r6.config(fg="black",bg=top["bg"]) 
    if i==0:
        r7.config(fg="black",bg=top["bg"]) 








top.after(2000, blink, 0, 0)



lo1=True
def stop1(a):
    global lo1
    lo1 = False


def blink1(i1, j1):
    global word
    global flag1
    global lo1
    if lo1 :
        top.after(2000, blink1, (i1+1) % 4, j1+1)
    else:
    	flag1=0
        white2(i1)
        lo1=True
        call(i1,word)
        top.after(2000, blink, 0, 0)
        return
    if i1 == 0:
        alarm.config(fg="red",bg="black")
        
        word="alarm"
        if j1 > 0:
            washroom.config(fg="black",bg=top["bg"])
            word="alarm"
    elif i1 == 1:
        alarm.config(fg="black",bg="red")
        water.config(fg="red",bg="black")
        word="WATER"
    elif i1 == 2:
        water.config(fg="black",bg=top["bg"])
        food.config(fg="red",bg="black")
        word="FOOD"
    elif i1 == 3:
        food.config(fg="black",bg=top["bg"])
        washroom.config(fg="red",bg="black")
        word="WASHROOM"


def white2(i1):
    if i1==1:
        alarm.config(fg="black",bg="red") 
    if i1==2:
        water.config(fg="black",bg=top["bg"]) 
    if i1==3:
        food.config(fg="black",bg=top["bg"]) 
    if i1==0:
        washroom.config(fg="black",bg=top["bg"]) 
   

def call(i1,word):
    #print i1
    if i1==1:
        alarm1()
    else:   
        helloCallBack1(word)
    










lo2=True
def stop2(a):
    global lo2
    lo2 = False


def blink2(i2, j2):
    global word2
    global lo2
    global flag1
    if lo2 :
        top.after(2000, blink2, (i2+1) % 4, j2+1)
    else:
    	flag1=0
        white3(i2)
        lo2=True
        call2(i2)
        top.after(2000, blink, 0, 0)
        return
    if i2 == 0:
        read.config(fg="red",bg="black")
        
        
        if j2 > 0:
            backspace.config(fg="black",bg=top["bg"])
            
    elif i2 == 1:
        read.config(fg="black",bg=top["bg"])
        space.config(fg="red",bg="black")
        
    elif i2 == 2:
        space.config(fg="black",bg=top["bg"])
        clear1.config(fg="red",bg="black")
        
    elif i2 == 3:
        clear1.config(fg="black",bg=top["bg"])
        backspace.config(fg="red",bg="black")
        


def white3(i2):
    if i2==1:
        read.config(fg="black",bg=top["bg"]) 
    if i2==2:
        space.config(fg="black",bg=top["bg"]) 
    if i2==3:
        clear1.config(fg="black",bg=top["bg"]) 
    if i2==0:
        backspace.config(fg="black",bg=top["bg"]) 
   

def call2(i2):
    if i2==1:
        say()  
    if i2==2:
        space1()    
    if i2==3:
        clear2()    
    if i2==0:
        backspace1() 
    



lo3=True
def stop3(a):
    global lo3
    lo3 = False


def blink3(i3, j3):
    global word
    global lo3
    global flag1
    if lo3 :
        top.after(2000, blink3, (i3+1) % 8, j3+1)
    else:
    	flag1=0
        white4(i3)
        lo3=True
        call3(word)
        top.after(2000, blink, 0, 0)
        return
    if i3 == 0:
        E.config(fg="red",bg="black")
        
        word="E"
        if j3 > 0:
            M.config(fg="black",bg=top["bg"])
            word="E"
    elif i3 == 1:
        E.config(fg="black",bg=top["bg"])
        A.config(fg="red",bg="black")
        word="A"
    elif i3 == 2:
        A.config(fg="black",bg=top["bg"])
        S.config(fg="red",bg="black")
        word="S"
    elif i3 == 3:
        S.config(fg="black",bg=top["bg"])
        F.config(fg="red",bg="black")
        word="F"
    elif i3 == 4:
        F.config(fg="black",bg=top["bg"])
        Q.config(fg="red",bg="black")
        word="Q"
    elif i3 == 5:
        Q.config(fg="black",bg=top["bg"])
        C.config(fg="red",bg="black")
        word="C"
    elif i3 == 6:
        C.config(fg="black",bg=top["bg"])
        J.config(fg="red",bg="black")
        word="J"
    elif i3 == 7:
        J.config(fg="black",bg=top["bg"])
        M.config(fg="red",bg="black")
        word="M"

def white4(i3):
    if i3==1:
        E.config(fg="black",bg=top["bg"]) 
    if i3==2:
        A.config(fg="black",bg=top["bg"]) 
    if i3==3:
        S.config(fg="black",bg=top["bg"]) 
    if i3==0:
        M.config(fg="black",bg=top["bg"]) 
    if i3==4:
        F.config(fg="black",bg=top["bg"]) 
    if i3==5:
        Q.config(fg="black",bg=top["bg"]) 
    if i3==6:
        C.config(fg="black",bg=top["bg"])
    if i3==7:
        J.config(fg="black",bg=top["bg"]) 
     
    
def call3(word):    
        helloCallBack1(word)


lo4=True
def stop4(a):
    global lo4
    lo4 = False


def blink4(i4, j4):
    global word
    global lo4
    global flag1
    if lo4 :
        top.after(2000, blink4, (i4+1) % 8, j4+1)
    else:
    	flag1=0
        white5(i4)
        lo4=True
        call4(word)
        top.after(2000, blink, 0, 0)
        return
    if i4 == 0:
        T.config(fg="red",bg="black")
        
        word="T"
        if j4 > 0:
            V.config(fg="black",bg=top["bg"])
            word="T"
    elif i4 == 1:
        T.config(fg="black",bg=top["bg"])
        I.config(fg="red",bg="black")
        word="I"
    elif i4 == 2:
        I.config(fg="black",bg=top["bg"])
        D.config(fg="red",bg="black")
        word="D"
    elif i4 == 3:
        D.config(fg="black",bg=top["bg"])
        G.config(fg="red",bg="black")
        word="G"
    elif i4 == 4:
        G.config(fg="black",bg=top["bg"])
        K.config(fg="red",bg="black")
        word="K"
    elif i4 == 5:
        K.config(fg="black",bg=top["bg"])
        W.config(fg="red",bg="black")
        word="W"
    elif i4 == 6:
        W.config(fg="black",bg=top["bg"])
        Z.config(fg="red",bg="black")
        word="Z"
    elif i4 == 7:
        Z.config(fg="black",bg=top["bg"])
        V.config(fg="red",bg="black")
        word="V"

def white5(i4):
    if i4==1:
        T.config(fg="black",bg=top["bg"]) 
    if i4==2:
        I.config(fg="black",bg=top["bg"]) 
    if i4==3:
        D.config(fg="black",bg=top["bg"]) 
    if i4==0:
        V.config(fg="black",bg=top["bg"]) 
    if i4==4:
        G.config(fg="black",bg=top["bg"]) 
    if i4==5:
        K.config(fg="black",bg=top["bg"]) 
    if i4==6:
        W.config(fg="black",bg=top["bg"])
    if i4==7:
        Z.config(fg="black",bg=top["bg"]) 
     
    
def call4(word):    
        helloCallBack1(word)


lo5=True
def stop5(a):
    global lo5
    lo5 = False


def blink5(i5, j5):
    global word
    global lo5
    global flag1
    if lo5 :
        top.after(2000, blink5, (i5+1) % 8, j5+1)
    else:
    	flag1=0
        white6(i5)
        lo5=True
        call5(word)
        top.after(2000, blink, 0, 0)
        return
    if i5 == 0:
        N.config(fg="red",bg="black")
        
        word="N"
        if j5 > 0:
            X.config(fg="black",bg=top["bg"])
            word="N"
    elif i5 == 1:
        N.config(fg="black",bg=top["bg"])
        O.config(fg="red",bg="black")
        word="O"
    elif i5 == 2:
        O.config(fg="black",bg=top["bg"])
        L.config(fg="red",bg="black")
        word="L"
    elif i5 == 3:
        L.config(fg="black",bg=top["bg"])
        P.config(fg="red",bg="black")
        word="P"
    elif i5 == 4:
        P.config(fg="black",bg=top["bg"])
        R.config(fg="red",bg="black")
        word="R"
    elif i5 == 5:
        R.config(fg="black",bg=top["bg"])
        U.config(fg="red",bg="black")
        word="U"
    elif i5 == 6:
        U.config(fg="black",bg=top["bg"])
        Y.config(fg="red",bg="black")
        word="Y"
    elif i5 == 7:
        Y.config(fg="black",bg=top["bg"])
        X.config(fg="red",bg="black")
        word="X"

def white6(i5):
    if i5==1:
        N.config(fg="black",bg=top["bg"]) 
    if i5==2:
        O.config(fg="black",bg=top["bg"]) 
    if i5==3:
        L.config(fg="black",bg=top["bg"]) 
    if i5==0:
        X.config(fg="black",bg=top["bg"]) 
    if i5==4:
        P.config(fg="black",bg=top["bg"]) 
    if i5==5:
        R.config(fg="black",bg=top["bg"]) 
    if i5==6:
        U.config(fg="black",bg=top["bg"])
    if i5==7:
        Y.config(fg="black",bg=top["bg"]) 
     
    
def call5(word):    
        helloCallBack1(word)



lo6=True
def stop6(a):
    global lo6
    lo6 = False


def blink6(i6, j6):
    global word
    global lo6
    global flag1
    if lo6 :
        top.after(2000, blink6, (i6+1) % 8, j6+1)
    else:
    	flag1=0
        white7(i6)
        lo6=True
        call6(word)
        top.after(2000, blink, 0, 0)
        return
    if i6 == 0:
        H.config(fg="red",bg="black")
        
        word="H"
        if j6 > 0:
            d4.config(fg="black",bg=top["bg"])
            word="H"
    elif i6 == 1:
        H.config(fg="black",bg=top["bg"])
        flstp.config(fg="red",bg="black")
        word="."
    elif i6 == 2:
        flstp.config(fg="black",bg=top["bg"])
        que.config(fg="red",bg="black")
        word="?"
    elif i6 == 3:
        que.config(fg="black",bg=top["bg"])
        d0.config(fg="red",bg="black")
        word="0"
    elif i6 == 4:
        d0.config(fg="black",bg=top["bg"])
        d1.config(fg="red",bg="black")
        word="1"
    elif i6 == 5:
        d1.config(fg="black",bg=top["bg"])
        d2.config(fg="red",bg="black")
        word="2"
    elif i6 == 6:
        d2.config(fg="black",bg=top["bg"])
        d3.config(fg="red",bg="black")
        word="3"
    elif i6 == 7:
        d3.config(fg="black",bg=top["bg"])
        d4.config(fg="red",bg="black")
        word="4"

def white7(i6):
    if i6==1:
        H.config(fg="black",bg=top["bg"]) 
    if i6==2:
        flstp.config(fg="black",bg=top["bg"]) 
    if i6==3:
        que.config(fg="black",bg=top["bg"]) 
    if i6==0:
        d4.config(fg="black",bg=top["bg"]) 
    if i6==4:
        d0.config(fg="black",bg=top["bg"]) 
    if i6==5:
        d1.config(fg="black",bg=top["bg"]) 
    if i6==6:
        d2.config(fg="black",bg=top["bg"])
    if i6==7:
        d3.config(fg="black",bg=top["bg"]) 
     
    
def call6(word):    
        helloCallBack1(word)


lo7=True
def stop7(a):
    global lo7
    lo7 = False


def blink7(i7, j7):
    global word
    global lo7
    global flag1
    if lo7 :
        top.after(2000, blink7, (i7+1) % 8, j7+1)
    else:
    	flag1=0
        white8(i7)
        lo7=True
        call7(i7,word)
        top.after(2000, blink, 0, 0)
        return
    if i7 == 0:
        d5.config(fg="red",bg="black")
        
        word="5"
        if j7 > 0:
            song5.config(fg="black",bg=top["bg"])
            word="5"
    elif i7 == 1:
        d5.config(fg="black",bg=top["bg"])
        d6.config(fg="red",bg="black")
        word="6"
    elif i7 == 2:
        d6.config(fg="black",bg=top["bg"])
        d7.config(fg="red",bg="black")
        word="7"
    elif i7 == 3:
        d7.config(fg="black",bg=top["bg"])
        d8.config(fg="red",bg="black")
        word="8"
    elif i7 == 4:
        d8.config(fg="black",bg=top["bg"])
        d9.config(fg="red",bg="black")
        word="9"
    elif i7 == 5:
        d9.config(fg="black",bg=top["bg"])
        song3.config(fg="red",bg="black")
        word="2"
    elif i7 == 6:
        song3.config(fg="black",bg=top["bg"])
        song4.config(fg="red",bg="black")
        word="3"
    elif i7 == 7:
        song4.config(fg="black",bg=top["bg"])
        song5.config(fg="red",bg="black")
        word="4"

def white8(i7):
    if i7==1:
        d5.config(fg="black",bg=top["bg"]) 
    if i7==2:
        d6.config(fg="black",bg=top["bg"]) 
    if i7==3:
        d7.config(fg="black",bg=top["bg"]) 
    if i7==0:
        song5.config(fg="black",bg=top["bg"]) 
    if i7==4:
        d8.config(fg="black",bg=top["bg"]) 
    if i7==5:
        d9.config(fg="black",bg=top["bg"]) 
    if i7==6:
        song3.config(fg="black",bg=top["bg"])
    if i7==7:
        song4.config(fg="black",bg=top["bg"]) 
     
    
def call7(i7,word):
        print i7
        if i7==7:
            myfileOpen()
            return
        if i7==6:
            save()
            return
        if i7==0:
            Shut_Down()
            return   
        helloCallBack1(word)


def myfileOpen():
    global s
    s=""
    text = E1.get("1.0",END)
    k=text.split()
    if(os.path.isfile(k[-1])):
        myfile=open(k[-1],"r")
        del k[-1]
        if len(k)!=0:
            s=' '.join(k)
            s=s+" "
        E1.delete("1.0",END)
        E1.insert(INSERT,s)
        loadedfile = myfile.read()
        myfile.close()
        E1.insert("end", loadedfile)
    else:
        E1.insert("end"," File doesn't exists")
#l=1

"""def aaz():
    print "ff"
    mk=0
    def harshitf():
        inp=raw_input()

        print inp
        if inp=="1":
            stopw()
        mk=mk+1
        if mk==2000000:
            return

        top.after(100,harshitf)    
    top.after(2000,harshitf)



thread.start_new_thread( aaz, ())"""





"""f = open('1.dat', 'r')
def try1():
    ch=f.read(1)
    #if not ch: break
    print ch
    if ch=="1":
        print "BLINK"
        stopw()
    top.after(150,try1)
top.after(10000,try1)"""

#f= open('1.txt','r')
#while True:
"""for ch in iter(lambda: f.read(1), ''):
    #print ch    
	if ch=="1":
        #print ch
		stopw(a)"""


"""print("Here")"""




"""from time import sleep
import thread"""



#def mainloop():
 #   print "x"
  #  top.mainloop()

#thread.start_new_thread(mainloop, ())

#raw_input()
# print "somethin"

# inp = open('test')
while True:
    
    inp=raw_input()
    if inp=="1":
        stopw()


top.mainloop()
