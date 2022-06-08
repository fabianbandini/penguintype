from api import getText
from util import loadText, loadSettings

currentUser = ""


def main():
    loadApp()


def loadApp():
    while True:
        print(loadText("welcome") + "\n\n")
        currentUser = input(loadText("login")) #to chönne mer en reggex dri tue
        #load highscore from db
        print(loadText("highscore")+"20")
        print(loadText("lang") + loadSettings()["user"]["lang"] + "\n")
        #show a list of commands = -help, -lang (to change languga), -start


main()
