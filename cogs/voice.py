import discord
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['come'])
    async def join(self, ctx):
        if ctx.guild is None:
            await ctx.send("This command can't be executed in DM channel")
            return

        voice_state = ctx.author.voice
        if (not voice_state) or (not voice_state.channel):
            await ctx.send('You have to join to voice channel')
            return
        
        channel = voice_state.channel
        await channel.connect()
        await ctx.send(f'Joining => <#{ctx.author.voice.channel.id}>')

    @commands.command(aliases=['dc', 'dis', 'leave'])
    async def disconnect(self, ctx):
        if ctx.guild is None:
            await ctx.send("This command can't be executed in DM channel")
            return
        
        if ctx.guild.voice_client is None:
            await ctx.send("I'm not in the voice channel")
            return
        
        await ctx.voice_client.disconnect()
        await ctx.send(f'I\'ve disconnected it.')

def setup(client):
    client.add_cog(Voice(client))
