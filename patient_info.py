import streamlit as st

def patient_info_form():
    st.title("Formulaire de Saisie des Données du Patient")

    name = st.text_input("Nom du patient")
    cin = st.text_input("CIN du patient")
    age = st.number_input("Âge du patient", min_value=0, step=1)  # Correction : Champ numérique pour l'âge
    hypertension = st.radio("Niveau d'hypertension", ["Normal", "Élevé"])
    glycemia = st.number_input("Taux de glycémie", min_value=0.0, step=0.01)  # Correction : Utilisation de 0.0 au lieu de 0
    smoker = st.radio("Fumeur", ["Oui", "Non"])
    weight = st.number_input("Poids (kg)", min_value=0.0, step=0.1)  # Correction : Utilisation de 0.0 au lieu de 0
    cholesterol = st.number_input("Cholestérol (mg/dL)", min_value=0.0, step=1.0)  # Correction : Utilisation de 0.0 au lieu de 0

    if st.button("Suivant"):
        if name.strip() and cin.strip():  # Vérifie si les champs obligatoires ne sont pas vides
            return {
                "name": name,
                "cin": cin,
                "age": age,
                "hypertension": hypertension,
                "glycemia": glycemia,
                "smoker": smoker,
                "weight": weight,
                "cholesterol": cholesterol
            }, True  # Retourne les données du patient et un drapeau pour indiquer que l'étape est terminée
        else:
            st.error("Veuillez remplir tous les champs obligatoires.")  # Affiche un message d'erreur si des champs obligatoires sont vides

    return None, False  # Si le bouton n'est pas cliqué ou si des champs sont vides, retourne des valeurs par défaut
