import discord
from discord.ext import commands
from core.cog_class import Cog
from countries import allCountries

class general(Cog):

    @commands.command(name="list")  # Pulls up list of countries for each decade
    async def _list(self, ctx, year):
        year = int(year)
        try:
            if year < 1900 or year > 2020:
                raise Exception("Year must be between 1900 and 2020")
            elif year % 10 != 0:
                raise Exception("Year must end in 0")
        except Exception as e:  # Other exceptions include MissingRequiredArgument and CommandNotFound
            await ctx.send(e)
        else:
            await ctx.send("Countries in " + str(year) + ":\n" + allCountries(year))

    @commands.command(name="play")  # Plays music based on command
    async def _play(self, ctx):
        pass

    @commands.command(brief = 'Ping the bot.',description='Ping the bot.') # Ping is always needed, right?
    async def ping(self, ctx):
        await ctx.send(f'Ping is {self.bot.latency} second.')

def setup(bot):
    bot.add_cog(general(bot))