import discord
from discord.ext import commands
from enum import Enum

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = intents)
    self.synced = False 
    self.added = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced: 
      await tree.sync(guild = discord.Object('1090057965622546464'))
      self.synced = True
    if not self.added:
      self.added = True
    print(f"Say hi to {self.user}!")

client = aclient()
tree = discord.app_commands.CommandTree(client)

@tree.command(description='Count members with "=CALUM= Private" role.', guild=discord.Object('1090057965622546464'))
@commands.check(lambda ctx: any(role.name in ['=CALUM= Officers', 'CÆLUM_on_member_join'] for role in ctx.author.roles))
async def privates(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Private')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Private' role is {member_count}.")

@tree.command(description='Count members with "=CALUM= Sergeatns" role.', guild=discord.Object('1090057965622546464'))
@commands.check(lambda ctx: any(role.name in ['=CALUM= Officers', 'CÆLUM_on_member_join'] for role in ctx.author.roles))
async def sergeants(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Sergeants')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Sergeants' role is {member_count}.")

@tree.command(description='Count members with "=CALUM= Officers" role.', guild=discord.Object('1090057965622546464'))
@commands.check(lambda ctx: any(role.name in ['=CALUM= Officers', 'CÆLUM_on_member_join'] for role in ctx.author.roles))
async def officers(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Officers')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Officers' role is {member_count}.")



@client.event
async def on_member_join(member):
    invites = await member.guild.invites()
    for invite in invites:
        if "https://discord.gg/HYMWgpFaBq" in invite.url:
            role = discord.utils.get(member.guild.roles, name="=CALUM= Private")
            await member.add_roles(role)
            break

client.run('TOKEN')


