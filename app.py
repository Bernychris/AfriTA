import streamlit as st

st.set_page_config(page_title="Afri.T.A - Panier", page_icon="🛒", layout="wide")

st.title("🛒 Choisissez votre animal")

st.markdown("""
<style>
.animal-card {
    background: #1e1e1e;
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    border: 1px solid #ff8c00;
    transition: 0.3s;
}
.animal-card:hover {
    transform: scale(1.05);
    border-color: #ffd700;
}
.animal-emoji {
    font-size: 4rem;
}
h1, h2, h3, p {
    color: white;
}
.stButton > button {
    background: linear-gradient(90deg, #ff8c00, #ffb347);
    color: white;
    border: none;
    border-radius: 50px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Utiliser session_state pour savoir quel animal est choisi
if "animal_page" not in st.session_state:
    st.session_state.animal_page = None

# Si un animal est choisi, afficher son formulaire
if st.session_state.animal_page == "chien":
    exec(open("pages/chien.py").read())
elif st.session_state.animal_page == "chat":
    exec(open("pages/chat.py").read())
elif st.session_state.animal_page == "lapin":
    exec(open("pages/lapin.py").read())
elif st.session_state.animal_page == "oiseau":
    exec(open("pages/oiseau.py").read())
else:
    # Afficher les boutons des animaux
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="animal-card">
            <div class="animal-emoji">🐕</div>
            <h3>Chien</h3>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🐕 Choisir Chien", key="btn_chien", use_container_width=True):
            st.session_state.animal_page = "chien"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="animal-card">
            <div class="animal-emoji">🐈</div>
            <h3>Chat</h3>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🐈 Choisir Chat", key="btn_chat", use_container_width=True):
            st.session_state.animal_page = "chat"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="animal-card">
            <div class="animal-emoji">🐇</div>
            <h3>Lapin</h3>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🐇 Choisir Lapin", key="btn_lapin", use_container_width=True):
            st.session_state.animal_page = "lapin"
            st.rerun()
    
    with col4:
        st.markdown("""
        <div class="animal-card">
            <div class="animal-emoji">🐦</div>
            <h3>Oiseau</h3>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🐦 Choisir Oiseau", key="btn_oiseau", use_container_width=True):
            st.session_state.animal_page = "oiseau"
            st.rerun()
