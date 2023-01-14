import random
from tkinter import *
import os
import pygame
import sys


class settings:
    
    def __init__(self):
        self.total=0
        self.lc={"banana":(227,207,87),"Blue":(0,0,255),"brown":(165,42,42),"chocolate":(210,105,30),"cobalt":(61,89,171),"crimson":(220,20,60),"darkgreen":(0,100,0),"emeraldgreen":(0,201,87),"firebrick1":(255,48,48),
        "hostwhite":(248,248,255),"hotpink":(255,105,180),"indianred1":(255,106,106),"indigo":(75,0,130),"khaki3":(205,198,115),"lavender":(230,230,250),"lightblue1":(191,239,255),"lightcoral":(240,128,128),
        "lightpink":(255,182,193),"lightsalmon1":(255,160,122),"lightslateblue":(132,112,255),"limegreen":(50,205,50),"magenta":(255,0,255),"maroon":(128,0,0),"mediumorchid3":(180,82,205),"melon":(227,168,105),
        "midnightblue":(25,25,112),"orange":(255,128,0),"peacock ":(51,161,201),"red1":(255,0,0),"royalblue4":(39,64,139),"sandybrown":(244,164,96),"tan4":(139,90,43),"teal":(0,128,128),"turquoise":(64,224,208),"violet":(238,130,238)}
        lc2=[]
        for i in self.lc:
            lc2.append(i)
        self.lc3=lc2
        self.y1=0
        self.pdict={}
  
    def initial(self):
        self.mes = Tk()
        self.mes.title("Snake and ladders")
        self.mes.geometry("300x300")
        Label(self.mes, text='        ').grid(row=1)
        b=Button(self.mes, text ="start", command = self.players).grid(row=1,column=1)
        b1=Button( text ="exit", command = self.mes.destroy).grid(row=1,column=2)
        self.mes.lift()
        self.mes.attributes("-topmost", True)
        self.mes.mainloop()
    
    def players(self):
        Label(self.mes, text='Enter number of players').grid(row=2,column=1)
        v=StringVar()
        self.y1=0
        self.e=Entry(self.mes ,width=5,textvariable=v)
        self.e.grid(row=2,column=2)
        self.e.focus()
        self.e.bind("<KeyPress-Return>",lambda x:self.box())
    
    def box(self,):
        self.total=int(self.e.get())
        self.setting()
    
    def setting(self):
        global h1,clicked
        try:
            self.pdict['%s'%self.e.get()]=('%s'%clicked.get())
        except:
            pass
        
        self.y1+=1
        if self.y1>self.total:
            self.game_window()
        else:
            v=StringVar()
            clicked=StringVar()
            clicked.set("color")
            Label(self.mes, text='Player%s'%(self.y1)).grid(row=self.y1+2,column=1)
            self.e=Entry(self.mes ,width=5,textvariable=v)
            self.e.grid(row=self.y1+2,column=2)
            self.e.focus()
            try: 
                self.lc3.remove(self.pdict[list(self.pdict)[self.y1-2]])
            except :
                pass
            o=OptionMenu(self.mes,clicked,*self.lc3)
            o.grid(row=self.y1+2,column=3)
            self.e.bind("<KeyPress-Return>",lambda x: self.setting())
    
    def game_window(self):
        global root
        global y,h,total,p
        self.mes.destroy()
        root=Tk()
        root.geometry("500x500")
        root.title("Snake and ladders")
        pygame.init()
        menubar = Menu(root)

        # a pulldown menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New game", command=self.new)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda :exit())
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=about1)
        helpmenu.add_command(label="instruction", command=inst)
        menubar.add_cascade(label="Help", menu=helpmenu)

        optionmenu = Menu(menubar, tearoff=0)
        optionmenu.add_command(label="Sound on", command=self.sound_on)
        optionmenu.add_command(label="Sound off", command=self.sound_off)
        menubar.add_cascade(label="Option", menu=optionmenu)
        
        root.config(menu=menubar)
        root.focus_force()
        # pygame.mixer.music.load('song3.mp3')
        # pygame.mixer.music.play()
        # pygame.mixer.music.set_volume(1.0)
        self.h=[]
        for i in range(0,self.total):
            a=0
            self.h.append(a)
        game(root,self.pdict,self.total,self.lc,self.h).game_start()
    
    def sound_on(self):
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1.0)

    def sound_off(self):
        pygame.mixer.music.stop()
    
    def new(self):
        root.destroy()
        os.execv(sys.executable, [sys.executable, '"' + sys.argv[0] + '"'] + sys.argv[1:])
    

