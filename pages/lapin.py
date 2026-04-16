import streamlit as st
import pandas as pd
from datetime import datetime
import os
import hashlib

st.set_page_config(page_title="Afri.T.A - Lapin", page_icon="🐇", layout="wide")

st.title("🐇 Transport pour Lapin")

# BANDEAU ROSE
st.markdown("""
<div style="background: linear-gradient(90deg, #e91e63, #c2185b); padding: 0.5rem; border-radius: 10px; margin-bottom: 1rem;">
    <p style="color: white; text-align: center; margin: 0; font-weight: bold;">🌸 SERVICE LAPIN - TRANSPORT LAGOMORPHE</p>
</div>
""", unsafe_allow_html=True)

TARIF_BASE = 15000

# ==================== TOUS LES PAYS D'AFRIQUE ====================
pays_afrique_centrale = [
    "🇨🇲 Cameroun", "🇬🇦 Gabon", "🇨🇬 Congo", "🇨🇩 RDC (Kinshasa)", 
    "🇨🇫 République Centrafricaine", "🇹🇩 Tchad", "🇬🇶 Guinée Équatoriale",
    "🇸🇹 Sao Tomé-et-Principe", "🇦🇴 Angola", "🇧🇮 Burundi", "🇷🇼 Rwanda"
]

autres_pays_afrique = [
    "🇩🇿 Algérie", "🇪🇬 Égypte", "🇱🇾 Libye", "🇲🇦 Maroc", "🇸🇩 Soudan", "🇹🇳 Tunisie",
    "🇧🇯 Bénin", "🇧🇫 Burkina Faso", "🇨🇻 Cap-Vert", "🇨🇮 Côte d'Ivoire", "🇬🇲 Gambie",
    "🇬🇭 Ghana", "🇬🇳 Guinée", "🇬🇼 Guinée-Bissau", "🇱🇷 Liberia", "🇲🇱 Mali",
    "🇲🇷 Mauritanie", "🇳🇪 Niger", "🇳🇬 Nigéria", "🇸🇳 Sénégal", "🇸🇱 Sierra Leone",
    "🇹🇬 Togo", "🇩🇯 Djibouti", "🇪🇷 Érythrée", "🇪🇹 Éthiopie", "🇰🇪 Kenya",
    "🇲🇬 Madagascar", "🇲🇼 Malawi", "🇲🇺 Maurice", "🇲🇿 Mozambique", "🇸🇨 Seychelles",
    "🇸🇴 Somalie", "🇸🇸 Soudan du Sud", "🇹🇿 Tanzanie", "🇺🇬 Ouganda", "🇿🇲 Zambie",
    "🇿🇼 Zimbabwe", "🇿🇦 Afrique du Sud", "🇧🇼 Botswana", "🇸🇿 Eswatini", "🇱🇸 Lesotho", "🇳🇦 Namibie"
]

pays_afrique = pays_afrique_centrale + ["--- Autres pays (devis personnalisé) ---"] + autres_pays_afrique

