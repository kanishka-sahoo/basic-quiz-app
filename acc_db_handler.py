"""
Account Database Handler:
Interfaces with the accounts.db database and provides an intermediate layer between app and db.
Author: Kanishka Sahoo
"""
import hashlib as hl
import sqlite3
import time

def register_user(usnm, pswd):  # add user data to table
    pswd = hl.md5(pswd.encode()).hexdigest()    # Converts the password to md5 hash using hashlib
    time_create = time.time()
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, acc_created) VALUES (?, ?, ?)", 
                (usnm, pswd, time_create))  # Stores the user data into the db
    conn.commit()
    conn.close()

def login_user(usnm, pswd): # performs login of user by checking both username ans password
    pswd = hl.md5(pswd.encode()).hexdigest()
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (usnm, pswd))
    result = c.fetchone()
    conn.close()
    if result:  # If user is present
        return True, result
    else:
        return False, result

def is_user_present(usnm):  # checks if user exists in table
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (usnm, ))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def get_leaderboard(usnm):  # computes the rank of all users in table and returns top 5
    leaderboard = []
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users ORDER BY score DESC, total_questions ASC")
    result = c.fetchall()
    length = len(result)
    leaderboard = result[:min(5, length):]
    c.execute("SELECT * FROM users WHERE username=?", (usnm, ))
    user = c.fetchone()
    leaderboard = list(dict.fromkeys(leaderboard))
    conn.close()
    return leaderboard, user, leaderboard.index(user)

def update_score(usnm, score, tot_qns): # changes score after completion of quiz
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (usnm, ))
    row = c.fetchone()
    c.execute("UPDATE users SET score=?, total_questions=? WHERE username=?", (score+int(row[2]), tot_qns+int(row[3]), usnm))
    result = c.fetchall()
    conn.commit()
    conn.close()

def get_user_details(usnm): # just gets the user details given username
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (usnm, ))
    row = c.fetchone()
    conn.close()
    return row