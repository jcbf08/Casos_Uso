import streamlit as st
from openai import OpenAI
from PIL import Image
import io
import os
import base64

# ========================
# Configuración de la App
# ========================
st.set_page_config(page_title="Detección de Objetos", page_icon="🤖", layout="centered")
st.title("🔍 Detección de Objetos en Imágenes con OpenAI Vision")

# ========================
# Configuración de OpenAI
# ========================
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

if not OPENAI_API_KEY:
    st.error("No se ha configurado la API Key de OpenAI. Añádela en los Secrets de Streamlit o como variable de entorno.")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)

# ========================
# Subida de Imagen
# ========================
uploaded_file = st.file_uploader("📤 Sube una imagen para analizar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)

    if st.button("Analizar Imagen"):
        with st.spinner("Analizando la imagen con OpenAI Vision..."):
            try:
                # Convertir imagen a base64
                img_bytes = io.BytesIO()
                image.save(img_bytes, format="PNG")
                img_bytes.seek(0)

                img_base64 = base64.b64encode(img_bytes.getvalue()).decode("utf-8")
                img_data_url = f"data:image/png;base64,{img_base64}"

                # Llamada a OpenAI Vision (gpt-4o)
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Eres un experto en visión por computadora que detecta y describe objetos en imágenes."},
                        {"role": "user", "content": [
                            {
                                "type": "text",
                                "text": "Detecta todos los objetos visibles en la imagen y descríbelos detalladamente."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": img_data_url
                                }
                            }
                        ]}
                    ]
                )

                result = response.choices[0].message.content
                st.subheader("Resultado de la detección:")
                st.write(result)

            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
