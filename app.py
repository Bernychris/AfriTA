import streamlit as st

st.set_page_config(page_title="Afri.T.A", page_icon="🐕", layout="wide")

st.markdown("""
<style>
/* Fond général */
.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
}

/* Menu de navigation */
.menu {
    background: #1e1e1e;
    padding: 0.8rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    border: 1px solid #2d8c3e;
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    justify-content: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.menu a {
    color: #ffffff !important;
    background: #2a2a2a;
    text-decoration: none;
    padding: 0.7rem 1.5rem;
    border-radius: 10px;
    font-size: 1rem;
    font-weight: bold;
    transition: all 0.3s ease;
    border: 1px solid #444;
}

.menu a:hover {
    background: #2d8c3e;
    border-color: #ffd700;
    transform: scale(1.02);
}

/* Titres */
h1, h2, h3, h4, p, label, .stMarkdown {
    color: #ffffff !important;
}

/* Cartes */
.info-card, .animal-card, .contact-card, .aide-card {
    background: #1e1e1e;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 0.5rem;
    border: 1px solid #333;
    transition: 0.3s;
}

.info-card:hover, .animal-card:hover {
    transform: translateY(-3px);
    border-color: #2d8c3e;
}

/* Messages */
.stAlert {
    background-color: #2a2a2a !important;
    color: white !important;
}

.stAlert div {
    color: white !important;
}

/* Boutons */
.stButton > button {
    background: linear-gradient(90deg, #2d8c3e, #1a5f2a);
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 30px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #3da84e, #2d8c3e);
}

/* Inputs */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stNumberInput > div > div {
    background-color: #2a2a2a !important;
    color: white !important;
    border: 1px solid #2d8c3e !important;
    border-radius: 10px !important;
}

/* Sidebar (si utilisée) */
.sidebar .sidebar-content {
    background: #1a1a1a;
}

/* Pied de page */
.footer {
    text-align: center;
    padding: 1.5rem;
    margin-top: 2rem;
    color: #888;
    border-top: 1px solid #333;
    font-size: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# Menu avec meilleure visibilité
st.markdown("""
<div class="menu">
    <a href="/" target="_self">🏠 Accueil</a>
    <a href="/panier" target="_self">🛒 Panier</a>
    <a href="/contact" target="_self">📞 Contact</a>
    <a href="/aide" target="_self">❓ Aide</a>
    <a href="/admin" target="_self">🔒 Admin</a>
</div>
""", unsafe_allow_html=True)

# Pages
accueil = st.Page("pages/accueil.py", title="Accueil", icon="🏠")
panier = st.Page("pages/panier.py", title="Panier", icon="🛒")
contact = st.Page("pages/contact.py", title="Contact", icon="📞")
aide = st.Page("pages/aide.py", title="Aide", icon="❓")
admin = st.Page("pages/admin.py", title="Admin", icon="🔒")

pg = st.navigation([accueil, panier, contact, aide, admin])
pg.run()