class game:

    def __init__(self,root,pdict,total,lc,h):
        self.root=root
        self.pdict=pdict
        self.total=total
        self.p=0
        self.lc=lc
        self.y=total
        self.h=h
    
    def initialboard(self):
        self.root=root
        global l
        l=li
        n=0
        for r in l:
            t=2
            Label(self.root, text='              ').grid(row=n,column=1)
            for c in r:
                if c in [31,41,59,67,83,92,99]:   
                    Label(self.root, text='%s'%(c),bg="red",width=5,height=2,relief=RAISED).grid(row=n,column=t,sticky=E)
                elif c in [2,8,17,29,32,39,62,72,75]:
                    Label(self.root, text='%s'%(c),bg="green",width=5,height=2,relief=RAISED).grid(row=n,column=t,sticky=E)
                else:
                    Label(self.root, text='%s'%(c),bg="yellow",width=5,height=2,relief=RAISED).grid(row=n,column=t,sticky=E)
                t+=1
            n+=1
        self.root.update()
    
    def board(self):
        n=0
        for r in li:
            t=2
            for c in r:
                if c in self.h:
                    f=self.h.index(c)
                    root.grid_slaves(n,t)[0].config(text="%s"%list(self.pdict)[f],bg="#%02x%02x%02x"%self.lc[self.pdict[list(self.pdict)[f]]])
                else:    
                    if c in [31,41,59,67,83,92,99]:   
                        Label(self.root, text='%s'%(c),bg="red",width=5,height=2,relief=RAISED).grid(row=n,column=t,sticky=E)
                    elif c in [2,8,17,29,32,39,62,72,75]:
                        Label(self.root, text='%s'%(c),bg="green",width=5,height=2,relief=RAISED).grid(row=n,column=t,sticky=E)
                    else:
                        Label(self.root, text='%s'%(c),bg="yellow",width=5,height=2,relief=RAISED).grid(row=n,column=t,sticky=E)
                t+=1
            n+=1
        root.update()
    
    def game_start(self):
        self.initialboard()
        Label(self.root, text="player ",width=5).grid(row=12,column=2)
        Label(self.root, text="%s"%list(self.pdict)[self.p],width=5).grid(row=12,column=3)
        self.z=Button(self.root,width=4,text="roll")
        Label(self.root, text="rolldice",width=5).grid(row=13,column=2)
        self.z.focus()
        self.z.bind("<KeyPress-Return>",lambda x:self.dice())
        self.z.bind("<Button-1>",lambda x:self.dice())
        self.z.grid(row=13,column=3)
        self.root.bind("<F1>",about)
        Label(self.root,text="").grid(row=14,column=2,columnspan=3)
        Label(self.root,text="").grid(row=13,column=4)
        self.root.mainloop()
    
    
    def dice(self):
        self.z.unbind("<KeyPress-Return>")
        try:
            self.root.grid_slaves(14,2)[0].config(text="")
        except:
            pass
        r=random.randint(1,6)
        self.root.grid_slaves(13,4)[0].config(text="%s"%(r))
        time=1
        if self.h[self.p]>0:
            time=self.start(r)
        elif self.h[self.p]==0 and r==6:
            self.root.grid_slaves(14,2)[0].config(text="player %s game start"%(self.p+1))
            r=random.randint(1,6)
            self.root.grid_slaves(13,4)[0].config(text="%s"%(r))
            time=self.start(r)
        if time==1:
            self.turn()
            self.z.bind("<KeyPress-Return>",lambda x:self.dice())
        else:
            if time==0:
                time=1
                self.root.after(500,lambda :[pygame.mixer.Sound('snake.wav').play(0),
                        self.start(0),self.turn(),self.z.bind("<KeyPress-Return>",lambda x:self.dice())])
            else:
                time=1
                self.root.after(500,lambda : [pygame.mixer.Sound('snake.wav').play(0),
                    self.start(0),self.turn(),
                    self.z.bind("<KeyPress-Return>",lambda x:self.dice())])
    
    def start(self,r):
        self.h[self.p]+=r
        if self.h[self.p]>100:
            self.h[self.p]-=r
        elif self.h[self.p]==100:
                self.score(self.p+1)
        elif self.h[self.p] in [31,41,59,67,83,92,99]:
            root.grid_slaves(14,2)[0].config( text="snake at %s"%self.h[self.p],fg="red")
            self.board()
            self.h[self.p]=self.snake(self.h[self.p])
            return 0
        elif self.h[self.p] in [2,8,17,29,32,39,62,72,75]:
            root.grid_slaves(14,2)[0].config( text="ladder at %s"%self.h[self.p],fg="blue")
            self.board()
            self.h[self.p]=self.ladder(self.h[self.p])
            return -1   
        c=0       
        for j in self.h:
            c+=1
            if j==self.h[self.p] and (c-1)!=self.p:
                self.h[c-1]=0
                root.grid_slaves(14,2)[0].config(text="PLAYER %s OUT"%c,fg="red")
                # pygame.mixer.Sound('playercut.wav').play()
        self.board()    
        return 1
    
    def turn(self):
        self.p+=1
        if self.p==(self.total):
            self.p=0 
        root.grid_slaves(12,2)[0].config(text="player ")
        root.grid_slaves(12,3)[0].config(text="%s"%list(self.pdict)[self.p])

    def snake(self,a):
        if a==31:
            a=14
        if a==41:
            a=20
        if a==59:
            a=37
        if a==67:
            a=50
        if a==83:
            a=80
        if a==92:
            a=76
        if a==99:
            a=5
        return a

    def ladder(self,i):
        if i==2:
            i=23
        if i==8:
            i=12
        if i==17:
            i=93
        if i==29:
            i=54
        if i==32:
            i=51
        if i==39:
            i=80
        if i==62:
            i=78
        if i==72:
            i=91
        if i==75:
            i=96
        return i
    
    def score(self,g):
        self.Root= Tk()
        self.Root.title("Score")
        if self.p==(self.total-1):
            self.p=0 
        canvas= Canvas(self.Root,width=500, height=500, bg="white")
        canvas.pack()
        
        if self.y==self.total:
            J=canvas.create_text(200,100, text=("Winner"), font=("Comic Sans", 30))
        else:
            J=canvas.create_text(200,100, text=("%s Place"%(y)), font=("Comic Sans", 30)) 
        
        z=canvas.create_text(200,200, text=("Player", list(self.pdict)[g-1]), font=("Comic Sans", 30))
        del self.pdict[list(self.pdict)[g-1]]
        self.y-=1
        del self.h[g-1]
        b = Button (canvas, text='New game',command=self.new2)
        b.place(x=200,y=300)
        b2=Button (canvas, text='Continue',command=self.continueApplication)
        b2.place(x=100,y=300)
        d = Button (canvas, text='exit game',command=lambda : exit())
        d.place(x=300,y=300)
        self.Root.lift()
        self.Root.attributes("-topmost", True)
        self.Root.mainloop()
    
    def continueApplication(self):
        global Root,root,p,y
        if len(self.h)==1:
            self.root.destroy()
            pygame.quit()
            self.Root.destroy()
            self.new2()
        else:
            self.Root.destroy()
            self.root.lift()
            self.root.grid_slaves(12,2)[0].config(text="player ")
            self.root.grid_slaves(12,3)[0].config(text="%s"%list(self.pdict)[p])
            self.z.bind("<KeyPress-Return>",lambda x:self.dice())
    def new2(self):
        self.Root.destroy()
        self.root.destroy()
        os.execv(sys.executable, [sys.executable, '"' + sys.argv[0] + '"'] + sys.argv[1:])
         
def inst():
    os.startfile(r'C:\Users\tayal\Desktop\school\game2\inst.txt')
    
def about(event):
    os.startfile(r'C:\Users\tayal\Desktop\school\game2\about.txt')
def about1():
    os.startfile(r'C:\Users\tayal\Desktop\school\game2\about.txt')

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
global li
li = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
z = 9
for f in li:
    if z % 2 == 0:
        for j in range((10 * z) + 1, (10 * (z + 1)) + 1):
            f.append(j)
        z -= 1
    else:
        for j in range((10 * (z + 1)), (10 * z), -1):
            f.append(j)
        z -= 1
s=settings()
s.initial()

