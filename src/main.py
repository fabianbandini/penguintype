from plistlib import load
from api import getText
from util import loadText, getHighscore, checkIfLangExists, loadLanguages
from database import checkUsername, saveLang, loadLang, pushScore

currentUser = ""


def main():
    loadApp()


def loadApp():
    while True:
        print(loadText("welcome") + "\n\n")
        currentUser = input(loadText("login"))  # to chönne mer en reggex dri tue
        exists = checkUsername(currentUser)
        if exists:
            print(loadText("highscore") + getHighscore(currentUser).__str__())
            print(loadText("lang") + loadLang(currentUser).__str__())
        else:
            for _language in loadLanguages():
                print("-" + _language)

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
        else:
            print(loadText("error") + "\n")


if __name__ == "__main__":
    main()
