'''
Tkinter App
Author: Kanishka Sahoo
Date: 2022/11/30
'''

import tkinter as tk    
import sys
import acc_db_handler as adh
import datetime as dt
import questions_handler as qh
class MainApp():
    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Python Quiz")
        self.master.geometry("1280x720")
        self.master.resizable(False, False)
        self.reg_or_login()
        self.scr = 0
        self.indx = 0

    def reg_or_login(self):
        for i in self.master.winfo_children():
            i.destroy()
        
        reg_login = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        reg_login.grid(row=128, column=70, sticky="NW")
        reg_login.place(x=0, y=0)

        # Adds the Welcome Text
        loggedout = tk.Label(master=reg_login, text="Welcome to Quiz", font=("ariel", 32, "bold"), bg="#d9d9d9")
        loggedout.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        loggedout2 = tk.Label(master=reg_login, text="You are not logged in.", font=("ariel", 24, "bold"), bg="#d9d9d9")
        loggedout2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        login_btn = tk.Button(master=reg_login, text="Login", width=20, font=("ariel", 16, "bold"), command=self.login)
        login_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        reg_btn = tk.Button(master=reg_login, text="Register", width=20, font=("ariel", 16, "bold"), command=self.register)
        reg_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        cred_btn = tk.Button(master=reg_login, text="Credits", width=20, font=("ariel", 16, "bold"), command=self.credits)
        cred_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    
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
                message.set("Password must contain atleast 1 special character")
            elif ";" in pswd:
                message.set("Password not accepted")
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
                self.usr = usr
                self.main_screen()
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

    def credits(self):
        for i in self.master.winfo_children():
            i.destroy()
        credits_body = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        credits_body.grid(row=128, column=70, sticky="NW")
        credits_body.place(x=0, y=0)

        # Title
        cred_title = tk.Label(master=credits_body, text="Credits", font=("ariel", 32, "bold"), bg="#d9d9d9")
        cred_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        # Text
        credits_text = """Kanishka Sahoo: Pretty Much Everything\nBhuvan Anand: ---\nMadhav Nair: ---"""
        cred_text = tk.Label(master=credits_body, text=credits_text,font=("ariel", 24, ), bg="#d9d9d9", height=5, width=52)
        cred_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Back Button
        back_btn = tk.Button(master=credits_body, text="Back", width=10, font=("ariel", 16, "bold"), command=self.reg_or_login)
        back_btn.place(relx=0.1, rely=0.1, anchor=tk.CENTER) 

    def main_screen(self):
        usr = self.usr
        
        for i in self.master.winfo_children():
            i.destroy()

        def do_leaderboard():
            self.leaderboards(usr[0])
        def go_to_start():  # Checks for the neccessary condition to start i.e. all the options are validated.
            if self.ques_no.get().isnumeric():
                if int(self.ques_no.get()) <= 50 or int(self.ques_no.get()) >= 1:
                    if self.sel_cat.get() == "Select Category" or self.sel_diff == "Select Difficulty":
                        prmp_txt.set("Did not enter options")
                    else:
                        self.staging_area()
                else:
                    prmp_txt.set("Number entered out of range")
            else:
                prmp_txt.set("Did not enter a number")
        
        def do_logout():
            self.reg_or_login()
        
        main_screen_body = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        main_screen_body.grid(row=128, column=70, sticky="NW")
        main_screen_body.place(x=0, y=0)

        # display text on successful login
        log_txt = tk.Label(master=main_screen_body, text=f"Welcome, {usr[0]}", font=("ariel", 32, "bold"), bg="#d9d9d9")
        log_txt.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Displays current Score
        score_text = tk.Label(master=main_screen_body, text=f"Score: {usr[2]}", font=("ariel", 32, "bold"), bg="#d9d9d9")
        score_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        # Takes user to logout page
        logout_btn = tk.Button(master=main_screen_body, text="Logout", width=10, font=("ariel", 16, "bold"), command=do_logout)
        logout_btn.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

        # Header of categories selection page
        opts_head = tk.Label(master=main_screen_body, text="Select Category", font=("ariel", 24, "normal"), bg="#d9d9d9")
        opts_head.place(relx=0.1, rely=0.3, anchor=tk.W)

        # Add disclaimer regarding number of categories can only be 1
        catg_discl = tk.Label(master=main_screen_body, text="Note: There can only be one category \nselected at one time.", font=("ariel", 16, "normal"), bg="#d9d9d9")
        catg_discl.place(relx=0.1, rely=0.35, anchor=tk.NW)

        # Category selection menu (dropdown)
        CATEGORIES = [
            "Entertainment: Music",
            "Entertainment: Television",
            "Entertainment: Video Games",
            "Science & Nature",
            "Science: Computers",
            "Science: Mathematics",
            "Sports",
            "Science: Gadgets",
            "Entertainment: Japanese Anime & Manga"
        ]
        self.sel_cat = tk.StringVar()
        self.sel_cat.set("Select Category")

        cat_dd = tk.OptionMenu(main_screen_body, self.sel_cat, *CATEGORIES)
        cat_dd.place(relx=0.1, rely=0.45, anchor=tk.NW)

        # Header of Difficulty selection area
        diff_head = tk.Label(master=main_screen_body, text="Select Difficulty", font=("ariel", 24, "normal"), bg="#d9d9d9")
        diff_head.place(relx=0.6, rely=0.3, anchor=tk.W)
        
        DIFFICULTIES = [
            "Hard",
            "Medium",
            "Easy"
        ]
        self.sel_diff = tk.StringVar()
        self.sel_diff.set("Select Difficulty")

        sel_dd = tk.OptionMenu(main_screen_body, self.sel_diff, *DIFFICULTIES)
        sel_dd.place(relx=0.6, rely=0.45, anchor=tk.NW)

        # Add number of questions slider
        ques_txt = tk.Label(master=main_screen_body, text="Select Questions (1 to 50)", font=("ariel", 24, "normal"), bg="#d9d9d9")
        ques_txt.place(relx=0.6, rely=0.55, anchor=tk.NW)

        self.ques_no = tk.StringVar()
        ques_no_box = tk.Entry(master=main_screen_body, width=10, font=("ariel", 24), textvariable=self.ques_no)
        ques_no_box.place(relx=0.6, rely=0.65, anchor=tk.NW)

        # Leaderboards button
        lebd_btn = tk.Button(master=main_screen_body, text="Leaderboards", width=12, font=("ariel", 16, "bold"), command=do_leaderboard)
        lebd_btn.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

        # Continue Buttton, takes user to staging area
        stg_ar = tk.Button(master=main_screen_body, text="Continue", width=10, font=("ariel", 16, "bold"), command=go_to_start)
        stg_ar.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

        # Prompt text
        prmp_txt = tk.StringVar()
        prmp = tk.Label(master=main_screen_body, textvariable=prmp_txt, bg="#d9d9d9", font=("ariel", 16, "bold"))
        prmp.place(relx=0.6, rely=0.75, anchor=tk.NW)
    
    def leaderboards(self, usr): # To be done

        def do_back():
            leader_board.destroy()
        
        leader_board = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        leader_board.grid(row=128, column=70, sticky="NW")
        leader_board.place(x=0, y=0)

        title_label = tk.Label(master=leader_board, text="Leaderboard", bg="#d9d9d9", font=("ariel", 32, "bold"))
        title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        back_btn = tk.Button(master=leader_board, text="BACK", width=10, font=("ariel", 16, "bold"), command=do_back)
        back_btn.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    def staging_area(self):   # Where rules are explained
        def goback():
            staging_area.destroy()
                
        staging_area = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        staging_area.grid(row=128, column=70, sticky="NW")
        staging_area.place(x=0, y=0)

        head_txt = tk.Label(master=staging_area, text="Confirm: ", font=("ariel", 32, "bold"), bg="#d9d9d9")
        head_txt.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        # Show data for confirmation
        cat_cnf = tk.Label(master=staging_area, text=f"Selected Category: {self.sel_cat.get()}", font=("ariel", 22, ), bg="#d9d9d9")
        cat_cnf.place(relx=0.3, rely=0.3, anchor=tk.W) 
        diff_cnf = tk.Label(master=staging_area, text=f"Selected Difficulty: {self.sel_diff.get()}", font=("ariel", 22, ), bg="#d9d9d9")
        diff_cnf.place(relx=0.3, rely=0.4, anchor=tk.W) 
        quno_cnf = tk.Label(master=staging_area, text=f"Number of Questions: {self.ques_no.get()}", font=("ariel", 22, ), bg="#d9d9d9")
        quno_cnf.place(relx=0.3, rely=0.5, anchor=tk.W)

        back_btn = tk.Button(master=staging_area, text="Back", width=10, font=("ariel", 16, "bold"), command=goback)
        back_btn.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

        confirm_button = tk.Button(master=staging_area, text="Confirm", width=10, font=("ariel", 16, "bold"), command=self.main_quiz)
        confirm_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

    def main_quiz(self): # Main quiz area
        for i in self.master.winfo_children():
            i.destroy()

        def next_question():    # updates the question and options during the quiz
            print(questions[self.indx][1], " : ", val.get())
            if self.indx == len(questions)-1:
                self.end_screen(len(questions))
            elif val.get() == questions[self.indx][1]:
                ans_fb.set("Correct!")
                self.indx = self.indx + 1
                question_text.set(questions[self.indx][0])
                opt1_text.set(questions[self.indx][2][0])
                opt2_text.set(questions[self.indx][2][1])
                opt3_text.set(questions[self.indx][2][2])
                opt4_text.set(questions[self.indx][2][3])
                opt1.config(value = opt1_text.get(), textvariable=opt1_text, variable=val)
                opt2.config(value = opt2_text.get(), textvariable=opt2_text, variable=val)
                opt3.config(value = opt3_text.get(), textvariable=opt3_text, variable=val)
                opt4.config(value = opt4_text.get(), textvariable=opt4_text, variable=val)
                val.set(None)
                self.scr += 1
                qno.set("Q: "+str(self.indx+1))
                score.set("Score: "+str(self.scr))
            else:
                ans_fb.set("Answer: "+questions[self.indx][1])
                self.indx = self.indx + 1
                question_text.set(questions[self.indx][0])
                opt1_text.set(questions[self.indx][2][0])
                opt2_text.set(questions[self.indx][2][1])
                opt3_text.set(questions[self.indx][2][2])
                opt4_text.set(questions[self.indx][2][3])
                opt1.config(value = opt1_text.get(), textvariable=opt1_text, variable=val)
                opt2.config(value = opt2_text.get(), textvariable=opt2_text, variable=val)
                opt3.config(value = opt3_text.get(), textvariable=opt3_text, variable=val)
                opt4.config(value = opt4_text.get(), textvariable=opt4_text, variable=val)
                qno.set("Q: "+str(self.indx+1))


        def check_answer():     # Checks the answer and provides feedback
            if val.get() == questions[self.indx][1]:
                ans_fb.set("Correct")
            else:
                ans_fb.set("Wrong")
        
        
        parameters = {
            "amount": int(self.ques_no.get()),
            "type": "multiple",
            "category": str(qh.get_category(self.sel_cat.get())),
            "difficulty": self.sel_diff.get().lower()
        }

        questions = qh.get_data(parameters)
        main_quiz = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        main_quiz.grid(row=128, column=70, sticky="NW")
        main_quiz.place(x=0, y=0)

        quiz_title = tk.Label(master=main_quiz, text=f"{self.sel_cat.get()}, {self.sel_diff.get()}", font=("ariel", 22, "bold"), bg="#d9d9d9")
        quiz_title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        
        score = tk.StringVar()
        score.set("Score: "+str(self.scr))

        score_text = tk.Label(master=main_quiz, textvariable=score, font=("ariel", 22, "bold"), bg="#d9d9d9")
        score_text.place(relx=0.9, rely=0.05, anchor=tk.CENTER)
        
        qno = tk.StringVar()
        qno.set("Q: "+str(self.indx+1))
        qno_text = tk.Label(master=main_quiz, textvariable=qno, font=("ariel", 22, "bold"), bg="#d9d9d9")
        qno_text.place(relx=0.1, rely=0.05, anchor=tk.W)

        quit_btn = tk.Button(master=main_quiz, text="Quit", width=10, font=("ariel", 16, "bold"), command=self.quit_screen)
        quit_btn.place(relx=0.1, rely=0.9, anchor=tk.CENTER)     

        question_text = tk.StringVar()
        question_text.set(questions[self.indx][0])

        question_ = tk.Label(master=main_quiz, textvariable=question_text, font=("ariel", 22, ), bg="#d9d9d9", justify=tk.LEFT, wraplength=1000)
        question_.place(relx=0.15, rely=0.2, anchor=tk.NW)

        # Add options block 

        val = tk.StringVar()
        val.set(None)
        opt1_text = tk.StringVar()
        opt1_text.set(questions[self.indx][2][0])
        opt1 = tk.Radiobutton(master=main_quiz, textvariable=opt1_text, value=opt1_text.get(), variable = val,font=("ariel", 22, ), bg="#d9d9d9", justify=tk.LEFT)
        opt1.place(relx=0.15, rely=0.4) 
        opt2_text = tk.StringVar()
        opt2_text.set(questions[self.indx][2][1])
        opt2 = tk.Radiobutton(master=main_quiz, textvariable=opt2_text, value=opt2_text.get(), variable = val,font=("ariel", 22, ), bg="#d9d9d9", justify=tk.LEFT)
        opt2.place(relx=0.15, rely=0.5)            
        opt3_text = tk.StringVar()
        opt3_text.set(questions[self.indx][2][2])
        opt3 = tk.Radiobutton(master=main_quiz, textvariable=opt3_text, value=opt3_text.get(), variable = val,font=("ariel", 22, ), bg="#d9d9d9", justify=tk.LEFT)
        opt3.place(relx=0.15, rely=0.6)        
        opt4_text = tk.StringVar()
        opt4_text.set(questions[self.indx][2][3])
        opt4 = tk.Radiobutton(master=main_quiz, textvariable=opt4_text, value=opt4_text.get(), variable = val,font=("ariel", 22, ), bg="#d9d9d9", justify=tk.LEFT)
        opt4.place(relx=0.15, rely=0.7)   

        # Next button
        next_btn = tk.Button(master=main_quiz, text="Next", font=("ariel", 18, ), command=next_question)
        next_btn.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

        # Check Answer Button
        check_btn = tk.Button(master=main_quiz, text="Check", font=("ariel", 18, ), command=check_answer)
        check_btn.place(relx=0.05, rely=0.5, anchor=tk.CENTER)

        # Answer feedback
        ans_fb = tk.StringVar()
        ans_txt = tk.Label(master=main_quiz, textvariable=ans_fb, font=("ariel", 22, ), bg="#d9d9d9", justify=tk.LEFT)
        ans_txt.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    
    def quit_screen(self):

        def do_quit():
            self.main_screen()
        
        def goback():
            q_scr.destroy()
        
        q_scr = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        q_scr.grid(row=128, column=70, sticky="NW")
        q_scr.place(x=0, y=0)

        q_title = tk.Label(master=q_scr, text="Are you sure you want to quit?", font=("ariel", 28, ), bg="#d9d9d9", justify=tk.LEFT)
        q_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        yes_button = tk.Button(master=q_scr, text="Yes", font=("ariel", 18, ), command=do_quit)
        yes_button.place(relx=0.4, rely=0.5, anchor=tk.W)

        no_button = tk.Button(master=q_scr, text="No", font=("ariel", 18, ), command=goback)
        no_button.place(relx=0.6, rely=0.5, anchor=tk.E)
        
    def end_screen(self, tot_qns): # End of quiz, shows score and nav buttons
        for i in self.master.winfo_children():
            i.destroy()

        end_scr = tk.Frame(master=self.master, background="#d9d9d9", width=1280, height=720)
        end_scr.grid(row=128, column=70, sticky="NW")
        end_scr.place(x=0, y=0)

        end_title = tk.Label(master=end_scr, text="Quiz Completed", font=("ariel", 32, ), bg="#d9d9d9", justify=tk.LEFT)
        end_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        scr_lbl = tk.Label(master=end_scr, text=f"Score: {self.scr}/{tot_qns}", font=("ariel", 28, ), bg="#d9d9d9", justify=tk.LEFT)
        scr_lbl.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


# Run the actual app
root = tk.Tk()
MainApp(root)
root.mainloop()