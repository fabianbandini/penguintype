from plistlib import load
from api import getText
import re
from util import loadText, getHighscore, checkIfLangExists, loadLanguages, startTyping
from database import checkUsername, saveLang, loadLang, pushScore, fetchFullScoreboard

currentUser = ""
running = True
pattern = "^[a-zA-Z]{3,8}$"


def main():
    loadApp()


def printLangs():
    for _language in loadLanguages():
        print("-" + _language)


def loadApp():
    running = True
    while running:
        print(loadText("welcome") + "\n\n")

        valid = False
        first = True

        while not valid:
            if not first:
                print("Invalid username.")
                first = False

            currentUser = input(loadText("login"))  # TODO: Implement REGEX

            if re.search(pattern, currentUser):
                valid = True

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
        print(loadText("help") + "\n")

        while running:
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
            elif usercmd == "-global":
                print("Your score is " + getHighscore(currentUser).__str__() + "\n")
                print(fetchFullScoreboard())
            else:
                print(loadText("error") + "\n")


if __name__ == "__main__":
    main()
