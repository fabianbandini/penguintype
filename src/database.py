import os
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# service account key JSON file contents
cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), '..', 'userdata',
                                            'penguintype-343c5-firebase-adminsdk-iz46y-3f36f8289b.json'))
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://penguintype-343c5-default-rtdb.europe-west1.firebasedatabase.app/'
})

scoreBoard = db.reference('/')


# fetches full scoreboard from firebase and prints the 5 best users
def fetchFullScoreboard():
    _scoreboard = scoreBoard.get()
    usernames = []
    users = {}

    for user in _scoreboard["scoreboard"]:
        usernames.append(user)

    for user in usernames:
        score = scoreBoard.child("scoreboard").child(user).child("score").get()
        users[user] = score

    sortedScores = sorted(users.values(), reverse=True)
    sortedUsers = {}

    for i in sortedScores:

        for y in users.keys():
            if users[y] == i:
                sortedUsers[y] = users[y]
                break
    index = 0

    for user in sortedUsers:
        if index < 10:
            print((index + 1).__str__() + ". " + user + " : " + sortedUsers[user].__str__())
            index += 1

    print("\n")


# fetches score from a defined user from firebase
def fetchScoreboard(username):
    return scoreBoard.child("scoreboard").child(username).child("score").get()


# pushes score from a user to firebase
def pushScore(username, score):
    scoreBoard.child("scoreboard").child(username).child("score").set(score)


# checks if a user already exists
def checkUsername(username):
    x = scoreBoard.child("scoreboard").child(username).child("score").get()
    if x is not None:
        return True
    else:
        return False


# saves a chosen language from a user to firebase
def saveLang(username, lang):
    scoreBoard.child("scoreboard").child(username).child("lang").set(lang)


# loads the saved language from firebase
def loadLang(username):
    return scoreBoard.child("scoreboard").child(username).child("lang").get()
