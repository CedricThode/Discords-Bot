import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    # Fetch the invites for the guild
    invites = await member.guild.invites()
    # Check if the invite is the specific link
    for invite in invites:
        if "https://discord.gg/26Sjm6Qett" in invite.url:
            # Gives role "=CALUM= Private" 
            role = discord.utils.get(member.guild.roles, name="=CALUM= Private")
            await member.add_roles(role)
            break

# TOKEN
client.run("TOKEN")



