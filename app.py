from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins="*")

openai.api_key = "OPENAI_API_KEY"  # ← Poné tu clave aquí

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje_usuario = data.get('mensaje', '')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente para ayudar a estudiantes con postulaciones universitarias."},
            {"role": "user", "content": mensaje_usuario}
        ],
        max_tokens=200
    )

    texto_respuesta = response['choices'][0]['message']['content'].strip()
    return jsonify({"respuesta": texto_respuesta})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
