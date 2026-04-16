import streamlit as st

st.markdown("""
<style>
h1, h2, h3, p { color: white; }
.contact-card { background: #1e1e1e; padding: 2rem; border-radius: 15px; border: 1px solid #888; }
.contact-card h3 { color: #ffd700; margin-top: 1rem; }
.contact-card h3:first-of-type { margin-top: 0; }
</style>
""", unsafe_allow_html=True)

st.title("📞 Contactez-nous")

st.markdown("""
<div class="contact-card">
    <h3>📍 Nos agences</h3>
    <p><strong>Douala :</strong> Akwa, Rue de l'Aéroport</p>
    <p><strong>Yaoundé :</strong> Mvog-Mbi, Face CHU</p>
    
    <h3>📞 Téléphone</h3>
    <p>+237 6XX XXX XXX</p>
    
    <h3>📧 Email</h3>
    <p>contact@afrita-transport.com</p>
    
    <h3>⏰ Horaires</h3>
    <p>Lundi - Samedi : 8h - 17h</p>
    <p>Dimanche : Fermé</p>
</div>
""", unsafe_allow_html=True)
