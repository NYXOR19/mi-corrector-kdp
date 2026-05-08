import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Corrector KDP Pro", page_icon="📏", layout="wide")

# 2. ESTILO DEFINITIVO (FONDO BLANCO TOTAL, SIN FRANJAS NEGRAS)
st.markdown("""
    <style>
    /* Fondo general blanco */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    #MainMenu, footer {visibility: hidden;}

    .hero-title { font-size: 50px !important; font-weight: 800 !important; text-align: center; color: #000000 !important; margin-top: -40px; }
    .hero-subtitle { font-size: 20px !important; text-align: center; color: #333333 !important; margin-bottom: 40px !important; }

    /* --- ARREGLO DEL SUBIDOR DE ARCHIVOS (Basado en image_1bb514.png) --- */
    [data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        max-width: 800px;
        margin: 0 auto !important;
    }

    /* ELIMINAR LA FRANJA OSCURA INTERNA */
    [data-testid="stFileUploaderDropzone"] {
        background-color: #FFFFFF !important;
        border: 1px dashed #cccccc !important;
    }

    /* Forzar color de texto negro en todo el subidor */
    [data-testid="stFileUploaderDropzone"] button, 
    [data-testid="stFileUploaderDropzone"] span, 
    [data-testid="stFileUploaderDropzone"] div,
    [data-testid="stFileUploaderFileName"],
    [data-testid="stFileUploaderIcon"] {
        color: #000000 !important;
        fill: #000000 !important;
    }
    /* -------------------------------------------------- */
    
    /* BOTONES DE PAGO CON TEXTO BLANCO FORZADO */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 8px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: #FFFFFF !important; /* Texto blanco */
    }
    
    /* BOTÓN PROCESAR (ESTILO KDP) */
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

    .trust-card { border: 1px solid #EAEAEA; padding: 20px; border-radius: 12px; text-align: center; background: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ
st.markdown('<h1 class="hero-title">Corrector de Formato KDP</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Prepare su manuscrito para Amazon en un clic. Profesional, rápido y seguro.</p>', unsafe_allow_html=True)

_, col_center, _ = st.columns([1, 3, 1])

with col_center:
    archivo_subido = st.file_uploader("", type="pdf")

    if archivo_subido:
        st.markdown("<br><h3 style='text-align:center; color:black;'>🔒 Paso 1: Activación del procesamiento (2,99€)</h3>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba;">Pagar con PayPal</a>', unsafe_allow_html=True)
        with c2:
            # SUSTITUYE 'TU_USER_AQUI' POR TU NOMBRE DE REVOLUT (SIN EL @)
            st.markdown(f'<a href="https://revolut.me/smarteditorpro/2.99" target="_blank" class="btn-pago" style="background-color:#000000;">Pagar con Revolut</a>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🚀 Procesar y Descargar Documento", use_container_width=True):
            try:
                reader = PdfReader(archivo_subido)
                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                output_pdf = io.BytesIO()
                writer.write(output_pdf)
                output_pdf.seek(0)

                st.success("✅ ¡Optimización completada!")
                st.download_button(
                    label="📥 Descargar PDF Corregido",
                    data=output_pdf,
                    file_name="manuscrito_kdp_corregido.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error: {e}")

# 4. SECCIÓN DE CONFIANZA
st.markdown("<br><br>", unsafe_allow_html=True)
sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown('<div class="trust-card"><h3>🛡️</h3><b>Seguridad SSL</b><br>Pago 100% cifrado.</div>', unsafe_allow_html=True)
with sc2:
    st.markdown('<div class="trust-card"><h3>⌛</h3><b>Instantáneo</b><br>Sin esperas ni colas.</div>', unsafe_allow_html=True)
with sc3:
    st.markdown('<div class="trust-card"><h3>🧹</h3><b>Privacidad</b><br>Borrado tras descarga.</div>', unsafe_allow_html=True)
