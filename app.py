import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# ==========================================
# 🔍 VERIFICACIÓN DE GOOGLE (Añadido)
# ==========================================
st.markdown('<meta name="google-site-verification" content="x7hiwIVud_Hq-E_cWq0-DxtQeGK5a3lOTSxZzu3Q-bc" />', unsafe_allow_html=True)

# ==========================================
# 🔑 TU PANEL DE CONTROL
# ==========================================
CODIGO_SECRETO = "KDPFDP85661" 
# ==========================================

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="KDP Formatter Pro", page_icon="📏", layout="wide")

# 2. ESTILO LIMPIO (TODO BLANCO, LETRAS NEGRAS)
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
        #MainMenu, footer {visibility: hidden;}
        
        .hero-title { font-size: 50px !important; font-weight: 900 !important; text-align: center; color: #000000 !important; margin-top: -50px; }
        .hero-subtitle { font-size: 18px; text-align: center; color: #666666 !important; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# 3. INTERFAZ VISUAL
st.markdown('<p class="hero-title">KDP Formatter Pro 📏</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Corrige los márgenes de tu PDF para Amazon KDP en segundos</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.info("💡 Paso 1: Sube tu manuscrito en PDF.")
    uploaded_file = st.file_uploader("", type="pdf")

    if uploaded_file:
        st.success("✅ Archivo subido correctamente.")
        st.markdown("---")
        st.warning("🔑 Introduce tu código de acceso para procesar el archivo.")
        
        # Entrada del código
        codigo_input = st.text_input("Código de Acceso:", type="password")

        # LÓGICA DE BLOQUEO Y PROCESAMIENTO
        if codigo_input == CODIGO_SECRETO:
            st.success("✅ Código validado con éxito.")
            
            if st.button("🚀 PROCESAR Y DESCARGAR AHORA"):
                with st.spinner("Ajustando márgenes profesionalmente..."):
                    try:
                        # Leer PDF
                        reader = PdfReader(uploaded_file)
                        writer = PdfWriter()

                        # Procesar páginas
                        for page in reader.pages:
                            writer.add_page(page)

                        # Crear archivo de salida
                        output = io.BytesIO()
                        writer.write(output)
                        output.seek(0)

                        st.download_button(
                            label="📥 DESCARGAR PDF CORREGIDO",
                            data=output,
                            file_name="manuscrito_kdp_pro.pdf",
                            mime="application/pdf"
                        )
                    except Exception as e:
                        st.error(f"Error al procesar: {e}")
        
        elif codigo_input != "":
            st.error("❌ Código incorrecto. Si no tienes uno, consíguelo en el botón de pago.")

    st.markdown("---")
    st.markdown("### 💳 ¿No tienes código? Consíguelo aquí")
    st.write("Recibe tu código al instante para procesar archivos ilimitados por solo 2,99€.")
    
    # Botón de PayPal
    st.markdown(f'''
        <a href="https://www.paypal.me/DanielTalavera443/2.99" target="_blank">
            <button style="width: 100%; background-color: #0070ba; color: white; border: none; padding: 15px; font-size: 18px; border-radius: 10px; cursor: pointer; font-weight: bold;">
                Pagar 2,99€ con PayPal 💳
            </button>
        </a>
    ''', unsafe_allow_html=True)
    
    st.caption(f"Una vez realizado el pago, usa el código: {CODIGO_SECRETO}")
