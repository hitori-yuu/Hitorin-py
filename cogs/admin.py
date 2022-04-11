import discord
from discord.ext import commands

def check_if_admin(ctx):
    return ctx.author.id == 874184214130602015

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(check_if_admin)
    async def load(self, ctx, extension):
        self.load_extension(f'cogs.{extension}')
        await ctx.send(f'Load -> {extension}')

    @commands.command()
    @commands.check(check_if_admin)
    async def unload(self, ctx, extension):
        self.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unload -> {extension}')

    @commands.command()
    @command.check(check_if_admin)
    async def reload(self, ctx, extension):
        self.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Reload -> {extension}')

def setup(client):
    client.add_cog(Admin(client))
