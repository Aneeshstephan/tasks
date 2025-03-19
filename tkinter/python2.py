from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
window = Tk()
window.title("REGISTRATION")
window.geometry("500x500")
window.configure(bg="lightblue")

# Name
lb1 = Label(window, text="Name", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb1.grid(row=0, column=0, sticky="e", padx=10)
en1 = Entry(window)
en1.grid(row=0, column=1, sticky="w", padx=5)

# Age
lb2 = Label(window, text="Age", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb2.grid(row=1, column=0, sticky="e", padx=10)
s = IntVar()
s.set(25)
sp = Spinbox(window, from_=1, to=50, width=10, textvariable=s)
sp.grid(row=1, column=1, sticky="w", padx=5)

# Gender 
lb3 = Label(window, text="Gender", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb3.grid(row=2, column=0, sticky="e", padx=10)
first = StringVar(value="none")
rb1 = Radiobutton(window, text="Male", variable=first, value="male", bg="lightblue", font=("arial", 12), width=10)
rb1.grid(row=2, column=1, sticky="w", padx=5)

rb2 = Radiobutton(window, text="Female", variable=first, value="female", bg="lightblue", font=("arial", 12), width=10)
rb2.grid(row=2, column=2, sticky="w", padx=5)

#Email
lb4=Label(window,text="Email", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb4.grid(row=3,column=0,sticky="e",padx=10)
en = Entry(window)
en.grid(row=3, column=1,sticky="w", padx=5)

#Phone number
lb5=Label(window,text="Ph.NO", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb5.grid(row=4,column=0,sticky="e",padx=10)
en = Entry(window)
en.grid(row=4, column=1,sticky="w", padx=5)

#address
lb5=Label(window,text="Address",font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb5.grid(row=5,column=0,sticky="e",padx=5)
sc=ScrolledText(window,width=30,height=3)
sc.grid(row=5,column=1,sticky="w", padx=5)

#College
lb6=Label(window,text="College", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb6.grid(row=6,column=0,sticky="e",padx=10)
en = Entry(window,width=50,)
en.grid(row=6, column=1,sticky="w", padx=5)

#languages
lb7=Label(window,text="Languages", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb7.grid(row=7,column=0,sticky="e",padx=10)

chb1=Checkbutton(window,text="malayalam",variable=1,bg="lightblue")
chb1.grid(row=7,column=1,sticky="w", padx=5)

chb2=Checkbutton(window,text="English",variable=2,bg="lightblue")
chb2.grid(row=8,column=1,sticky="w", padx=5)

chb3=Checkbutton(window,text="Hindi",variable=3,bg="lightblue")
chb3.grid(row=9,column=1,sticky="w", padx=5)

#username 
lb8=Label(window,text="UserName", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb8.grid(row=10,column=0,sticky="e",padx=10)
en = Entry(window,)
en.grid(row=10, column=1,sticky="w", padx=5)

#password
lb6=Label(window,text="Password", font=("arial", 16, "bold"), fg="black", bg="lightblue", padx=10, pady=5)
lb6.grid(row=11,column=0,sticky="e",padx=10)
en = Entry(window,)
en.grid(row=11, column=1,sticky="w", padx=5)

#WARNING
def warning():
    messagebox.showinfo("login","Reg successfull")
btn1=Button(window,text="click ",font=("arial", 16, "bold"), fg="black", bg="white", padx=10, pady=5,
command=warning)
btn1.grid(row=12,column=1)
window.mainloop()
