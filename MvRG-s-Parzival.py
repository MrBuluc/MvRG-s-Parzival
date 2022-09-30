from pyexpat.errors import messages
import discord
from discord.ext import commands
import json

secret = json.load(open("secret.json"))
token = secret["dcToken"]

Bot = commands.Bot("!Przvl ", intents=discord.Intents.all())

@Bot.event
async def on_ready():
    print("Merhaba ben Parzival ve hazırım")

@Bot.command()
async def sayHi(msg):
    await msg.send("Merhaba ben Parzival")

Bot.run(token)
