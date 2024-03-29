from tkinter import *

import sqlite3
from tkinter.messagebox import showinfo, showerror

con = sqlite3.Connection("database")
cur = con.cursor()
global abcd
abcd = []

rt1 = Tk()
rt1.title("LIBRARY MANAGEMENT SYSTEM")
rt1.configure(background='light green')
Label(rt1, text="LIBRARY MANAGEMENT SYSTEMS", font="times 20 bold", bd=3, bg="light yellow").grid(row=0, column=0)
Label(rt1, text="PRAVENDRA,PRINCE,RAJAT", font="times 15 bold").grid(row=1, column=0)
Label(rt1, text="`University Number=171500236,171500238,171500251", font="times 15 bold").grid(row=2, column=0)
Label(rt1, text="BATCH=3rd(year)", font="times 15 bold").grid(row=3, column=0)
rt1.after(5000, rt1.destroy)
rt1.mainloop()
root = Tk()
root.title("python project")


def issue():
    root2 = Toplevel()

    def database():
        def search1():
            x = {"Database System Concepts (Abraham Silberschatz,Henry Korth)": 1,
                 "Database Management Systems(Raghu Ramakrishnan)": 2,
                 "An Introduction to Database Systems (Bipin Desai)": 3,
                 "Principles of database systems(J.D.Ullman)": 4,
                 "Fundamentals of database systems(elmasri and S.Navathe)": 5}
            for i, j in x.items():
                if (v1.get() == j or v2.get() == j or v3.get() == j or v4.get() == j or v5.get() == j):
                    abcd.append(i)
            for i in abcd:
                print("This book is issued  : ", *i)

        root3 = Toplevel()
        root3.geometry('800x800')
        Label(root3, text="DATABASE MANAGEMENT SYSTEM")
        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        Checkbutton(root3, text="Database System Concepts (Abraham Silberschatz,Henry Korth)", variable=v1,
                    onvalue=1).grid(row=0, column=0, sticky='W')
        Checkbutton(root3, text="Database Management Systems(Raghu Ramakrishnan)", variable=v2, onvalue=2).grid(row=1,
                                                                                                                column=0,
                                                                                                                sticky='W')
        Checkbutton(root3, text="An Introduction to Database Systems (Bipin Desai)", variable=v3, onvalue=3).grid(row=2,
                                                                                                                  column=0,
                                                                                                                  sticky='W')
        Checkbutton(root3, text="Principles of database systems(J.D.Ullman)", variable=v4, onvalue=4).grid(row=3,
                                                                                                           column=0,
                                                                                                           sticky='W')
        Checkbutton(root3, text="Fundamentals of database systems(elmasri and S.Navathe)", variable=v5, onvalue=5).grid(
            row=4, column=0, sticky='W')
        Button(root3, text="ISSUE", bd=3, bg='light yellow', command=search1).grid(row=5, column=0)
        Button(root3, text="Exit", bd=3, bg='light yellow', command=root3.destroy).grid(row=6, column=0)

    def mathematics():
        def search2():
            x = {"discrete mathematics and its applications(kenneth H rosen)": 1,
                 "discrete mathematics with applications(Susanna A Epp)": 2,
                 "introductory discrete mathematics (V balakrishnan)": 3,
                 "discrete mathematical structures (Bernard Kolman)": 4,
                 "Schaums outline of theory and probability (Schaums)": 5, "discrete mathematics(Laslo lovasz)": 6,
                 "elements of discrete mathematics(chung laung liu)": 7, "discrete mathematics(Norman L biggs)": 8}
            for i, j in x.items():
                if (
                        v1.get() == j or v2.get() == j or v3.get() == j or v4.get() == j or v5.get() == j or v6.get() == j or v7.get() == j or v8.get() == j):
                    abcd.append(i)
            for i in abcd:
                print("This book is issued  : ", *i)

        root4 = Toplevel()
        root4.geometry('800x800')
        Label(root4, text='DISCRETE MATHEMATICS').grid(row=0, column=0)
        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        Checkbutton(root4, text="Discrete mathematics and its applications(kenneth H rosen)", variable=v1,
                    onvalue=1).grid(row=1, column=0, sticky='W')
        Checkbutton(root4, text="Discrete mathematics with applications(Susanna A Epp)", variable=v2, onvalue=2).grid(
            row=2, column=0, sticky='W')
        Checkbutton(root4, text="Introductory discrete mathematics (V balakrishnan)", variable=v3, onvalue=3).grid(
            row=3, column=0, sticky='W')
        Checkbutton(root4, text="Discrete mathematical structures (Bernard Kolman)", variable=v4, onvalue=4).grid(row=4,
                                                                                                                  column=0,
                                                                                                                  sticky='W')
        Checkbutton(root4, text="Schaums outline of theory and probability (Schaums)", variable=v5, onvalue=5).grid(
            row=5, column=0, sticky='W')
        Checkbutton(root4, text="Discrete mathematics(Laslo lovasz)", variable=v6, onvalue=6).grid(row=6, column=0,
                                                                                                   sticky='W')
        Checkbutton(root4, text="Elements of discrete mathematics(chung laung liu)", variable=v7, onvalue=7).grid(row=7,
                                                                                                                  column=0,
                                                                                                                  sticky='W')
        Checkbutton(root4, text="Discrete mathematics(Norman L biggs)", variable=v8, onvalue=8).grid(row=8, column=0,
                                                                                                     sticky='W')
        Button(root4, text="ISSUE", bd=3, bg='light yellow', command=search2).grid(row=9, column=0)
        Button(root4, text="Exit", bd=3, bg='light yellow', command=root4.destroy).grid(row=10, column=0)

    def python():
        def search3():
            x = {"Automate with boring stuff with python(Al Sweigart)": 1, "Learn python in one day(jamie chan)": 2,
                 "black hat python(justin seitz)": 3, "python cookbook(david beazley)": 4,
                 "a byte of python(swaroop c h)": 5, "think python(allen downey)": 6,
                 "head first python(paul barry)": 7, "vilent python(tj. o'connor)": 8}

            for i, j in x.items():
                if (
                        v1.get() == j or v2.get() == j or v3.get() == j or v4.get() == j or v5.get() == j or v6.get() == j or v7.get() == j or v8.get() == j):
                    abcd.append(i)
            for i in abcd:
                print("This book is issued  : ", *i)

        root5 = Toplevel()
        root5.geometry('300x300')
        Label(root5, text='PYTHON').grid(row=0, column=0)
        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        Checkbutton(root5, text="Automate with boring stuff with python(Al Sweigart)", variable=v1, onvalue=1).grid(
            row=1, column=0, sticky='W')
        Checkbutton(root5, text="Learn python in one day(Jamie Chan)", variable=v2, onvalue=2).grid(row=2, column=0,
                                                                                                    sticky='W')
        Checkbutton(root5, text="Black Hat Python(Justin Seitz)", variable=v3, onvalue=3).grid(row=3, column=0,
                                                                                               sticky='W')
        Checkbutton(root5, text="Python Cookbook(David Beazley)", variable=v4, onvalue=4).grid(row=4, column=0,
                                                                                               sticky='W')
        Checkbutton(root5, text="A byte of python(Swaroop C.H)", variable=v5, onvalue=5).grid(row=5, column=0,
                                                                                              sticky='W')
        Checkbutton(root5, text="Think Python(Allen Downey)", variable=v6, onvalue=6).grid(row=6, column=0, sticky='W')
        Checkbutton(root5, text="Head First Python(Paul Barry)", variable=v7, onvalue=7).grid(row=7, column=0,
                                                                                              sticky='W')
        Checkbutton(root5, text="Vilent Python(T.J. O'Connor)", variable=v8, onvalue=8).grid(row=8, column=0,
                                                                                             sticky='W')
        Button(root5, text="ISSUE", bd=3, bg='light yellow', command=search3).grid(row=9, column=0)
        Button(root5, text="Exit", bd=3, bg='light yellow', command=root5.destroy).grid(row=10, column=0)

    def digital():
        def search4():
            x = {"digital electronics(s. salivahan)": 1, "digital fundamental (FLOYD)": 2,
                 "digital design(morris mano)": 3, "digital electronics (william gothmann h)": 4,
                 "fundamentals of didgital electronics(anand kumar)": 5,
                 "digital electronics principles(Anil K Maini)": 6}
            for i, j in x.items():
                if (v1.get() == j or v2.get() == j or v3.get() == j or v4.get() == j or v5.get() == j or v6.get() == j):
                    abcd.append(i)
            for i in abcd:
                print("This book is issued  : ", *i)

        root6 = Toplevel()
        root6.geometry('300x300')
        Label(root6, text='DIGITAL ELECTRONICS').grid(row=0, column=0)
        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        Checkbutton(root6, text="digital electronics(s. salivahan)", variable=v1, onvalue=1).grid(row=1, column=0,
                                                                                                  sticky='W')
        Checkbutton(root6, text="digital fundamental (FLOYD)", variable=v2, onvalue=2).grid(row=2, column=0, sticky='W')
        Checkbutton(root6, text="digital design(morris mano)", variable=v3, onvalue=3).grid(row=3, column=0, sticky='W')
        Checkbutton(root6, text="digital electronics (william gothmann h)", variable=v4, onvalue=4).grid(row=4,
                                                                                                         column=0,
                                                                                                         sticky='W')
        Checkbutton(root6, text="fundamentals of didgital electronics(anand kumar)", variable=v5, onvalue=5).grid(row=5,
                                                                                                                  column=0,
                                                                                                                  sticky='W')
        Checkbutton(root6, text="digital electronics principles(Anil K Maini)", variable=v6, onvalue=6).grid(row=6,
                                                                                                             column=0,
                                                                                                             sticky='W')
        Button(root6, text="ISSUE", bd=3, bg='light yellow', command=search4).grid(row=7, column=0)
        Button(root6, text="Exit", bd=3, bg='light yellow', command=root6.destroy).grid(row=8, column=0)

    def novels():
        def search5():
            x = {"ULYSSES(james joyce)": 1, "THE Great Gatsby(F. Scott Fitzgerald)": 2,
                 "a portrait of the artist as a young man(james joyce)": 3, "lolita(vladimir nabokov)": 4,
                 "the sound and the fury(william faulkner)": 5, "the darkness at the noon(arthur kostler)": 6}
            for i, j in x.items():
                if (v1.get() == j or v2.get() == j or v3.get() == j or v4.get() == j or v5.get() == j or v6.get() == j):
                    abcd.append(i)
            for i in abcd:
                print("This book is issused  : ", *i)

        root7 = Toplevel()
        root7.geometry('300x300')
        Label(root7, text='novels').grid(row=0, column=0)
        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        Checkbutton(root7, text="ULYSSES(james joyce)", variable=v1, onvalue=1).grid(row=1, column=0, sticky='W')
        Checkbutton(root7, text="THE Great Gatsby(F. Scott Fitzgerald)", variable=v2, onvalue=2).grid(row=2, column=0,
                                                                                                      sticky='W')
        Checkbutton(root7, text="a portrait of the artist as a young man(james joyce)", variable=v3, onvalue=3).grid(
            row=3, column=0, sticky='W')
        Checkbutton(root7, text="lolita(vladimir nabokov)", variable=v4, onvalue=4).grid(row=4, column=0, sticky='W')
        Checkbutton(root7, text="the sound and the fury(william faulkner)", variable=v5, onvalue=5).grid(row=5,
                                                                                                         column=0,
                                                                                                         sticky='W')
        Checkbutton(root7, text="the darkness at the noon(arthur kostler)", variable=v6, onvalue=6).grid(row=6,
                                                                                                         column=0,
                                                                                                         sticky='W')
        Button(root7, text="ISSUE", bd=3, bg='light yellow', command=search5).grid(row=7, column=0)
        Button(root7, text="EXIT", bd=3, bg='light yellow', command=root7.destroy).grid(row=8, column=0)

    Label(root2, text="CLICK ON THE BUTTON TO SELECT A SUBJECT", font="arabic 20 bold ", bd=10, bg='light green',
          fg='black', relief='raised').grid(row=0, column=3, columnspan=4)
    Button(root2, text="DATABASE MANAGEMENT SYSTEM", height=2, width=30, bd=10, bg='turquoise', fg='black',
           font='times 10 bold', command=database).grid(row=1, column=4)
    Button(root2, text="Discrete Mathematics", height=2, width=30, bd=10, bg='turquoise', fg='black',
           font='times 10 bold', command=mathematics).grid(row=2, column=4)
    Button(root2, text="python", command=python, height=2, width=30, bd=10, bg='turquoise', fg='black',
           font='times 10 bold').grid(row=3, column=4)
    Button(root2, text="Digital Electronics", command=digital, height=2, width=30, bd=10, bg='turquoise', fg='black',
           font='times 10 bold').grid(row=4, column=4)
    Button(root2, text="novels", command=novels, height=2, width=30, bd=10, bg='turquoise', fg='black',
           font='times 10 bold').grid(row=5, column=4)
    Button(root2, text="EXIT", command=root2.destroy, height=2, width=30, bd=10, bg='yellow', fg='black',
           font='times 10 bold').grid(row=6, column=4)


