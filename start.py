import discord
import json
from bot.bot import bot
from discord import Guild

with open('config.json') as config:
    configuration = json.load(config)

bot.run(configuration['bot']['token'])