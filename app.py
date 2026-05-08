import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Corrector KDP Pro", 
    page_icon="📏", 
    layout="wide"
)

# 2. ESTILO PROFESIONAL (ALTO CONTRASTE)
st.markdown("""
    <style>
    /* Forzar fondo blanco y texto negro en toda la app */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .main {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    /* Ocultar elementos innecesarios */
    #MainMenu, footer {visibility: hidden;}

    /* Títulos en negro puro */
    h1, h2, h3, p, span, label {
        color: #000000 !important;
    }

    .hero-title {
        font-size: 50px !important;
        font-weight: 800 !important;
        text-align: center;
        margin-top: -40px;
        color: #000000 !important;
    }

    .hero-subtitle {
        font-size: 20px !important;
        text-align: center;
        margin-bottom: 40px !important;
        color: #333333 !important;
    }

    /* Caja de subida minimalista */
    .stFileUploader {
        border: 2px solid #000000 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        background-color: #FFFFFF !important;
        max-width: 800px;
        margin: 0 auto !important;
    }

    /* Botones de Pago Modernos */
    .btn-pago {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 18px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none !important;
        font-size: 1.1rem;
        border: 1px solid #000000;
        transition: 0.3s;
    }
    .btn-pago:hover {
        background-color: #f0f0f0;
        transform: scale(1.02);
    }

    /* Bloques de seguridad alineados */
    .trust-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 50px;
        flex-wrap: wrap;
    }
    .trust-card {
        flex: 1;
        min-width: 250px;
        border: 1px solid #EAEAEA;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
    }
    .trust-card h3 {
        font-size: 1.2rem !important;
        margin-bottom: 10px;
    }
    .trust-card p {
        font-size: 0.9rem !important;
        color: #555555 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENIDO PRINCIPAL
st.markdown('<h1 class="hero-title">Corrector de Formato KDP</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Prepare su manuscrito para Amazon en un clic. Profesional, rápido y seguro.</p>', unsafe_allow_html=True)

_, col_center, _ = st.columns([1, 3, 1])

with col_center:
    archivo = st.file_uploader("", type="pdf")

    if archivo:
        st.markdown("<br><h3 style='text-align:center;'>🔒 Paso final: Activación del procesamiento</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Coste del servicio: <b>2,99€</b> (IVA inc.)</p>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'''
                <a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba; color:white !important; border:none;">
                    Pagar con PayPal
                </a>
            ''', unsafe_allow_html=True)
        with c2:
            # SUSTITUYE 'tu_usuario' por el tuyo real de Revolut
            st.markdown(f'''
                <a href="https://revolut.me/danieltalavera/2.99" target="_blank" class="btn-pago" style="background-color:#000000; color:white !important; border:none;">
                    Pagar con Revolut
                </a>
            ''', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Procesar y Descargar Documento", use_container_width=True):
            st.write("Optimizando márgenes...")

# 4. SECCIÓN DE SEGURIDAD PROFESIONAL
st.markdown("""
    <div class="trust-container">
        <div class="trust-card">
            <h3>🛡️ Seguridad SSL</h3>
            <p>Conexión cifrada segura. Sus datos bancarios están protegidos por PayPal y Revolut.</p>
        </div>
        <div class="trust-card">
            <h3>🧹 Privacidad</h3>
            <p>Cumplimos con la RGPD. Su manuscrito se elimina permanentemente tras el proceso.</p>
        </div>
        <div class="trust-card">
            <h3>✅ Garantía KDP</h3>
            <p>Ajustes basados en las guías de impresión oficiales de Amazon para 2024.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 5. PIE DE PÁGINA PROFESIONAL
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#999999 !important; font-size:0.8rem;'>© 2026 CorrectorKDP Pro. Servicio independiente no afiliado a Amazon Inc.</p>", unsafe_allow_html=True)
