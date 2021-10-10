import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx, extension):
        if ctx.author.id == 874184214130602015:
            self.load_extension(f'cogs.{extension}')
            await ctx.send(f'Load -> {extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        if ctx.author.id == 874184214130602015:
            self.unload_extension(f'cogs.{extension}')
            await ctx.send(f'Unload -> {extension}')

    @commands.command()
    async def reload(self, ctx, extension):
        if ctx.author.id == 874184214130602015:
            self.reload_extension(f'cogs.{extension}')
            await ctx.send(f'Reload -> {extension}')

def setup(client):
    client.add_cog(Admin(client))
