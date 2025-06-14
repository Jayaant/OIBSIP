from tkinter import *
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1080x720")
        self.root.configure(bg="lightblue")

        Framelogin = Frame(self.root, bg="coral")
        Framelogin.place(x=330, y=150, width=500, height=400)

        title = Label(Framelogin, text="User Login", font=("Helvetica", 38, "bold"), fg="black", bg="coral")
        title.place(x=118, y=30)

        subtitle = Label(Framelogin, text="Enter User ID and Password", font=("Helvetica", 10, "bold"), fg="black", bg="coral")
        subtitle.place(x=160, y=100)

        # Username code
        lbluser = Label(Framelogin, text="User ID", font=("Helvetica", 18, "bold"), fg="black", bg="coral")
        lbluser.place(x=60, y=150)
        self.username = Entry(Framelogin, font=("Helvetica", 14), bg="#CD5C5C")
        self.username.place(x=60, y=180, width=320, height=35)

        # Password code
        lblpass = Label(Framelogin, text="Password", font=("Helvetica", 18, "bold"), fg="black", bg="coral")
        lblpass.place(x=60, y=230)
        self.password = Entry(Framelogin, font=("Helvetica", 14), bg="#CD5C5C", show="*")
        self.password.place(x=60, y=260, width=320, height=35)

        # Button code
        submit = Button(Framelogin, command=self.check_function, text="Login", bd=0,
                        font=("Helvetica", 18, "bold"), fg="black", bg="#CD5C5C")
        submit.place(x=210, y=320)

    def check_function(self):
        if self.username.get()=="" or self.password.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.root)
        elif self.username.get() != "Oasis" or self.password.get() != "12345678":
            messagebox.showerror("Error!", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root = Tk()
obj = Login(root)
root.mainloop()
