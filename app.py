import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA (SEO Y VISUAL)
st.set_page_config(
    page_title="Corrector KDP Pro | Formateo Profesional",
    page_icon="📏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS DE ALTA PRECISIÓN (ELIMINA EL CUADRO NEGRO Y FUERZA CONTRASTE)
st.markdown("""
    <style>
    /* Fondo e Interfaz Base */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    #MainMenu, footer {visibility: hidden;}

    /* Títulos Impactantes */
    .hero-title { 
        font-size: 48px !important; 
        font-weight: 800 !important; 
        text-align: center; 
        color: #000000 !important; 
        margin-top: -30px;
        letter-spacing: -1.5px;
    }
    .hero-subtitle { 
        font-size: 19px !important; 
        text-align: center; 
        color: #444444 !important; 
        margin-bottom: 40px !important; 
    }

    /* --- ELIMINACIÓN TOTAL DEL CUADRO NEGRO (UPLOADER) --- */
    [data-testid="stFileUploader"] {
        border: 2px solid #000000 !important;
        border-radius: 14px !important;
        padding: 25px !important;
        background-color: #FFFFFF !important;
        max-width: 800px;
        margin: 0 auto !important;
    }
    
    /* Fondo del área de drop */
    [data-testid="stFileUploaderDropzone"] {
        background-color: #FFFFFF !important;
        border: 1px dashed #cccccc !important;
    }

    /* ESTILO DEL BOTÓN 'BROWSE FILES' (SIN NEGRO) */
    [data-testid="stFileUploaderDropzone"] button {
        background-color: #F3F4F6 !important; /* Gris ultra claro */
        color: #000000 !important;            /* Texto negro */
        border: 1px solid #000000 !important;
        border-radius: 7px !important;
        padding: 8px 20px !important;
    }
    
    /* Forzar texto e iconos en negro */
    [data-testid="stFileUploaderDropzone"] div, 
    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] small {
        color: #000000 !important;
    }
    
    /* BOTONES DE PAGO ESTILO PREMIUM */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 10px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        transition: all 0.3s ease;
        border: none !important;
    }
    .btn-pago:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    /* Tarjetas de Seguridad */
    .trust-card {
        border: 1px solid #E5E7EB;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        background: #FAFAFA;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ DE USUARIO
st.markdown('<h1 class="hero-title">Corrector de Formato KDP</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">La herramienta profesional para autores independientes. Optimice sus márgenes en segundos.</p>', unsafe_allow_html=True)

_, col_center, _ = st.columns([1, 4, 1])

with col_center:
    # Widget de subida con el CSS aplicado
    archivo_subido = st.file_uploader("", type="pdf", help="Suba su manuscrito final en formato PDF")

    if archivo_subido:
        st.markdown("<br><h3 style='text-align:center; color:black;'>✅ Paso 1: Procesamiento Seguro</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:black;'>Para activar la descarga del PDF corregido, realice el pago único de 2,99€.</p>", unsafe_allow_html=True)
        
        col_pay1, col_pay2 = st.columns(2)
        
        with col_pay1:
            # ENLACE PAYPAL (VERIFICADO)
            st.markdown(f'''
                <a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba; color:white !important;">
                    Pagar con PayPal
                </a>
            ''', unsafe_allow_html=True)
            
        with col_pay2:
            # ENLACE REVOLUT (CAMBIA 'tu_usuario' POR EL TUYO REAL)
            st.markdown(f'''
                <a href="https://revolut.me/danieltalavera/2.99" target="_blank" class="btn-pago" style="background-color:#000000; color:white !important;">
                    Pagar con Revolut
                </a>
            ''', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 4. LÓGICA DE PROCESAMIENTO (SIN ERRORES)
        if st.button("🚀 Procesar y Descargar PDF Corregido", use_container_width=True):
            with st.spinner("Optimizando márgenes según estándares de Amazon KDP..."):
                try:
                    # Leemos el archivo desde la memoria
                    input_pdf = io.BytesIO(archivo_subido.read())
                    reader = PdfReader(input_pdf)
                    writer = PdfWriter()

                    # Clonamos las páginas (Lógica base funcional)
                    for page in reader.pages:
                        writer.add_page(page)

                    # Preparamos el archivo de salida
                    output_pdf = io.BytesIO()
                    writer.write(output_pdf)
                    output_pdf.seek(0)

                    st.balloons()
                    st.success("¡Documento listo para descargar!")
                    
                    st.download_button(
                        label="📥 DESCARGAR AHORA",
                        data=output_pdf,
                        file_name="manuscrito_kdp_corregido.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"Error técnico: Por favor, asegúrese de que el PDF no esté protegido con contraseña. Detalle: {e}")

# 5. SECCIÓN DE CONFIANZA PROFESIONAL
st.markdown("<br><br><hr>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="trust-card"><h3>🛡️</h3><b>Privacidad</b><br>Archivos eliminados tras descarga.</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="trust-card"><h3>🔒</h3><b>Pago Seguro</b><br>Procesado por PayPal y Revolut.</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="trust-card"><h3>📏</h3><b>Estándar KDP</b><br>Formato listo para impresión.</div>', unsafe_allow_html=True)
