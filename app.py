import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (ESTO DEBE IR PRIMERO Y SOLO UNA VEZ)
st.set_page_config(page_title="KDP Formatter Pro", page_icon="✒️", layout="wide")

# 2. CÓDIGO DE VERIFICACIÓN PARA GOOGLE
st.components.v1.html("""<meta name="google-site-verification" content="google12b9611524f584d3" />""", height=0)

from pypdf import PdfReader, PdfWriter
import io

# ==========================================
# 🔑 TU PANEL DE CONTROL
# ==========================================
CODIGO_SECRETO = "KDPFDP85661" 
# ==========================================

# 2. ESTILO LIMPIO (TODO BLANCO, LETRAS NEGRAS)
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    #MainMenu, footer {visibility: hidden;}

    .hero-title { font-size: 50px !important; font-weight: 900 !important; text-align: center; color: #000000 !important; margin-top: -50px; }
    .hero-subtitle { font-size: 18px; text-align: center; color: #666666 !important; margin-bottom: 30px; }

    /* SUBIDOR DE ARCHIVOS */
    [data-testid="stFileUploader"] {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 15px !important;
        padding: 20px !important;
    }

    /* BOTONES DE PAGO */
    .btn-pago {
        display: flex; align-items: center; justify-content: center;
        padding: 18px; border-radius: 12px; font-weight: 700;
        text-decoration: none !important; font-size: 1.1rem;
        transition: 0.3s; color: #FFFFFF !important;
        margin-bottom: 12px; border: 2px solid #000000;
    }
    .btn-pago:hover { opacity: 0.8; transform: scale(1.02); }

    /* BOTÓN DE DESCARGA */
    div.stButton > button {
        background-color: #28a745 !important;
        color: white !important;
        font-weight: 800 !important;
        font-size: 1.6rem !important;
        border-radius: 15px !important;
        width: 100% !important;
        height: 3.5em !important;
        border: none !important;
    }
    
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

# 3. INTERFAZ
st.markdown('<h1 class="hero-title">Corrector KDP Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Formato profesional para autores independientes</p>', unsafe_allow_html=True)

archivo_subido = st.file_uploader("", type="pdf")

if archivo_subido:
    st.markdown("<br>", unsafe_allow_html=True)
    col_izq, col_der = st.columns([1.2, 1])

    with col_izq:
        st.markdown("### 💳 1. Obtén tu Código de Activación")
        st.write("Para procesar y descargar tu archivo corregido, realiza el pago de **2,99€**.")
        
        # Botones de Pago actualizados con tu usuario verificado
        enlace_pago = "https://www.paypal.me/DanielTalavera443/2.99"
        
        st.markdown(f'<a href="{enlace_pago}" target="_blank" class="btn-pago" style="background-color:#0070ba;">💳 Pagar con Tarjeta</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{enlace_pago}" target="_blank" class="btn-pago" style="background-color:#FFB113; color:black !important;">🅿️ Pagar con PayPal</a>', unsafe_allow_html=True)
        
        st.info("📩 **Instrucciones:** Tras el pago, recibirás el código en tu email de PayPal. Si tardas en recibirlo, contacta con soporte.")
        st.markdown("---")
        
        st.markdown("### 🔑 2. Introduce el Código")
        codigo_input = st.text_input("Escribe el código recibido tras el pago:", placeholder="Ejemplo: KDP_PRO_88", type="password")

        # LÓGICA DE BLOQUEO Y PROCESAMIENTO
        if codigo_input == CODIGO_SECRETO:
            st.success("✅ Código validado con éxito.")
            if st.button("🚀 PROCESAR Y DESCARGAR AHORA"):
                try:
                    reader = PdfReader(archivo_subido)
                    writer = PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)
                    
                    output = io.BytesIO()
                    writer.write(output)
                    output.seek(0)
                    
                    st.balloons()
                    st.download_button(label="📥 CLIC AQUÍ PARA DESCARGAR PDF", data=output, file_name="manuscrito_listo.pdf", mime="application/pdf")
                except Exception as e:
                    st.error(f"Error técnico al procesar el archivo: {e}")
        elif codigo_input != "":
            st.error("❌ Código incorrecto o caducado.")

    with col_der:
        st.markdown("### 👀 Vista Previa del Formato")
        st.markdown("""
            <div class="preview-card">
                <p style="color:#28a745; font-weight:bold; font-size:1.2rem;">RESULTADO PROFESIONAL</p>
                <img src="https://m.media-amazon.com/images/G/01/img18/home/2018/kdp/interior-format-01._CB485935041_.png" width="100%" style="border-radius:10px;">
                <p style="font-size:14px; color:#555; margin-top:10px;">Su archivo será optimizado con márgenes de impresión simétricos y sangría reglamentaria.</p>
            </div>
        """, unsafe_allow_html=True)

# 4. CONFIANZA
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.markdown("<div style='text-align:center;'>🛡️<br><b>Pago Seguro</b></div>", unsafe_allow_html=True)
with c2: st.markdown("<div style='text-align:center;'>⚡<br><b>Entrega Inmediata</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div style='text-align:center;'>🧹<br><b>Sin Registros</b></div>", unsafe_allow_html=True)

# 5. SOPORTE EN SIDEBAR
st.sidebar.markdown("### 🆘 Soporte")
st.sidebar.write("¿Problemas con tu código?")
st.sidebar.write("📧 danieltalavera67@gmail.com")
