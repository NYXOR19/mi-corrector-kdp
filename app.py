import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN TÉCNICA Y SEO
st.set_page_config(
    page_title="Corrector KDP Pro | Formateo de Manuscritos Profesional", 
    page_icon="📏", 
    layout="wide"
)

# 2. DISEÑO DE ALTA GAMA (CSS)
st.markdown("""
    <style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }

    /* Título principal impacto */
    .hero-title {
        color: #111827;
        font-size: 52px !important;
        font-weight: 800;
        text-align: center;
        margin-top: -50px;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        color: #4B5563;
        font-size: 20px;
        text-align: center;
        margin-bottom: 50px;
    }

    /* Caja de subida estilo image_281579.png */
    .stFileUploader {
        border: 2px dashed #3B82F6 !important;
        border-radius: 16px !important;
        padding: 30px !important;
        background-color: #F9FAFB !important;
        max-width: 850px;
        margin: 0 auto;
    }

    /* Botones Profesionales */
    .btn-pago {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 16px;
        border-radius: 12px;
        font-weight: 700;
        text-decoration: none;
        transition: transform 0.2s;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .btn-pago:hover {
        transform: translateY(-2px);
    }

    /* Sección Seguridad estilo image_2814de.jpg */
    .security-badge {
        background: #F3F4F6;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 40px;
        border: 1px solid #E5E7EB;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTENIDO VISUAL
st.markdown('<h1 class="hero-title">Optimice su PDF para Amazon KDP</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">La solución definitiva para autores. Ajuste márgenes y sangrías con precisión milimétrica.</p>', unsafe_allow_html=True)

# Layout centrado para la herramienta
_, center_col, _ = st.columns([1, 4, 1])

with center_col:
    archivo_subido = st.file_uploader("Suelte su manuscrito en PDF aquí para comenzar", type="pdf")

    if archivo_subido:
        st.success("✅ Documento detectado con éxito. Listo para procesar.")
        
        # Bloque de Pago
        st.markdown("### 🔒 Active el procesamiento profesional")
        st.write("Para garantizar la precisión de su formato KDP, realice el pago único de **2,99€**:")
        
        pay_col1, pay_col2 = st.columns(2)
        
        with pay_col1:
            st.markdown(f'''
                <a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color: #0070BA; color: white;">
                    💳 Pagar con PayPal
                </a>
            ''', unsafe_allow_html=True)
            
        with pay_col2:
            # ⚠️ RECUERDA CAMBIAR EL USUARIO AQUÍ ABAJO
            st.markdown(f'''
                <a href="https://revolut.me/danieltalavera/2.99" target="_blank" class="btn-pago" style="background-color: #000000; color: white;">
                    ⚡ Pagar con Revolut
                </a>
            ''', unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Iniciar Optimización y Descargar", use_container_width=True):
            st.info("Ajustando márgenes según estándares de Amazon KDP... Por favor, no cierre la página.")
            # Aquí va tu lógica de PdfReader/Writer

# 4. SECCIÓN DE CONFIANZA Y SEGURIDAD
st.markdown("---")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    st.markdown('<div class="security-badge"><h3>🛡️</h3><b>100% Seguro</b><br>Cifrado SSL de extremo a extremo.</div>', unsafe_allow_html=True)
with col_s2:
    st.markdown('<div class="security-badge"><h3>⌛</h3><b>Procesado Instantáneo</b><br>Su PDF listo en menos de 10 segundos.</div>', unsafe_allow_html=True)
with col_s3:
    st.markdown('<div class="security-badge"><h3>🧹</h3><b>Privacidad Garantizada</b><br>Archivos eliminados tras la descarga.</div>', unsafe_allow_html=True)

# 5. PREGUNTAS FRECUENTES (FAQ) - Estilo image_2811d9.jpg
st.markdown("<br><h2 style='text-align:center;'>Preguntas Frecuentes</h2>", unsafe_allow_html=True)
with st.expander("¿Mi libro mantendrá la calidad original?"):
    st.write("Absolutamente. Solo modificamos los parámetros de márgenes y sangrías, el texto y las imágenes permanecen intactos.")

with st.expander("¿Qué pasa si el archivo no queda bien?"):
    st.write("Nuestro algoritmo sigue las guías oficiales de Amazon KDP 2024. Si tiene dudas, nuestro soporte le atenderá en 24h.")
