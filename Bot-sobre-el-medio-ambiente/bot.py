import discord 
from discord.ext import commands
import random
import os 


intents = discord.Intents.default()
intents.message_content = True

bot= commands.Bot(command_prefix="$", intents=intents)

list_frases=["Enseñar a cuidar el medio ambiente es enseñar a valorar la vida","Aunque supiera que mañana se acaba el mundo, hoy mismo plantaría un árbol","Nunca sabremos el valor del agua hasta que el pozo esté seco"]
list_info=["https://eacnur.org/es/blog/acciones-cuidar-medio-ambiente-casa","https://www.un.org/es/un75/climate-crisis-race-we-can-win"]
@bot.event
async def on_ready():
    print(f"Tu bot esta iniciado")
    
@bot.command()
async def comandos(ctx):
    await ctx.send("los comandos que puede recibir este bot son : $frase , $meme , $info , $diario")     
@bot.command()
async def frase(ctx):
    num_fras= random.choice(list_frases)
    await ctx.send(num_fras)

@bot.command()
async def meme(ctx):
    list_images= random.choice(os.listdir("./Images"))
    with open(f'images/{list_images}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def info(ctx):
    num_info= random.choice(list_info)
    await ctx.send(num_info)
    
@bot.command()
async def diario(ctx):
    await ctx.send("http://127.0.0.1:5000")

bot.run("MTEzODg2NjE1NDc0NDU3ODEyMA.GE2it4.SDQ_xLcACOm6gteFzUjY-Qgkh6jgDHNKnwwc4A")
