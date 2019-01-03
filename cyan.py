import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Bot Is Ready')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def shop():
    await bot.say('Items in Shop: Custom Emoji - 2 Gold | Custom Role -  4 Gold | Custom Command - 7  Gold | Custom Text Channel - 30 Gold | Custom Voice Channel - 20 Gold Your gold is your current level')

@bot.command()
async def buy():
    await bot.say('Pm the founder')

@bot.command()
async def value():
        await bot.say('The current invite link value is: 2 invite link = 0.10 Gold.')

bot.remove_command('help')




@bot.command()
async def help():
    await bot.say('Commands: shop ~ displays shop items | value ~ shows value of a reward | Hi ~ Replies how are you | Buy ~ Purchase an item | Forums ~Shows the forums | I was made by @238411903175491586.')

@bot.command()
async def hi():
    await bot.say('How are you')

@bot.command()
async def forums():
    await bot.say('Our current forums are http://aspectcommunity.mistforums.com')



bot.run("NDk4MjI0MzIwNzY2NTQxODQ2.Dw8XNQ.ncZqh4QOmTf-am8cjqJUkuOJ5vw")
bot.close()