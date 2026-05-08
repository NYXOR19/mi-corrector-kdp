import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# Configuración de la página
st.set_page_config(page_title="Corrector KDP Pro", page_icon="📚")

st.title("📚 Optimizador de PDFs para Amazon KDP")
st.write("Ajusta tus márgenes y sangrías en segundos.")

# Subida de archivo
archivo_subido = st.file_uploader("Sube tu manuscrito en PDF aquí", type="pdf")

if archivo_subido is not None:
    st.success("✅ Archivo cargado correctamente")
    st.info("### 💳 Paso 1: Realiza el pago de $2.99 USD")
    enlace_paypal ="https://www.paypal.me/DanielTalavera443/2.99"
    st.markdown(f'''
        <a href="{enlace_paypal}" target="_blank">
            <button style="background-color: #0070ba; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px;">
                Pagar con PayPal ahora
            </button>
        </a>
    ''', unsafe_allow_html=True)

    st.divider()

    if st.button("Procesar y Preparar Descarga"):
        lector = PdfReader(archivo_subido)
        escritor = PdfWriter()
        
        for pagina in lector.pages:
            # Ajuste técnico de márgenes
            pagina.mediabox.upper_right = (
                pagina.mediabox.right + 9,
                pagina.mediabox.top + 9
            )
            escritor.add_page(pagina)
        
        # Guardar resultado
        salida_pdf = io.BytesIO()
        escritor.write(salida_pdf)
        
        st.success("✨ ¡Listo!")
        st.download_button(
            label="⬇️ Descargar PDF Optimizado",
            data=salida_pdf.getvalue(),
            file_name="libro_final_kdp.pdf",
            mime="application/pdf"
        )