# ==================== DISTANCES COMPLÈTES (Afrique centrale) ====================
distances_connues = {
    ("🇨🇲 Cameroun", "🇬🇦 Gabon"): 850, ("🇨🇲 Cameroun", "🇨🇬 Congo"): 1200,
    ("🇨🇲 Cameroun", "🇨🇩 RDC (Kinshasa)"): 1800, ("🇨🇲 Cameroun", "🇨🇫 République Centrafricaine"): 900,
    ("🇨🇲 Cameroun", "🇹🇩 Tchad"): 1100, ("🇨🇲 Cameroun", "🇬🇶 Guinée Équatoriale"): 350,
    ("🇨🇲 Cameroun", "🇸🇹 Sao Tomé-et-Principe"): 800, ("🇨🇲 Cameroun", "🇦🇴 Angola"): 2200,
    ("🇨🇲 Cameroun", "🇧🇮 Burundi"): 2000, ("🇨🇲 Cameroun", "🇷🇼 Rwanda"): 2100,
    ("🇬🇦 Gabon", "🇨🇲 Cameroun"): 850, ("🇬🇦 Gabon", "🇨🇬 Congo"): 900,
    ("🇬🇦 Gabon", "🇨🇩 RDC (Kinshasa)"): 1200, ("🇬🇦 Gabon", "🇨🇫 République Centrafricaine"): 1300,
    ("🇬🇦 Gabon", "🇹🇩 Tchad"): 1600, ("🇬🇦 Gabon", "🇬🇶 Guinée Équatoriale"): 400,
    ("🇬🇦 Gabon", "🇸🇹 Sao Tomé-et-Principe"): 500, ("🇬🇦 Gabon", "🇦🇴 Angola"): 1400,
    ("🇬🇦 Gabon", "🇧🇮 Burundi"): 2100, ("🇬🇦 Gabon", "🇷🇼 Rwanda"): 2200,
    ("🇨🇬 Congo", "🇨🇲 Cameroun"): 1200, ("🇨🇬 Congo", "🇬🇦 Gabon"): 900,
    ("🇨🇬 Congo", "🇨🇩 RDC (Kinshasa)"): 500, ("🇨🇬 Congo", "🇨🇫 République Centrafricaine"): 1000,
    ("🇨🇬 Congo", "🇹🇩 Tchad"): 1400, ("🇨🇬 Congo", "🇬🇶 Guinée Équatoriale"): 800,
    ("🇨🇬 Congo", "🇸🇹 Sao Tomé-et-Principe"): 700, ("🇨🇬 Congo", "🇦🇴 Angola"): 1500,
    ("🇨🇬 Congo", "🇧🇮 Burundi"): 1900, ("🇨🇬 Congo", "🇷🇼 Rwanda"): 2000,
    ("🇨🇩 RDC (Kinshasa)", "🇨🇲 Cameroun"): 1800, ("🇨🇩 RDC (Kinshasa)", "🇬🇦 Gabon"): 1200,
    ("🇨🇩 RDC (Kinshasa)", "🇨🇬 Congo"): 500, ("🇨🇩 RDC (Kinshasa)", "🇨🇫 République Centrafricaine"): 1500,
    ("🇨🇩 RDC (Kinshasa)", "🇹🇩 Tchad"): 1900, ("🇨🇩 RDC (Kinshasa)", "🇬🇶 Guinée Équatoriale"): 1300,
    ("🇨🇩 RDC (Kinshasa)", "🇸🇹 Sao Tomé-et-Principe"): 1200, ("🇨🇩 RDC (Kinshasa)", "🇦🇴 Angola"): 1000,
    ("🇨🇩 RDC (Kinshasa)", "🇧🇮 Burundi"): 1000, ("🇨🇩 RDC (Kinshasa)", "🇷🇼 Rwanda"): 1100,
    ("🇨🇫 République Centrafricaine", "🇨🇲 Cameroun"): 900, ("🇨🇫 République Centrafricaine", "🇬🇦 Gabon"): 1300,
    ("🇨🇫 République Centrafricaine", "🇨🇬 Congo"): 1000, ("🇨🇫 République Centrafricaine", "🇨🇩 RDC (Kinshasa)"): 1500,
    ("🇨🇫 République Centrafricaine", "🇹🇩 Tchad"): 800, ("🇨🇫 République Centrafricaine", "🇬🇶 Guinée Équatoriale"): 1100,
    ("🇨🇫 République Centrafricaine", "🇸🇹 Sao Tomé-et-Principe"): 1600, ("🇨🇫 République Centrafricaine", "🇦🇴 Angola"): 2000,
    ("🇨🇫 République Centrafricaine", "🇧🇮 Burundi"): 1800, ("🇨🇫 République Centrafricaine", "🇷🇼 Rwanda"): 1900,
    ("🇹🇩 Tchad", "🇨🇲 Cameroun"): 1100, ("🇹🇩 Tchad", "🇬🇦 Gabon"): 1600,
    ("🇹🇩 Tchad", "🇨🇬 Congo"): 1400, ("🇹🇩 Tchad", "🇨🇩 RDC (Kinshasa)"): 1900,
    ("🇹🇩 Tchad", "🇨🇫 République Centrafricaine"): 800, ("🇹🇩 Tchad", "🇬🇶 Guinée Équatoriale"): 1300,
    ("🇹🇩 Tchad", "🇸🇹 Sao Tomé-et-Principe"): 1800, ("🇹🇩 Tchad", "🇦🇴 Angola"): 2400,
    ("🇹🇩 Tchad", "🇧🇮 Burundi"): 2200, ("🇹🇩 Tchad", "🇷🇼 Rwanda"): 2300,
    ("🇬🇶 Guinée Équatoriale", "🇨🇲 Cameroun"): 350, ("🇬🇶 Guinée Équatoriale", "🇬🇦 Gabon"): 400,
    ("🇬🇶 Guinée Équatoriale", "🇨🇬 Congo"): 800, ("🇬🇶 Guinée Équatoriale", "🇨🇩 RDC (Kinshasa)"): 1300,
    ("🇬🇶 Guinée Équatoriale", "🇨🇫 République Centrafricaine"): 1100, ("🇬🇶 Guinée Équatoriale", "🇹🇩 Tchad"): 1300,
    ("🇬🇶 Guinée Équatoriale", "🇸🇹 Sao Tomé-et-Principe"): 700, ("🇬🇶 Guinée Équatoriale", "🇦🇴 Angola"): 1500,
    ("🇬🇶 Guinée Équatoriale", "🇧🇮 Burundi"): 2100, ("🇬🇶 Guinée Équatoriale", "🇷🇼 Rwanda"): 2200,
    ("🇸🇹 Sao Tomé-et-Principe", "🇨🇲 Cameroun"): 800, ("🇸🇹 Sao Tomé-et-Principe", "🇬🇦 Gabon"): 500,
    ("🇸🇹 Sao Tomé-et-Principe", "🇨🇬 Congo"): 700, ("🇸🇹 Sao Tomé-et-Principe", "🇨🇩 RDC (Kinshasa)"): 1200,
    ("🇸🇹 Sao Tomé-et-Principe", "🇨🇫 République Centrafricaine"): 1600, ("🇸🇹 Sao Tomé-et-Principe", "🇹🇩 Tchad"): 1800,
    ("🇸🇹 Sao Tomé-et-Principe", "🇬🇶 Guinée Équatoriale"): 700, ("🇸🇹 Sao Tomé-et-Principe", "🇦🇴 Angola"): 1300,
    ("🇸🇹 Sao Tomé-et-Principe", "🇧🇮 Burundi"): 2000, ("🇸🇹 Sao Tomé-et-Principe", "🇷🇼 Rwanda"): 2100,
    ("🇦🇴 Angola", "🇨🇲 Cameroun"): 2200, ("🇦🇴 Angola", "🇬🇦 Gabon"): 1400,
    ("🇦🇴 Angola", "🇨🇬 Congo"): 1500, ("🇦🇴 Angola", "🇨🇩 RDC (Kinshasa)"): 1000,
    ("🇦🇴 Angola", "🇨🇫 République Centrafricaine"): 2000, ("🇦🇴 Angola", "🇹🇩 Tchad"): 2400,
    ("🇦🇴 Angola", "🇬🇶 Guinée Équatoriale"): 1500, ("🇦🇴 Angola", "🇸🇹 Sao Tomé-et-Principe"): 1300,
    ("🇦🇴 Angola", "🇧🇮 Burundi"): 1800, ("🇦🇴 Angola", "🇷🇼 Rwanda"): 1900,
    ("🇧🇮 Burundi", "🇨🇲 Cameroun"): 2000, ("🇧🇮 Burundi", "🇬🇦 Gabon"): 2100,
    ("🇧🇮 Burundi", "🇨🇬 Congo"): 1900, ("🇧🇮 Burundi", "🇨🇩 RDC (Kinshasa)"): 1000,
    ("🇧🇮 Burundi", "🇨🇫 République Centrafricaine"): 1800, ("🇧🇮 Burundi", "🇹🇩 Tchad"): 2200,
    ("🇧🇮 Burundi", "🇬🇶 Guinée Équatoriale"): 2100, ("🇧🇮 Burundi", "🇸🇹 Sao Tomé-et-Principe"): 2000,
    ("🇧🇮 Burundi", "🇦🇴 Angola"): 1800, ("🇧🇮 Burundi", "🇷🇼 Rwanda"): 300,
    ("🇷🇼 Rwanda", "🇨🇲 Cameroun"): 2100, ("🇷🇼 Rwanda", "🇬🇦 Gabon"): 2200,
    ("🇷🇼 Rwanda", "🇨🇬 Congo"): 2000, ("🇷🇼 Rwanda", "🇨🇩 RDC (Kinshasa)"): 1100,
    ("🇷🇼 Rwanda", "🇨🇫 République Centrafricaine"): 1900, ("🇷🇼 Rwanda", "🇹🇩 Tchad"): 2300,
    ("🇷🇼 Rwanda", "🇬🇶 Guinée Équatoriale"): 2200, ("🇷🇼 Rwanda", "🇸🇹 Sao Tomé-et-Principe"): 2100,
    ("🇷🇼 Rwanda", "🇦🇴 Angola"): 1900, ("🇷🇼 Rwanda", "🇧🇮 Burundi"): 300,
}

