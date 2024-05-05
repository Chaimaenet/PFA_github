# app.py
import streamlit as st
from login import login
from add_doctor import add_doctor
from backend import predict_avc  # Importer la fonction de prédiction

def main():
    st.title("Système de Prédiction d'AVC")

    # Ajouter le médecin Moncef Kachouri s'il n'existe pas déjà
    add_doctor("Moncef Kachouri", "13646203")

    # Récupérer la connexion de l'utilisateur
    connected, username = login()

    # Si l'utilisateur n'est pas connecté, afficher la page de connexion
    if not connected:
        return

    # Afficher le nom de l'utilisateur connecté
    st.write(f"Connecté en tant que : {username}")

    # Initialisation de st.session_state.form_filled s'il n'existe pas
    if 'form_filled' not in st.session_state:
        st.session_state.form_filled = False

    if not st.session_state.form_filled:
        # Afficher le formulaire de saisie des données du patient
        st.header("Formulaire de Saisie des Données du Patient")
        nom_patient = st.text_input("Nom du patient")
        cin_patient = st.text_input("CIN du patient")
        age_patient = st.number_input("Âge du patient", min_value=0)
        taux_glycemie = st.number_input("Taux de glycémie", min_value=0.0)
        taux_cholesterol = st.number_input("Taux de cholestérol", min_value=0.0)
        fumeur = st.radio("Fumeur", options=["Oui", "Non"])

        if st.button("Valider"):
            # Vérifier si tous les champs sont remplis
            if nom_patient and cin_patient and age_patient and taux_glycemie and taux_cholesterol:
                st.session_state.form_filled = True
                st.success("Formulaire validé avec succès !")
                # Passer à l'interface de prédiction
                interface_prediction(nom_patient, cin_patient, age_patient, taux_glycemie, taux_cholesterol, fumeur)
            else:
                st.error("Veuillez remplir tous les champs obligatoires du formulaire.")
    else:
        interface_prediction()

def interface_prediction(nom_patient=None, cin_patient=None, age_patient=None, taux_glycemie=None, taux_cholesterol=None, fumeur=None):
    st.subheader("Interface de Prédiction d'AVC")

    if nom_patient is not None:
        # Afficher les données du patient
        st.write(f"Nom du patient : {nom_patient}")
        st.write(f"CIN du patient : {cin_patient}")
        st.write(f"Âge du patient : {age_patient}")
        st.write(f"Taux de glycémie : {taux_glycemie}")
        st.write(f"Taux de cholestérol : {taux_cholesterol}")
        st.write(f"Fumeur : {fumeur}")

    # Ajouter le formulaire de téléchargement de l'image MRI
    uploaded_file = st.file_uploader("Télécharger une image MRI", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Afficher l'image MRI
        st.image(uploaded_file, caption="Image MRI")

        # Ajouter le bouton de prédiction
        if st.button("Voir le résultat"):
            rec = predict_avc(uploaded_file)
            if rec is not None:
                if rec > 0.5:
                    st.error("Le patient est atteint d'un AVC !")
                else:
                    st.success("Le patient est sain.")

if __name__ == "__main__":
    main()
