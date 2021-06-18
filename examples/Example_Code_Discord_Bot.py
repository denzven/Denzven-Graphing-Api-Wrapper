import discord
from discord.ext import commands
import os
import datetime
import DenzGraphingApiWrapper_py as GraphingApi #pip install DenzGraphingApiWrapper-py

bot = commands.Bot(command_prefix=(">"))

@bot.event
async def on_connect():
	print("the bot is ready")

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}\n')

@bot.event
async def on_command_error(ctx, error):
	raise error

@bot.command()
async def pythonanywhere_graph(ctx, formula):
    url = GraphingApi.py_anywhere_graph(formula)
    await ctx.send(url)

@bot.command()
async def heroku_graph(ctx, formula):
    url = GraphingApi.heroku_graph(formula)
    await ctx.send(url)

@bot.command()
async def pythonanywhere_graph_with_Embed(ctx, formula):
    url = GraphingApi.py_anywhere_graph(formula)
    embed = discord.Embed(title = f' the graphical representation of \n ```{formula} = 0```',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def heroku_graph_with_Embed(ctx, formula):
    url = GraphingApi.heroku_graph(formula)
    embed = discord.Embed(title = f' the graphical representation of \n ```{formula} = 0```',color = discord.Color.green(),url = url)
    embed.set_image(url = url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'rendered by {ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/denzven/DenzGraphingApiWrapper_py")

@bot.command()
async def docs(ctx):
    await ctx.send("https://denzgraphingapiwrapper-py.readthedocs.io/en/latest/")

@bot.command()
async def pypi(ctx):
    await ctx.send("https://pypi.org/project/DenzGraphingApiWrapper-py/")

@bot.command()
async def test_pypi(ctx):
    await ctx.send("https://test.pypi.org/project/DenzGraphingApiWrapper-py-denzven/")

@bot.command()
async def code(ctx):
    await ctx.send(file = discord.File(r'main.py'), content = "Here is the Code of This Bot")
	
bot.run(os.environ['bottoken']) #69 nice