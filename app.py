import streamlit as st

st.set_page_config(page_title="Afri.T.A", page_icon="🐕", layout="wide")

# Style CSS pour le menu latéral
st.markdown("""
<style>
/* Fond général */
.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
}

/* ========== MENU LATÉRAL (SIDEBAR) ========== */
/* Fond de la sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
    border-right: 2px solid #2d8c3e;
}

/* Texte dans la sidebar */
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* Éléments du menu dans la sidebar */
section[data-testid="stSidebar"] ul li a {
    background: #1e1e1e !important;
    color: white !important;
    border-radius: 10px !important;
    margin: 5px 0 !important;
    padding: 10px 15px !important;
    border: 1px solid #2d8c3e !important;
    font-weight: bold !important;
}

section[data-testid="stSidebar"] ul li a:hover {
    background: #2d8c3e !important;
    border-color: #ffd700 !important;
    transform: scale(1.02);
}

/* Élément actif du menu */
section[data-testid="stSidebar"] ul li a[aria-current="page"] {
    background: #2d8c3e !important;
    border-color: #ffd700 !important;
}

/* Titre dans la sidebar */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffd700 !important;
}

/* Bouton pour ouvrir/fermer la sidebar (les flèches) */
button[kind="header"] {
    background: #2d8c3e !important;
    color: white !important;
    border-radius: 50% !important;
}

button[kind="header"]:hover {
    background: #3da84e !important;
}

/* ========== MENU PRINCIPAL EN HAUT ========== */
.custom-menu {
    background: #1e1e1e;
    padding: 0.8rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    border: 2px solid #2d8c3e;
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    justify-content: center;
}

.custom-menu a {
    color: white;
    background: #2a2a2a;
    text-decoration: none;
    padding: 0.7rem 1.5rem;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: bold;
    border: 1px solid #2d8c3e;
    transition: all 0.3s ease;
}

.custom-menu a:hover {
    background: #2d8c3e;
    border-color: #ffd700;
    transform: scale(1.02);
}

/* ========== AUTRES ÉLÉMENTS ========== */
h1, h2, h3, h4, p, label, .stMarkdown, .stSubheader {
    color: #ffffff !important;
}

.info-card, .animal-card, .contact-card, .aide-card {
    background: #1e1e1e;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 0.5rem;
    border: 1px solid #2d8c3e;
}

.stButton > button {
    background: linear-gradient(90deg, #2d8c3e, #1a5f2a) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.6rem 1.2rem !important;
    font-weight: bold !important;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #3da84e, #2d8c3e) !important;
}

.stTextInput > div > div > input,
.stSelectbox > div > div,
.stNumberInput > div > div {
    background-color: #2a2a2a !important;
    color: white !important;
    border: 1px solid #2d8c3e !important;
    border-radius: 10px !important;
}

.footer {
    text-align: center;
    padding: 1.5rem;
    margin-top: 2rem;
    color: #888;
    border-top: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# Menu personnalisé en haut
st.markdown("""
<div class="custom-menu">
    <a href="/" target="_self">🏠 Accueil</a>
    <a href="/panier" target="_self">🛒 Panier</a>
    <a href="/contact" target="_self">📞 Contact</a>
    <a href="/aide" target="_self">❓ Aide</a>
    <a href="/admin" target="_self">🔒 Admin</a>
</div>
""", unsafe_allow_html=True)

# Pages
accueil = st.Page("pages/accueil.py", title="🏠 Accueil", icon="🏠")
panier = st.Page("pages/panier.py", title="🛒 Panier", icon="🛒")
contact = st.Page("pages/contact.py", title="📞 Contact", icon="📞")
aide = st.Page("pages/aide.py", title="❓ Aide", icon="❓")
admin = st.Page("pages/admin.py", title="🔒 Admin", icon="🔒")

pg = st.navigation([accueil, panier, contact, aide, admin])
pg.run()
