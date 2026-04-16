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
    display: flex;
    gap: 0.3rem;
    flex-wrap: wrap;
}
nav a {
    color: white !important;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    font-size: 0.9rem;
}
nav a:hover { background: #2d8c3e; }
.animal-card { background: #1e1e1e; border-radius: 15px; padding: 1.5rem; text-align: center; border: 1px solid #ff8c00; transition: 0.3s; }
.animal-card:hover { transform: scale(1.05); border-color: #ffd700; }
.animal-emoji { font-size: 4rem; }
.animal-card h3 { color: white; margin: 0.5rem 0; }
</style>
""", unsafe_allow_html=True)

# Menu principal
st.markdown("""
<nav>
    <a href="/" target="_self">🏠 Accueil</a>
    <a href="/panier" target="_self">🛒 Panier</a>
    <a href="/contact" target="_self">📞 Contact</a>
    <a href="/aide" target="_self">❓ Aide</a>
    <a href="/admin" target="_self">🔒 Admin</a>
</nav>
""", unsafe_allow_html=True)

# Définir les pages
accueil = st.Page("pages/accueil.py", title="Accueil", icon="🏠")
panier = st.Page("pages/panier.py", title="Panier", icon="🛒")
contact = st.Page("pages/contact.py", title="Contact", icon="📞")
aide = st.Page("pages/aide.py", title="Aide", icon="❓")
admin = st.Page("pages/admin.py", title="Admin", icon="🔒")

pg = st.navigation([accueil, panier, contact, aide, admin])
pg.run()
