import streamlit as st
import qrcode
import io
import base64
from datetime import datetime

st.set_page_config(page_title="Afri.T.A - Ma Facture", page_icon="📄", layout="wide")

st.markdown("""
<style>
.facture-container {
    background: white;
    color: black;
    padding: 2rem;
    border-radius: 15px;
    max-width: 550px;
    margin: auto;
    box-shadow: 0 0 20px rgba(255,215,0,0.3);
    font-family: Arial, sans-serif;
}
.facture-title {
    text-align: center;
    font-size: 1.8rem;
    font-weight: bold;
    color: #2d8c3e;
    margin-bottom: 1rem;
}
.facture-soustitre {
    text-align: center;
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 1.5rem;
}
.facture-ligne {
    display: flex;
    justify-content: space-between;
    padding: 0.7rem 0;
    border-bottom: 1px solid #eee;
}
.facture-ligne span:first-child {
    font-weight: bold;
    color: #333;
}
.facture-ligne span:last-child {
    color: #555;
}
.facture-total {
    font-size: 1.3rem;
    font-weight: bold;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 2px solid #2d8c3e;
    display: flex;
    justify-content: space-between;
}
.facture-total span:first-child {
    color: #2d8c3e;
}
.facture-total span:last-child {
    color: #e91e63;
    font-size: 1.4rem;
}
.facture-footer {
    text-align: center;
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px dashed #ccc;
    font-size: 0.8rem;
    color: #888;
}
.stButton > button {
    background: linear-gradient(90deg, #ffd700, #ffc107);
    color: black;
    border: none;
    border-radius: 50px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 Ma Facture Afri.T.A")

if "facture_numero" in st.session_state:
    # Récupérer toutes les informations
    numero = st.session_state.facture_numero
    prix = st.session_state.facture_prix
    client = st.session_state.facture_client
    animal = st.session_state.facture_animal
    race = st.session_state.facture_race
    email = st.session_state.get("facture_email", "Non renseigné")
    telephone = st.session_state.get("facture_tel", "Non renseigné")
    depart = st.session_state.get("facture_depart", "Non renseigné")
    arrivee = st.session_state.get("facture_arrivee", "Non renseigné")
    distance = st.session_state.get("facture_distance", "Non renseigné")
    poids = st.session_state.get("facture_poids", "Non renseigné")
    zone = st.session_state.get("facture_zone", "Non renseigné")
    
    # Générer le QR Code
    qr_data = f"AFRITA|{numero}|{client}|{animal}|{race}|{prix}|{datetime.now().strftime('%Y%m%d')}"
    qr = qrcode.make(qr_data)
    buffered = io.BytesIO()
    qr.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    # Afficher la facture
    st.markdown(f"""
    <div class="facture-container">
        <div class="facture-title">🐕 AFRI.T.A TRANSPORT</div>
        <div class="facture-soustitre">Agence de transport animalier - Cameroun</div>
        
        <div style="text-align:center; margin: 1rem 0;">
            <img src="data:image/png;base64,{qr_base64}" width="130">
            <p style="font-size:0.7rem; color:#888;">Scannez ce QR code à l'agence</p>
        </div>
        
        <div class="facture-ligne">
            <span>📄 NUMÉRO DE FACTURE</span>
            <span><strong>{numero}</strong></span>
        </div>
        <div class="facture-ligne">
            <span>📅 DATE</span>
            <span><strong>{datetime.now().strftime('%d/%m/%Y à %H:%M')}</strong></span>
        </div>
        
        <div style="margin: 1rem 0; padding: 0.5rem; background: #f5f5f5; border-radius: 10px;">
            <div class="facture-ligne" style="border-bottom: none;">
                <span>👤 CLIENT</span>
                <span><strong>{client}</strong></span>
            </div>
            <div class="facture-ligne" style="border-bottom: none;">
                <span>📞 TÉLÉPHONE</span>
                <span>{telephone}</span>
            </div>
            <div class="facture-ligne" style="border-bottom: none;">
                <span>📧 EMAIL</span>
                <span>{email}</span>
            </div>
        </div>
        
        <div style="margin: 1rem 0;">
            <div class="facture-ligne">
                <span>🐕 ANIMAL</span>
                <span><strong>{animal}</strong></span>
            </div>
            <div class="facture-ligne">
                <span>📌 RACE</span>
                <span>{race}</span>
            </div>
            <div class="facture-ligne">
                <span>⚖️ POIDS</span>
                <span>{poids} kg</span>
            </div>
        </div>
        
        <div style="margin: 1rem 0;">
            <div class="facture-ligne">
                <span>📍 DÉPART</span>
                <span>{depart}</span>
            </div>
            <div class="facture-ligne">
                <span>📍 ARRIVÉE</span>
                <span>{arrivee}</span>
            </div>
            <div class="facture-ligne">
                <span>📏 DISTANCE</span>
                <span>{distance} km</span>
            </div>
            <div class="facture-ligne">
                <span>🗺️ ZONE TARIFAIRE</span>
                <span>{zone}</span>
            </div>
        </div>
        
        <div class="facture-total">
            <span>💰 MONTANT TOTAL</span>
            <span>{int(prix):,} FCFA</span>
        </div>
        
        <div class="facture-footer">
            📍 À présenter à l'agence - Douala ou Yaoundé<br>
            📞 +237 6XX XXX XXX | 📧 contact@afrita-transport.com<br>
            ⚡ Paiement uniquement en espèces à l'agence
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Conseil :** Prenez une capture d'écran ou imprimez cette page pour la présenter à l'agence.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Retour à l'accueil", use_container_width=True):
            st.session_state.clear()
            st.switch_page("pages/accueil.py")
    with col2:
        if st.button("🛒 Nouvelle réservation", use_container_width=True):
            st.session_state.clear()
            st.switch_page("pages/panier.py")
else:
    st.warning("❌ Aucune facture trouvée. Veuillez d'abord générer une facture depuis une page de transport.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Retour à l'accueil", use_container_width=True):
            st.switch_page("pages/accueil.py")
    with col2:
        if st.button("🛒 Aller au panier", use_container_width=True):
            st.switch_page("pages/panier.py")
