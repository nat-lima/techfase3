import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "mes": 6,
    "br": 250,
    "uf_RJ": 1, "uf_MG": 0, "uf_BA": 0, "uf_PR": 0,
    "condicao_metereologica_Nublado": 1, "condicao_metereologica_Nevoeiro": 0, 
    "condicao_metereologica_Sol forte": 0, "condicao_metereologica_Céu Claro": 0,
    "fase_dia_Tarde": 1, "fase_dia_Anoitecer": 0, "fase_dia_Madrugada": 0, "fase_dia_Plena Noite": 0
}

response = requests.post(url, json=data)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
