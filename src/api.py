from util import loadSettings, loadApiRoute, loadFromApi

currentLang = loadSettings()["user"]["lang"]


def fetchData():
    data = loadFromApi(loadApiRoute(currentLang))
    return data


def generateText():
    data = fetchData()
    text = ""
    for word in data["words"]:
        if word == data["words"][len(data["words"])-1]:
            text += word + "."
        else:
            text += (word + " ")

    return text


def getText():
    text = generateText()
    if text == "":
        return "Error occurred api.py line:23"
    return text
