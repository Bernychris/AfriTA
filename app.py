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

# Style CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8f0e8 100%);
    }
    .main-header {
        background: linear-gradient(90deg, #1a5f2a 0%, #2d8c3e 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
    }
    .main-header p {
        color: #ffd700;
        margin: 0;
    }
    .form-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    .result-card {
        background: linear-gradient(135deg, #1a5f2a 0%, #2d8c3e 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .animal-card {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        cursor: pointer;
        border: 2px solid #ddd;
        transition: all 0.3s ease;
    }
    .animal-card:hover {
        transform: scale(1.05);
        border-color: #2d8c3e;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .animal-card-selected {
        background: linear-gradient(135deg, #1a5f2a 0%, #2d8c3e 100%);
        border: 2px solid #ffd700;
        color: white;
    }
    .animal-card-selected h3 {
        color: white;
    }
    .animal-emoji {
        font-size: 3rem;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 2rem;
        color: #666;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div class="main-header">
    <h1>🐕 Afri.T.A - Transport Animalier</h1>
    <p>📍 Basé au Cameroun | Service dans toute l'Afrique 🌍</p>
</div>
""", unsafe_allow_html=True)

# ==================== ANIMAUX AVEC LEURS RACES ET TARIFS ====================
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
        "Sacré de Birmanie": 1.4,
    },
    "🐇 Lapin": {
        "Bélier": 1.0,
        "Nain": 1.1,
        "Angora": 1.3,
        "Fauve de Bourgogne": 1.0,
    },
    "🐦 Oiseau": {
        "Perruche": 1.0,
        "Perroquet Gris": 2.0,
        "Ara": 2.5,
        "Canari": 1.0,
        "Inséparable": 1.2,
    }
}

# ==================== PAYS D'AFRIQUE ====================
pays_afrique = [
    "Cameroun", "Gabon", "Congo", "République Centrafricaine", "Tchad", "Guinée Équatoriale",
    "Nigéria", "Sénégal", "Côte d'Ivoire", "Ghana", "Mali", "Burkina Faso", "Bénin", "Togo",
    "Algérie", "Maroc", "Tunisie", "Égypte", "Kenya", "Tanzanie", "Afrique du Sud"
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

# ==================== FICHIER DE DONNÉES ====================
DATA_FILE = "afrita_data.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=[
        "Date", "Pays_depart", "Pays_arrivee", "Distance_km",
        "Type_animal", "Race", "Coefficient_race", "Poids_kg", 
        "Service", "Prix_total_FCFA"
    ]).to_csv(DATA_FILE, index=False)

# ==================== SESSION STATE ====================
if "animal_selectionne" not in st.session_state:
    st.session_state.animal_selectionne = "🐕 Chien"
if "race_selectionnee" not in st.session_state:
    st.session_state.race_selectionnee = "Berger Allemand"

# ==================== SÉLECTION DE L'ANIMAL ====================
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.subheader("🐾 1. Choisissez votre animal")

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
                premieres_races = list(races_par_animal[animal].keys())
                st.session_state.race_selectionnee = premieres_races[0]
                if "coeff_race_custom" in st.session_state:
                    del st.session_state.coeff_race_custom
                st.rerun()

# ==================== SÉLECTION DE LA RACE ====================
st.markdown("---")
st.subheader("📋 2. Choisissez la race")

races_disponibles = list(races_par_animal[st.session_state.animal_selectionne].keys())
coefficients_race = races_par_animal[st.session_state.animal_selectionne]

races_avec_autre = races_disponibles + ["✏️ Autre (précisez votre race)"]

race_choisie = st.selectbox(
    "Sélectionnez la race de votre animal",
    races_avec_autre,
    index=0
)

if race_choisie == "✏️ Autre (précisez votre race)":
    race_personnalisee = st.text_input("Écrivez le nom de votre race :", placeholder="Ex: Berger Australien, Yorkshire, Chien nu du Pérou, etc.")
    
    if race_personnalisee:
        st.session_state.race_selectionnee = race_personnalisee
        
        st.markdown("**📊 Catégorie de la race :**")
        
        col_rare1, col_rare2, col_rare3 = st.columns(3)
        
        with col_rare1:
            if st.button("📌 Race standard\n(Prix normal)", key="rare_standard"):
                st.session_state.coeff_race_custom = 1.0
                st.session_state.categorie_race = "standard"
                st.rerun()
        
        with col_rare2:
            if st.button("✨ Race premium\n(+30%)", key="rare_premium"):
                st.session_state.coeff_race_custom = 1.3
                st.session_state.categorie_race = "premium"
                st.rerun()
        
        with col_rare3:
            if st.button("⭐ Race très rare\n(+60%)", key="rare_tres_rare"):
                st.session_state.coeff_race_custom = 1.6
                st.session_state.categorie_race = "tres_rare"
                st.rerun()
        
        if "coeff_race_custom" in st.session_state:
            coeff_race = st.session_state.coeff_race_custom
            if st.session_state.categorie_race == "standard":
                st.success(f"✅ Race : **{race_personnalisee}** - Catégorie : **Standard** (prix normal)")
            elif st.session_state.categorie_race == "premium":
                st.info(f"✅ Race : **{race_personnalisee}** - Catégorie : **Premium** (+30%)")
            else:
                st.warning(f"✅ Race : **{race_personnalisee}** - Catégorie : **Très rare** (+60%)")
        else:
            coeff_race = 1.0
            st.info("👆 Cliquez sur une catégorie ci-dessus pour définir le prix")
    else:
        st.session_state.race_selectionnee = "À préciser"
        coeff_race = 1.0
        st.warning("✏️ Veuillez écrire le nom de votre race")
else:
    st.session_state.race_selectionnee = race_choisie
    coeff_race = coefficients_race[race_choisie]
    if "coeff_race_custom" in st.session_state:
        del st.session_state.coeff_race_custom
    
    if coeff_race > 1.3:
        st.success(f"⭐ Race premium : +{int((coeff_race-1)*100)}% sur le tarif")
    elif coeff_race > 1.1:
        st.info(f"✨ Race standard+ : +{int((coeff_race-1)*100)}% sur le tarif")
    else:
        st.success("📌 Race standard : prix de base")

# ==================== SUITE DU FORMULAIRE ====================
st.markdown("---")
st.subheader("📍 3. Informations de transport")

col1, col2 = st.columns(2)

with col1:
    pays_depart = st.selectbox("Pays de départ", pays_afrique)
    poids = st.number_input("Poids (kg)", min_value=0.1, max_value=100.0, value=5.0, step=0.5)

with col2:
    pays_arrivee = st.selectbox("Pays d'arrivée", pays_afrique)
    service = st.selectbox("Service", list(tarifs_services.keys()))
    date_transport = st.date_input("Date du transport", datetime.now())

# ==================== CALCUL DU PRIX ====================
distance = calculer_distance(pays_depart, pays_arrivee)

if distance:
    tarif_base = tarif_base_animal[st.session_state.animal_selectionne]
    coeff_service = tarifs_services[service]
    
    prix_total = distance * poids * tarif_base * coeff_race * coeff_service
    
    st.markdown("---")
    st.subheader("💰 4. Devis estimé")
    
    col_r1, col_r2, col_r3, col_r4 = st.columns(4)
    with col_r1:
        st.metric("📏 Distance", f"{distance} km")
    with col_r2:
        st.metric("🐾 Tarif base", f"{tarif_base} FCFA")
    with col_r3:
        coeff_total = coeff_race * coeff_service
        st.metric("⭐ Coefficient", f"x {coeff_total:.1f}")
    with col_r4:
        st.metric("💰 Prix total", f"{int(prix_total):,} FCFA")
    
    st.info("💳 **Paiement à l'agence uniquement** - Douala (Akwa) ou Yaoundé (Mvog-Mbi)")
    
    if st.button("✅ Confirmer la demande", use_container_width=True):
        nouvelle_ligne = pd.DataFrame([{
            "Date": date_transport.strftime("%Y-%m-%d"),
            "Pays_depart": pays_depart,
            "Pays_arrivee": pays_arrivee,
            "Distance_km": distance,
            "Type_animal": st.session_state.animal_selectionne,
            "Race": st.session_state.race_selectionnee,
            "Coefficient_race": coeff_race,
            "Poids_kg": poids,
            "Service": service,
            "Prix_total_FCFA": int(prix_total)
        }])
        nouvelle_ligne.to_csv(DATA_FILE, mode="a", header=False, index=False)
        st.success("✅ Demande enregistrée avec succès !")
        st.balloons()
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
        st.metric("💰 Prix moyen", f"{int(df['Prix_total_FCFA'].mean()):,} FCFA")
    with col_a3:
        st.metric("⚖️ Poids moyen", f"{df['Poids_kg'].mean():.1f} kg")
    with col_a4:
        st.metric("📏 Distance moyenne", f"{int(df['Distance_km'].mean())} km")
    
    tab1, tab2, tab3 = st.tabs(["📈 Prix par race", "🐾 Répartition des animaux", "🌍 Transports par pays"])
    
    with tab1:
        prix_par_race = df.groupby("Race")["Prix_total_FCFA"].mean().reset_index()
        fig1 = px.bar(prix_par_race, x="Race", y="Prix_total_FCFA", 
                      title="Prix moyen par race", color="Race")
        st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        animaux_counts = df["Type_animal"].value_counts().reset_index()
        animaux_counts.columns = ["Animal", "Nombre"]
        fig2 = px.pie(animaux_counts, values="Nombre", names="Animal", 
                      title="Répartition des animaux transportés")
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        transports = df["Pays_depart"].value_counts().reset_index()
        transports.columns = ["Pays", "Nombre"]
        fig3 = px.bar(transports, x="Pays", y="Nombre", title="Nombre de départs par pays")
        st.plotly_chart(fig3, use_container_width=True)
    
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
    <p>⭐ Les races premium ont un supplément (jusqu'à +60%)</p>
</div>
""", unsafe_allow_html=True)
