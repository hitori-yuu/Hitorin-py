import discord
from discord.ext import commands
import datetime

class Useful(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def info(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('List of subcommands.\n[`bot`] , [`user`] , [`member`] , [`server`]')

    @info.command()
    async def bot(self, ctx):
        await ctx.send('Sorry, This command is under adjustment.')

    @info.command()
    async def user(self, ctx, user: discord.User):
        bot = 'USER'
        if user.bot:
            bot = 'BOT'
        embed = discord.Embed(title = 'User Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = user.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = 'User Name', value = user.name + '#' + user.discriminator, inline = True)
        embed.add_field(name = 'User ID', value = user.id, inline = True)
        embed.add_field(name = 'Type', value = bot, inline = True)
        embed.add_field(name = 'Created at', value = user.created_at.strftime('%Y/%m/%d %H:%M'), inline = True)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

    @info.command()
    async def member(self, ctx, member: discord.Member):
        bot = 'USER'
        if member.bot:
            bot = 'BOT'
        embed = discord.Embed(title = 'Member Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = member.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = 'Member Name', value = member.name + '#' + member.discriminator, inline = True)
        embed.add_field(name = 'Member ID', value = member.id, inline = True)
        embed.add_field(name = 'Type', value = bot, inline = True)
        embed.add_field(name = 'Nickname', value = member.nick or 'None', inline = True)
        embed.add_field(name = 'Roles', value = len(member._roles), inline = True)
        embed.add_field(name = 'Top Role', value = member.top_role.mention, inline = True)
        embed.add_field(name = 'Status', value = str(member.status).title(), inline = True)
        embed.add_field(name = 'Activity', value = f"{str(member.activity.type).split('.')[-1].title() if member.activity else 'None'} {member.activity.name if member.activity else ''}", inline = True)
        embed.add_field(name = 'Joined At', value = member.joined_at.strftime('%Y/%m/%d %H:%M'), inline = True)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

    @info.command()
    async def server(self, ctx, server: discord.Guild):
        embed = discord.Embed(title = 'Server Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = server.icon_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = 'Server Name', value = server.name, inline = True)
        embed.add_field(name = 'Server ID', value = server.id, inline = True)
        embed.add_field(name = 'Server Owner', value = f'<@{server.owner_id}>', inline = True)
        embed.add_field(name = 'Members', value = server.member_count, inline = True)
        embed.add_field(name = 'Channels', value = len(server._channels), inline = True)
        embed.add_field(name = 'Roles', value = len(server._roles), inline = True)
        embed.add_field(name = 'Created At', value = server.created_at.strftime('%Y/%m/%d %H:%M'), inline = True)
        embed.add_field(name = 'Boosts', value = f'Count: {server.premium_subscription_count} , Tier: {server.premium_tier}', inline = True)
        embed.add_field(name = 'Description', value = f'```{server.description}```', inline = False)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)
        print(datetime.datetime.fromisoformat(f'{server.created_at}'))

def setup(client):
    client.add_cog(Useful(client))