def return2():
    if len(abcd) == 0:
        showerror('error', 'no books issued')
    elif str(e.get()) == "Database System Concepts" and str(f.get()) == "Abraham Silberschatz,Henry Korth":
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "Database Management Systems" and str(f.get()) == "Raghu Ramakrishnan"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "An Introduction to Database Systems" and str(f.get()) == "Bipin Desai"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "Principles of database systems" and str(f.get()) == "J.D.Ullman"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "Fundamentals of database systems" and str(f.get()) == "elmasri and S.Navathe"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "discrete mathematics and its applications" and str(f.get()) == "kenneth H rosen"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "discrete mathematics with applications" and str(f.get()) == "Susanna A Epp"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "introductory discrete mathematics" and str(f.get()) == "V balakrishnan"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "discrete mathematical structures" and str(f.get()) == "Bernard Kolman"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "Schaums outline of theory and probability" and str(f.get()) == "Schaums"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "discrete mathematics" and str(f.get()) == "Laslo lovasz"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "elements of discrete mathematics" and str(f.get()) == "chung laung liu"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "discrete mathematics" and str(f.get()) == "Norman L biggs"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "Automate with boring stuff with python" and str(f.get()) == "Al Sweigart"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "Learn python in one day" and str(f.get()) == "jamie chan"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "black hat python" and str(f.get()) == "justin seitz"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "python cookbook" and str(f.get()) == "david beazley"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "a byte of python" and str(f.get()) == "swaroop c h"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "think python" and str(f.get()) == "allen downey"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "head first python" and str(f.get()) == "paul barry"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "vilent python" and str(f.get()) == "tj. o'connor"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "digital electronics" and str(f.get()) == "s. salivahan"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "digital electronics" and str(f.get()) == "william gothmann h"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "digital fundamental" and str(f.get()) == "FLOYD"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "digital design" and str(f.get()) == "morris mano"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "fundamentals of didgital electronics" and str(f.get()) == "anand kumar"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "digital electronics principles" and str(f.get()) == "Anil K Maini"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "ULYSSES" and str(f.get()) == "james joyce"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "THE Great Gatsby" and str(f.get()) == "F. Scott Fitzgerald"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "a portrait of the artist as a young man" and str(f.get()) == "james joyce"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "lolita" and str(f.get()) == "vladimir nabokov"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "the sound and the fury" and str(f.get()) == "william faulkner"):
        showinfo('reutrn', 'the book has been succesfully returned')
    elif (str(e.get()) == "the darkness at the noon" and str(f.get()) == "arthur kostler"):
        showinfo('reutrn', 'the book has been succesfully returned')
    else:
        showerror('error', 'either the data entered is wrong or no such book exists')


