import discord
from discord.ext import commands
from main import sui
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')    

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pas(ctx, l_pas = 5):
    await ctx.send(sui(l_pas))
bot.run("MTE1NzcwNzE3MTE1NzUwODE1Nw.G70qK6.Z8Vh2_NVW3ZQKYoI_9KdDqlLKnSMxzAuGrazgQ")