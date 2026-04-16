import streamlit as st
import pandas as pd
from datetime import datetime
import os
import hashlib

st.set_page_config(page_title="Afri.T.A - Oiseau", page_icon="🐦", layout="wide")

st.markdown("""
<style>
h1, h2, h3, p, label { color: white; }
.stTextInput > div > div > input, .stSelectbox > div > div, .stNumberInput > div > div { background-color: #2a2a2a; color: white; border: 1px solid #00bcd4; }
.stButton > button { background: linear-gradient(90deg, #00bcd4, #0097a7); color: white; border: none; border-radius: 50px; }
.info-box { background: #1e1e1e; padding: 1rem; border-radius: 10px; border-left: 4px solid #00bcd4; margin: 1rem 0; }
.success-box { background: #1e1e1e; padding: 1rem; border-radius: 10px; border-left: 4px solid #00bcd4; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

st.title("🐦 Transport pour Oiseau")

races = {"Perruche": 1.0, "Perroquet Gris": 2.0, "Ara": 2.5, "Canari": 1.0}

st.subheader("👤 Vos informations")
col1, col2 = st.columns(2)
with col1:
    nom_client = st.text_input("Nom complet", key="oiseau_nom")
    email = st.text_input("Email", key="oiseau_email")
with col2:
    telephone = st.text_input("Téléphone", key="oiseau_tel")
    adresse = st.text_input("Adresse", key="oiseau_adresse")

st.subheader("📍 Informations transport")
col3, col4 = st.columns(2)
with col3:
    liste_races = list(races.keys()) + ["✏️ Autre race (précisez)"]
    race_choisie = st.selectbox("Race", liste_races, key="oiseau_race")
    
    if race_choisie == "✏️ Autre race (précisez)":
        autre_race = st.text_input("Précisez la race de votre oiseau", placeholder="Ex: Cacatoès, Amazone, etc.", key="oiseau_autre_race")
        categorie_race = st.radio("Catégorie de la race", ["Standard (prix normal)", "Premium (+30%)", "Très rare (+60%)"], key="oiseau_categorie")
        if categorie_race == "Standard (prix normal)":
            coeff_race = 1.0
        elif categorie_race == "Premium (+30%)":
            coeff_race = 1.3
        else:
            coeff_race = 1.6
        race_affichee = autre_race if autre_race else "Race personnalisée"
    else:
        coeff_race = races[race_choisie]
        race_affichee = race_choisie
    
    poids = st.number_input("Poids (kg)", min_value=0.1, max_value=10.0, value=0.5, step=0.1, key="oiseau_poids")
with col4:
    pays_depart = st.selectbox("Pays de départ", ["Cameroun", "Gabon", "Congo", "Tchad", "Nigéria"], key="oiseau_depart")
    pays_arrivee = st.selectbox("Pays d'arrivée", ["Cameroun", "Gabon", "Congo", "Tchad", "Nigéria"], key="oiseau_arrivee")

distances = {("Cameroun","Gabon"):850, ("Cameroun","Congo"):1200, ("Cameroun","Tchad"):1100, ("Cameroun","Nigéria"):600}
distance = distances.get((pays_depart, pays_arrivee), 800)

tarif_base = 8
prix = distance * poids * tarif_base * coeff_race

st.markdown(f'<div class="info-box">📏 Distance estimée : <strong>{distance} km</strong></div>', unsafe_allow_html=True)
st.markdown(f'<div class="success-box">💰 Prix total : <strong>{int(prix):,} FCFA</strong></div>', unsafe_allow_html=True)

if st.button("✅ Générer ma facture", use_container_width=True, key="oiseau_generer"):
    if nom_client and telephone:
        numero_facture = f"AFR-{datetime.now().strftime('%Y%m%d%H%M%S')}-{hashlib.md5(str(prix).encode()).hexdigest()[:4]}"
        
        data_file = "factures.csv"
        if not os.path.exists(data_file):
            pd.DataFrame(columns=["Numero", "Date", "Client", "Telephone", "Email", "Animal", "Race", "Coeff", "Poids", "Depart", "Arrivee", "Distance", "Prix", "Statut"]).to_csv(data_file, index=False)
        
        nouvelle_facture = pd.DataFrame([{"Numero": numero_facture, "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Client": nom_client, "Telephone": telephone, "Email": email, "Animal": "Oiseau", "Race": race_affichee, "Coeff": coeff_race, "Poids": poids, "Depart": pays_depart, "Arrivee": pays_arrivee, "Distance": distance, "Prix": int(prix), "Statut": "En attente paiement"}])
        nouvelle_facture.to_csv(data_file, mode="a", header=False, index=False)
        
        st.session_state.facture_numero = numero_facture
        st.session_state.facture_prix = int(prix)
        st.session_state.facture_client = nom_client
        st.session_state.facture_animal = "Oiseau"
        st.session_state.facture_race = race_affichee
        
        st.success(f"✅ Facture générée ! Numéro : {numero_facture}")
        st.balloons()
        
        if st.button("📄 Voir ma facture", key="oiseau_voir_facture"):
            st.switch_page("pages/facture.py")
    else:
        st.warning("Veuillez remplir votre nom et téléphone")
