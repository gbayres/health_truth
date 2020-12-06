from app import predict
from app import app
from flask import render_template
from flask import request, redirect
import csv
import os
import pandas as pd


@app.route("/", methods=["GET", "POST"])
def index():

    predicao=[""]
    if request.method == "POST":
        
        req = request.form
        missing = list()

        csvRow = []
        for k, v in req.items():
            csvRow.append(v)
            if v == "":
                missing.append(k)
                
        if missing:
            feedback = f"Falta preencher {', '.join(missing)}"
            return render_template("public/index.html", feedback=feedback)

        if req["identifier"] == "request_pergunta":
            with open("./app/database/dados.csv", 'a') as database:
                print("Passou pelo request_pergunta")
                
                try:
                    predicao = predict.predizer(csvRow[5])
                    print("Deu certo")
                except Exception as e:
                    print(e)
                    predicao = ["Indisponível"]
                    print("Deu indisponível")
                    
                csvRow.append(predicao[0])
                writer = csv.writer(database)
                writer.writerow(csvRow)
                print(predicao)


        elif req["identifier"] == "request_resposta":
            with open("./app/database/respostas.csv", 'a') as respostas:
                print("Passou pelo request_resposta")
                writer = csv.writer(respostas)
                writer.writerow(csvRow)

                veredito = csvRow[8]

                
            df = pd.read_csv("./app/database/dados.csv")

            noticia = df.iloc()[int(csvRow[1]) - 1]["Notícia"]
            
            df.iloc[int(csvRow[1]) - 1, df.columns.get_loc('Resposta')] = \
                                "|-|".join(map(lambda x: x.replace("|",""), csvRow))
            
            predict.add_a_base_de_treino(noticia, veredito)

            with open("./app/database/dados.csv", 'w') as file:
                file.write(df.to_csv(index=False))
            
##        print("request: ", request.url)
        return redirect(request.url)
        

    with open ("./app/database/dados.csv") as database:
        reader = csv.reader(database)
        csvRow = [item for item in reader if item != ""]

##    print(csvRow)
    return render_template("public/index.html", csvRow=csvRow, predicao=predicao[0])


