from util import loadSettings, loadApiRoute, loadFromApi
from random import randrange

currentLang = loadSettings()["user"]["lang"]
textLength = loadSettings()["user"]["length"]


def fetchData():
    data = loadFromApi(loadApiRoute(currentLang))
    return data


def generateText():
    data = fetchData()
    text = ""
    counter = 0

    while counter < textLength:
        word = data["words"][randrange(len(data["words"])-1)]
        text += (word + " ")
        counter += 1

    if counter == textLength:
        word = data["words"][randrange(len(data["words"]) - 1)]
        text += (word + ".")

    return text


def getText():
    text = generateText()
    if text == "":
        return "Error occurred api.py line:23"
    return text
