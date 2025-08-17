import os
import sqlite3
import pickle
import subprocess
import jwt

# ------------------ Command Injection ------------------
def list_files(directory):
    os.system("ls " + directory)  # Vulnerable to injection via unsanitized input

# ------------------ SQL Injection ------------------
def get_user_info(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Vulnerable
    cursor.execute(query)
    return cursor.fetchall()
# this is a comment




# ------------------ Unsafe Deserialization ------------------
def load_profile(pickled_data):
    return pickle.loads(pickled_data)  # Arbitrary code execution risk

# ------------------- Subprocess Shell Injection -------------------
def ping_host(host):
    return subprocess.call(f"ping -c 1 {host}", shell=True)  # Dangerous use of shell=True