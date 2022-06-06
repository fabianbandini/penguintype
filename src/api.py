from util import loadSettings, loadApiRoute, loadFromApi

text = ""
currentLang = loadSettings()["user"]["lang"]


def fetchData():
    data = loadFromApi(loadApiRoute(currentLang))

    return data


def generateText():
    return "Hello World"


def getText():
    if text == "":
        return
    return text


print(fetchData())
