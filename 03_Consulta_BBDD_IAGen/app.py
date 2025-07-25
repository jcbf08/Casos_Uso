import streamlit as st
import sqlite3
import pandas as pd
import os
from openai import OpenAI

# =========================
# Configuración de la App
# =========================
st.set_page_config(page_title="Consulta Natural a SQL", page_icon="🧠", layout="wide")
st.title("🧠 **Consultas en Lenguaje Natural a SQL con IAGen (OpenAI)**")
st.markdown("Escribe una pregunta en texto y el sistema la convertirá en una consulta SQL para ejecutarla sobre la base de datos **Chinook**.")

# =========================
# Configuración de OpenAI
# =========================
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
if not OPENAI_API_KEY:
    st.error("No se encontró la API Key de OpenAI. Configúrala en los Secrets de Streamlit.")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)

# =========================
# Descargar y preparar la BD Chinook
# =========================
DB_URL = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/Data/Chinook_Sqlite.sqlite"
DB_FILE = "Chinook_Sqlite.sqlite"
# Documentación: https://docs.yugabyte.com/preview/sample-data/chinook/

if not os.path.exists(DB_FILE):
    import requests
    st.info("Descargando base de datos Chinook...")
    r = requests.get(DB_URL)
    with open(DB_FILE, "wb") as f:
        f.write(r.content)

# =========================
# Función para ejecutar SQL
# =========================
def run_sql_query(query: str):
    try:
        with sqlite3.connect(DB_FILE) as conn:
            return pd.read_sql_query(query, conn)
    except Exception as e:
        return str(e)

# =========================
# Generar SQL con OpenAI
# =========================
def generate_sql_from_text(user_text: str, schema_info: str):
    prompt = f"""
    Eres un experto en SQL. Convierte la siguiente consulta en lenguaje natural a una consulta SQL válida para una base de datos SQLite con el siguiente esquema:

    {schema_info}

    Pregunta: {user_text}

    Genera únicamente la consulta SQL.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# =========================
# Obtener esquema de tablas
# =========================
def get_schema_info():
    with sqlite3.connect(DB_FILE) as conn:
        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
        schema = []
        for table_name in tables['name']:
            columns = pd.read_sql_query(f"PRAGMA table_info({table_name});", conn)
            cols = ", ".join(columns['name'])
            schema.append(f"- {table_name} ({cols})")
        return "\n".join(schema)

schema_info = get_schema_info()
st.sidebar.subheader("📚 Tablas y Columnas Disponibles")
st.sidebar.text(schema_info)

# =========================
# Interfaz Principal
# =========================
user_question = st.text_area("Escribe tu pregunta en lenguaje natural:", "Muestra los primeros 5 artistas")

if st.button("🔍 Consultar"):
    with st.spinner("Generando consulta SQL con IAGen..."):
        sql_query = generate_sql_from_text(user_question, schema_info)
        st.code(sql_query, language="sql")

        result = run_sql_query(sql_query)
        if isinstance(result, str):
            st.error(f"Error al ejecutar la consulta: {result}")
        else:
            st.success("Consulta ejecutada correctamente.")
            st.dataframe(result)
