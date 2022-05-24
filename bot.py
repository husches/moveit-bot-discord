from http import client
import discord
from discord.ext import commands
import asyncio

intents=discord.Intents.default()

bot = commands.Bot(command_prefix='$')
TOKEN = "OTcyMTIwMjg5MjE3NTA3NDAw.GarLqo.piV-_Ud68os_pewf4RqjcmAaHvrsT_fC7CNjBU"
bot_text_channel = bot.get_channel(974632452909826048)


@bot.command()
async def move(ctx, channel : discord.VoiceChannel, *members: discord.Member):
    for member in members:
        await member.move_to(channel)


@bot.command()
#supposed to find all members connected to the server
async def people(ctx):
    member_ids = []

    channel_gruppe1 = bot.get_channel(960465581503565854)
    members_gruppe1 = list(channel_gruppe1.voice_states.keys())
    channel_gruppe2 = bot.get_channel(960465619491356683)
    members_gruppe2 = list(channel_gruppe2.voice_states.keys())
    channel_gruppe3 = bot.get_channel(960465704686084106)
    members_gruppe3 = list(channel_gruppe3.voice_states.keys())
    channel_gruppe4 = bot.get_channel(960465741344296990)
    members_gruppe4 = list(channel_gruppe4.voice_states.keys())
    channel_gruppe5 = bot.get_channel(960465772763840542)
    members_gruppe5 = list(channel_gruppe5.voice_states.keys())
    channel_gruppe6 = bot.get_channel(960465895535300608)
    members_gruppe6 = list(channel_gruppe6.voice_states.keys())
    channel_gruppe7 = bot.get_channel(960465923234492447)
    members_gruppe7 = list(channel_gruppe7.voice_states.keys())
    channel_gruppe8 = bot.get_channel(960465949029466113)
    members_gruppe8 = list(channel_gruppe8.voice_states.keys())
    channel_gruppe9 = bot.get_channel(948860107888947245)
    members_gruppe9 = list(channel_gruppe9.voice_states.keys())

    for member_id1 in members_gruppe1:
        member_ids.append(member_id1)
    for member_id2 in members_gruppe2:
        member_ids.append(member_id2)
    for member_id3 in members_gruppe3:
        member_ids.append(member_id3)
    for member_id4 in members_gruppe4:
        member_ids.append(member_id4)
    for member_id5 in members_gruppe5:
        member_ids.append(member_id5)
    for member_id6 in members_gruppe6:
        member_ids.append(member_id6)
    for member_id7 in members_gruppe7:
        member_ids.append(member_id7) 
    for member_id8 in members_gruppe8:
        member_ids.append(member_id8)
    for member_id9 in members_gruppe9:
        member_ids.append(member_id9)   

    #member_ids = list(channel.voice_states.keys())
    print(member_ids)
    return member_ids

@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user: discord.Member, time: int=1):
    '''Mute a member in the guild'''
    secs = time * 60
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await ctx.channel.set_permissions(user, send_messages=False)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(user, connect=False)

    await ctx.send(f"{user.mention} has been muted for {time} minutes.")
    await asyncio.sleep(secs)
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await ctx.channel.set_permissions(user, send_messages=None)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(user, connect=None)
    await ctx.send(f'{user.mention} has been unmuted from the guild.')



@bot.command()
async def moveAllto(ctx, channel:discord.VoiceChannel):
    print(ctx.channel.id)
    if ctx.channel.id == 974632452909826048 or ctx.channel.id == 960464145508081674:
        members_connected = await people(ctx) #Get the people
        for member_id in members_connected:
            member = await ctx.guild.fetch_member(member_id)
            #await mute(ctx, member)
            await member.move_to(channel)
            #await mute(ctx, member)
            await ctx .send(f"{member.mention} has been moved to Channel Announcements.")
    else:
        await ctx .send("I'm Sorry! In here, I was restricted by @Tim Aaron Möck!!!")




@bot.event
async def on_ready():
    print("READY")

bot.run(TOKEN)