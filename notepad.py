import tkinter as tkt 
import tkinter.messagebox as tmg
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os as o
from tkinter import *
sample=tkt.Tk()

sample.wm_iconbitmap("tkinter\\Notepad_23093.ico")

sample.geometry("600x300")
sample.maxsize(1500,750)

sample.title("Untitled - Notepad")

file=None

def newfile():
    sample.title("Untitled - Notepad")
    text.delete(1.0,END)

def new_window():
    pample=tkt.Tk()
    pample.wm_iconbitmap("notepad_23093.ico")
    pample.geometry("600x300")
    pample.title("Untitled - Notepad")
    pample.mainloop()

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if(file==""):
        file=None
    else:
        sample.title(o.path.basename(file) + " - Notepad")
        text.delete(1.0,END)
        f=open(file,"r")
        text.insert(1.0,f.read())
        f.close()
        
#def save():
#    #tmg.askyesno("Save or Not","Are you sure,You wanna Save??") 
#    val=tmg.askquestion("Save or Not","Are you sure!!You wanna Save??")
#    if(val=="yes"):
#        tmg.showinfo("Message","Saved")

def savefile():
    global file
    if(file==None):
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if(file==""):
            file=None
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()
            sample.title(o.path.basename(file) + " - Notepad")
    else:
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()

def saveasfile():
    global file
    file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if(file==""):
        file=None
    else:
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()
        sample.title(o.path.basename(file) + " - Notepad")

def pagesize():
    pample=tkt.Tk()
    pample.wm_iconbitmap("notepad_23093.ico")
    pample.geometry("300x150")
    pample.title("Untitled - Notepad")
    
    def window():
        sample.geometry(f"{widthi.get()}x{heighti.get()}")

    width=Label(pample,text="Width",font="comicsans 10 bold")
    height=Label(pample,text="Height",font="comicsans 10 bold")
    width.grid()
    height.grid(row=1)

    widthi=IntVar()
    heighti=IntVar()

    widthe=Entry(pample,textvariable=widthi)
    heighte=Entry(pample,textvariable=heighti)
    widthe.grid(row=0,column=1)
    heighte.grid(row=1,column=1)

    bt=Button(pample,text="Apply",command=window).grid(column=1)
    pample.mainloop()

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def delete():
    text.delete(1.0,END)

def time():
    import time
    localtime=time.asctime(time.localtime(time.time()))
    print(localtime)

def helpp():
    tmg.showerror("ERROR","Not Connected To Internet")

def about():
    tmg.showinfo("About Notepad","Windows Notepad is a  simple text editor for Windows \
                \n it creates and edits plain text documents.")

def printt():
    #tmg.showwarning("Warning","Printer not connected!!!")
    tmg.askretrycancel("Warning","Printer not connected!!!")
    #tmg.askokcancel("Warning","Printer not connected!!!")

i=1
def status():
    #tmg.showerror("ERROR","Error 404 occurs")
    global i
    i=i+1
    if(i%2==0):
        statusvar.set(" ")
        statusbar.update()
    #import time
    #time.sleep(10)
    else:
        statusvar.set("Windows(CRLF) \t \t \t \t \t UTF-8")
        
def rate():
    def rating():
        tmg.showinfo("Thanks",f"Thanks for the rating of {slider.get()}")    
    Label(text="RATE US !!!").pack()
    slider=Scale(sample,from_=0,to=10,orient=HORIZONTAL,tickinterval=3)
    slider.set(3)
    slider.pack()
    bt=Button(text="Submit",command=rating).pack()
    #bt=Button(text="Submit",command=quit).pack()
    #bt=Button(text="Submit",command=sample.destroy).pack()
  
    
mainmenu=Menu(sample)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New \t \t \t \t \t Ctrl+N",command=newfile)
m1.add_command(label="New Window \t \t \t \t \tCtrl+Shift+N",command=new_window)
m1.add_command(label="Open... \t \t \t \t \t Ctrl+O",command=openfile)
m1.add_command(label="Save \t \t \t \t \t Ctrl+S",command=savefile)
m1.add_command(label="Save As... \t \t \t \t \t Ctrl+Shift+S",command=saveasfile)
m1.add_separator()
m1.add_command(label="Page Setup...",command=pagesize)
m1.add_command(label="Print... \t \t \t \t \t Ctrl+P",command=printt)
m1.add_separator()
m1.add_command(label="Exit",command=quit)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Undo \t \t \t \t \t Ctrl+Z")
m2.add_separator()
m2.add_command(label="Cut \t \t \t \t \t Ctrl+X",command=cut)
m2.add_command(label="Copy \t \t \t \t \t Ctrl+C",command=copy)
m2.add_command(label="Paste \t \t \t \t \t Ctrl+V",command=paste)
m2.add_command(label="Delete \t \t \t \t \t Del",command=delete)
m2.add_separator()
m2.add_command(label="Search with Bing... \t \t \t \t \t Ctrl+E")
m2.add_command(label="Find... \t \t \t \t \t Ctrl+F")
m2.add_command(label="Find Next \t \t \t \t \t F3")
m2.add_command(label="Find Previous \t \t \t \t \t Shift+F3")
m2.add_command(label="Replace... \t \t \t \t \t Ctrl+H")
m2.add_command(label="Go To... \t \t \t \t \t Ctrl+G")
m2.add_separator()
m2.add_command(label="Select All \t \t \t \t \t Ctrl+A")
m2.add_command(label="Time/Date \t \t \t \t \t F5",command=time)
#sample.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Word Wrap")
m3.add_command(label="Font")
mainmenu.add_cascade(label="Format",menu=m3)

m4=Menu(mainmenu,tearoff=0)
hehe=Menu(m4,tearoff=0)
hehe.add_command(label="Zoom In \t \t \t \t \t Ctrl+Plus")
hehe.add_command(label="Zoom In \t \t \t \t \t Ctrl+Minus")
hehe.add_command(label="Restore Default Zoom \t \t \t \t \t Ctrl+0")
m4.add_cascade(label="Zoom",menu=hehe)
m4.add_command(label="Status Bar",command=status)
mainmenu.add_cascade(label="View",menu=m4)

m5=Menu(mainmenu,tearoff=0)
m5.add_command(label="View Help",command=helpp)
m5.add_command(label="Send Feedback",command=rate)
m5.add_separator()
m5.add_command(label="About Notepad",command=about)
mainmenu.add_cascade(label="Help",menu=m5)

sample.config(menu=mainmenu)
yscrollbar=Scrollbar(sample)
yscrollbar.pack(side=RIGHT,fill=Y)
xscrollbar=Scrollbar(sample,orient=HORIZONTAL)
text=Text(sample,font="consolas 11",background="white",yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
text.pack(expand=True,fill=BOTH)
yscrollbar.config(command=text.yview)


statusvar=StringVar()
statusvar.set("Windows(CRLF) \t \t \t \t \t UTF-8")
statusbar=Label(sample,textvariable=statusvar)
statusbar.pack(fill=X,side=BOTTOM,anchor="se")


xscrollbar.pack(side=BOTTOM,fill=X)
xscrollbar.config(command=text.xview)

sample.mainloop()