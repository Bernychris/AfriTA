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
</style>
""", unsafe_allow_html=True)

st.markdown("""
<nav>
    <a href="/" target="_self">🏠 Accueil</a>
    <a href="/chien" target="_self">🐕 Chien</a>
    <a href="/chat" target="_self">🐈 Chat</a>
    <a href="/lapin" target="_self">🐇 Lapin</a>
    <a href="/oiseau" target="_self">🐦 Oiseau</a>
    <a href="/contact" target="_self">📞 Contact</a>
    <a href="/aide" target="_self">❓ Aide</a>
    <a href="/admin" target="_self">🔒 Admin</a>
</nav>
""", unsafe_allow_html=True)

accueil = st.Page("pages/accueil.py", title="Accueil", icon="🏠")
chien = st.Page("pages/chien.py", title="Chien", icon="🐕")
chat = st.Page("pages/chat.py", title="Chat", icon="🐈")
lapin = st.Page("pages/lapin.py", title="Lapin", icon="🐇")
oiseau = st.Page("pages/oiseau.py", title="Oiseau", icon="🐦")
contact = st.Page("pages/contact.py", title="Contact", icon="📞")
aide = st.Page("pages/aide.py", title="Aide", icon="❓")
admin = st.Page("pages/admin.py", title="Admin", icon="🔒")

pg = st.navigation([accueil, chien, chat, lapin, oiseau, contact, aide, admin])
pg.run()
