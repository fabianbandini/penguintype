from plistlib import load
from api import getText
from util import loadText, getHighscore, checkIfLangExists, loadLanguages, startTyping
from database import checkUsername, saveLang, loadLang, pushScore

currentUser = ""
running = True


def main():
    loadApp()


def printLangs():
    for _language in loadLanguages():
        print("-" + _language)


def loadApp():
    while running:
        print(loadText("welcome") + "\n\n")
        currentUser = input(loadText("login"))  # to chönne mer en reggex dri tue
        exists = checkUsername(currentUser)
        if exists:
            print(loadText("highscore") + getHighscore(currentUser).__str__())
            print(loadText("lang") + loadLang(currentUser).__str__())
        else:
            printLangs()

            print("\nPlease enter your desired language to type in.\n")

            langExists = False
            while not langExists:
                selectedLang = input("Language: ")
                if checkIfLangExists(selectedLang):
                    print("You choose " + selectedLang + "\n")
                    saveLang(currentUser, selectedLang)
                    pushScore(currentUser, 0)
                    langExists = True

                if not langExists:
                    print("Please enter a valid language \n")

        # show a list of commands = -help, -lang (to change languga), -start
        print(loadText("help") + "\n")

        usercmd = input("Enter cmd: \n")

        if usercmd == "-help":
            print(loadText("helpcmd"))
        elif usercmd == "-start":
            startTyping(currentUser)
        elif usercmd == "-lang":
            print("Choose your language:")
            printLangs()

            langInput = input("Choose:")

            if checkIfLangExists(langInput):
                saveLang(currentUser, langInput)
        elif usercmd == "-exit":
            running = False

        else:
            print(loadText("error") + "\n")


if __name__ == "__main__":
    main()
