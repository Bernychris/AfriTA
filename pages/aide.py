import streamlit as st

st.markdown("""
<style>
h1, h2, h3, p { color: white; }
.aide-card { background: #1e1e1e; padding: 2rem; border-radius: 15px; border: 1px solid #fff; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

st.title("❓ Centre d'aide")

st.markdown("""
<div class="aide-card">
    <h3>📋 Comment réserver ?</h3>
    <p>1. Cliquez sur "Panier" dans le menu</p>
    <p>2. Choisissez votre animal</p>
    <p>3. Remplissez le formulaire</p>
    <p>4. Générez votre facture</p>
    <p>5. Présentez la facture à l'agence</p>
</div>

<div class="aide-card">
    <h3>💰 Paiement</h3>
    <p>Le paiement s'effectue UNIQUEMENT à l'agence en espèces.</p>
</div>

<div class="aide-card">
    <h3>🐕 Quels animaux transportez-vous ?</h3>
    <p>Chiens, Chats, Lapins, Oiseaux. Autres animaux sur demande.</p>
</div>

<div class="aide-card">
    <h3>🌍 Quels pays couvrez-vous ?</h3>
    <p>Cameroun, Gabon, Congo, Tchad, Nigéria, Sénégal et toute l'Afrique sur demande.</p>
</div>

<div class="aide-card">
    <h3>📞 Besoin d'aide ?</h3>
    <p>Appelez-nous au <strong>+237 6XX XXX XXX</strong></p>
</div>
""", unsafe_allow_html=True)
