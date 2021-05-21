# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:33:07 2021

@author: helen
"""

import discord
from discord.ext import commands
from countries import allCountries
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

@bot.command(name = "list") #Pulls up list of countries for each decade
async def _list(ctx, year: int): 
    try:
        if year < 1900 or year > 2020:
            raise Exception("Year must be between 1900 and 2020")
        elif year % 10 != 0:
            raise Exception("Year must end in 0")
    except Exception as e: #Other exceptions include MissingRequiredArgument and CommandNotFound
        await ctx.send(e)
    else:
        await ctx.send("Countries in " + str(year) + ":\n" + allCountries(year))
    
        
@bot.command(name = "play") #Plays music based on command
async def _play(ctx):
    pass

bot.run('ODQ0Nzc1NTk3NDk4ODI2ODMy.YKXUlQ.gehTTphc0f9hHC-lAT1F9juc-6A') 
