import discord
from discord.ext import commands

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
        channel = discord.utils.get(before.guild.channels, name='moderation-log')
        if channel:
            await channel.send(f"Message edited in {before.channel.mention}: {before.author.mention} edited their message:\n\n{before.content} -> {after.content}\n\n{before.jump_url}")

client = aclient()
tree = discord.app_commands.CommandTree(client)

@tree.command(description='Count members with "=CALUM= Private" role.')
@commands.check(lambda ctx: any(role.name in ['=CALUM= Officers', 'CÆLUM_on_member_join'] for role in ctx.author.roles))
async def privates(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Private')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Private' role is {member_count}.")

@tree.command(description='Count members with "=CALUM= Sergeatns" role.')
@commands.check(lambda ctx: any(role.name in ['=CALUM= Officers', 'CÆLUM_on_member_join'] for role in ctx.author.roles))
async def sergeants(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='=CALUM= Sergeants')
    channel = discord.utils.get(guild.channels, name='role-counter')
    member_count = len(role.members)
    await channel.send(f"The number of members with the '=CALUM= Sergeants' role is {member_count}.")

@tree.command(description='Count members with "=CALUM= Officers" role.')
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
        if "Invite_link" in invite.url:
            role = discord.utils.get(member.guild.roles, name="=CALUM= Private")
            await member.add_roles(role)
            break

client.run('TOKEN')
