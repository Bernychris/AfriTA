import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Admin Afri.T.A", page_icon="🔒", layout="wide")

MOT_DE_PASSE = "afrita2024"

st.title("🔒 Espace Agent Afri.T.A")

mdp = st.text_input("Mot de passe agent", type="password")

if mdp == MOT_DE_PASSE:
    st.success("✅ Accès autorisé")
    
    # Vérifier si le fichier factures.csv existe
    if os.path.exists("factures.csv"):
        df = pd.read_csv("factures.csv")
        
        # Ajouter la colonne Statut si elle n'existe pas
        if "Statut" not in df.columns:
            df["Statut"] = "En attente paiement"
            df.to_csv("factures.csv", index=False)
    else:
        st.warning("Aucune facture pour le moment")
        df = pd.DataFrame(columns=["Numero", "Date", "Client", "Telephone", "Email", "Animal", "Race", "Poids", "Depart", "Arrivee", "Distance", "Prix", "Statut"])
    
    st.markdown("---")
    
    # ========== 1. RECHERCHER PAR NUMÉRO ==========
    st.subheader("🔍 Rechercher une facture")
    col1, col2 = st.columns([2, 1])
    with col1:
        numero_recherche = st.text_input("Numéro de facture", placeholder="Ex: AFR-20250416-143022-A3F2")
    with col2:
        if st.button("🔍 Rechercher"):
            if numero_recherche and len(df) > 0:
                resultat = df[df["Numero"] == numero_recherche]
                if len(resultat) > 0:
                    st.success("✅ Facture trouvée !")
                    st.dataframe(resultat)
                    
                    # Récupérer l'index de la ligne
                    index = df[df["Numero"] == numero_recherche].index[0]
                    statut_actuel = df.loc[index, "Statut"]
                    
                    st.markdown(f"**Statut actuel :** {statut_actuel}")
                    nouveau_statut = st.selectbox(
                        "Changer le statut",
                        ["En attente paiement", "Payée", "En cours de transport", "Livrée", "Annulée"],
                        index=["En attente paiement", "Payée", "En cours de transport", "Livrée", "Annulée"].index(statut_actuel) if statut_actuel in ["En attente paiement", "Payée", "En cours de transport", "Livrée", "Annulée"] else 0
                    )
                    
                    if st.button("✅ Mettre à jour le statut"):
                        df.loc[index, "Statut"] = nouveau_statut
                        df.to_csv("factures.csv", index=False)
                        st.success(f"✅ Statut mis à jour : {nouveau_statut}")
                        st.rerun()
                else:
                    st.error("❌ Facture non trouvée")
            else:
                st.warning("Entrez un numéro de facture")
    
    st.markdown("---")
    
    # ========== 2. LISTE DE TOUTES LES COMMANDES ==========
    st.subheader("📋 Toutes les commandes")
    
    if len(df) > 0:
        # Filtres
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            statut_filter = st.selectbox("Filtrer par statut", ["Toutes"] + list(df["Statut"].unique()))
        with col_f2:
            if "Animal" in df.columns:
                animal_filter = st.selectbox("Filtrer par animal", ["Tous"] + list(df["Animal"].unique()))
        
        # Appliquer les filtres
        df_filtered = df.copy()
        if statut_filter != "Toutes":
            df_filtered = df_filtered[df_filtered["Statut"] == statut_filter]
        if animal_filter != "Tous" and "Animal" in df.columns:
            df_filtered = df_filtered[df_filtered["Animal"] == animal_filter]
        
        st.metric("📊 Nombre de commandes", len(df_filtered))
        st.dataframe(df_filtered[["Numero", "Date", "Client", "Animal", "Race", "Depart", "Arrivee", "Prix", "Statut"]], use_container_width=True)
        
        # Bouton pour modifier le statut directement depuis la liste
        st.subheader("✏️ Modifier un statut rapidement")
        col_m1, col_m2, col_m3 = st.columns([2, 1, 1])
        with col_m1:
            numero_modif = st.selectbox("Choisir une facture", df["Numero"].tolist())
        with col_m2:
            nouveau_statut_liste = st.selectbox("Nouveau statut", ["En attente paiement", "Payée", "En cours de transport", "Livrée", "Annulée"])
        with col_m3:
            if st.button("Appliquer"):
                df.loc[df["Numero"] == numero_modif, "Statut"] = nouveau_statut_liste
                df.to_csv("factures.csv", index=False)
                st.success(f"✅ Statut mis à jour pour {numero_modif} : {nouveau_statut_liste}")
                st.rerun()
        
        # Bouton pour exporter
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Exporter en CSV", csv, "commandes.csv", "text/csv")
        
        # ========== 3. STATISTIQUES ==========
        st.subheader("📊 Statistiques")
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.metric("💰 Chiffre d'affaires", f"{df['Prix'].sum():,} FCFA")
        with col_s2:
            st.metric("📦 Total commandes", len(df))
        with col_s3:
            st.metric("✅ Payées", len(df[df["Statut"] == "Payée"]))
        with col_s4:
            st.metric("🚚 En cours", len(df[df["Statut"] == "En cours de transport"]))
    else:
        st.info("Aucune commande pour le moment")
        
elif mdp:
    st.error("❌ Mot de passe incorrect")
else:
    st.info("🔐 Entrez le mot de passe pour accéder à l'espace agent")
