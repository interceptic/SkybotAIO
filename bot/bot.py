import discord
import asyncio
from discord.ext import commands
from bot.modals.evalue import Embed
from bot.modals.admin import give_admin, remove_admin
import json
import datetime
from bot.modals.list import Setup
from bot.modals.calculator import calculate
from bot.build_embed import build
from minecraft.info.tmbk import representTBMK

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
    embed = discord.Embed(
        title="Fetching...",
        description=f"Obtaining data from api, please wait...",
        color=0xFF007B
    )
    embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
    embed.timestamp = datetime.datetime.now()
    await ctx.respond(embed=embed)
    try:
        class_thing = Embed()
        await class_thing.send_embed(ctx, name)
    except TypeError as error:
        embed = discord.Embed(
        title="Exception Triggered",
        description=f"Error: {error}",
        color=0xFF0000
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)



@bot.slash_command(name='admin', description='Give or remove admin from yourself...')
async def admin(ctx, remove: bool = False):
    with open("config.json") as conf:
        config = json.load(conf)
    if ctx.author.id != config['bot']['owner_discord_id']:
        await ctx.respond("Sorry, you're not allowed to use this command", ephemeral=True)
        return
    if remove: 
        await remove_admin(ctx, config['bot']['owner_discord_id'], config['bot']['admin_role_id'])
        return 
    await give_admin(ctx, config['bot']['owner_discord_id'], config['bot']['admin_role_id'])
    return


@bot.slash_command(name='list', description="List an account")
async def list(ctx, username: str, price: int, profile: bool):
    setup = Setup
    await setup.check(ctx)
    
@bot.slash_command(name='buy', description="Calculate the price for coins")
async def buy(ctx, amount: int):
    value = calculate(amount, False)
    amount = representTBMK(amount * 1000000)    
    embed = await build(f"Price for {amount}", f"You can buy {amount} for ${round(value, 2)} USD", 0x00FFDC)
    await ctx.respond(embed=embed)

@bot.slash_command(name='sell', description="Calculate the price for coins")
async def sell(ctx, amount: int):
    value = calculate(amount, True)
    if value == False:
        embed = await build("Invalid Sell Amount", "Minimum amount to sell is 500 million.", 0xFF0000)
        await ctx.respond(embed=embed)
        return
    amount = representTBMK(amount * 1000000)    
    embed = await build(f"Price for {amount}", f"You can sell {amount} for ${round(value, 2)} USD", 0x00FFDC)
    await ctx.respond(embed=embed)
