import discord
import pytz
from discord.ext import commands
from datetime import datetime, timezone
from pytz import timezone as tz


intents = discord.Intents.all()
intents.members = True
intents.message_content = True

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False 

    async def on_ready(self):
        if not self.synced: 
            await tree.sync(guild=discord.utils.get(self.guilds, name='my_guild'))
            self.synced = True
        print(f"{self.user} is online!")

    async def on_message_edit(self, before, after):
        if before.channel.category.name == '╔══════•|• Staff •|•══════╗':
            return  # Ignore messages edited in the "staff" category
        if before.channel.category.name == '╔═══•|• Server Info •|•════╗':
            return  # Ignore messages edited in the "Server Info" category

    # Checks if the message contains a GIF or link
        if any(attachment.proxy_url.startswith(('http://', 'https://')) for attachment in after.attachments):
            return  # Ignore links
    
        if any(attachment.url.endswith(('.gif', '.gifv')) for attachment in after.attachments):
        # Check if the message contains a Discord Tenor GIF
            if any(attachment.proxy_url.startswith('https://media.discordapp.net/tenor') for attachment in after.attachments):
                return
            if any(attachment.proxy_url.startswith('https://cdn.discordapp.com/attachments/') for attachment in after.attachments):
                return  
            
        
        channel = discord.utils.get(before.guild.channels, name='moderation-log')
        cet_tz = timezone('CET')
        if channel:
            embed = discord.Embed(title='Message Edited', color=discord.Color.gold())
            embed.add_field(name='Channel', value=before.channel.mention, inline=False)
            embed.add_field(name='User', value=before.author.mention, inline=False)
            embed.add_field(name='Before', value=f'```{before.content}```', inline=False)
            embed.add_field(name='After', value=f'```{after.content}```', inline=False)
            embed.add_field(name='Edited At', value=datetime.now(cet_tz).strftime('%Y-%m-%d %H:%M:%S %Z'), inline=False)
            embed.add_field(name='Original Sent At', value=before.created_at.astimezone(cet_tz).strftime('%Y-%m-%d %H:%M:%S %Z'), inline=False)
            embed.add_field(name='Jump URL', value=before.jump_url, inline=False)
            await channel.send(embed=embed)


    async def on_message_delete(self, message):
        if message.channel.category.name == '╔══════•|• Staff •|•══════╗':
            return  # Ignore messages deleted in the "staff" category
    
        channel = discord.utils.get(message.guild.channels, name='moderation-log')
        if channel:
            embed = discord.Embed(title='Message Deleted', color=discord.Color.red())
            embed.add_field(name='Channel', value=message.channel.mention, inline=False)
            embed.add_field(name='User', value=message.author.mention, inline=False)
            embed.add_field(name='Message', value=f'```{message.content}```', inline=False)
            embed.add_field(name='Deleted At', value=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'), inline=False)
            await channel.send(embed=embed)

client = aclient()
tree = discord.app_commands.CommandTree(client)

@tree.command(description='Count members with "=CALUM= Private" role.')
@commands.check(lambda ctx: max(role.position for role in ctx.author.roles) >= max(
        discord.utils.get(ctx.guild.roles, name='=CALUM= Officers').position,
        discord.utils.get(ctx.guild.roles, name='CÆLUM_on_member_join').position))
async def privates(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Private')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Private' role is {member_count}.")
    return

@tree.command(description='Count members with "=CALUM= Sergeatns" role.')
@commands.check(lambda ctx: max(role.position for role in ctx.author.roles) >= max(
        discord.utils.get(ctx.guild.roles, name='=CALUM= Officers').position,
        discord.utils.get(ctx.guild.roles, name='CÆLUM_on_member_join').position))
async def sergeants(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Sergeants')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Sergeants' role is {member_count}.")
    return

@tree.command(description='Count members with "=CALUM= Officers" role.')
@commands.check(lambda ctx: max(role.position for role in ctx.author.roles) >= max(
        discord.utils.get(ctx.guild.roles, name='=CALUM= Officers').position,
        discord.utils.get(ctx.guild.roles, name='CÆLUM_on_member_join').position))
async def officers(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Officers')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Officers' role is {member_count}.")
    return

@client.event
async def on_member_join(member):
    invites = await member.guild.invites()
    for invite in invites:
        if "https://discord.gg/HYMWgpFaBq" in invite.url:
            role = discord.utils.get(member.guild.roles, name="=CALUM= Private")
            await member.add_roles(role)
            break

client.run('TOKEN')
