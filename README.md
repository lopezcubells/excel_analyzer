# ExcelStats — Analizador de filas

App web para analizar archivos Excel y CSV, mostrando la cantidad de filas por hoja.

## Stack

- **Backend**: Python + Flask + Pandas
- **Frontend**: HTML/CSS/JS estático (servido por Flask)
- **Deploy**: Railway (Gunicorn)

## Estructura

```
excel-analyzer/
├── app.py              # Servidor Flask
├── requirements.txt    # Dependencias Python
├── Procfile            # Comando de inicio para Railway
└── static/
    └── index.html      # Frontend
```

## Deploy en Railway

### Opción 1: Desde GitHub (recomendado)

1. Subí esta carpeta a un repositorio de GitHub.
2. Entrá a [railway.app](https://railway.app) y creá un nuevo proyecto.
3. Elegí **"Deploy from GitHub repo"** y seleccioná tu repo.
4. Railway detecta automáticamente el `Procfile` y despliega.
5. En **Settings → Networking**, generá un dominio público.

### Opción 2: Railway CLI

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

## Correr localmente

```bash
pip install -r requirements.txt
python app.py
# Abrí http://localhost:5000
```

## Funcionalidades

- Soporta `.xlsx`, `.xls` y `.csv`
- Muestra filas por hoja (multi-hoja)
- Drag & drop o selección de archivo
- Los archivos no se guardan en el servidor