def return1():
    root8 = Toplevel()
    Label(root8, text="ENTER THE DEtAILS OF THE BOOK YOU WANT TO RETURN", font="arabic 20 bold ", relief='ridge').grid(
        row=0, column=2)
    Label(root8, text="Enter the book title").grid(row=1, column=2)
    global e
    e = Entry(root8)
    e.grid(row=2, column=2)
    Label(root8, text="Enter the author name").grid(row=3, column=2)
    global f
    f = Entry(root8)
    f.grid(row=4, column=2)
    Button(root8, text="return", command=return2).grid(row=5, column=2)


def show():
    showinfo('BOOKS ISSUED ', abcd)


def nextpage():
    root1 = Tk()
    Label(root1, text="WLECOME ADMIN ", font="sans 20 bold", bg="light green", bd=7, relief="raised").grid(row=0,
                                                                                                           column=0,
                                                                                                           columnspan=5)
    Button(root1, text="ISSUE", command=issue, height=2, width=10, bd=10, bg='turquoise', fg='black',
           font='times 10 bold').grid(row=1, column=0)
    Button(root1, text="RETURN", height=2, width=10, bd=10, bg='turquoise', fg='black', font='times 10 bold',
           command=return1).grid(row=1, column=1)
    Button(root1, text="SHOW", height=2, width=10, bd=10, bg='turquoise', fg='black', font='times 10 bold',
           command=show).grid(row=1, column=2)


