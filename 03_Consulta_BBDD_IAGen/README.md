# 🧠 Caso 3: Consultas en Lenguaje Natural a SQL con IAGen

Este proyecto demuestra cómo usar **IA Generativa (OpenAI)** para convertir **consultas en texto natural** en sentencias SQL y ejecutarlas sobre la base de datos pública **Chinook** (SQLite).

---

## **¿Qué hace esta app?**
- Permite al usuario escribir una **pregunta en lenguaje natural** (ejemplo: *"Muestra los primeros 5 artistas"*).
- Convierte la pregunta en una consulta **SQL válida** usando **OpenAI GPT-4o-mini**.
- Ejecuta la consulta sobre la base de datos **Chinook** y muestra los resultados en una tabla.
- Muestra el **esquema de tablas y columnas** en la barra lateral para guiar al usuario.

---

## **Requisitos**
- **Python 3.9 o superior.**
- Clave de API de OpenAI (variable de entorno `OPENAI_API_KEY`).

Instala las dependencias:
```bash
pip install -r requirements.txt
