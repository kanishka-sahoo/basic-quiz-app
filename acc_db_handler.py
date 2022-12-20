import hashlib as hl
import sqlite3
import time

def register_user(usnm, pswd):
    users = []
    pswd = hl.md5(pswd.encode()).hexdigest()    # Converts the password to md5 hash
    time_create = time.time()
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, acc_created) VALUES (?, ?, ?)", 
                (usnm, pswd, time_create))  # Stores the user data into the db
    conn.commit()
    conn.close()

def login_user(usnm, pswd):
    users = []
    pswd = hl.md5(pswd.encode()).hexdigest()
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (usnm, pswd))
    result = c.fetchone()
    conn.close()
    if result:  # If user is present
        conn.close()
        return True, result
    else:
        return False, result

def is_user_present(usnm):
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (usnm, ))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def logout(usnm):
    curr_time = time.time()
    print(curr_time)
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute(f"UPDATE users SET last_played=? WHERE username=?", (curr_time, usnm))
    res = c.fetchone()
    c.execute("SELECT * FROM users WHERE username=?", (usnm, ))
    result = c.fetchone()
    conn.close()