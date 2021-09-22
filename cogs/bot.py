import discord
from discord.ext import commands
import datetime

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title = 'Invite Link', description = '**BOT invitation link** -> [Click here](https://discord.com/api/oauth2/authorize?client_id=876116418037444630&permissions=8&scope=bot)',color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = self.client.user.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Bot(client))