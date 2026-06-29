from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No se recibió ningún archivo."}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "El archivo no tiene nombre."}), 400

    filename = file.filename.lower()
    if not (filename.endswith(".xlsx") or filename.endswith(".xls") or filename.endswith(".csv")):
        return jsonify({"error": "Formato no soportado. Usá .xlsx, .xls o .csv"}), 400

    try:
        if filename.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            xl = pd.ExcelFile(file)
            sheets = xl.sheet_names
            result = {}
            total = 0
            for sheet in sheets:
                df_sheet = xl.parse(sheet)
                result[sheet] = len(df_sheet)
                total += len(df_sheet)
            return jsonify({
                "total_rows": total,
                "sheets": result,
                "filename": file.filename,
                "sheet_count": len(sheets),
            })

        rows = len(df)
        return jsonify({
            "total_rows": rows,
            "sheets": {"Hoja principal": rows},
            "filename": file.filename,
            "sheet_count": 1,
        })

    except Exception as e:
        return jsonify({"error": f"Error al procesar el archivo: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
