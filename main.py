import discord
from discord.ext import commands
import sys, os

token = open("token.txt").read()
intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('d?'), 
    intents=intents, 
    case_insensitive=True
)

cogs = ['jishaku']

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        cogs.append(f"cogs.{file[:-3]}")

for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception as error:
        print(error)

bot.run(token)
