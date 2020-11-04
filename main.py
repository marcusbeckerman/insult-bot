import discord
import random
import time
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
TOKEN = "Enter token here"


def get_insult():
    f = open("insults.json")
    insults = eval(str(f.read()))
    return random.choice(insults)

async def insult_func(ctx,interval):
    members = ctx.guild.members
    while True:
        insult = get_insult()
        user = random.choice(members)
        while user.bot == True:
            user = random.choice(members)
        await ctx.send(user.mention + ", " + insult.lower())
        time.sleep(int(interval))


@bot.command()
async def insult_timer(ctx, interval):
    '''insults a random person at an interval in seconds'''
    await ctx.send("Sending an insult every " + interval + " seconds.")
    await insult_func(ctx, interval)

@bot.command()
async def insult(ctx, *, name):
    list = ctx.guild.members
    for member in list:
        if member.display_name.lower() == name.lower():
            await ctx.send(member.mention + ", " + get_insult().lower())

bot.run(TOKEN)
