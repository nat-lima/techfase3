import requests
import csv
import zipfile
import pandas as pd
import numpy as np
import time
from app.utils.links import url_dadosabertos_prf_2025,url_dadosabertos_prf_2024, url_dadosabertos_prf_2023
import firebase_admin # type: ignore
from firebase_admin import credentials # type: ignore
from firebase_admin import firestore # type: ignore
from flask import jsonify


def get_content_dadosabertosprf():
    try:
        # Use a service account
        #return jsonify({"1" : "chegou aqui"})
        #cred = credentials.Certificate('app/key/techfase3-firebase-adminsdk-fbsvc-e71cc04b8f.json')
        #firebase_admin.initialize_app(cred)

        #db = firestore.client()

        """
        response = requests.get(url_dadosabertos_prf_2025)
        with open("../../csv/datatran2025.zip", "wb") as file:
            file.write(response.content)
            print("Download concluído!")

        # Caminho do arquivo ZIP e da pasta de destino
        zip_path = "../../csv/datatran2025.zip"
        extract_path = "../../csv"

        # Abrir e extrair o ZIP
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
        """
        my_dict = {}

        count = 0
        #doc_ref = db.collection("datatran").document("2025x8PFM1DJoOUIdW8D")
        with open('app/csv/datatran2025.csv', newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';')
            #linha = next(reader)
            #doc_ref.set(linha)
            #print(linha)
            for row in reader:
                count = count + 1
            
            
        count2 = 0
        with open('app/csv/datatran2024.csv', newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';')
            #linha = next(reader)
            #doc_ref.set(linha)
            for row in reader:
                count2 = count2 + 1
         
 
        dict1 = {'File': 'datatran2025.csv', 'Lines Inserted': count}
        dict2 = {'File': 'datatran2024.csv', 'Lines Inserted': count2}    
            
        return jsonify(dict1, dict2)    
        """    
            for row in reader:
                my_dict = row
                print(list(my_dict.values())[0])
                doc_ref.set(my_dict)
        """                               
    except Exception as e:
        return (jsonify(str(e))), 500
