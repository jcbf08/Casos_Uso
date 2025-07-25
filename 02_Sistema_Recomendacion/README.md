# 🎬 Sistema de Recomendación con MovieLens

Este proyecto utiliza el dataset **MovieLens (ml-latest-small)** para construir un **sistema de recomendación de películas basado en contenido** (Content-Based Filtering).

---

## **¿Qué hace este proyecto?**
- Descarga automáticamente el dataset **MovieLens**.
- Procesa las películas y sus géneros.
- Utiliza **TF-IDF + similitud coseno** para recomendar películas similares a una seleccionada.

---

## **Requisitos**
- **Python 3.10+**
- Librerías necesarias:
  ```bash
  pip install pandas scikit-learn requests
