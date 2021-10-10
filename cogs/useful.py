import discord
from discord.ext import commands
import datetime
import platform

class Useful(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def info(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('List of subcommands.\n[`bot`] , [`user`] , [`member`] , [`server`], [`emoji`]')

    @info.command()
    async def bot(self, ctx):
        client = self.client.user
        created = client.created_at.strftime('%Y/%m/%d %H:%M')
        owner = self.client.get_user(874184214130602015)
        joined = 'None'
        if (type(ctx.channel) != discord.DMChannel):
            joined = ctx.guild.me.joined_at.strftime('%Y/%m/%d %H:%M')
        embed = discord.Embed(title = 'Bot Details', description = '**BOT invitation link** -> [Click here](https://discord.com/api/oauth2/authorize?client_id=876116418037444630&permissions=8&scope=bot)', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = self.client.user.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = '__General:__', value = f'**[Name]** {client.name}#{client.discriminator}\n**[ID]** {client.id}\n**[Email]** {client.email}', inline = False)
        embed.add_field(name = '__Temporal:__', value = f'**[Created At]** {created}\n**[Joined At]** {joined}', inline = False)
        embed.add_field(name = '__Development:__', value = f'**[Author]** {owner.name}#{owner.discriminator}\n**[Version]** {discord.__version__} {discord.version_info.releaselevel}', inline = False)
        embed.add_field(name = '__System:__', value = f'**[Platform]** {platform.system()} {platform.release()}\n**[Python]** {platform.python_version()}', inline = False)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

    @info.command()
    async def user(self, ctx, u):
        user = await self.client.fetch_user(u)
        bot = 'USER'
        if user.bot:
            bot = 'BOT'
        created = user.created_at.strftime('%Y/%m/%d %H:%M')
        embed = discord.Embed(title = 'User Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = user.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = '__General:__', value = f'**[Name]** {user.name}#{user.discriminator}\n**[ID]** {user.id}\n**[Type]** {bot}', inline = False)
        embed.add_field(name = '__Temporal:__', value = f'**[Created At]** {created}', inline = False)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

    @info.command()
    async def member(self, ctx, member: discord.Member):
        bot = 'USER'
        if member.bot:
            bot = 'BOT'
        none = 'None'
        none_1 = ''
        split = '.'
        created = member.created_at.strftime('%Y/%m/%d %H:%M')
        joined = member.joined_at.strftime('%Y/%m/%d %H:%M')
        embed = discord.Embed(title = 'Member Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = member.avatar_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = '__General:__', value = f'**[Name]** {member.name}#{member.discriminator}\n**[Nickname]** {member.nick}\n**[ID]** {member.id}\n**[Type]** {bot}', inline = False)
        embed.add_field(name = '__Role:__', value = f'**[Roles]** {len(member._roles)}\n**[Top Role]** {member.top_role.mention}', inline = False)
        embed.add_field(name = '__Status:__', value = f'**[Status]** {str(member.status).title()}\n**[Activity]** {str(member.activity.type).split(split)[-1].title() if member.activity else none} {member.activity.name if member.activity else none_1}', inline = False)
        embed.add_field(name = '__Temporal:__', value = f'**[Created At]** {created}\n**[Joined At]** {joined}', inline = False)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

    @info.command()
    async def server(self, ctx, g):
        server = await self.client.fetch_guild(g)
        created = server.created_at.strftime('%Y/%m/%d %H:%M')
        embed = discord.Embed(title = 'Server Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = server.icon_url_as(format=None, static_format='png', size=1024))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = '__General:__', value = f'**[Name]** {server.name}\n**[ID]** {server.id}\n**[Owner]** <@{server.owner_id}>', inline = True)
        embed.add_field(name = '__Members:__', value = f'**[Members]** {server._members}\n**[Humans]** {len(list(filter(lambda m: not m.bot, server._members)))}\n**[Bots]** {len(list(filter(lambda m: m.bot, server._members)))}')
        embed.add_field(name = '__Amount:__', value = f'**[Channels]** {len(server.channels)}\n**[Text Channels]** {len(server.text_channels)}\n**[Voice Channels]** {len(server.voice_channels)}\n**[Roles]** {len(server._roles)}', inline = False)
        embed.add_field(name = '__Temporal:__', value = f'**[Created At]** {created}', inline = False)
        embed.add_field(name = '__Boosts:__', value = f'**[Amount]** {server.premium_subscription_count}\n**[Tier]** {server.premium_tier}', inline = False)
        embed.set_footer(text = datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))
        await ctx.send(embed = embed)

    @info.command()
    async def emoji(self, ctx, emoji: discord.Emoji = None):
        e = await emoji.guild.fetch_emoji(emoji.id)
        managed = 'Yes' if e.managed else 'No'
        animated = 'Yes' if e.animated else 'No'
        available = 'Everyone' if not e.roles else ' '.join(role.name for role in e.roles)
        created = e.created_at.strftime('%Y/%m/%d %H:%M')
        embed = discord.Embed(title = 'Emoji Details', color = discord.Colour.from_rgb(88, 101, 242))
        embed.set_thumbnail(url = emoji.url_as(format=None, static_format='png'))
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        embed.add_field(name = '__General:__', value = f'**[Name]** {e.name}\n**[ID]** {e.id}\n**[URL]** [Link]({e.url})\n**[Author]** {e.user.mention}\n**[Created At]** {created}\n**[Available]** {available}', inline = False)
        embed.add_field(name = '__Other:__', value = f'**[Animated]** {animated}\n**[Managed]** {managed}')
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Useful(client))