#!/usr/bin/python3

import sqlite3

con = sqlite3.connect(f"{input('Enter the database to be hacked: ')}")
cur = con.cursor()

password = input("Enter a new password for the admin account: ")
cur.execute("""
            UPDATE "users" SET "password" = ? WHERE "username" = 'admin';
            """, password)
con.commit()
con.close()
print("Hacked!")
