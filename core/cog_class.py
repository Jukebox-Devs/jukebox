'''
This file is to implement the cog feature in such a way
that it can be easily coded into different commands.

When calling the bot instead of calling commands.bot or bot in the main file,
you can now just call self.bot in other cog files.
'''

import discord
from discord.ext import commands

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot