import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# service account key JSON file contents
cred = credentials.Certificate('./userdata/penguintype-343c5-firebase-adminsdk-iz46y-3f36f8289b.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://penguintype-343c5-default-rtdb.europe-west1.firebasedatabase.app/'
})

scoreBoard = db.reference('/scoreboard')

def fetchScoreboard():
    return scoreBoard.get()

def pushScore(username, score):
    scoreBoard.push({
        username: {
            'score': score
        }
    })