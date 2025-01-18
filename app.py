from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para upload e conversão
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Verificar se um arquivo foi enviado
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado."}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Nenhum arquivo selecionado."}), 400

        # Verificar o formato de saída
        output_format = request.form.get('format')
        if not output_format:
            return jsonify({"error": "Formato de saída não especificado."}), 400

        # Normalizar o formato "jpg" para "jpeg"
        output_format = "jpeg" if output_format.lower() == "jpg" else output_format.lower()

        # Abrir o arquivo na memória
        input_stream = BytesIO(file.read())
        with Image.open(input_stream) as img:
            # Converter para RGB se necessário
            if output_format in ["jpeg", "jpg"]:
                img = img.convert("RGB")

            # Salvar o arquivo convertido na memória
            output_stream = BytesIO()
            img.save(output_stream, output_format.upper())
            output_stream.seek(0)

        # Retornar o arquivo convertido para download
        output_filename = f"converted.{output_format}"
        return send_file(output_stream, as_attachment=True, download_name=output_filename)

    except Exception as e:
        return jsonify({"error": f"Erro durante a conversão: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
