import streamlit as st
import pandas as pd
from datetime import datetime
import os
import hashlib

st.set_page_config(page_title="Afri.T.A - Chien", page_icon="🐕", layout="wide")

st.markdown("""
<style>
h1, h2, h3, p, label { color: white; }
.stTextInput > div > div > input, .stSelectbox > div > div, .stNumberInput > div > div { background-color: #2a2a2a; color: white; border: 1px solid #2196f3; }
.stButton > button { background: linear-gradient(90deg, #2196f3, #1976d2); color: white; border: none; border-radius: 50px; }
.info-box { background: #1e1e1e; padding: 1rem; border-radius: 10px; border-left: 4px solid #2196f3; margin: 1rem 0; }
.success-box { background: #1e1e1e; padding: 1rem; border-radius: 10px; border-left: 4px solid #2196f3; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

st.title("🐕 Transport pour Chien")

# ==================== TOUS LES PAYS D'AFRIQUE ====================
pays_afrique = [
    "Algérie", "Angola", "Bénin", "Botswana", "Burkina Faso", "Burundi",
    "Cameroun", "Cap-Vert", "République Centrafricaine", "Comores", "Congo",
    "République Démocratique du Congo", "Côte d'Ivoire", "Djibouti", "Égypte",
    "Érythrée", "Eswatini", "Éthiopie", "Gabon", "Gambie", "Ghana",
    "Guinée", "Guinée-Bissau", "Guinée Équatoriale", "Kenya", "Lesotho",
    "Liberia", "Libye", "Madagascar", "Malawi", "Mali", "Maroc",
    "Maurice", "Mauritanie", "Mozambique", "Namibie", "Niger", "Nigéria",
    "Ouganda", "Rwanda", "Sao Tomé-et-Principe", "Sénégal", "Seychelles",
    "Sierra Leone", "Somalie", "Soudan", "Soudan du Sud", "Tanzanie",
    "Tchad", "Togo", "Tunisie", "Zambie", "Zimbabwe", "Afrique du Sud"
]

# ==================== DISTANCES CONNUES ====================
distances_connues = {
    ("Cameroun", "Gabon"): 850, ("Cameroun", "Congo"): 1200,
    ("Cameroun", "République Centrafricaine"): 900, ("Cameroun", "Tchad"): 1100,
    ("Cameroun", "Guinée Équatoriale"): 350, ("Cameroun", "Nigéria"): 600,
    ("Cameroun", "Sénégal"): 3200, ("Cameroun", "Côte d'Ivoire"): 2500,
    ("Cameroun", "Mali"): 2800, ("Cameroun", "Burkina Faso"): 2400,
    ("Cameroun", "Niger"): 1500, ("Gabon", "Cameroun"): 850,
    ("Gabon", "Congo"): 900, ("Congo", "Cameroun"): 1200,
    ("Congo", "Gabon"): 900, ("Nigéria", "Cameroun"): 600,
    ("Nigéria", "Gabon"): 1100, ("Nigéria", "Congo"): 1400,
    ("République Centrafricaine", "Cameroun"): 900, ("Tchad", "Cameroun"): 1100,
}

def calculer_distance(depart, arrivee):
    if depart == arrivee:
        return 0
    return distances_connues.get((depart, arrivee))

# ==================== RACES ====================
races = {"Berger Allemand": 1.0, "Golden Retriever": 1.1, "Buldog Français": 1.5, "Caniche": 1.3, "Husky": 1.25}

st.subheader("👤 Vos informations")
col1, col2 = st.columns(2)
with col1:
    nom_client = st.text_input("Nom complet", key="chien_nom")
    email = st.text_input("Email", key="chien_email")
with col2:
    telephone = st.text_input("Téléphone", key="chien_tel")
    adresse = st.text_input("Adresse", key="chien_adresse")

st.subheader("📍 Informations transport")
col3, col4 = st.columns(2)
with col3:
    liste_races = list(races.keys()) + ["✏️ Autre race (précisez)"]
    race_choisie = st.selectbox("Race", liste_races, key="chien_race")
    
    if race_choisie == "✏️ Autre race (précisez)":
        autre_race = st.text_input("Précisez la race", placeholder="Ex: Berger Australien", key="chien_autre_race")
        categorie_race = st.radio("Catégorie", ["Standard", "Premium (+30%)", "Très rare (+60%)"], key="chien_categorie")
        if categorie_race == "Standard":
            coeff_race = 1.0
        elif categorie_race == "Premium (+30%)":
            coeff_race = 1.3
        else:
            coeff_race = 1.6
        race_affichee = autre_race if autre_race else "Race personnalisée"
    else:
        coeff_race = races[race_choisie]
        race_affichee = race_choisie
    
    poids = st.number_input("Poids (kg)", min_value=1.0, max_value=100.0, value=10.0, step=1.0, key="chien_poids")
with col4:
    pays_depart = st.selectbox("Pays de départ", pays_afrique, key="chien_depart")
    pays_arrivee = st.selectbox("Pays d'arrivée", pays_afrique, key="chien_arrivee")

distance = calculer_distance(pays_depart, pays_arrivee)
tarif_base = 15

if distance is not None:
    prix = distance * poids * tarif_base * coeff_race
    st.markdown(f'<div class="info-box">📏 Distance estimée : <strong>{distance} km</strong></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="success-box">💰 Prix total : <strong>{int(prix):,} FCFA</strong></div>', unsafe_allow_html=True)
    
    if st.button("✅ Générer ma facture", use_container_width=True, key="chien_generer"):
        if nom_client and telephone:
            numero_facture = f"AFR-{datetime.now().strftime('%Y%m%d%H%M%S')}-{hashlib.md5(str(prix).encode()).hexdigest()[:4]}"
            data_file = "factures.csv"
            if not os.path.exists(data_file):
                pd.DataFrame(columns=["Numero", "Date", "Client", "Telephone", "Email", "Animal", "Race", "Poids", "Depart", "Arrivee", "Distance", "Prix", "Statut"]).to_csv(data_file, index=False)
            nouvelle_facture = pd.DataFrame([{"Numero": numero_facture, "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Client": nom_client, "Telephone": telephone, "Email": email, "Animal": "Chien", "Race": race_affichee, "Poids": poids, "Depart": pays_depart, "Arrivee": pays_arrivee, "Distance": distance, "Prix": int(prix), "Statut": "En attente paiement"}])
            nouvelle_facture.to_csv(data_file, mode="a", header=False, index=False)
            st.session_state.facture_numero = numero_facture
            st.session_state.facture_prix = int(prix)
            st.session_state.facture_client = nom_client
            st.session_state.facture_animal = "Chien"
            st.session_state.facture_race = race_affichee
            st.success(f"✅ Facture générée ! Numéro : {numero_facture}")
            st.balloons()
            if st.button("📄 Voir ma facture", key="chien_voir_facture"):
                st.switch_page("pages/facture.py")
        else:
            st.warning("Veuillez remplir votre nom et téléphone")
else:
    st.warning("🌍 **Devis personnalisé** - Contactez-nous pour ce trajet. Nous vous répondrons sous 24h.")
