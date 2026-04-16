import streamlit as st

st.set_page_config(page_title="Afri.T.A", page_icon="🐕", layout="wide")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%); }
nav {
    background: #1e1e1e;
    padding: 0.5rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    border: 1px solid #333;
}
nav a {
    color: white !important;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    margin: 0 0.2rem;
}
nav a:hover {
    background: #2d8c3e;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<nav style="display: flex; gap: 1rem; align-items: center;">
    <a href="/" style="font-size: 1.1rem;">🏠 Accueil</a>
    <a href="/Panier" style="font-size: 1.1rem;">🛒 Panier</a>
    <a href="/Contact" style="font-size: 1.1rem;">📞 Contact</a>
    <a href="/Aide" style="font-size: 1.1rem;">❓ Aide</a>
</nav>
""", unsafe_allow_html=True)

accueil = st.Page("pages/accueil.py", title="Accueil", icon="🏠")
panier = st.Page("pages/panier.py", title="Panier", icon="🛒")
contact = st.Page("pages/contact.py", title="Contact", icon="📞")
aide = st.Page("pages/aide.py", title="Aide", icon="❓")

pg = st.navigation([accueil, panier, contact, aide])
pg.run()
