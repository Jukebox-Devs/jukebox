# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:33:07 2021

@author: helen
"""

import discord, os
from discord.ext import commands
import nest_asyncio

nest_asyncio.apply()

bot = commands.Bot(command_prefix = "+")

#Make a help page

@bot.event
async def on_ready():
    print("Bot is ready") #Message prints out to the console when using an IDE
    
@bot.event
async def on_command_error(ctx, error):
    pass

@bot.command(brief = 'Load Cog',description='Load Cog module.') # Load the Cog module
async def load(ctx,ext):
    bot.load_extension(f'cmds.{ext}')
    await ctx.send(f"Loaded Cog {ext}.")

@bot.command(brief = 'Unload Cog',description='Unload Cog module.') # Seperate the Cog module
async def unload(ctx,ext):
    bot.unload_extension(f'cmds.{ext}')
    await ctx.send(f"Unloaded Cog {ext}.")

@bot.command(brief = 'Reload Cog',description='Reload Cog module.')  # Load the Cog module again
async def reload(ctx,ext):
    bot.reload_extension(f'cmds.{ext}')
    await ctx.send(f"Reloaded Cog {ext}.")

# @bot.command(name = "list") #Pulls up list of countries for each decade
# async def _list(ctx, year: int):
#     try:
#         if year < 1900 or year > 2020:
#             raise Exception("Year must be between 1900 and 2020")
#         elif year % 10 != 0:
#             raise Exception("Year must end in 0")
#     except Exception as e: #Other exceptions include MissingRequiredArgument and CommandNotFound
#         await ctx.send(e)
#     else:
#         await ctx.send("Countries in " + str(year) + ":\n" + allCountries(year))
    
        
# @bot.command(name = "play") #Plays music based on command
# async def _play(ctx):
#     pass


# Conveniently load all the cog from filepath instead of adding them one by one
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')


bot.run('token') 
