import streamlit as st
import pandas as pd

st.set_page_config(page_title="Admin Afri.T.A", page_icon="🔒", layout="wide")

MOT_DE_PASSE = "afrita2024"

st.title("🔒 Espace Agent Afri.T.A")

mdp = st.text_input("Mot de passe agent", type="password")

if mdp == MOT_DE_PASSE:
    st.success("✅ Accès autorisé")
    
    try:
        df = pd.read_csv("factures.csv")
    except:
        st.warning("Aucune facture pour le moment")
        df = pd.DataFrame(columns=["Numero", "Date", "Client", "Telephone", "Animal", "Race", "Poids", "Depart", "Arrivee", "Prix", "Statut"])
    
    st.markdown("---")
    
    st.subheader("🔍 Rechercher une facture")
    col1, col2 = st.columns([2, 1])
    with col1:
        numero_recherche = st.text_input("Numéro de facture", placeholder="Ex: AFR-20250416-143022-A3F2")
    with col2:
        if st.button("🔍 Rechercher"):
            if numero_recherche:
                resultat = df[df["Numero"] == numero_recherche]
                if len(resultat) > 0:
                    st.success("✅ Facture trouvée !")
                    st.dataframe(resultat)
                    
                    nouveau_statut = st.selectbox("Changer le statut", ["En attente paiement", "Payée", "En cours de transport", "Livrée", "Annulée"])
                    if st.button("Mettre à jour"):
                        df.loc[df["Numero"] == numero_recherche, "Statut"] = nouveau_statut
                        df.to_csv("factures.csv", index=False)
                        st.success(f"Statut mis à jour : {nouveau_statut}")
                        st.rerun()
                else:
                    st.error("❌ Facture non trouvée")
    
    st.markdown("---")
    st.subheader("📋 Toutes les commandes")
    
    if len(df) > 0:
        if "Statut" in df.columns:
            statut_filter = st.selectbox("Filtrer par statut", ["Toutes"] + list(df["Statut"].unique()))
            if statut_filter != "Toutes":
                df = df[df["Statut"] == statut_filter]
        
        st.metric("Nombre de commandes", len(df))
        st.dataframe(df, use_container_width=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Exporter en CSV", csv, "commandes.csv", "text/csv")
        
        st.subheader("📊 Statistiques")
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            st.metric("💰 Chiffre d'affaires", f"{df['Prix'].sum():,} FCFA")
        with col_s2:
            st.metric("📦 Total commandes", len(df))
        with col_s3:
            if "Statut" in df.columns:
                st.metric("✅ Commandes payées", len(df[df["Statut"] == "Payée"]))
    else:
        st.info("Aucune commande pour le moment")
elif mdp:
    st.error("❌ Mot de passe incorrect")
