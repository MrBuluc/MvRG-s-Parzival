from pyexpat.errors import messages
from unittest import result
import discord
from discord.ext import commands
import json
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore

Bot = commands.Bot("!Przvl ", intents=discord.Intents.all())

@Bot.event
async def on_ready():
    print("Merhaba ben Parzival ve hazırım")

@Bot.command()
async def labAcikMi(msg):
    await msg.send(labOpenStr(getLatestLabOpen()))

def botRun():
    secret = json.load(open("secrets\secret.json"))
    token = secret["dcToken"]
    Bot.run(token)

def initializeFirebase():
    return firebase_admin.initialize_app()
    
def getLatestLabOpen():
    docs = firestore.Client().collection(u"LabOpen").order_by(u"time", direction=firestore.Query.DESCENDING).limit(1).stream()
    for doc in docs:
        return doc.to_dict()
    
def convertTimeToStr(time):
    return f"{time.day}.{time.month}.{time.year} {time.hour}:{time.minute}"

def labOpenStr(labOpen):
    name = labOpen["userName"]
    timeStr = convertTimeToStr(labOpen["time"])
    acikMi = labOpen["acikMi"]
    if acikMi:
        emo = "✅"
        acik = "açıldı"
    else:
        emo = "❌"
        acik = "kapandı"
    return f"Lab {name} tarafından {timeStr} de {acik} {emo}"
    
if __name__ == "__main__":
    initializeFirebase()
    botRun()
    