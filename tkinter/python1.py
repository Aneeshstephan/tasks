#username,password login page
from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("First Login Page")
window.geometry("500x500")

lb1 = Label(window, text="User Name", font=("Arial", 16, "bold"), fg="white", bg="Cyan",
            padx=20, pady=10, borderwidth=5, relief="ridge")
lb1.grid(row=0, column=0, padx=10, pady=10)

en1 = Entry(window)
en1.grid(row=0, column=1, padx=10, pady=10)

lb2 = Label(window, text="Password", font=("Arial", 16, "bold"), fg="white", bg="Cyan",
            padx=20, pady=10, borderwidth=5, relief="ridge")
lb2.grid(row=1, column=0, padx=10, pady=10)

en2 = Entry(window)
en2.grid(row=1, column=1, padx=10, pady=10)
def hello():
    messagebox.showinfo("login","login successfull")

btn1 = Button(window, text="Login", font=("Arial", 16, "bold"), fg="white", bg="Cyan",
              padx=20, pady=10, borderwidth=5, relief="raised", activeforeground="lightblue",
              activebackground="red", cursor="hand2", command=hello)
btn1.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
