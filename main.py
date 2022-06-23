import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

for i in range(len(cogs)):
	cogs[i].setup(client)

client.run("OTE3MzI1MjY0ODAxOTAyNjIz.Ya3Dug.QcU6QpcnaTaLM8piF13Yl1lZKYM")
