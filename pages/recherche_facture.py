import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Voir ma facture", page_icon="📄", layout="wide")

st.title("📄 Voir ma facture")

st.markdown("""
<style>
h1, h2, h3, p, label { color: white; }
</style>
""", unsafe_allow_html=True)

numero = st.text_input("Entrez votre numéro de facture", placeholder="Ex: AFR-20250416143022-a3f2")

if st.button("🔍 Rechercher"):
    if numero:
        if os.path.exists("factures.csv"):
            df = pd.read_csv("factures.csv")
            facture = df[df["Numero"] == numero]
            
            if len(facture) > 0:
                f = facture.iloc[0]
                st.success("✅ Facture trouvée !")
                
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 15px; margin-top: 1rem;">
                    <h3 style="color: #2d8c3e;">AFRI.T.A TRANSPORT</h3>
                    <p><strong>📄 Numéro :</strong> {f['Numero']}</p>
                    <p><strong>👤 Client :</strong> {f['Client']}</p>
                    <p><strong>📞 Téléphone :</strong> {f['Telephone']}</p>
                    <p><strong>🐕 Animal :</strong> {f['Animal']} - {f['Race']}</p>
                    <p><strong>⚖️ Poids :</strong> {f['Poids']} kg</p>
                    <p><strong>📍 Trajet :</strong> {f['Depart']} → {f['Arrivee']}</p>
                    <p><strong>📅 Date :</strong> {f['Date']}</p>
                    <p><strong>💰 Montant :</strong> {int(f['Prix']):,} FCFA</p>
                    <p><strong>📌 Statut :</strong> {f['Statut']}</p>
                    <hr>
                    <p style="text-align:center;">📍 À présenter à l'agence - Douala ou Yaoundé</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ Aucune facture trouvée avec ce numéro")
        else:
            st.warning("Aucune facture enregistrée pour le moment")
    else:
        st.warning("Veuillez entrer un numéro de facture")
