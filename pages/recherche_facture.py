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
                
                # Facture avec texte noir sur fond blanc
                st.markdown(f"""
                <div style="background: white; padding: 1.5rem; border-radius: 15px; margin-top: 1rem; border: 1px solid #ddd;">
                    <h3 style="color: #2d8c3e; text-align: center;">AFRI.T.A TRANSPORT</h3>
                    <p style="text-align: center; color: #666; margin-bottom: 1rem;">Agence de transport animalier - Cameroun</p>
                    
                    <hr>
                    
                    <p><strong style="color: #333;">📄 Numéro de facture :</strong> <span style="color: #555;">{f['Numero']}</span></p>
                    <p><strong style="color: #333;">👤 Client :</strong> <span style="color: #555;">{f['Client']}</span></p>
                    <p><strong style="color: #333;">📞 Téléphone :</strong> <span style="color: #555;">{f['Telephone']}</span></p>
                    <p><strong style="color: #333;">🐕 Animal :</strong> <span style="color: #555;">{f['Animal']} - {f['Race']}</span></p>
                    <p><strong style="color: #333;">⚖️ Poids :</strong> <span style="color: #555;">{f['Poids']} kg</span></p>
                    <p><strong style="color: #333;">📍 Trajet :</strong> <span style="color: #555;">{f['Depart']} → {f['Arrivee']}</span></p>
                    <p><strong style="color: #333;">📅 Date :</strong> <span style="color: #555;">{f['Date']}</span></p>
                    
                    <hr>
                    
                    <p style="font-size: 1.2rem;"><strong style="color: #2d8c3e;">💰 Montant total :</strong> <strong style="color: #e91e63;">{int(f['Prix']):,} FCFA</strong></p>
                    <p><strong style="color: #333;">📌 Statut :</strong> <span style="color: #555;">{f['Statut']}</span></p>
                    
                    <hr>
                    
                    <p style="text-align: center; color: #888; font-size: 0.8rem;">
                        📍 À présenter à l'agence - Douala ou Yaoundé<br>
                        📞 +237 6XX XXX XXX
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ Aucune facture trouvée avec ce numéro")
        else:
            st.warning("Aucune facture enregistrée pour le moment")
    else:
        st.warning("Veuillez entrer un numéro de facture")
