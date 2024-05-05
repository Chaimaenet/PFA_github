import streamlit as st
import sqlite3
from hashlib import sha256

def create_doctor_table_if_not_exists():
    conn = sqlite3.connect('doctor_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS doctors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT,
                 password TEXT)''')
    conn.commit()
    conn.close()

def add_doctor(username, password):
    conn = sqlite3.connect('doctor_info.db')
    c = conn.cursor()
    hashed_password = sha256(password.encode()).hexdigest()
    c.execute('''INSERT INTO doctors (username, password) VALUES (?, ?)''', (username, hashed_password))
    conn.commit()
    conn.close()

def add_doctor_form():
    st.title("Ajouter un Médecin")

    create_doctor_table_if_not_exists()

    username = st.text_input("Nom d'utilisateur", key="username_add_doctor")  # Ajout d'une clé unique
    password = st.text_input("Mot de passe", type="password", key="password_add_doctor")  # Ajout d'une clé unique
    confirm_password = st.text_input("Confirmer le mot de passe", type="password", key="confirm_password_add_doctor")  # Ajout d'une clé unique

    if st.button("Ajouter"):
        if password == confirm_password:
            add_doctor(username, password)
            st.success("Médecin ajouté avec succès")
        else:
            st.error("Les mots de passe ne correspondent pas")

# Utilisation
add_doctor_form()
