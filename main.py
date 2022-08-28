import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from faceit_api import *
from faceit_cmds import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("-"), intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="-help")
    )
    print(f"{bot.user.name} success.")


@bot.command(name="profile")
async def profile(ctx, nickname):
    try:
        profile = find_profile(nickname)
    except KeyError as err:
        print("Invalid name\n Error: {}".format(err))
        return

    embed = discord.Embed(
        title="Player **{}**".format(nickname),
        url="https://www.faceit.com/en/players/{}".format(nickname),
        color=0x824DFF,
    )
    embed.set_thumbnail(url=profile["player_avatar"])
    embed.add_field(name="Level", value=profile["player_level"], inline=True)
    embed.add_field(name="ELO", value=profile["player_elo"], inline=True)
    await ctx.send(embed=embed)


bot.run(TOKEN)
