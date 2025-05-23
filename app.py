from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar modelo treinado
modelo = joblib.load("./resultados/modelo_treinado.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Recebe os dados enviados no corpo da requisição
    df = pd.DataFrame([data])  # Converte para DataFrame
    previsao = modelo.predict(df)[0]  # Faz a previsão
    return jsonify({"previsao": int(previsao)})  # Retorna o resultado em JSON

if __name__ == "__main__":
    app.run(debug=True)