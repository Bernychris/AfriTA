import streamlit as st

st.markdown("""
<style>
.main-header { background: linear-gradient(90deg, #2d8c3e 0%, #1a5f2a 100%); padding: 2rem; border-radius: 20px; text-align: center; margin-bottom: 2rem; border-left: 5px solid #ffd700; }
.main-header h1 { color: white; margin: 0; }
.main-header p { color: #ffd700; margin: 0.5rem 0 0 0; }
.info-card { background: #1e1e1e; border-radius: 15px; padding: 1.5rem; text-align: center; border: 1px solid #2d8c3e; transition: 0.3s; }
.info-card:hover { border-color: #ffd700; }
h2, h3, p { color: white; }
.stButton > button { background: linear-gradient(90deg, #2d8c3e, #1a5f2a); color: white; border: none; border-radius: 50px; }
.stButton > button:hover { transform: scale(1.02); background: linear-gradient(90deg, #3da84e, #2d8c3e); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>🐕 Afri.T.A - Transport Animalier</h1><p>📍 Basé au Cameroun | Service dans toute l\'Afrique 🌍</p></div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <h3>✨ Bienvenue sur Afri.T.A ✨</h3>
    <p>Votre partenaire de confiance pour le transport d'animaux de compagnie en Afrique.</p>
    <p>🐕 Chiens | 🐈 Chats | 🐇 Lapins | 🐦 Oiseaux</p>
    <p>🔒 Transport sécurisé | 📋 Suivi en temps réel | 💳 Paiement à l'agence</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="info-card"><h4>📦 Service Premium</h4><p>Véhicules climatisés<br>Personnel formé</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="info-card"><h4>🌍 Couverture</h4><p>Toute l\'Afrique<br>Départs quotidiens</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="info-card"><h4>🛡️ Assurance</h4><p>Transport assuré<br>Suivi vétérinaire</p></div>', unsafe_allow_html=True)

st.info("👉 Cliquez sur **Panier** dans le menu ci-dessus pour commencer votre réservation")
