import discord
from discord.ext import commands
import json
import os

class Setting(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def prefix(self, ctx, prefix):
        path = os.path.realpath('../data/prefixes.json')
        with open(path, 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open(path, 'w') as f:
            json.dump(prefixes, f, indent = 4)

        await ctx.send(f'Prefix changed to : `{prefix}`')

def setup(client):
    client.add_cog(Setting(client))