def get_coefficient_distance(distance):
    if distance <= 500: return 1.0
    elif distance <= 1000: return 1.5
    elif distance <= 1500: return 2.0
    elif distance <= 2500: return 2.5
    else: return 3.0

def calculer_distance(depart, arrivee):
    if depart == arrivee: return 0
    return distances_connues.get((depart, arrivee))

races = {"Bélier": 1.0, "Nain": 1.1, "Angora": 1.3}

st.subheader("👤 Vos informations")
col1, col2 = st.columns(2)
with col1:
    nom_client = st.text_input("Nom complet", key="lapin_nom")
    email = st.text_input("Email", key="lapin_email")
with col2:
    telephone = st.text_input("Téléphone", key="lapin_tel")
    adresse = st.text_input("Adresse", key="lapin_adresse")

st.subheader("📍 Informations transport")
col3, col4 = st.columns(2)
with col3:
    liste_races = list(races.keys()) + ["✏️ Autre race (précisez)"]
    race_choisie = st.selectbox("Race", liste_races, key="lapin_race")
    
    if race_choisie == "✏️ Autre race (précisez)":
        autre_race = st.text_input("Précisez la race", placeholder="Ex: Géant des Flandres", key="lapin_autre_race")
        categorie_race = st.radio("Catégorie", ["Standard", "Premium (+30%)", "Très rare (+60%)"], key="lapin_categorie")
        if categorie_race == "Standard": coeff_race = 1.0
        elif categorie_race == "Premium (+30%)": coeff_race = 1.3
        else: coeff_race = 1.6
        race_affichee = autre_race if autre_race else "Race personnalisée"
    else:
        coeff_race = races[race_choisie]
        race_affichee = race_choisie
    
    poids = st.number_input("Poids (kg)", min_value=0.5, max_value=50.0, value=2.0, step=0.5, key="lapin_poids")
