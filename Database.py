import csv
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

class Database:
    def __init__(self):
        self.data=self.getRecords()
        self.unique_words=self.getUniqueWords(self.data)

    def getRecords(self):
        data = []
        with open("movie-pang02.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        data.pop(0)
        return data

    def getUniqueWords(self, sentences):
        en_stops = set(stopwords.words('english'))
        unique={}
        for i in range(len(sentences)):
            words = sentences[i][1].split()
            for word in words:
                if word in en_stops or word in string.punctuation:
                    continue
                if word not in unique:
                    unique[word] = {"Pos": 0, "Neg": 0}
                if word in unique.keys() and sentences[i][0]=="Pos":
                    unique[word]["Pos"] += 1
                if word in unique.keys() and sentences[i][0]=="Neg":
                    unique[word]["Neg"] += 1
        return unique

    def isPresent(self, msg):
        print(msg)
        for i in self.unique_words.keys():
            if i in msg:
                print(i, self.unique_words[i])