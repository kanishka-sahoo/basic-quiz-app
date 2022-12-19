import hashlib as hl
import sqlite3
import time

def register_user(usnm, pswd):
    users = []
    pswd = hl.md5(pswd.encode()).hexdigest()
    time_create = time.time()
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, acc_created) VALUES (?, ?, ?)", 
                (usnm, pswd, time_create))
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
    if result:
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

