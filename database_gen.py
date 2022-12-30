import sqlite3

conn = sqlite3.connect('accounts.db') 
c = conn.cursor()

c.execute('''
            DROP TABLE IF EXISTS users;
            ''')


c.execute('''
          CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY, 
            password TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            total_questions INTEGER DEFAULT 0,
            acc_created INTEGER DEFAULT 0);
          ''')

conn.commit()