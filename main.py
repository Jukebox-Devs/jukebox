# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:33:07 2021

@author: helen
"""

import discord
from discord.ext import commands
from countries import allCountries

bot = commands.Bot(command_prefix = "+")

#Make a help page

@bot.command(name = "list") #Pulls up list of countries for each decade
async def _list(ctx, year: int): 
    if year < 1900 or year > 2020:
        raise Exception("Year must be between 1900 and 2020")
    elif year % 10 != 0:
        raise Exception("Year must end in 0")
    ctx.send("Countries in " + year + ":\n" + allCountries(year))
        

@bot.command(name = "play") #Plays music based on command
async def _play(ctx):
    pass
