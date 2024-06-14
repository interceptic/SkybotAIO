import discord
import asyncio
from discord.ext import commands
from bot.modals.evalue import Embed
from bot.modals.admin import give_admin, remove_admin
import json


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


@bot.slash_command(name='admin', description='Give or remove admin from yourself...')
async def admin(ctx, remove: bool = False):
    with open("config.json") as conf:
        config = json.load(conf)
    if ctx.author.id != config['bot']['owner_discord_id']:
        ctx.send("Sorry, you're not allowed to use this command")
        return
    if remove: 
        await remove_admin(ctx, config['bot']['owner_discord_id'], config['bot']['admin_role_id'])
        return 
    await give_admin(ctx, config['bot']['owner_discord_id'], config['bot']['admin_role_id'])
    return