import discord
from discord.ext import commands as coms
from discord.utils import get
import count
global Elist
Elist=[]

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
        Elist.append(msg.id)
        emoji = client.get_emoji(792376634547634176)
        await msg.add_reaction('\u2705')

    await client.process_commands(msg)

'''@client.command()
async def say(ctx):
    await ctx.send("hey")
    %print(Elist)'''

@client.command()
@coms.has_permissions(administrator=True)
async def hold_election(ctx):
    Elist=[]
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
    for msg in Elist:
        message = await ctx.channel.fetch_message(msg)
        reaction = get(message.reactions, emoji='✅')
        votelist[party]=reaction.count
        party+=1
    #print(votelist)
    seatlist=count.main(seats, votelist)
    await ctx.send(seatlist)

client.run('NzgzMDQyODgwMDcxNTMyNTg2.X8U_gg.0OSQgEFuX5v-9ZgefkXWknMFOIY')
