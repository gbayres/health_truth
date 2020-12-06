import json
from urllib.request import urlopen
import csv

def pegarVereditos(query, #A palavra chave a ser pesquisada
                  lang="pt-BR", #Idioma
                  age="1080", #Idade da informação
                  size="15", #Número de notícias por request
                  pageToken="", #Número da página
                  offset="", #resultados a partir de qual índice
                  key="", #google key
                  publisher=""): #portal que publicou a noticia

        params = {
            "query": query,
            "languageCode": lang,
            "maxAgeDays": age,
            "pageSize": size,
            "pageToken": pageToken,
            "reviewPublisherSiteFilter": publisher,
            "offset": "",
            "key": "",
            }


        link = "https://factchecktools.googleapis.com/v1alpha1/claims:search?"

        params_list = []

        for key, value in params.items():

            if value:
                params_list.append(f'{key}={value}')

        FINAL_LINK = link + '&'.join(params_list)

        print(f"Link acessado: {FINAL_LINK}")

        content = urlopen(FINAL_LINK).read()
        content_json = json.loads(content)

        vereditos = {}

        try:
                x = content_json["claims"]
        except:
                print(content_json)
                
        

        for noticia in content_json["claims"]:

            texto = noticia["text"]
            veredito = noticia["claimReview"][0]["textualRating"]

            vereditos[texto] = veredito
    
        return(vereditos)

def freqVereditos(vereditos):

    freq = {}
    for value in vereditos.values():
        if value not in freq.keys():
            freq[value] = 1
        else:
            freq[value] += 1

    return freq
            
def tratarVereditos(vereditos):

    new_dict = {}
    
    falso = ["mentira", "falso", "errado", "fake", "mentiroso"]
    enganoso = ["enganador", "impreciso", "enganoso", "exagerado", "descontextualizado"]
    verdadeiro = ["verdadeiro", "verdade", "correto", "certo"]

    for i in falso:
        for key, value in vereditos.items():
            if value.lower().startswith(i):
                new_dict[key] = "Falso"

    for i in enganoso:
        for key, value in vereditos.items():
            if value.lower().startswith(i):
                new_dict[key] = "Enganoso"

    for i in verdadeiro:
        for key, value in vereditos.items():
            if value.lower().startswith(i):
                new_dict[key] = "Verdadeiro"

    return new_dict

def escreverVereditos(vereditos):
    
      with open("base_para_predicao.csv", 'a') as respostas:

          writer = csv.writer(respostas)

          for key, value in vereditos.items():
              writer.writerow([key, value])


def run(query, age="1080", size="40"):
       
        vereditos = pegarVereditos(query, size=size)
        vereditos = tratarVereditos(vereditos)
        escreverVereditos(vereditos)
        return len(vereditos.keys())


def lerVereditos():

      with open("base_para_predicao.csv") as respostas:

          reader = csv.reader(respostas)

          for row in reader:
                  print(row)

keywords = [
            "obesidade",
            "aids",
            "cancer",
            "probioticos",
            "dieta mediterranea",
            "alzheimer",
            "fumar",
            "vitamina",
            "fibromialgia",
            "demencia",
            "prostata",
            "mama",
            "ovario",
            "transplante fecal",
            "aspirina",
            "aterosclerose",
            "menopausa",
            "impotencia",
            "bipolaridade",
            "vacina",
            "leite",
            "bacteria",
            "zika",
            "ebola",
            "testosterona",
            "hormonio",
            "melanoma",
            "infarto",
            "cardiaco",
            "diabetes",
            "pressao alta",
            "hipertensao",
            "colesterol",
            "parkinson",
            "remedio natural",
            "artrite",
            "artrose",
            "anticoagulante",
            "hiv",
            "cefaleia",
            "menstruar",
            "pilula",
            "veneno",
            "cura",
            "dieta",
            "depressao",
            "ansiedade",
            "omega 3",
            "morte",
            "exercicio",
            "carcinoma",
            "hpv",
            "analgesico",
            "dipirona",
            "ibuprofeno",
            "cha",
            "cha preto",
            "epilepsia",
            "desnutricao",
            "osteoporose",
            "gravidez",
            "esclerose multipla",
            "tumor",
            "esporao",
            "jejum",
            "insonia",
            "prebioticos",
            "vegetariano",
            "virus",
            "alergia",
            "anti inflamatorio",
            "constipacao",
            "diarreia",
            "caroco",
            "coceira",
            "cirrose",
            "zinco",
            "suplemento",
            "progesterona",
            "vaginose",
            "penis",
            "vagina",
            "libido",
            "sexo",
            "anal",
            "oral",
            "infeccao",
            "transmissivel",
            "virose",
            "gripe",
            "febre",
            "vomito",
            "coriza",
            "retardo mental",
            "intubar",
            "parasita",
            "esquistossomose",
            "olho",
            "rim",
            "figado",
            "ouvido",
            "nariz",
            "perna",
            "braco",
            "peito",
            "silicone",
            "nadegas",
            "musculo",
            "nervo",
            "olfato",
            "paladar",
            "audicao",
            "cerebro",
            "reumatismo",
            "trauma",
            "sangue",
            "dor",
            "farmacia",
            "erva",
            "maconha",
            "medicinal",
            "medicina",
            "ovo",
            "urticaria",
            "verruga",
            "sarampo"
            ]
            
for i in range(79, len(keywords)):

        kw = keywords[i]
        print(f"Pesquisar {kw}")

        if i%10 == 0:
                input("Aperte ENTER para proceder")

        try:
                n = run(kw)

                print(f"{n} linhas escritas!")
                print(f"{i} - Feito!\n")
        except:
                print("Um erro ocorreu...")
                
            
            
            
            
            
            
            
