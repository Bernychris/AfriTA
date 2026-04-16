import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# Configuration de la page
st.set_page_config(
    page_title="Afri.T.A - Transport Animalier",
    page_icon="🐕",
    layout="wide"
)

# ==================== THÈME SOMBRE ====================
st.markdown("""
<style>
    /* Fond noir général */
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
    }
    
    /* Texte principal en blanc */
    .main-header h1, .main-header p, .stMarkdown, .stSubheader, 
    .stSelectbox label, .stNumberInput label, .stDateInput label,
    .stRadio label, .stCheckbox label {
        color: white !important;
    }
    
    /* En-tête */
    .main-header {
        background: linear-gradient(90deg, #2d8c3e 0%, #1a5f2a 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid #ffd700;
    }
    
    /* Cartes de formulaire (fond gris foncé) */
    .form-card {
        background: #1e1e1e;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
        border: 1px solid #333;
    }
    
    /* Cartes résultats */
    .result-card {
        background: linear-gradient(135deg, #2d8c3e 0%, #1a5f2a 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #ffd700;
    }
    .result-card h3, .result-card h2, .result-card p {
        color: white !important;
    }
    
    /* Cartes animaux */
    .animal-card {
        background: #2a2a2a;
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        cursor: pointer;
        border: 2px solid #444;
        transition: all 0.3s ease;
    }
    .animal-card:hover {
        transform: scale(1.05);
        border-color: #2d8c3e;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .animal-card-selected {
        background: linear-gradient(135deg, #2d8c3e 0%, #1a5f2a 100%);
        border: 2px solid #ffd700;
    }
    .animal-card-selected h3 {
        color: white;
    }
    .animal-emoji {
        font-size: 3rem;
    }
    .animal-card h3 {
        color: white;
        margin: 0;
    }
    
    /* Pied de page */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 2rem;
        color: #888;
        border-top: 1px solid #333;
    }
    
    /* Messages */
    .stAlert {
        background-color: #1e1e1e !important;
        color: white !important;
    }
    
    /* Bouton */
    .stButton > button {
        background: linear-gradient(90deg, #2d8c3e, #1a5f2a);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 50px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #3da84e, #2d8c3e);
    }
    
    /* Selectbox et inputs en mode sombre */
    .stSelectbox > div > div, .stNumberInput > div > div, .stDateInput > div > div {
        background-color: #2a2a2a !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ==================== EN-TÊTE ====================
st.markdown("""
<div class="main-header">
    <h1>🐕 Afri.T.A - Transport Animalier</h1>
    <p>📍 Basé au Cameroun | Service dans toute l'Afrique 🌍</p>
</div>
""", unsafe_allow_html=True)

# ==================== DEVISES ====================
devises = {
    "FCFA (XAF)": 1.0,
    "Euro (€)": 0.0015,
    "Dollar ($)": 0.0016
}

col_devise1, col_devise2 = st.columns([1, 3])
with col_devise1:
    devise_choisie = st.selectbox("💰 Devise", list(devises.keys()))
taux_conversion = devises[devise_choisie]

# ==================== ANIMAUX ====================
tarif_base_animal = {
    "🐕 Chien": 15,
    "🐈 Chat": 12,
    "🐇 Lapin": 10,
    "🐦 Oiseau": 8,
}

races_par_animal = {
    "🐕 Chien": {
        "Berger Allemand": 1.0,
        "Golden Retriever": 1.1,
        "Berger Malinois": 1.2,
        "Rottweiler": 1.15,
        "Buldog Français": 1.5,
        "Caniche": 1.3,
        "Husky": 1.25,
        "Chihuahua": 1.1,
        "Labrador": 1.1,
    },
    "🐈 Chat": {
        "Européen": 1.0,
        "Siamois": 1.4,
        "Persan": 1.5,
        "Maine Coon": 1.6,
        "Bengal": 1.8,
        "Sphynx": 1.7,
    },
    "🐇 Lapin": {
        "Bélier": 1.0,
        "Nain": 1.1,
        "Angora": 1.3,
    },
    "🐦 Oiseau": {
        "Perruche": 1.0,
        "Perroquet Gris": 2.0,
        "Ara": 2.5,
        "Canari": 1.0,
    }
}

# ==================== PAYS ====================
pays_afrique = [
    "Cameroun", "Gabon", "Congo", "République Centrafricaine", "Tchad", "Guinée Équatoriale",
    "Nigéria", "Sénégal", "Côte d'Ivoire", "Ghana", "Mali", "Burkina Faso", "Bénin", "Togo"
]

# ==================== SERVICES ====================
tarifs_services = {
    "🚗 Standard": 1.0,
    "❄️ Climatisé": 1.3,
    "👨‍⚕️ Avec vétérinaire": 1.6,
}

# ==================== DISTANCES ====================
distances_connues = {
    ("Cameroun", "Gabon"): 850,
    ("Cameroun", "Congo"): 1200,
    ("Cameroun", "République Centrafricaine"): 900,
    ("Cameroun", "Tchad"): 1100,
    ("Cameroun", "Guinée Équatoriale"): 350,
    ("Cameroun", "Nigéria"): 600,
}

def calculer_distance(depart, arrivee):
    return distances_connues.get((depart, arrivee))

# ==================== FICHIER DONNÉES ====================
DATA_FILE = "afrita_data.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=[
        "Date", "Pays_depart", "Pays_arrivee", "Distance_km",
        "Type_animal", "Race", "Poids_kg", "Service", "Prix_total", "Devise"
    ]).to_csv(DATA_FILE, index=False)

# ==================== SESSION STATE ====================
if "animal_selectionne" not in st.session_state:
    st.session_state.animal_selectionne = None
if "race_selectionnee" not in st.session_state:
    st.session_state.race_selectionnee = None
if "etape" not in st.session_state:
    st.session_state.etape = 1

# ==================== FORMULAIRE ====================
st.markdown('<div class="form-card">', unsafe_allow_html=True)

# ÉTAPE 1 : Choix de l'animal
st.subheader("🐾 ÉTAPE 1 : Choisissez votre animal")

col1, col2, col3, col4 = st.columns(4)
animaux = ["🐕 Chien", "🐈 Chat", "🐇 Lapin", "🐦 Oiseau"]
icones = ["🐕", "🐈", "🐇", "🐦"]
noms = ["Chien", "Chat", "Lapin", "Oiseau"]

for idx, (col, animal, icone, nom) in enumerate(zip([col1, col2, col3, col4], animaux, icones, noms)):
    with col:
        if st.session_state.animal_selectionne == animal:
            st.markdown(f"""
            <div class="animal-card animal-card-selected" style="text-align:center">
                <div class="animal-emoji">{icone}</div>
                <h3>{nom}</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button(f"{icone}\n{nom}", key=f"btn_{animal}", use_container_width=True):
                st.session_state.animal_selectionne = animal
                st.session_state.race_selectionnee = None
                st.rerun()

# ÉTAPE 2 : Choix de la race (apparaît seulement si un animal est sélectionné)
if st.session_state.animal_selectionne:
    st.markdown("---")
    st.subheader(f"📋 ÉTAPE 2 : Choisissez la race de votre {st.session_state.animal_selectionne}")
    
    races_disponibles = list(races_par_animal[st.session_state.animal_selectionne].keys())
    coefficients_race = races_par_animal[st.session_state.animal_selectionne]
    
    for race in races_disponibles:
        coeff = coefficients_race[race]
        col_race, col_prix = st.columns([3, 1])
        with col_race:
            if st.button(f"🐾 {race}", key=f"race_{race}"):
                st.session_state.race_selectionnee = race
                st.session_state.coeff_race = coeff
                st.rerun()
        with col_prix:
            if coeff > 1.3:
                st.markdown("<span style='color:#ff8c00'>⭐ Premium</span>", unsafe_allow_html=True)
            elif coeff > 1.1:
                st.markdown("<span style='color:#ffd700'>✨ Standard+</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='color:#2d8c3e'>📌 Standard</span>", unsafe_allow_html=True)
    
    # Option autre race
    if st.button("✏️ Autre race (précisez)", key="autre_race_btn"):
        st.session_state.afficher_autre_race = True
    
    if st.session_state.get("afficher_autre_race", False):
        race_perso = st.text_input("Nom de votre race :", placeholder="Ex: Berger Australien")
        col_cat1, col_cat2, col_cat3 = st.columns(3)
        with col_cat1:
            if st.button("📌 Standard (prix normal)"):
                st.session_state.race_selectionnee = race_perso if race_perso else "Race personnalisée"
                st.session_state.coeff_race = 1.0
                st.session_state.afficher_autre_race = False
                st.rerun()
        with col_cat2:
            if st.button("✨ Premium (+30%)"):
                st.session_state.race_selectionnee = race_perso if race_perso else "Race personnalisée"
                st.session_state.coeff_race = 1.3
                st.session_state.afficher_autre_race = False
                st.rerun()
        with col_cat3:
            if st.button("⭐ Très rare (+60%)"):
                st.session_state.race_selectionnee = race_perso if race_perso else "Race personnalisée"
                st.session_state.coeff_race = 1.6
                st.session_state.afficher_autre_race = False
                st.rerun()

# ÉTAPE 3 : Informations transport (apparaît si race choisie)
if st.session_state.race_selectionnee:
    st.markdown("---")
    st.subheader("📍 ÉTAPE 3 : Informations de transport")
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        pays_depart = st.selectbox("Pays de départ", pays_afrique)
        poids = st.number_input("Poids (kg)", min_value=0.1, max_value=100.0, value=5.0, step=0.5)
    
    with col_t2:
        pays_arrivee = st.selectbox("Pays d'arrivée", pays_afrique)
        service = st.selectbox("Service", list(tarifs_services.keys()))
        date_transport = st.date_input("Date du transport", datetime.now())
    
    distance = calculer_distance(pays_depart, pays_arrivee)
    
    if distance:
        tarif_base = tarif_base_animal[st.session_state.animal_selectionne]
        coeff_race = st.session_state.coeff_race
        coeff_service = tarifs_services[service]
        
        prix_fcfa = distance * poids * tarif_base * coeff_race * coeff_service
        prix_converti = prix_fcfa * taux_conversion
        
        st.markdown("---")
        st.subheader("💰 ÉTAPE 4 : Devis estimé")
        
        col_r1, col_r2, col_r3, col_r4 = st.columns(4)
        with col_r1:
            st.metric("📏 Distance", f"{distance} km")
        with col_r2:
            st.metric("⚖️ Poids", f"{poids} kg")
        with col_r3:
            coeff_total = coeff_race * coeff_service
            st.metric("⭐ Coefficient", f"x {coeff_total:.1f}")
        with col_r4:
            st.metric("💰 Prix total", f"{int(prix_converti):,} {devise_choisie}")
        
        st.info("💳 **Paiement à l'agence uniquement** - Douala (Akwa) ou Yaoundé (Mvog-Mbi)")
        
        if st.button("✅ Confirmer la demande", use_container_width=True):
            nouvelle_ligne = pd.DataFrame([{
                "Date": date_transport.strftime("%Y-%m-%d"),
                "Pays_depart": pays_depart,
                "Pays_arrivee": pays_arrivee,
                "Distance_km": distance,
                "Type_animal": st.session_state.animal_selectionne,
                "Race": st.session_state.race_selectionnee,
                "Poids_kg": poids,
                "Service": service,
                "Prix_total": int(prix_converti),
                "Devise": devise_choisie
            }])
            nouvelle_ligne.to_csv(DATA_FILE, mode="a", header=False, index=False)
            st.success("✅ Demande enregistrée avec succès !")
            st.balloons()
            
            # Réinitialisation
            st.session_state.animal_selectionne = None
            st.session_state.race_selectionnee = None
            st.rerun()
    else:
        st.warning("🌍 **Devis personnalisé** - Contactez-nous pour cette destination !")

st.markdown('</div>', unsafe_allow_html=True)

# ==================== ANALYSE DESCRIPTIVE ====================
st.markdown("---")
st.subheader("📊 Statistiques des transports")

df = pd.read_csv(DATA_FILE)

if len(df) > 0:
    col_a1, col_a2, col_a3, col_a4 = st.columns(4)
    with col_a1:
        st.metric("📦 Total demandes", len(df))
    with col_a2:
        st.metric("💰 Prix moyen", f"{int(df['Prix_total'].mean()):,} {df['Devise'].iloc[0]}")
    with col_a3:
        st.metric("⚖️ Poids moyen", f"{df['Poids_kg'].mean():.1f} kg")
    with col_a4:
        st.metric("📏 Distance moyenne", f"{int(df['Distance_km'].mean())} km")
    
    tab1, tab2 = st.tabs(["📈 Prix par race", "🐾 Répartition des animaux"])
    
    with tab1:
        prix_par_race = df.groupby("Race")["Prix_total"].mean().reset_index()
        fig1 = px.bar(prix_par_race, x="Race", y="Prix_total", 
                      title="Prix moyen par race", color="Race")
        st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        animaux_counts = df["Type_animal"].value_counts().reset_index()
        animaux_counts.columns = ["Animal", "Nombre"]
        fig2 = px.pie(animaux_counts, values="Nombre", names="Animal", 
                      title="Répartition des animaux transportés")
        st.plotly_chart(fig2, use_container_width=True)
    
    with st.expander("📋 Voir toutes les données"):
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger CSV", csv, "afrita_data.csv")
else:
    st.info("💡 Aucune donnée pour l'instant. Effectuez une première demande !")

# Pied de page
st.markdown("""
<div class="footer">
    <p>🐕 Afri.T.A - Transport Animalier - Agence basée au Cameroun</p>
    <p>📍 Douala | Yaoundé | 📞 +237 6XX XXX XXX | 🌍 Service dans toute l'Afrique</p>
</div>
""", unsafe_allow_html=True)
