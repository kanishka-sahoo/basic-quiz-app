'''
Tkinter App
Author: Kanishka Sahoo
Date: 2022/11/30
'''

import tkinter as tk    
import sys
import acc_db_handler as adh
import datetime as dt

class MainApp():
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Python Quiz")
        self.master.geometry("1280x720")
        self.reg_or_login()

    def reg_or_login(self):
        for i in self.master.winfo_children():
            i.destroy()
        
        reg_login = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        reg_login.grid(row=128, column=70, sticky="NW")
        reg_login.place(x=0, y=0)

        loggedout = tk.Label(master=reg_login, text="Welcome to Quiz", font=("ariel", 32, "bold"), bg="#d9d9d9")
        loggedout.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        loggedout2 = tk.Label(master=reg_login, text="You are not logged in.", font=("ariel", 24, "bold"), bg="#d9d9d9")
        loggedout2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        login_btn = tk.Button(master=reg_login, text="Login", width=10, font=("ariel", 16, "bold"), command=self.login)
        login_btn.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

        reg_btn = tk.Button(master=reg_login, text="Register", width=10, font=("ariel", 16, "bold"), command=self.register)
        reg_btn.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()

        message = tk.StringVar()
        
        def createUser():
            usnm = username.get()
            pswd = password.get()
            pswd2 = password_cnf.get()

            # Validate username and password
            if usnm == '' or password == '' or password_cnf == '':
                message.set("Please Enter Details")
            elif not usnm.isalnum():
                message.set("Username can only be letters or numbers")
            elif len(usnm) < 6:
                message.set("Username must be longer than 6 characters")
            elif adh.is_user_present(usnm=usnm):
                message.set("User already exists")
            elif pswd != pswd2:
                message.set("Passwords don't match")
            elif len(pswd) < 6:
                message.set("Password must be 6 characters or more")
            elif pswd.isalnum():
                message.set("Password must contain atleast 1 special characteer")
            else:
                adh.register_user(usnm=usnm, pswd=pswd)
                self.login()
                
        reg_page = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        reg_page.grid(row=128, column=70, sticky="NW")
        reg_page.place(x=0, y=0)

        # Shows sign up text
        log_txt = tk.Label(master=reg_page, text="Sign Up", font=("ariel", 32, "bold"), bg="#d9d9d9")
        log_txt.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        # username field
        usrnm_lbl = tk.Label(master=reg_page, text="Username:", font=("ariel", 24, "bold"), bg="#d9d9d9")
        usrnm_lbl.place(relx=0.27, rely=0.35, anchor=tk.E)
        username = tk.StringVar()
        usrnm = tk.Entry(master=reg_page, width=30, font=("ariel", 24), textvariable=username)
        usrnm.place(relx=0.28, rely=0.35, anchor=tk.W)

        # password field
        pswd_lbl = tk.Label(master=reg_page, text="Password:", font=("ariel", 24, "bold"), bg="#d9d9d9")
        pswd_lbl.place(relx=0.27, rely=0.45, anchor=tk.E)
        password = tk.StringVar()
        pswd = tk.Entry(master=reg_page, width=30, show='', font=("ariel", 24), textvariable=password)
        pswd.place(relx=0.28, rely=0.45, anchor=tk.W)

        # confirm password field
        pswd_cnf_lbl = tk.Label(master=reg_page, text="Confirm:", font=("ariel", 24, "bold"), bg="#d9d9d9")
        pswd_cnf_lbl.place(relx=0.27, rely=0.55, anchor=tk.E)
        password_cnf = tk.StringVar()
        pswd = tk.Entry(master=reg_page, width=30, show='', font=("ariel", 24), textvariable=password_cnf)
        pswd.place(relx=0.28, rely=0.55, anchor=tk.W)

        # Register Button
        login_btn = tk.Button(master=reg_page, text="Register", width=10, font=("ariel", 16, "bold"), command=createUser)
        login_btn.place(relx=0.705, rely=0.65, anchor=tk.E)

        # Back Button
        back_btn = tk.Button(master=reg_page, text="Back", width=10, font=("ariel", 16, "bold"), command=self.reg_or_login)
        back_btn.place(relx=0.1, rely=0.1, anchor=tk.CENTER)   

        # Validate User:
        val_usr = tk.Label(master=reg_page, textvariable=message, font=("ariel", 24, "bold"), bg="#d9d9d9")
        val_usr.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def login(self):
        # Destroys all the elements of root (master) before creating new ones
        for i in self.master.winfo_children():
            i.destroy()

        message = tk.StringVar()

        def validateLogin():
            usnm = username.get()
            pswd = password.get()
            isCorrect, usr = adh.login_user(usnm=usnm, pswd=pswd)
            if usnm == '' or password == '':
                message.set("Please Enter Details")
            elif isCorrect:
                self.main_screen(usr)
            else:
                message.set("Username and/or password is wrong")

        def toggle_pswd():
            if pswd.cget('show') == '•':
                pswd.config(show='')
            else:
                pswd.config(show='•')
        
        # Create frame to cover the screen
        login_body = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        login_body.grid(row=128, column=70, sticky="NW")
        login_body.place(x=0, y=0)

        # Shows sign in text
        log_txt = tk.Label(master=login_body, text="Sign In", font=("ariel", 32, "bold"), bg="#d9d9d9")
        log_txt.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        # username field
        usrnm_lbl = tk.Label(master=login_body, text="Username:", font=("ariel", 24, "bold"), bg="#d9d9d9")
        usrnm_lbl.place(relx=0.27, rely=0.35, anchor=tk.E)
        username = tk.StringVar()
        usrnm = tk.Entry(master=login_body, width=30, font=("ariel", 24), textvariable=username)
        usrnm.place(relx=0.28, rely=0.35, anchor=tk.W)

        # password field
        pswd_lbl = tk.Label(master=login_body, text="Password:", font=("ariel", 24, "bold"), bg="#d9d9d9")
        pswd_lbl.place(relx=0.27, rely=0.45, anchor=tk.E)
        password = tk.StringVar()
        pswd = tk.Entry(master=login_body, width=27, show='•', font=("ariel", 24), textvariable=password)
        pswd.place(relx=0.28, rely=0.45, anchor=tk.W)

        # Show/Hide Password
        tog_pwd = tk.Button(master=login_body, text='👁', font=("ariel", 16, "bold"), bg="#d9d9d9", command=toggle_pswd, width=3)
        tog_pwd.place(relx = 0.67, rely=0.45, anchor=tk.W)

        # Login Button
        login_btn = tk.Button(master=login_body, text="Login", width=10, font=("ariel", 16, "bold"), command=validateLogin)
        login_btn.place(relx=0.715, rely=0.55, anchor=tk.E)

        # Back Button
        back_btn = tk.Button(master=login_body, text="Back", width=10, font=("ariel", 16, "bold"), command=self.reg_or_login)
        back_btn.place(relx=0.1, rely=0.1, anchor=tk.CENTER) 

        # Validate User:
        val_usr = tk.Label(master=login_body, textvariable=message, font=("ariel", 24, "bold"), bg="#d9d9d9")
        val_usr.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def main_screen(self, usr):
        for i in self.master.winfo_children():
            i.destroy()

        main_screen_body = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        main_screen_body.grid(row=128, column=70, sticky="NW")
        main_screen_body.place(x=0, y=0)

        # display text on successful login
        log_txt = tk.Label(master=main_screen_body, text=f"Welcome, {usr[0]}", font=("ariel", 32, "bold"), bg="#d9d9d9")
        log_txt.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        parsed_time = dt.datetime.fromtimestamp(float(usr[-1]))
        acc_ctn = tk.Label(master=main_screen_body, text=f"Account created: {parsed_time}", font=("ariel", 16, "bold"), bg="#d9d9d9")
        acc_ctn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Takes user to logout page
        logout_btn = tk.Button(master=main_screen_body, text="Logout", width=10, font=("ariel", 16, "bold"), command=self.reg_or_login)
        logout_btn.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

        # Header of categories selection page
        opts_head = tk.Label(master=main_screen_body, text="Select Categories", font=("ariel", 24, "normal"), bg="#d9d9d9")
        opts_head.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

        # Start Buttton, takes user to staging area, where rules are shown
        stg_ar = tk.Button(master=main_screen_body, text="Start", width=10, font=("ariel", 16, "bold"))
        stg_ar.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

# Run the actual app
root = tk.Tk()
MainApp(root)
root.mainloop()