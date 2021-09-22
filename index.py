import discord
from discord.ext import commands, tasks
import os
import json
import time
import datetime
intents = discord.Intents.all()
intents.typing = False

def get_prefix(client, message):
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)
        if (type(message.channel) == discord.DMChannel):
            return prefixes['0']
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intents = intents)

@client.event
async def on_ready():
    print(f'Ready -> {client.user.name}#{client.user.discriminator}')
    loop.start()

@tasks.loop(seconds = 10)
async def loop():
    await client.change_presence(status = discord.Status.online, activity = discord.Game(f'.help \ 1.0.0v \ {len(client.users)}users \ {len(client.guilds)}servers'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That command doesn\'t exist.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.ArgumentParsingError):
        await ctx.send('Please specify a valid argument.')

@client.event
async def on_command_error(ctx, error):
    print(error)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_guild_join(guild):
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('./data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@client.event
async def on_guild_remove(guild):
    with open('./data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

client.run('ODc2MTE2NDE4MDM3NDQ0NjMw.YRfY_w.FWOGmfq57xsaPy3bEsqai4jxW_g')

# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('That command doesn\'t exist.')

# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.ArgumentParsingError):
#         await ctx.send('Please specify a valid argument.')

# @<command>.error
# async def <command>_error(ctx, error):
#     if isinstance(error, commands.<error_type>):
#         await ctx.send(<error_message>)
