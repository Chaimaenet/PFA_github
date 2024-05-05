# fichier login.py

import streamlit as st
import sqlite3
from hashlib import sha256

def verify_credentials(username, password):
    conn = sqlite3.connect('doctor_info.db')
    c = conn.cursor()
    hashed_password = sha256(password.encode()).hexdigest()
    c.execute('''SELECT * FROM doctors WHERE username = ? AND password = ?''', (username, hashed_password))
    result = c.fetchone()
    conn.close()
    return result is not None

def login():
    st.title("Page de Connexion pour le Médecin")

    # Si les informations de connexion sont déjà stockées dans la session, utilisez-les
    if 'connected' in st.session_state:
        if st.session_state.connected:
            return True, st.session_state.username

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if verify_credentials(username, password):
            st.success("Connexion réussie")
            st.session_state.connected = True  # Stocke l'état de connexion dans la session
            st.session_state.username = username  # Stocke le nom d'utilisateur dans la session
            return True, username
        else:
            st.error("Identifiants incorrects")
            return False, None

    return False, None
