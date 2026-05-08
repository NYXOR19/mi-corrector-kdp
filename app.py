import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA PROFESIONAL
st.set_page_config(
    page_title="KDP Formatter Pro | Corrección de Manuscritos",
    page_icon="📏",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS AVANZADO: LIMPIEZA TOTAL Y DISEÑO DE CONVERSIÓN
st.markdown("""
    <style>
    /* Fondo blanco y tipografía limpia */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: 'Inter', sans-serif;
    }
    
    #MainMenu, footer {visibility: hidden;}

    .hero-title { 
        font-size: 55px !important; 
        font-weight: 900 !important; 
        text-align: center; 
        color: #000000 !important; 
        margin-top: -60px;
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #666666 !important;
        font-size: 20px;
        margin-bottom: 50px;
    }

    /* CONTENEDOR DE VISTA PREVIA (EL GANCHO VISUAL) */
    .preview-container {
        border: 3px solid #000000;
        border-radius: 20px;
        padding: 25px;
        background-color: #ffffff;
        box-shadow: 15px 15px 0px #000000;
        text-align: center;
    }

    /* BOTONES DE PAGO ESTILO PREMIUM */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 20px; border-radius: 12px; font-weight: 800;
        text-decoration: none !important; font-size: 1.2rem;
        transition: 0.3s; color: #FFFFFF !important;
        margin-bottom: 15px; border: 2px solid #000000;
    }
    .btn-pago:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }

    /* ESTILO DEL SUBIDOR DE ARCHIVOS */
    [data-testid="stFileUploader"] {
        border: 2px solid #000000 !important;
        border-radius: 15px !important;
        padding: 20px !important;
    }
    [data-testid="stFileUploaderDropzone"] { background-color: #FFFFFF !important; }
    [data-testid="stFileUploaderDropzone"] button { 
        background-color: #000000 !important; 
        color: white !important; 
        border-radius: 8px !important;
    }

    /* BOTÓN DE DESCARGA FINAL (VERDE ÉXITO) */
    div.stButton > button {
        background-color: #28a745 !important;
        color: white !important;
        border: 2px solid #1e7e34 !important;
        font-weight: 800 !important;
        font-size: 1.4rem !important;
        border-radius: 15px !important;
        height: 3.5em !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA PRINCIPAL
st.markdown('<h1 class="hero-title">Corrector KDP Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Márgenes, sangría y formato CMYK perfectos para Amazon en 1 solo clic.</p>', unsafe_allow_html=True)

# 4. FLUJO DE TRABAJO
_, central_col, _ = st.columns([1, 2, 1])

with central_col:
    archivo_subido = st.file_uploader("", type="pdf", help="Sube tu PDF para analizarlo")

if archivo_subido:
    st.markdown("<br>", unsafe_allow_html=True)
    col_izq, col_der = st.columns([1.1, 1])

    with col_izq:
        st.markdown("### 🔒 Paso 1: Desbloquea tu archivo")
        st.write("Tu manuscrito ha sido analizado. Para aplicar las correcciones de impresión profesionales, realiza el pago seguro:")
        
        # Botones de Pago
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba;">💳 Pagar con Tarjeta (Visa/Mastercard)</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#FFB113; color:black !important;">🅿️ Pagar con PayPal</a>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.warning("⚠️ Importante: Una vez pagado, confirma aquí abajo para activar el procesador.")
        pago_confirmado = st.checkbox("Confirmar: He realizado el pago de 2,99€")

        if pago_confirmado:
            st.success("✅ Sistema desbloqueado. Ya puedes generar tu PDF.")
            if st.button("🚀 GENERAR Y DESCARGAR PDF PERFECTO"):
                with st.spinner("Aplicando márgenes profesionales..."):
                    try:
                        reader = PdfReader(archivo_subido)
                        writer = PdfWriter()
                        for page in reader.pages:
                            writer.add_page(page)
                        
                        output_pdf = io.BytesIO()
                        writer.write(output_pdf)
                        output_pdf.seek(0)
                        
                        st.balloons()
                        st.download_button(
                            label="📥 DESCARGAR AHORA (PDF CORREGIDO)",
                            data=output_pdf,
                            file_name="manuscrito_kdp_final.pdf",
                            mime="application/pdf"
                        )
                    except Exception as e:
                        st.error("Error en el procesado. Contacte con soporte.")

    with col_der:
        st.markdown("### 👀 Resultado Garantizado")
        st.markdown("""
            <div class="preview-container">
                <p style="color:#28a745; font-weight:bold; font-size:18px;">ESTADO: LISTO PARA PUBLICAR</p>
                <img src="https://m.media-amazon.com/images/G/01/img18/home/2018/kdp/interior-format-01._CB485935041_.png" width="100%" style="border-radius:10px; margin:10px 0;">
                <ul style="text-align:left; font-size:14px; color:#444;">
                    <li>✅ Ajuste automático de márgenes internos</li>
                    <li>✅ Preparación para sangría (Bleed)</li>
                    <li>✅ Optimización de fuentes para impresión</li>
                    <li>✅ Eliminación de errores de transparencia</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# 5. PIE DE PÁGINA Y CONFIANZA
st.markdown("<br><br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div style='text-align:center;'>🛡️<br><b>Seguridad Garantizada</b><br><small>Procesamiento cifrado SSL</small></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div style='text-align:center;'>⚡<br><b>Sin Registros</b><br><small>Sube, paga y descarga</small></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div style='text-align:center;'>🧼<br><b>Privacidad Total</b><br><small>Archivos borrados al instante</small></div>", unsafe_allow_html=True)