def enter():
    Label(root, text="Access granted", font="times 15 bold").grid(row=10, column=2)
    Button(root, text="next page", command=nextpage, bd=5, bg='yellow').grid(row=11, column=2)


Label1 = Label(root, text="ENTER USERNAME:", font="times 15 bold", relief="ridge", bd=0)
Label1.grid(row=5, column=2, padx=50)

entry1 = Entry(root, bd=5)
entry1.grid(row=6, column=2)

username = entry1.get()

Label2 = Label(root, text='PASSWORD: ', font="times 15 bold", relief="ridge", bd=0, fg='red')
Label2.grid(row=7, column=2, padx=50)

entry2 = Entry(root, bd=5, show="*")
entry2.grid(row=8, column=2)

password = entry2.get()


def exit1():
    Label(root, text="Access denied", font="times 15 bold").grid(row=10, column=2)


if (username == "GLAM" and password == "111111"):
    btn = Button(root, text='Login', command=exit1, bd=5)
    btn.grid(row=9, column=2)
    root = Tk()
else:
    btn = Button(root, text='Login', command=enter, bd=5, bg='yellow')
    btn.grid(row=9, column=2)

img1 = PhotoImage(file='library.gif')
Label(root, image=img1).grid(row=1, column=2)
Label(root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="black", relief="raised", bd=7, font="forte 20 bold",
      width='50').grid(row=0, column=0, columnspan=4)

root.mainloop()
