from tkinter import *
top = Tk()
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=None)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Save as...", command=None)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=None)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=None)
editmenu.add_command(label="Copy", command=None)
editmenu.add_command(label="Paste", command=None)
editmenu.add_command(label="Delete", command=None)
editmenu.add_command(label="Select All", command=None)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=None)
helpmenu.add_command(label="About...", command=None)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)
top.geometry("450x300")
top.title("Tkinter")

# the label for user_name
Label(top,text="Log in",font=("Arial", 15)).place(x=40,y=20)
Label.size = 50
user_name = Label(top,text="Username: ").place(x=40,y=60)

# the label for user_password
user_password = Label(top,text="Password: ").place(x=40,y=100)

submit_button = Button(top,text="Submit", bg="green").place(x=40,y=130)

cancel_button = Button(top,text="Cancel", bg="red",command=quit).place(x=120,y=130)

user_name_input_area = Entry(top,width=30).place(x=110,y=60)

user_password_entry_area = Entry(top,width=30).place(x=110,y=100)

top.mainloop()