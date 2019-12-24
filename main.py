import discord
import random
import time
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
TOKEN = "NjU4OTU4NTcyMzA2MTY5ODY2.XgHVBA.9iR_qVox2sN8OYS30G6QV5whoeA"


async def insult_func(ctx,interval):
    members = ctx.guild.members
    f = open("insults.json")
    insults = eval(str(f.read()))
    while True:
        insult = random.choice(insults)
        user = random.choice(members)
        while user.bot == True:
            user = random.choice(members)
        await ctx.send(user.mention + ", " + insult.lower())
        time.sleep(int(interval))

@bot.command()
async def insult(ctx, interval):
    '''insults a random person at an interval in seconds'''
    await ctx.send("Sending an insult every " + interval + " seconds.")
    await insult_func(ctx, interval)


bot.run(TOKEN)
