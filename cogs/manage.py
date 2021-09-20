import discord
from discord.ext import commands

class Manage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, extension):
        self.load_extension(f'cogs.{extension}')
        await ctx.send(f'Load -> {extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        self.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unload -> {extension}')

def setup(client):
    client.add_cog(Manage(client))