import discord
import asyncio
from discord.ext import commands
from bot.modals.evalue import Embed

intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(intents=intents, slash_command_prefix='/')  

@bot.event
async def on_ready():
    print('\x1b[32mLogged in!\x1b[0m')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Made by Interceptic"))
    await bot.sync_commands()
    

@bot.slash_command(name='value', description='Skyblock Account Value')
async def value(ctx, name: str): 
    await ctx.respond('Fetching API Data... please wait.')
    embed = Embed()
    await embed.send_embed(ctx, name)