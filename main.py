from tkinter import *

root = Tk()
root.geometry("1360x640")

bgi = PhotoImage(file="images/technology-wallpaper.png")
mywindow = Label(root, image=bgi)
mywindow.place(x=0,y=0,relwidth=1,relheight=1)
#----***************** C language part************--------

def questions():
        global a1;global a6;global a7;global a2;global a5;global a10
        global a3;global a8;global a4;global a9;global i
        cpic = PhotoImage(file="images/3343732.png")
        cwindow = Label(root, image=cpic)
        cwindow.place(x=0, y=0, relwidth=1, relheight=1)
        #----------------1--------------------
        a = Label(root, text=" let's start the game \n\t 1.father of C is? \n \tA.dennies ratchi      B.guen rosss vessum     C.monty ",font=('Bernard MT Condensed',10))
        a.place(x=0, y=15)
        a1 = Entry(root)
        a1.place(x=55, y=70,height=15,width=15)
        checkbutton = Button(root, text="..submit..", command=check)
        checkbutton.place(x=100, y=65, height=17, width=60)
        #-----------------2------------------
        a = Label(root,text="\n\t 2.extension if an file in C is? \n  A.py      B.c     C.cpp ",font=('Bernard MT Condensed',10))
        a.place(x=0, y=100)
        a2 = Entry(root)
        a2.place(x=55, y=155, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check2)
        checkbutton1.place(x=100, y=155, height=17, width=60)
        #------------------3-------------------
        a = Label(root, text="\n\t 3.How many number of loops in C? \n  A.3     B.4     C.2 ",font=('Bernard MT Condensed',10))
        a.place(x=0, y=188)
        a3 = Entry(root)
        a3.place(x=55, y=233, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check3)
        checkbutton1.place(x=100, y=236, height=17, width=60)
        # ------------------4-------------------
        a = Label(root, text="\n\t 4.How many number of conditional statements in C? \n  A.3      B.2     C.4 ",font=('Bernard MT Condensed',10))
        a.place(x=0, y=268)
        a4 = Entry(root)
        a4.place(x=55, y=318, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check4)
        checkbutton1.place(x=100, y=321, height=17, width=60)
        # -------------------5------------------
        a = Label(root, text="\n\t 5.collection of different data types in C is ? \n  A.union      B.structure      C.pointer",font=('Bernard MT Condensed',10))
        a.place(x=0, y=358)
        a5 = Entry(root)
        a5.place(x=55, y=408, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check5)
        checkbutton1.place(x=100, y=410, height=17, width=60)
        # --------------------6-----------------
        a = Label(root,text="\n\t 6.collection of similer data types in C is ? \n  A.Array       B.structure     C.pointer ",font=('Bernard MT Condensed',10))
        a.place(x=0, y=458)
        a6 = Entry(root)
        a6.place(x=55, y=508, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check6)
        checkbutton1.place(x=100, y=510, height=17, width=60)
        # ---------------------7----------------
        a = Label(root,text="  7.while loop in C is an ? \n \t A.exit controlled         B.entry controlled         C.both ",font=('Bernard MT Condensed',10))
        a.place(x=670, y=15)
        a7 = Entry(root)
        a7.place(x=725, y=65, height=15, width=15)
        checkbutton = Button(root, text="..submit..", command=check7)
        checkbutton.place(x=770, y=62, height=17, width=60)
        # ----------------------8-------------
        a = Label(root, text="\n 8.Do while loop in C is an? \n \t A.entry controlled          B.both           C.exit controlled ",font=('Bernard MT Condensed',10))
        a.place(x=670, y=100)
        a8 = Entry(root)
        a8.place(x=725, y=155, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check8)
        checkbutton1.place(x=770, y=155, height=17, width=60)
        # ---------------------9----------------
        a = Label(root, text="\n 9.C is an _______ level language? \n \t A.High level       B.lowlevel       C.medium level ",font=('Bernard MT Condensed',10))
        a.place(x=670, y=188)
        a9 = Entry(root)
        a9.place(x=725, y=238 , height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check9)
        checkbutton1.place(x=770, y=238, height=17, width=60)
        # -------------------10------------------
        a = Label(root, text="\n\t 10.C is the _______ programming language? \n\t  A.object oriented   B.procedural  C.functional ",font=('Bernard MT Condensed',10))
        a.place(x=670, y=268)
        a10 = Entry(root)
        a10.place(x=725, y=318, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=check10)
        checkbutton1.place(x=770, y=321, height=17, width=60)
        # -------------------------------------
        # ------------- center strips for sperating sides-----------------
        for i in range(0, 70):
            strips = Label(root, text="*||* ")
            strips.pack()
        quit1b= Button(root, text='quit', command=returnscreen)
        quit1b.place(x=1200,y=550)

