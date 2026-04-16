import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Voir ma facture", page_icon="📄", layout="wide")

st.title("📄 Voir ma facture")

numero = st.text_input("Entrez votre numéro de facture", placeholder="Ex: AFR-20250416143022-a3f2")

if st.button("🔍 Rechercher"):
    if numero:
        if os.path.exists("factures.csv"):
            df = pd.read_csv("factures.csv")
            facture = df[df["Numero"] == numero]
            
            if len(facture) > 0:
                f = facture.iloc[0]
                st.success("✅ Facture trouvée !")
                
                # Affichage de la facture
                st.markdown("---")
                st.subheader("📄 DÉTAIL DE LA FACTURE")
                
                st.write(f"**📄 Numéro :** {f['Numero']}")
                st.write(f"**👤 Client :** {f['Client']}")
                st.write(f"**📞 Téléphone :** {f['Telephone']}")
                st.write(f"**🐕 Animal :** {f['Animal']} - {f['Race']}")
                st.write(f"**⚖️ Poids :** {f['Poids']} kg")
                st.write(f"**📍 Trajet :** {f['Depart']} → {f['Arrivee']}")
                st.write(f"**📅 Date :** {f['Date']}")
                st.write(f"**💰 Montant :** {int(f['Prix']):,} FCFA")
                st.write(f"**📌 Statut :** {f['Statut']}")
                
                st.markdown("---")
                st.info("📍 À présenter à l'agence - Douala ou Yaoundé\n\n📞 +237 6XX XXX XXX")
            else:
                st.error("❌ Aucune facture trouvée avec ce numéro")
        else:
            st.warning("Aucune facture enregistrée pour le moment")
    else:
        st.warning("Veuillez entrer un numéro de facture")
