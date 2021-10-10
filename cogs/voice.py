import discord
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['come'])
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f'Joining => <#{ctx.author.voice.channel.id}>')

    @commands.command(aliases=['dc', 'dis', 'leave'])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send(f'I\'ve disconnected it.')

def setup(client):
    client.add_cog(Voice(client))