def returnscreen():
    mgi = PhotoImage(file="images/technology-wallpaper.png")
    mwindow = Label(root, image=mgi)
    mwindow.place(x=0, y=0, relwidth=1, relheight=1)
    startb = Button(root, text="START", command=languagebuttons, font=('Matura MT Script Capitals', 30))
    startb.place(x=50, y=200, height=70, width=230)
    quitb = Button(root, text="QUIT", command=root.quit, font=('Matura MT Script Capitals', 30))
    quitb.place(x=50, y=400, height=70, width=230)
#------------answer checking part-------------
def check():
        n = a1.get()
        if n == 'a'  or n== 'A' :
            ans = Label(root,text= " your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55,y=85)
        else:
            ans =Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55,y=85)

#------2
def check2():
        n=a2.get()
        if n == 'b' or n == 'B':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=175)

        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=175)
#-------3
def check3():
        n=a3.get()
        if n == 'a' or n == 'A':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=255)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=255)
#--------4
def check4():
        n=a4.get()
        if n == 'c' or n == 'C':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=340)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=340)
#--------5
def check5():
        n=a5.get()
        if n == 'B' or n == 'b':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=425)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=425)
#--------6
def check6():
        n=a6.get()
        if n == 'a' or n == 'A':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=510)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=510)
#---7
def check7():
        n = a7.get()
        if n == 'b'  or n== 'B' :
            ans = Label(root,text= " your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725,y=80)
        else:
            ans =Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725,y=80)
#------8
def check8():
        n=a8.get()
        if n == 'c' or n == 'C':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725, y=175)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725, y=175)
#-------9
def check9():
        n=a9.get()
        if n == 'a' or n == 'A':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725, y=255)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725, y=255)
#--------10
def check10():
        n=a10.get()
        if n == 'b' or n == 'B':
            ans = Label(root, text=" your answer is correct.....")
            ans.place(x=725, y=340)
        else:
            ans = Label(root, text="wrong answer...")
            ans.place(x=725, y=340)

#----***************** C++ language part************--------

