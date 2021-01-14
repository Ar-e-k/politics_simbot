import discord
from discord.ext import commands as coms
from discord.utils import get
import count
import tokn

client = coms.Bot(command_prefix="%")

@client.event
async def on_ready():
    print("ready")

def find_parties(client):
    roles={}
    for guild in client.guilds:
        for role in guild.roles:
            chan = str(role).lower()
            if "party" in chan:
                roles[chan] = role
    return roles

@client.event
async def on_message(msg):
    name=msg.author
    name=str(name).split("#")[0]
    if name=="Election bot":
        emoji = client.get_emoji(792376634547634176)
        await msg.add_reaction('\u2705')

    if str(msg.channel)=="bird":
        msg_txt=msg.clean_content
        for letter in msg_txt:
            if letter.islower():
                channel=msg.channel
                await channel.send("UPPER CASE")
                break


    await client.process_commands(msg)

'''@client.command()
async def say(ctx):
    await ctx.send("hey")
    %print(Elist)'''

@client.command()
@coms.has_permissions(administrator=True)
async def hold_election(ctx):
    #print("here")
    parties=find_parties(client)
    for key in parties:
        await ctx.send(key)

@client.command()
@coms.has_permissions(administrator=True)
async def end_election(ctx, seats):
    #print("Almost there")
    votelist={}
    party=1
    party_list=list(find_parties(client).keys())
    async for msg in ctx.channel.history(limit=100):
        message = await ctx.channel.fetch_message(msg.id)
        reaction = get(message.reactions, emoji='✅')
        if type(reaction)!=type(None):
            votelist[party_list[len(party_list)-party]]=(reaction.count-1)
            if len(party_list)-party==0:
                break
            party+=1
    print(votelist)
    seatlist=count.main(int(seats), votelist)
    await ctx.send(seatlist)

'''@client.event
async def on_command_error(ctx, error):
    if isinstance(error, coms.MissingRequiredArgument):
        await ctx.send("Invalid argument\nTry help command name, to see what arguments you require")
    elif isinstance(error, coms.MissingPermissions):
        await ctx.send("Dont try it\nIf you need the command please contact an admin")
    elif isinstance(error, coms.CommandNotFound):
        await ctx.send("There is no such command\nTry %help command to see the avaliable commands")'''
tk=tokn.token()

client.run(tk)
