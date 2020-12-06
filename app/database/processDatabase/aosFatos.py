import os
import csv

def writeCsv():
    files = [file for file in os.listdir() if file.endswith(".csv")]

    first = True
    base = []

    for file in files:
        print(file)
        print(len(base))
        with open(file, encoding="iso-8859-1") as csvFile:
            reader = csv.reader(csvFile, delimiter=";")

            verdadeiros = 0
            falsos = 0

            for item in reader:
               if len(item) == 2 and item[0]!="":
                    a, b = item

                    if b == "" and verdadeiros <= 15:
                       base.append([a,"Verdadeiro"])
                       verdadeiros += 1

                    if b == "desinf" and falsos <= 15:
                       print("foi")
                       base.append([a,"Falso"])
                       falsos += 1

                    if falsos == 15 and verdadeiros == 15:
                       break
                    

            base = base[1:]

        if first:
            var = "w"
            first = False
        else:
            var = "a"
            
        with open("base/base_para_predicao.csv", var, encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile)
            for row in base:
                writer.writerow(row)
     
            
    print(len(base))
    print(30*len(files))


def joinCsv():

    to_write = []
    with open("base_original/base_para_predicao.csv", encoding="utf-8") as csvFile:

        reader = csv.reader(csvFile, delimiter=",")
        for item in reader:
            if len(item) == 2 and item[1]=="Verdadeiro" or item[1]=="Falso":
                to_write.append(item)

    with open("base/base_para_predicao.csv", "a", encoding="utf-8") as csvFile:
        writer = csv.writer(csvFile)
        for row in to_write:
            writer.writerow(row)