def Cquestions():
        global a1;global a6;global a7;global a2;global a5;global a10
        global a3;global a8;global a4;global a9
        ph = PhotoImage(file="images/Clangph.png")
        cphoto = Label(root, image=ph)
        cphoto.place(relheight=1,relwidth=1)
        #----------------1--------------------
        a = Label(root, text=" ...............LET'S START THE GAME................ \n\t 1. Who invented C++? \n\t a).Dennis Ritchie   b).Ken Thompson   c).Brian Kernighan   d).Bjarne Stroustrup ",font=('Bernard MT Condensed',10))
        a.place(x=0, y=15)
        a1 = Entry(root)
        a1.place(x=55, y=70,height=15,width=15)
        checkbutton = Button(root, text="..submit..", command=Ccheck)
        checkbutton.place(x=100, y=72, height=17, width=60)
        #-----------------2------------------
        a = Label(root,text="\n\t 2.Which of the following is used for comments in C++?\n\t a)./* comment */   b).// comment */   c).// comment    d).both // comment or /* comment */",font=('Bernard MT Condensed',10))
        a.place(x=0, y=100)
        a2 = Entry(root)
        a2.place(x=55, y=155, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck2)
        checkbutton1.place(x=100, y=155, height=17, width=60)
        #------------------3-------------------
        a = Label(root, text="\n\t 3.Which of the following is header file extension used in c++? \n\t a).hg   b).cpp   c).h   d).hf",font=('Bernard MT Condensed',10))
        a.place(x=0, y=188)
        a3 = Entry(root)
        a3.place(x=55, y=233, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck3)
        checkbutton1.place(x=100, y=236, height=17, width=60)
        # ------------------4-------------------
        a = Label(root, text="\n\t 4.Which of the following is not a type of Constructor in C++? \n\t a).Default constructor   b).Parameterized constructor   c).Copy constructor   d).Friend constructor",font=('Bernard MT Condensed',10))
        a.place(x=0, y=268)
        a4 = Entry(root)
        a4.place(x=55, y=318, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck4)
        checkbutton1.place(x=100, y=321, height=17, width=60)
        # -------------------5------------------
        a = Label(root, text="\n\t 5.what is the extension of an file in C++ ? \n  A).c    B).cpp   C).py",font=('Bernard MT Condensed',10))
        a.place(x=0, y=358)
        a5 = Entry(root)
        a5.place(x=55, y=408, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck5)
        checkbutton1.place(x=100, y=410, height=17, width=60)
        # --------------------6-----------------
        a = Label(root,text="\n\t 6.Which of the following approach is used by C++? \n\t a).Left-right   b).Right-left   c).Bottom-up   d).Top-down",font=('Bernard MT Condensed',10))
        a.place(x=0, y=458)
        a6 = Entry(root)
        a6.place(x=55, y=508, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck6)
        checkbutton1.place(x=100, y=510, height=17, width=60)
        # ---------------------7----------------
        a = Label(root,text="  7. Which of the following type is provided by C++ but not C? \n\t  a).double   b).float   c).int   d).bool",font=('Bernard MT Condensed',10))
        a.place(x=670, y=15)
        a7 = Entry(root)
        a7.place(x=725, y=65, height=15, width=15)
        checkbutton = Button(root, text="..submit..", command=Ccheck7)
        checkbutton.place(x=770, y=62, height=17, width=60)
        # ----------------------8-------------
        a = Label(root, text="\n 8. Which of the following correctly declares an array in C++?\n\t a).array{10};   b).array array[10];   c).int array;   d).int array[10];",font=('Bernard MT Condensed',10))
        a.place(x=670, y=100)
        a8 = Entry(root)
        a8.place(x=725, y=155, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck8)
        checkbutton1.place(x=770, y=155, height=17, width=60)
        #---------------------9----------------
        a=Label(root, text="\n  9.What is Inheritance in C++?\n\t a).Deriving new classes from existing classes   b).Overloading of classes   \n c).Classes with same names   d).Wrapping of data into a single class",font=('Bernard MT Condensed',10))
        a.place(x=670, y=188)
        a9 = Entry(root)
        a9.place(x=725, y=255 , height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck9)
        checkbutton1.place(x=770, y=256, height=17, width=60)
        # -------------------10------------------
        a = Label(root, text="\n\t 10. What is meant by a polymorphism in C++?\n\t a).class having only single form   b).class having four forms   c).class having many forms   d).class having two forms",font=('Bernard MT Condensed',10))
        a.place(x=670, y=288)
        a10 = Entry(root)
        a10.place(x=725, y=345, height=15, width=15)
        checkbutton1 = Button(root, text="..submit..", command=Ccheck10)
        checkbutton1.place(x=770, y=347, height=17, width=60)
        # -------------------------------------
        # ------------- center strips for sperating sides-----------------
        for i in range(0, 70):
            strips = Label(root, text="*||* ")
            strips.pack()
        quit1b = Button(root, text='quit', command=returnscreen)
        quit1b.place(x=1200, y=550)
#------------answer checking part-------------
def Ccheck():
        n = a1.get()
        if n == 'd'  or n== 'D' :
            ans = Label(root,text= " your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55,y=80)

        else:
            ans =Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55,y=80)

#------2
def Ccheck2():
        n=a2.get()
        if n == 'd' or n == 'D':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=175)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=175)
#-------3
def Ccheck3():
        n=a3.get()
        if n == 'c' or n == 'C':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=255)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=255)
#--------4
def Ccheck4():
        n=a4.get()
        if n == 'd' or n == 'D':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=340)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=340)
#--------5
def Ccheck5():
        n=a5.get()
        if n == 'B' or n == 'b':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=425)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=425)
