# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default() # Gets the default intents from discord.
intents.members = True # enables members intents on the bot.
client = discord.Client(intents=intents) # Creates the client with the intents.

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
  embed = discord.Embed(title="Druze nemas ruke!", description=None, color = discord.Color.magenta())
  embed.add_field(name="Pazi:", value="• nemas\n• ruke!\n• :)", inline=True)
  await member.send(embed=embed)

client.run(TOKEN)