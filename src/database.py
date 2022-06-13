import os

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


def fetchScoreboard():
    return scoreBoard.get()


def fetchScoreboard(username):
    return scoreBoard.child("scoreboard").child(username).child("score").get()


def pushScore(username, score):
    scoreBoard.child("scoreboard").child(username).child("score").set(score)


def checkUsername(username):
    x = scoreBoard.child("scoreboard").child(username).child("score").get()
    if x is not None:
        return True
    else:
        return False


def saveLang(username, lang):
    scoreBoard.child("scoreboard").child(username).child("lang").set(lang)


def loadLang(username):
    return scoreBoard.child("scoreboard").child(username).child("lang").get()