#--------6
def Ccheck6():
        n=a6.get()
        if n == 'c' or n == 'C':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=55, y=510)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=55, y=510)
#---7
def Ccheck7():
        n = a7.get()
        if n == 'd'  or n== 'D' :
            ans = Label(root,text= " your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725,y=80)
        else:
            ans =Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725,y=80)
#------8
def Ccheck8():
        n=a8.get()
        if n == 'd' or n == 'D':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725, y=175)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725, y=175)
#-------9
def Ccheck9():
        n=a9.get()
        if n == 'a' or n == 'A':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725, y=275)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725, y=275)
#--------10
def Ccheck10():
        n=a10.get()
        if n == 'c' or n == 'C':
            ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
            ans.place(x=725, y=340)
        else:
            ans = Label(root, text="wrong answer...",font=('Harrington', 10))
            ans.place(x=725, y=340)

# ----***************** Python language part ************--------

def pquestions():
    global a1;global a6;global a7;
    global a2;global a5;global a10
    global a3;global a8;global a4;global a9
    ph = PhotoImage(file="images/technology-wallpaper.png")
    pphoto = Label(root, image=ph)
    pphoto.pack()
    pphoto.place(x=0,y=0,relheight=1,relwidth=1)

    # ----------------1--------------------
    a = Label(root,text=" \t........................LET'S START THE GAME..................... \n\t 1.father of Python is? \n \tA.dennies ratchi    B.Guido vann rossum   C.monty ",font=('Bernard MT Condensed',10))
    a.place(x=0, y=15)
    a1 = Entry(root)
    a1.place(x=55, y=65, height=15, width=15)
    checkbutton = Button(root, text="..submit..", command=Pcheck)
    checkbutton.place(x=100, y=67, height=17, width=60)
    # -----------------2------------------
    a = Label(root, text="\n\t 2.extension if an file in Python is? \n  A.py   B.c  C.cpp ",font=('Bernard MT Condensed',10))
    a.place(x=0, y=100)
    a2 = Entry(root)
    a2.place(x=55, y=155, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck2)
    checkbutton1.place(x=100, y=155, height=17, width=60)
    # ------------------3-------------------
    a = Label(root, text="\n\t 3.is that python is space sensitive ? \n\t A.no   B.yes  C.based on machine and software ",font=('Bernard MT Condensed',10))
    a.place(x=0, y=188)
    a3 = Entry(root)
    a3.place(x=55, y=238, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck3)
    checkbutton1.place(x=100, y=240, height=17, width=60)
    # ------------------4-------------------
    a = Label(root, text="\n\t 4.which of the following is python had? \n  A.compiler   B.intreptur  C.as we want ",font=('Bernard MT Condensed',10))
    a.place(x=0, y=268)
    a4 = Entry(root)
    a4.place(x=55, y=318, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck4)
    checkbutton1.place(x=100, y=321, height=17, width=60)
    # -------------------5------------------
    a = Label(root, text="\n\t 5. Which of the following is used to define a block of code in Python language? \n\t a.Indentation b.Key c.Brackets d.All of the mentioned ",font=('Bernard MT Condensed',10))
    a.place(x=0, y=358)
    a5 = Entry(root)
    a5.place(x=55, y=408, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck5)
    checkbutton1.place(x=100, y=410, height=17, width=60)
    # --------------------6-----------------
    a = Label(root, text="\n\t 6. Which keyword is used for function in Python language? \n\t a.Function b.Def c.Fun d.Define",font=('Bernard MT Condensed',10))
    a.place(x=0, y=458)
    a6 = Entry(root)
    a6.place(x=55, y=508, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck6)
    checkbutton1.place(x=100, y=510, height=17, width=60)
    # ---------------------7----------------
    a = Label(root, text=" \n\t 7.Which of the following character is used to give single-line comments in Python? \n\t a.// b.# c.! d./*",font=('Bernard MT Condensed',10))
    a.place(x=670, y=15)
    a7 = Entry(root)
    a7.place(x=725, y=65, height=15, width=15)
    checkbutton = Button(root, text="..submit..", command=Pcheck7)
    checkbutton.place(x=770, y=62, height=17, width=60)
    # ----------------------8-------------
    a = Label(root, text=" 8.What does pip stand for python? \n\t a.unlimited length  b.all private members must have leading and trailing underscores \n c.Preferred Installer Program d.none of the mentioned ",font=('Bernard MT Condensed',10))
    a.place(x=670, y=100)
    a8 = Entry(root)
    a8.place(x=725, y=155, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck8)
    checkbutton1.place(x=770, y=155, height=17, width=60)
    # ---------------------9----------------
    a = Label(root, text="\n 9.python is an _______ level language? \n \t A.High level   B.lowlevel  C.medium level ",font=('Bernard MT Condensed',10))
    a.place(x=670, y=188)
    a9 = Entry(root)
    a9.place(x=725, y=238, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck9)
    checkbutton1.place(x=770, y=240, height=17, width=60)
    # -------------------10------------------
    a = Label(root,text="\n\t 10.python is the _______ programming language? \n\t  A.object oriented   B.procedural  C.functional ",font=('Bernard MT Condensed',10))
    a.place(x=670, y=268)
    a10 = Entry(root)
    a10.place(x=725, y=318, height=15, width=15)
    checkbutton1 = Button(root, text="..submit..", command=Pcheck10)
    checkbutton1.place(x=770, y=321, height=17, width=60)
    # -------------------------------------
    # ------------- center strips for sperating sides-----------------
    for i in range(0, 70):
        strips = Label(root, text="*|!|* ")
        strips.pack()
    #-------------- return button-----------------------------------
    quit1b = Button(root, text='quit', command=returnscreen)
    quit1b.place(x=1200, y=550)