with col4:
    pays_depart = st.selectbox("Pays de départ", pays_afrique, key="lapin_depart")
    pays_arrivee = st.selectbox("Pays d'arrivée", pays_afrique, key="lapin_arrivee")

st.info("🌟 **Notre zone de prédilection : l'Afrique centrale** (Cameroun, Gabon, Congo, RDC, RCA, Tchad, Guinée Éq., Sao Tomé, Angola, Burundi, Rwanda). Pour les autres pays, contactez-nous pour un devis personnalisé.")

distance = calculer_distance(pays_depart, pays_arrivee)

if distance is not None:
    coeff_distance = get_coefficient_distance(distance)
    prix = poids * TARIF_BASE * coeff_distance * coeff_race
    
    if distance <= 500: zone = "Zone 1 (0-500 km) : x1.0"
    elif distance <= 1000: zone = "Zone 2 (501-1000 km) : x1.5"
    elif distance <= 1500: zone = "Zone 3 (1001-1500 km) : x2.0"
    elif distance <= 2500: zone = "Zone 4 (1501-2500 km) : x2.5"
    else: zone = "Zone 5 (2500 km et +) : x3.0"
    
    st.info(f"📏 Distance : {distance} km | {zone} | ⭐ Coeff race : x{coeff_race}")
    st.success(f"💰 Prix total : {int(prix):,} FCFA")
    
    if st.button("✅ Générer ma facture", use_container_width=True, key="lapin_generer"):
        if nom_client and telephone:
            numero_facture = f"AFR-{datetime.now().strftime('%Y%m%d%H%M%S')}-{hashlib.md5(str(prix).encode()).hexdigest()[:4]}"
            data_file = "factures.csv"
            if not os.path.exists(data_file):
                pd.DataFrame(columns=["Numero", "Date", "Client", "Telephone", "Email", "Animal", "Race", "Poids", "Depart", "Arrivee", "Distance", "Prix", "Statut"]).to_csv(data_file, index=False)
            nouvelle_facture = pd.DataFrame([{"Numero": numero_facture, "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Client": nom_client, "Telephone": telephone, "Email": email, "Animal": "Lapin", "Race": race_affichee, "Poids": poids, "Depart": pays_depart, "Arrivee": pays_arrivee, "Distance": distance, "Prix": int(prix), "Statut": "En attente paiement"}])
            nouvelle_facture.to_csv(data_file, mode="a", header=False, index=False)
            st.session_state.facture_numero = numero_facture
            st.session_state.facture_prix = int(prix)
            st.session_state.facture_client = nom_client
            st.session_state.facture_animal = "Lapin"
            st.session_state.facture_race = race_affichee
            st.success(f"✅ Facture générée ! Numéro : {numero_facture}")
            st.balloons()
            if st.button("📄 Voir ma facture", key="lapin_voir_facture"):
                st.switch_page("pages/facture.py")
        else:
            st.warning("Veuillez remplir votre nom et téléphone")
else:
    st.warning("🌍 **Devis personnalisé** - Cette destination est hors de notre zone de prédilection (Afrique centrale). Veuillez nous contacter au +237 6XX XXX XXX ou par email à contact@afrita-transport.com")
