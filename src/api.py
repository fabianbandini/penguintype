import os
from util import loadApiRoute, loadFromApi
from database import loadLang
from random import randrange

textLength = 12


def fetchData(username):
    open(os.path.join(os.path.dirname(__file__), 'data', 'texts.txt'), 'w').close()
    data = loadFromApi(loadApiRoute(loadLang(username)))
    return data


def generateText():
    data = fetchData()
    text = ""
    counter = 0

    while counter < textLength:
        word = data["words"][randrange(len(data["words"]) - 1)]
        text += (word + " ")
        counter += 1

    if counter == textLength:
        word = data["words"][randrange(len(data["words"]) - 1)]
        text += (word + ".")

    saveText(text)
    return text


def saveText(text):
    file = open(os.path.join(os.path.dirname(__file__), 'data', 'texts.txt'), "a")
    file.write(text+"\n")
    file.close()


def getText():
    text = generateText()
    if text == "":
        return "Error occurred api.py line:23"
    return text