# ------------answer checking part-------------
def Pcheck():
    n = a1.get()
    if n == 'b' or n == 'B':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=55, y=85)
    else:
        ans = Label(root, text="wrong answer...", font=('Harrington', 10))
        ans.place(x=55, y=85)
# ------2
def Pcheck2():
    n = a2.get()
    if n == 'a' or n == 'A':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=55, y=175)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=55, y=175)
# -------3
def Pcheck3():
    n = a3.get()
    if n == 'b' or n == 'B':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=55, y=260)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=55, y=260)
# --------4
def Pcheck4():
    n = a4.get()
    if n == 'b' or n == 'B':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=55, y=340)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=55, y=340)
# --------5
def Pcheck5():
    n = a5.get()
    if n == 'a' or n == 'A':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=55, y=425)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=55, y=425)
# --------6
def Pcheck6():
    n = a6.get()
    if n == 'b' or n == 'B':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=55, y=510)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=55, y=510)
# ---7
def Pcheck7():
    n = a7.get()
    if n == 'b' or n == 'B':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=725, y=80)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=725, y=80)
# ------8
def Pcheck8():
    n = a8.get()
    if n == 'c' or n == 'C':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=725, y=175)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=725, y=175)
# -------9
def Pcheck9():
    n = a9.get()
    if n == 'a' or n == 'A':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=725, y=255)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=725, y=255)


# --------10
def Pcheck10():
    n = a10.get()
    if n == 'a' or n == 'A':
        ans = Label(root, text=" your answer is correct.....",font=('Harrington', 10))
        ans.place(x=725, y=340)
    else:
        ans = Label(root, text="wrong answer...",font=('Harrington', 10))
        ans.place(x=725, y=340)


def languagebuttons():
    cbutton = Button(root, text='C  LANGUAGE', fg='black', command=questions, font=('broadway', 20))
    cbutton.place(x=850, y=130,height=50,width=200)
    Cbutton = Button(root, text='C++ LANGUAGE', fg='black', command=Cquestions, font=('broadway', 20))
    Cbutton.place(x=850, y=300,height=50,width=230)
    pybutton = Button(root, text='PYTHON LANGUAGE', fg='black', command=pquestions, font=('broadway', 20))
    pybutton.place(x=850, y=500,height=50,width=300)

startb = Button(root, text="START", command=languagebuttons, font=('Matura MT Script Capitals', 30))
startb.place(x=50,y=200,height=70,width=230)
quitb = Button(root, text="QUIT", command=root.quit, font=('Matura MT Script Capitals', 30))
quitb.place(x=50,y=400,height=70,width=230)

root.mainloop()