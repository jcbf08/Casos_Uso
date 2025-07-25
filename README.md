# 🚀 Casos de Uso de IAGen (IA Generativa)

Este repositorio reúne **proyectos y demos prácticos** basados en **IA Generativa (IAGen)** aplicados a distintos casos de uso.  
El objetivo es proporcionar ejemplos listos para usar y fácilmente desplegables para que puedas explorar el potencial de modelos generativos en **imágenes, texto y datos estructurados**.

---

## **Contenido del Repositorio**

### **1. Detección de Objetos en Imágenes**
- **Descripción:** Aplicación en Streamlit para detectar y describir objetos en imágenes usando OpenAI Vision, con una interfaz simple e interactiva para subir imágenes y obtener resultados en tiempo real.
- **Carpeta:** `./01_Detectar_Imagenes/`
- **Tecnologías:** `OpenAI API`, `Streamlit`, `Pillow`.

### **2. Sistema de Recomendación**
- **Descripción:** Recomendador de películas con Streamlit, basado en contenido usando TF-IDF y similitud coseno (scikit-learn), con opciones para filtrar por género y ajustar la cantidad de recomendaciones.
- **Carpeta:** `./02_Sistema_Recomendacion/`
- **Tecnologías:** `Streamlit`, `Scikit-Learn`, `Pandas`.

### **3. Consulta Inteligente de Base de Datos**
- **Descripción:** App en Streamlit que permite realizar consultas en lenguaje natural sobre una base de datos SQLite (Chinook), convirtiendo automáticamente el texto a SQL mediante OpenAI IAGen y mostrando los resultados en una tabla interactiva.
- **Carpeta:** `./03_Consulta_BBDD_IAGen/`
- **Tecnologías:** `LangChain`, `OpenAI`, `Streamlit`.
