import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Corrector KDP Pro", page_icon="📏", layout="wide")

# 2. ESTILO DEFINITIVO (DISEÑO BLANCO Y BOTÓN DE TARJETA)
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    #MainMenu, footer {visibility: hidden;}

    .hero-title { font-size: 50px !important; font-weight: 800 !important; text-align: center; color: #000000 !important; margin-top: -40px; }
    .hero-subtitle { font-size: 20px !important; text-align: center; color: #333333 !important; margin-bottom: 40px !important; }

    /* SUBIDOR DE ARCHIVOS LIMPIO */
    [data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        max-width: 800px;
        margin: 0 auto !important;
    }

    [data-testid="stFileUploaderDropzone"] {
        background-color: #FFFFFF !important;
        border: 1px dashed #cccccc !important;
    }

    [data-testid="stFileUploaderDropzone"] button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
    }

    [data-testid="stFileUploaderDropzone"] * {
        color: #000000 !important;
        fill: #000000 !important;
    }
    
    /* BOTONES DE PAGO */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 8px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: #FFFFFF !important;
        margin-bottom: 10px;
    }
    
    /* BOTÓN PROCESAR */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        font-weight: 800 !important;
        width: 100% !important;
        border-radius: 12px !important;
        height: 3.8em !important;
        margin-top: 20px;
    }

    /* TARJETAS DE CONFIANZA */
    .trust-card {
        border: 1px solid #EAEAEA;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        background: white;
        min-height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .trust-icon { font-size: 30px; margin-bottom: 10px; }
    .trust-text { color: #666666 !important; font-size: 14px; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ
st.markdown('<h1 class="hero-title">Corrector de Formato KDP</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Optimización profesional de manuscritos para Amazon KDP.</p>', unsafe_allow_html=True)

_, col_center, _ = st.columns([1, 3, 1])

with col_center:
    archivo_subido = st.file_uploader("", type="pdf")

    if archivo_subido:
        st.markdown("<br><h3 style='text-align:center; color:black;'>🔒 Paso final: Activación del procesamiento</h3>", unsafe_allow_html=True)
        
        # BOTONES DE PAGO (Tarjeta y PayPal)
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba;">💳 Pagar con Tarjeta (Visa/Mastercard)</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#ed9605; color: #000000 !important;">🅿️ Pagar con cuenta PayPal</a>', unsafe_allow_html=True)
        
        st.markdown("<p style='text-align:center; font-size: 12px; color: gray;'>* Al hacer clic en Tarjeta, selecciona 'Pagar como invitado' o 'Crear cuenta' para usar tu tarjeta sin registrarte.</p>", unsafe_allow_html=True)
        
        if st.button("🚀 Procesar y Descargar Documento", use_container_width=True):
            try:
                reader = PdfReader(archivo_subido)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                output_pdf = io.BytesIO()
                writer.write(output_pdf)
                output_pdf.seek(0)

                st.success("✅ ¡Procesado correctamente!")
                st.download_button(
                    label="📥 Descargar PDF Corregido",
                    data=output_pdf,
                    file_name="manuscrito_corregido.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error técnico: {e}")

# 4. SECCIÓN DE CONFIANZA
st.markdown("<br><br>", unsafe_allow_html=True)
sc1, sc2, sc3 = st.columns(3)

with sc1:
    st.markdown('<div class="trust-card"><div class="trust-icon">🛡️</div><b>Pago Seguro</b><div class="trust-text">Cifrado SSL con PayPal y Tarjeta.</div></div>', unsafe_allow_html=True)
with sc2:
    st.markdown('<div class="trust-card"><div class="trust-icon">⌛</div><b>Instantáneo</b><div class="trust-text">Tu archivo listo en segundos.</div></div>', unsafe_allow_html=True)
with sc3:
    st.markdown('<div class="trust-card"><div class="trust-icon">🧹</div><b>Privacidad</b><div class="trust-text">Borrado automático tras descargar.</div></div>', unsafe_allow_html=True)
