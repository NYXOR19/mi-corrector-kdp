import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# VERIFICACION DE GOOGLE (Añadido sin tocar el diseño)
st.markdown('<meta name="google-site-verification" content="x7hiwIVud_Hq-E_cWq0-DxtQeGK5a3lOTSxZzu3Q-bc" />', unsafe_allow_html=True)

# ==========================================
# 🔑 TU PANEL DE CONTROL
# ==========================================
CODIGO_SECRETO = "KDPFDP85661" 

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="KDP Formatter Pro", page_icon="📏", layout="wide")

# 2. ESTILO LIMPIO
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("KDP Formatter Pro")

# 3. DISEÑO EN COLUMNAS (Como lo tenías antes)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("1. Sube tu manuscrito")
    uploaded_file = st.file_uploader("Selecciona tu archivo PDF", type="pdf")
    
    if uploaded_file:
        codigo_input = st.text_input("Introduce el código de acceso", type="password")
        
        if codigo_input == CODIGO_SECRETO:
            st.success("✅ Código correcto")
            if st.button("Procesar y Ajustar PDF"):
                reader = PdfReader(uploaded_file)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                
                output = io.BytesIO()
                writer.write(output)
                output.seek(0)
                
                st.download_button("📥 Descargar PDF Corregido", output, "kdp_final.pdf")
        elif codigo_input != "":
            st.error("❌ Código incorrecto")

with col2:
    st.subheader("2. Pago y Acceso")
    st.info("Obtén tu código al instante")
    
    # El cuadrado de PayPal/Tarjeta a la derecha
    st.markdown(f'''
        <div style="border: 2px solid #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
            <p>Acceso ilimitado por 2,99€</p>
            <a href="https://www.paypal.me/DanielTalavera443/2.99" target="_blank">
                <button style="width: 100%; background-color: #0070ba; color: white; border: none; padding: 12px; border-radius: 5px; cursor: pointer; font-weight: bold;">
                    Pagar con PayPal o Tarjeta
                </button>
            </a>
            <p style="font-size: 12px; margin-top: 10px;">El código aparecerá aquí tras el pago</p>
        </div>
    ''', unsafe_allow_html=True)
    
    st.write(f"Código: **{CODIGO_SECRETO}**")

st.markdown("---")
st.caption("Herramienta profesional para autores de Amazon KDP")
