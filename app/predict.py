import numpy as np
import pandas as pd
import sklearn
import csv
from nltk.corpus import stopwords
import string 

def add_a_base_de_treino(noticia, veredito):
    with open("./app/database/base_para_predicao.csv", 'a') as database:
            print("Passou pelo funçao predição")
            writer = csv.writer(database)            
            writer.writerow([noticia, veredito])

def predizer(noticia_a_predizer):
    df = pd.read_csv("./app/database/base_para_predicao.csv")
    df.drop_duplicates(inplace = True)

    with open("./app/database/base_para_predicao.csv", 'w') as file:
        file.write(df.to_csv(index=False))

    def process_text(text):
        
        nopunc = [char for char in text if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('portuguese')]
        return clean_words

    df['Notícia'].head().apply(process_text)

    from sklearn.feature_extraction.text import CountVectorizer
    vect = CountVectorizer(analyzer=process_text)
    messages_bow = vect.fit_transform(df['Notícia'])

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(messages_bow, df['Veredito'], test_size = 0.20, random_state = 0)

    from sklearn.naive_bayes import MultinomialNB
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)

##    #Print the predictions
##    print(classifier.predict(X_train))
##    #Print the actual values
##    print(y_train.values)

    #Evaluate the model on the training data set
    from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
    pred = classifier.predict(X_train)
##    print(classification_report(y_train ,pred ))
##    print('Confusion Matrix: \n',confusion_matrix(y_train,pred))
##    print()
##    print('Accuracy: ', accuracy_score(y_train,pred))

    newData = [noticia_a_predizer]
    newX = vect.transform(newData)
    y_pred = classifier.predict(newX)

##    print(y_pred)

    return y_pred

