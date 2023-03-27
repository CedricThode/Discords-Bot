import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    # Check if the member joined via the specific link
    if "https://discord.gg/Qhvv92HYSt" in member.guild.me.invite_url:
        # Replace "=CALUM= Private" with the name of the role you want to assign
        role = discord.utils.get(member.guild.roles, name="=CALUM= Private")
        await member.add_roles(role)

# Replace "YOUR_TOKEN_HERE" with your bot token
client.run("MTA5MDAzNTU1MTE1NzEwODg1Ng.GLQBcT.HhoseTfJIwnei-Ykf351drDjxAH-I68tUJ60vw")

