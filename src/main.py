from api import getText
from util import loadText, loadSettings, getHighscore

currentUser = ""


def main():
    loadApp()


def loadApp():
    while True:
        print(loadText("welcome") + "\n\n")
        currentUser = input(loadText("login")) #to chönne mer en reggex dri tue
        #load highscore from db
        print(loadText("highscore")+getHighscore(currentUser).__str__())
        print(loadText("lang") + loadSettings()["user"]["lang"] + "\n")
        #show a list of commands = -help, -lang (to change languga), -start
        print(loadText("help")+"\n")

        usercmd = input("Enter cmd: \n")

        if usercmd == "-help":
            print(loadText("helpcmd"))
        else:
            print(loadText("error")+"\n")

            
if __name__ == "__main__":
    main()
