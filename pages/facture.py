import streamlit as st
import qrcode
import io
import base64
from datetime import datetime

st.set_page_config(page_title="Afri.T.A - Ma Facture", page_icon="📄", layout="wide")

st.markdown("""
<style>
.facture-container { background: white; color: black; padding: 2rem; border-radius: 15px; max-width: 500px; margin: auto; box-shadow: 0 0 20px rgba(255,215,0,0.2); }
.facture-title { text-align: center; font-size: 1.5rem; font-weight: bold; color: #2d8c3e; }
.facture-ligne { display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #ddd; }
.facture-total { font-size: 1.2rem; font-weight: bold; margin-top: 1rem; padding-top: 1rem; border-top: 2px solid #ffd700; }
.stButton > button { background: linear-gradient(90deg, #ffd700, #ffc107); color: black; border: none; border-radius: 50px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("📄 Ma Facture Afri.T.A")

if "facture_numero" in st.session_state:
    numero = st.session_state.facture_numero
    prix = st.session_state.facture_prix
    client = st.session_state.facture_client
    animal = st.session_state.facture_animal
    race = st.session_state.facture_race
    
    qr_data = f"AFRITA|{numero}|{client}|{animal}|{race}|{prix}|{datetime.now().strftime('%Y%m%d')}"
    qr = qrcode.make(qr_data)
    buffered = io.BytesIO()
    qr.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()
    
    st.markdown(f"""
    <div class="facture-container">
        <div class="facture-title">AFRI.T.A TRANSPORT</div>
        <div style="text-align:center; margin:1rem 0">
            <img src="data:image/png;base64,{qr_base64}" width="150">
        </div>
        <div class="facture-ligne"><span>📄 Numéro</span><span><strong>{numero}</strong></span></div>
        <div class="facture-ligne"><span>👤 Client</span><span><strong>{client}</strong></span></div>
        <div class="facture-ligne"><span>🐕 Animal</span><span><strong>{animal} - {race}</strong></span></div>
        <div class="facture-ligne"><span>📅 Date</span><span><strong>{datetime.now().strftime('%d/%m/%Y %H:%M')}</strong></span></div>
        <div class="facture-total"><span>💰 Montant</span><span><strong>{prix:,} FCFA</strong></span></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Prenez une capture d'écran ou imprimez cette page")
    
    if st.button("🏠 Retour à l'accueil"):
        st.switch_page("pages/accueil.py")
else:
    st.warning("Aucune facture trouvée")
    if st.button("← Retour à l'accueil"):
        st.switch_page("pages/accueil.py")
