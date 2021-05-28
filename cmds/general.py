import discord
from discord.ext import commands
from core.cog_class import Cog
from countries import allCountries

class general(Cog):

    @client.command(name = "list") #Pulls up list of countries for each decade
    async def _list(ctx, year: int): 
        try:
            if year < 1900 or year > 2020:
                raise Exception("Year must be between 1900 and 2020")
            elif year % 10 != 0:
                raise Exception("Year must end in 0")
        except Exception as e: #Other exceptions include MissingRequiredArgument and BadArgument
            await ctx.send(e)
        else:
            clist = allCountries(year)

            page1 = discord.Embed(
                title = str(year) + "s Countries (1/" + str(len(clist)) + ")",
                description = clist[0],
                color = discord.Color.blue()
            )
            page2 = discord.Embed(
                title = str(year) + "s Countries (2/" + str(len(clist)) + ")",
                description = clist[1],
                color = discord.Color.blue()
            )
            page3 = discord.Embed(
                title = str(year) + "s Countries (3/" + str(len(clist)) + ")",
                description = clist[2],
                color = discord.Color.blue()
            )
            pages = [page1, page2, page3]

            if len(clist) == 4:
                page4 = discord.Embed(
                    title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                    description = clist[3],
                    color = discord.Color.blue()
                )
                pages.append(page4)
            elif len(clist) == 5:
                page4 = discord.Embed(
                    title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                    description = clist[3],
                    color = discord.Color.blue()
                )
                pages.append(page4)
                page5 = discord.Embed(
                    title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                    description = clist[4],
                    color = discord.Color.blue()
                )
                pages.append(page5)
            elif len(clist) == 6:
                page4 = discord.Embed(
                    title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                    description = clist[3],
                    color = discord.Color.blue()
                )
                pages.append(page4)
                page5 = discord.Embed(
                    title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                    description = clist[4],
                    color = discord.Color.blue()
                )
                pages.append(page5)
                page6 = discord.Embed(
                    title = str(year) + "s Countries (6/" + str(len(clist)) + ")",
                    description = clist[5],
                    color = discord.Color.blue()
                )
                pages.append(page6)
            elif len(clist) == 7:
                page4 = discord.Embed(
                    title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                    description = clist[3],
                    color = discord.Color.blue()
                )
                pages.append(page4)
                page5 = discord.Embed(
                    title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                    description = clist[4],
                    color = discord.Color.blue()
                )
                pages.append(page5)
                page6 = discord.Embed(
                    title = str(year) + "s Countries (6/" + str(len(clist)) + ")",
                    description = clist[5],
                    color = discord.Color.blue()
                )
                pages.append(page6)
                page7 = discord.Embed(
                    title = str(year) + "s Countries (7/" + str(len(clist)) + ")",
                    description = clist[6],
                    color = discord.Color.blue()
                )
                pages.append(page7)


            message = await ctx.send(embed = page1)
            await message.add_reaction('⏮')
            await message.add_reaction('◀')
            await message.add_reaction('▶')
            await message.add_reaction('⏭')

            def check(reaction, user):
                return user == ctx.author

            i = 0
            reaction = None

            while True:
                if str(reaction) == '⏮':
                    i = 0
                    await message.edit(embed = pages[i])
                elif str(reaction) == '◀':
                    if i > 0:
                        i -= 1
                        await message.edit(embed = pages[i])
                elif str(reaction) == '▶':
                    if i < len(clist) - 1:
                        i += 1
                        await message.edit(embed = pages[i])
                elif str(reaction) == '⏭':
                    i = len(clist) - 1
                    await message.edit(embed = pages[i])

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 50.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            await message.clear_reactions()

    @commands.command(name="play")  # Plays music based on command
    async def _play(self, ctx):
        country = " ".join(args[0:len(args) - 1])
        year = int(args[len(args) - 1])
        inputBool = countryExists(country, year)
        await ctx.send(year)
        try:
            if year < 1900 or year > 2020:
                raise Exception("Year must be between 1900 and 2020")
            elif year % 10 != 0:
                raise Exception("Year must end in 0")
            elif inputBool == False:
                raise Exception(country + " does not exist in the " + str(year)+ "s")
        except Exception as e:
            await ctx.send(e)
    
    @client.command(name = "top") #Pulls up list of top countries, decades, and songs
    async def top(ctx, category):
        if category == "countries":
            pass
        elif category == "decades":
            pass
        elif category == "songs":
            pass
        else:
            try:
                raise Exception("Plase re-enter your command in the format '+top [category]', where the only valid terms for [category] are 'countries', 'decades', and 'songs'")
            except Exception as e:
                await ctx.send(e)

    @commands.command(brief = 'Ping the bot.',description='Ping the bot.') # Ping is always needed, right?
    async def ping(self, ctx):
        await ctx.send(f'Ping is {self.bot.latency} second.')

def setup(bot):
    bot.add_cog(general(bot))
