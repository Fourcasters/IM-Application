from tkinter import *
import tkinter as tk
from tkinter import messagebox
import bcrypt
import sqlite3

app = tk.Tk()
app.title("Login System")
app.geometry("300x250")
label = Label(app, text="Welcome To App")
label.place(x=95, y=40),

database = sqlite3.connect("user.db")
# cursor = database.cursor()

login_username = tk.StringVar()
login_password = tk.StringVar()


def login():
    loginWindow = Toplevel(app)
    loginWindow.title("Login with python")
    loginWindow.geometry("300x250")
    log_label = Label(loginWindow, text="Login with username and password")
    log_label.place(x=35, y=40)

    usernameE = Entry(loginWindow, relief=FLAT, textvariable=login_username)
    usernameE.place(x=70, y=80)
    passwordE = Entry(loginWindow, show='*', relief=FLAT, textvariable=login_password)
    passwordE.place(x=70, y=120)

    submit = Button(loginWindow, text="Submit",
                    pady=5, padx=20, command=login_database)
    submit.place(x=85, y=150)


reg_username = tk.StringVar()
reg_password = tk.StringVar()


def register():
    registerWindow = Toplevel(app)
    registerWindow.title("Login with python")
    registerWindow.geometry("300x250")
    reg_label = Label(registerWindow, text="Register with username and password")
    reg_label.place(x=35, y=40)
    username = Entry(registerWindow, textvar=reg_username, relief=FLAT, )
    username.place(x=70, y=80)
    password = Entry(registerWindow, show='*', relief=FLAT, textvar=reg_password)
    password.place(x=70, y=120)

    submit = Button(registerWindow, text="Submit",
                    pady=5, padx=20, command=reg_database)
    submit.place(x=85, y=150)


def reg_database():
    username = reg_username.get()
    password = reg_password.get()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    conn = sqlite3.connect("user.db")
    with conn:
        cursor = conn.cursor()
        try:
            cursor.execute('CREATE TABLE IF NOT EXISTS users(Username TEXT, Password TEXT)')
            cursor.execute('INSERT INTO users(Username,Password) VALUES(?,?)', (username, hashed))
            conn.commit()

            messagebox.showinfo("Successfully", "Username Was Added")

        except:
            messagebox.showerror("Commit error", "Could not commit user to database. Please try again")


def login_database():
    username = login_username.get()
    password = login_password.get()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    conn = sqlite3.connect("user.db")
    with conn:
        cursor = conn.cursor()
        try:
            find_user = 'SELECT * FROM users WHERE Username = ?'
            cursor.execute(find_user, [username])
            result = cursor.fetchall()
            user = bcrypt.checkpw(password.encode(), result[0][1])
            if result:
                if user:
                    messagebox.showinfo("Successfully", "Login successful")
                else:
                    messagebox.showwarning("Login Error", "Wrong username or password")
            else:
                messagebox.showwarning("User not found", "Could not find user from database. Please try again")
        except:
            messagebox.showwarning("User not found", "Could not find user from database. Please try again")


login = Button(app, text="Login",
               pady=5, padx=30, command=login)
login.place(x=100, y=100)
btn_register = Button(app, text="Register", pady=5, padx=20, command=register)
btn_register.place(x=100, y=150)

app.mainloop()
