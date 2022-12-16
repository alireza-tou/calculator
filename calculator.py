from tkinter import *

root=Tk()
root.title("calculator")

number=StringVar(root,"")


asd=""

def adad(a):
    global asd
    asd =asd + a  
    number.set(asd)
    
def clean():
    global asd
    asd=""
    number.set("")

def equal():
    global asd
    number.set(str(eval(asd)))


entry=Entry(root,textvariable=number)

b1=Button(root,text="1",height=3,width=5,command=lambda:adad("1"))

b2=Button(root,text="2",height=3,width=5,command=lambda:adad("2"))

b3=Button(root,text="3",height=3,width=5,command=lambda:adad("3"))

b4=Button(root,text="4",height=3,width=5,command=lambda:adad("4"))

b5=Button(root,text="5",height=3,width=5,command=lambda:adad("5"))

b6=Button(root,text="6",height=3,width=5,command=lambda:adad("6"))

b7=Button(root,text="7",height=3,width=5,command=lambda:adad("7"))

b8=Button(root,text="8",height=3,width=5,command=lambda:adad("8"))

b9=Button(root,text="9",height=3,width=5,command=lambda:adad("9"))

b0=Button(root,text="0",height=3,width=5,command=lambda:adad("0"))

bplus=Button(root,text="+",height=3,width=5,command=lambda:adad("+"))

bneg=Button(root,text="-",height=3,width=5,command=lambda:adad("-"))

bzarb=Button(root,text="*",height=3,width=5,command=lambda:adad("*"))

btaghsim=Button(root,text="/",height=3,width=5,command=lambda:adad("/"))

bmosavi=Button(root,text="=",height=3,width=5,command=lambda:equal())

bclean=Button(root,text="clear",height=3,width=5,command=lambda : clean())





entry.grid(row=0,columnspan=4,sticky="n e w s",padx=3,pady=3)

b1.grid(row=1,column=0,padx=3,pady=3)

b2.grid(row=1,column=1,padx=3,pady=3)

b3.grid(row=1,column=2,padx=3,pady=3)

b4.grid(row=2,column=0,padx=3,pady=3)

b5.grid(row=2,column=1,padx=3,pady=3)

b6.grid(row=2,column=2,padx=3,pady=3)

b7.grid(row=3,column=0,padx=3,pady=3)

b8.grid(row=3,column=1,padx=3,pady=3)

b9.grid(row=3,column=2,padx=3,pady=3)

b0.grid(row=4,column=0,padx=3,pady=3)

bplus.grid(row=1,column=3,padx=3,pady=3)

bneg.grid(row=2,column=3,padx=3,pady=3)

bzarb.grid(row=3,column=3,padx=3,pady=3)

btaghsim.grid(row=4,column=3,padx=3,pady=3)

bmosavi.grid(row=4,column=2,padx=3,pady=3)

bclean.grid(row=4,column=1,padx=3,pady=3)
 




root.mainloop()