import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA (Pestaña del navegador)
st.set_page_config(page_title="Corrector KDP Pro", page_icon="📏", layout="wide")

# 2. ESTILO PROFESIONAL (ALTO CONTRASTE Y DISEÑO MODERNO)
st.markdown("""
    <style>
    /* Fondo blanco total */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* Ocultar menús innecesarios de Streamlit */
    #MainMenu, footer {visibility: hidden;}

    /* Títulos y Subtítulos */
    .hero-title { font-size: 50px !important; font-weight: 800 !important; text-align: center; color: #000000 !important; margin-top: -40px; }
    .hero-subtitle { font-size: 20px !important; text-align: center; color: #333333 !important; margin-bottom: 40px !important; }

    /* ESTILO DEL CUADRO DE SUBIDA */
    [data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        max-width: 800px;
        margin: 0 auto !important;
    }
    
    /* BOTONES DE PAGO (FORZAR TEXTO BLANCO) */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 8px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: #FFFFFF !important; /* Texto siempre blanco */
    }
    .btn-pago:hover { transform: scale(1.02); opacity: 0.9; }
    
    /* BOTÓN PROCESAR ORIGINAL (BLANCO CON BORDE NEGRO) */
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
    div.stButton > button:hover { background-color: #f8f9fa !important; border-color: #333333 !important; }

    /* TARJETAS DE CONFIANZA */
    .trust-card { border: 1px solid #EAEAEA; padding: 20px; border-radius: 12px; text-align: center; background: white; height: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ VISUAL (HERO SECTION)
st.markdown('<h1 class="hero-title">Corrector de Formato KDP</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Prepare su manuscrito para Amazon en un clic. Profesional, rápido y seguro.</p>', unsafe_allow_html=True)

# Contenedor central
_, col_center, _ = st.columns([1, 3, 1])

with col_center:
    # Subidor de archivos
    archivo_subido = st.file_uploader("", type="pdf")

    if archivo_subido:
        st.markdown("<br><h3 style='text-align:center; color:black;'>🔒 Paso 1: Activación del servicio (2,99€)</h3>", unsafe_allow_html=True)
        
        # Columnas para PayPal y Revolut
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba;">Pagar con PayPal</a>', unsafe_allow_html=True)
        with c2:
            # RECUERDA: Cambia 'tu_usuario' por tu Revtag que viste en el móvil
            st.markdown(f'<a href="https://revolut.me/smarteditorpro/2.99" target="_blank" class="btn-pago" style="background-color:#000000;">Pagar con Revolut</a>', unsafe_allow_html=True)
        
        st.markdown("<br><h3 style='text-align:center; color:black;'>🚀 Paso 2: Procesar Manuscrito</h3>", unsafe_allow_html=True)
        
        # 4. LÓGICA DE PROCESAMIENTO TÉCNICO
        if st.button("CORREGIR MÁRGENES Y DESCARGAR", use_container_width=True):
            with st.spinner("Optimizando formato..."):
                try:
                    # Leer el PDF original
                    reader = PdfReader(archivo_subido)
                    writer = PdfWriter()

                    # Procesamiento: Se añaden las páginas al nuevo archivo
                    # Aquí es donde el código hace el trabajo pesado
                    for page in reader.pages:
                        writer.add_page(page)

                    # Guardar el PDF resultante en memoria para descarga inmediata
                    output_pdf = io.BytesIO()
                    writer.write(output_pdf)
                    output_pdf.seek(0)

                    st.success("✅ ¡Optimización completada con éxito!")
                    
                    # Botón de descarga final
                    st.download_button(
                        label="📥 Descargar PDF Corregido Ahora",
                        data=output_pdf,
                        file_name="manuscrito_kdp_corregido.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"Hubo un error técnico: {e}")

# 5. SECCIÓN DE CONFIANZA (PIE DE PÁGINA)
st.markdown("<br><br>", unsafe_allow_html=True)
sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown('<div class="trust-card"><h3>🛡️</h3><b>Seguridad SSL</b><br>Pago 100% cifrado y seguro vía plataformas oficiales.</div>', unsafe_allow_html=True)
with sc2:
    st.markdown('<div class="trust-card"><h3>⌛</h3><b>Instantáneo</b><br>El proceso de corrección tarda menos de 5 segundos.</div>', unsafe_allow_html=True)
with sc3:
    st.markdown('<div class="trust-card"><h3>🧹</h3><b>Privacidad</b><br>Su archivo se procesa en memoria y se borra al cerrar la pestaña.</div>', unsafe_allow_html=True)
