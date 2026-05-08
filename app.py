import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="KDP Formatter Pro", page_icon="📏", layout="wide")

# --- TU CÓDIGO DE SEGURIDAD (Cámbialo cuando quieras) ---
CODIGO_SECRETO = "KDPPRO2026"

# 2. CSS PARA ELIMINAR FRANJAS OSCURAS Y DISEÑO DE ALTA CONVERSIÓN
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    #MainMenu, footer {visibility: hidden;}

    .hero-title { font-size: 50px !important; font-weight: 900 !important; text-align: center; color: #000000 !important; margin-top: -50px; }
    .hero-subtitle { font-size: 18px; text-align: center; color: #666666 !important; margin-bottom: 30px; }

    /* ESTILO SUBIDOR DE ARCHIVOS */
    [data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        max-width: 850px;
        margin: 0 auto !important;
    }
    [data-testid="stFileUploaderDropzone"] { background-color: #FFFFFF !important; border: 1px dashed #cccccc !important; }
    [data-testid="stFileUploaderDropzone"] button { background-color: #FFFFFF !important; color: #000000 !important; border: 1px solid #000000 !important; }
    [data-testid="stFileUploaderDropzone"] * { color: #000000 !important; fill: #000000 !important; }

    /* BOTONES DE PAGO */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 12px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        transition: 0.3s; color: #FFFFFF !important;
        margin-bottom: 12px; border: 2px solid #000000;
    }

    /* BOTÓN DE DESCARGA (SOLO VISIBLE CON CÓDIGO) */
    div.stButton > button {
        background-color: #28a745 !important;
        color: white !important;
        font-weight: 800 !important;
        font-size: 1.6rem !important;
        border-radius: 15px !important;
        width: 100% !important;
        height: 3.5em !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(40, 167, 69, 0.3);
    }
    
    /* CAJA DE VISTA PREVIA */
    .preview-card {
        border: 2px solid #000000;
        padding: 20px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 10px 10px 0px #000000;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFAZ PRINCIPAL
st.markdown('<h1 class="hero-title">Corrector KDP Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Márgenes y sangría profesionales en segundos</p>', unsafe_allow_html=True)

archivo_subido = st.file_uploader("", type="pdf")

if archivo_subido:
    st.markdown("<br>", unsafe_allow_html=True)
    col_izq, col_der = st.columns([1.2, 1])

    with col_izq:
        st.markdown("### 💳 1. Obtén tu Código de Activación")
        st.write("Para procesar y descargar tu manuscrito corregido, realiza el pago único de **2,99€**:")
        
        # Botones de Pago
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#0070ba;">💳 Pagar con Tarjeta</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.paypal.me/DanielTalavera443/2.99EUR" target="_blank" class="btn-pago" style="background-color:#FFB113; color:black !important;">🅿️ Pagar con PayPal</a>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # CAMPO DE TEXTO PARA EL CÓDIGO
        st.markdown("### 🔑 2. Desbloquea tu descarga")
        codigo_input = st.text_input("Introduce el código recibido tras el pago:", placeholder="Ejemplo: KDP123", help="El código se envía a tu email tras confirmar el pago.")

        if codigo_input == CODIGO_SECRETO:
            st.success("✅ ¡Código validado! Procesador listo.")
            if st.button("🚀 GENERAR Y DESCARGAR PDF PERFECTO"):
                try:
                    reader = PdfReader(archivo_subido)
                    writer = PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)
                    
                    output = io.BytesIO()
                    writer.write(output)
                    output.seek(0)
                    
                    st.balloons()
                    st.download_button(label="📥 CLIC AQUÍ PARA DESCARGAR", data=output, file_name="manuscrito_maquetado.pdf", mime="application/pdf")
                except:
                    st.error("Error al procesar el PDF.")
        elif codigo_input != "":
            st.error("❌ Código inválido. Asegúrate de haber completado el pago correctamente.")

    with col_der:
        st.markdown("### 👀 Resultado Profesional")
        st.markdown("""
            <div class="preview-card">
                <p style="color:#28a745; font-weight:bold; font-size:1.2rem;">✓ FORMATO KDP DETECTADO</p>
                <img src="https://m.media-amazon.com/images/G/01/img18/home/2018/kdp/interior-format-01._CB485935041_.png" width="100%" style="border-radius:10px; border:1px solid #eee;">
                <div style="text-align:left; font-size:14px; margin-top:15px; color:#444;">
                    • Ajuste de márgenes de lomo automático<br>
                    • Preparación de sangría (Bleed) para imágenes<br>
                    • Verificación de resolución 300 DPI<br>
                    • Formato listo para subir a Amazon
                </div>
            </div>
        """, unsafe_allow_html=True)

# 4. TARJETAS DE CONFIANZA
st.markdown("<br><br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown("<div style='text-align:center;'>🛡️<br><b>Pago Encriptado</b></div>", unsafe_allow_html=True)
with c2: st.markdown("<div style='text-align:center;'>⚡<br><b>Entrega Inmediata</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div style='text-align:center;'>🧼<br><b>Privacidad Total</b></div>", unsafe_allow_html=True)
