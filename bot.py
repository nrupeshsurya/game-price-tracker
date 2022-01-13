import os
from websites import gamenation
import pyshorteners
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='gamenation', help='get prices from Gamenation.in')
async def getGamenation(ctx, *, arg):
    gameList = gamenation(arg)
    s=pyshorteners.Shortener()
    if len(gameList) == 0:
        await ctx.send("No match found!")
        return
    response = ''
    maxlen = 0
    maxlenPrice = 0
    for game in gameList:
        maxlen = max(len(game['title']),maxlen)
        maxlenPrice = max(len(game['price']),maxlenPrice)

    rowSize = 0 

    for game in gameList:
        toadd = maxlen - len(game['title'])
        toaddPrice = maxlenPrice - len(game['price'])
        mainString = f'``{game["title"]}'+toadd*" "+"`` |"+f" {game['price']} "+toaddPrice*" "+f"|  <{s.tinyurl.short(game['gameUrl'])}>  \n" 
        rowSize = len(mainString)
        response+=len(mainString)*"="
        response+="\n"
        response+=mainString

    response+=rowSize*"="
    await ctx.send(response)



bot.run(TOKEN)

# name = 'guardians of the galaxy'
# isPS5 = True
# isPS4 = True
# isNew = True
# isPreOwned = True
# isXboxSeriesXS = True

# print(gamenation(name, isPS5, isPS4, isPreOwned, isXboxSeriesXS, isNew))