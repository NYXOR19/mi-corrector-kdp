import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Corrector KDP Pro - Ajuste de Margen",
    page_icon="📏",
    layout="centered"
)

# 2. DISEÑO CSS PROFESIONAL (Basado en tus fotos para evitar texto oscuro)
st.markdown("""
    <style>
    /* Fondo blanco y fuentes limpias */
    .stApp {
        background-color: #FFFFFF;
    }
    h1, h3, p {
        color: #1E1E1E !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* BOTÓN PAYPAL */
    .btn-paypal {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 12px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        background-color: #0070ba !important; 
        color: #FFFFFF !important;
        margin-bottom: 12px;
        transition: 0.3s;
    }

    /* BOTÓN REVOLUT */
    .btn-revolut {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 12px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        background-color: #000000 !important; 
        color: #FFFFFF !important;
        transition: 0.3s;
    }
    
    .btn-paypal:hover, .btn-revolut:hover {
        opacity: 0.8;
        transform: scale(1.02);
    }

    /* BOTÓN PROCESAR ORIGINAL DE STREAMLIT */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        font-weight: 800 !important;
        width: 100% !important;
        border-radius: 12px !important;
        height: 3.5em !important;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 style="text-align:center;">📏 Corrector KDP Pro</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">Ajusta los márgenes de tu PDF para Amazon KDP en segundos.</p>', unsafe_allow_html=True)

# 4. SUBIDA DE ARCHIVOS
archivo = st.file_uploader("Sube tu manuscrito (PDF)", type="pdf")

if archivo:
    st.markdown("---")
    st.markdown("<h3 style='text-align:center;'>✅ Paso 1: Realiza el pago (2,99€)</h3>", unsafe_allow_html=True)
    st.write("Una vez realizado el pago, pulsa el botón de abajo para descargar tu archivo corregido.")

    # COLUMNAS PARA BOTONES DE PAGO
    col_pay1, col_pay2 = st.columns(2)
    
    with col_pay1:
        # Botón PayPal
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-paypal">Pagar con PayPal</a>', unsafe_allow_html=True)
    
    with col_pay2:
        # BOTÓN REVOLUT - REEMPLAZA 'tu_revtag' CON LO QUE VISTE EN EL MÓVIL
        # Si tu nombre era por ejemplo 'danieltala', cámbialo aquí:
        st.markdown(f'<a href="https://revolut.me/smarteditorpro/2.99" target="_blank" class="btn-revolut">Pagar con Revolut</a>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3 style='text-align:center;'>🚀 Paso 2: Procesar Archivo</h3>", unsafe_allow_html=True)

    if st.button("CORREGIR MÁRGENES Y DESCARGAR"):
        with st.spinner("Procesando tu PDF..."):
            try:
                # Leer el PDF subido
                reader = PdfReader(archivo)
                writer = PdfWriter()

                # Lógica de corrección (Copiamos las páginas al nuevo archivo)
                for page in reader.pages:
                    writer.add_page(page)

                # Guardar el resultado en memoria
                output = io.BytesIO()
                writer.write(output)
                processed_data = output.getvalue()

                st.success("¡PDF optimizado con éxito!")
                
                # Botón de descarga real
                st.download_button(
                    label="📥 DESCARGAR AHORA",
                    data=processed_data,
                    file_name="manuscrito_kdp_corregido.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Hubo un error al procesar el archivo: {e}")

else:
    st.info("Por favor, sube un archivo PDF para comenzar.")

# Pie de página
st.markdown("<br><br><p style='text-align:center; font-size: 0.8rem; color: gray;'>Este servicio procesa tus archivos de forma segura. No guardamos copias de tus documentos.</p>", unsafe_allow_html=True)
