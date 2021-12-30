import discord
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

client = discord.Client()

client = commands.Bot(command_prefix = '$')
@client.event
async def on_ready():
  print("Online")

f = open("help", "r")
h = f.read()
f.close()    
    
@client.command()
@commands.has_role("sudo")
async def sudo(ctx, arg=None, arg2=None, usr : discord.Member=None):
  if arg == None:
    await ctx.send("`sh: sudo: nothing to do`")
  if arg == "heck":
    if arg2 == "true":
      if not usr == None:
        await usr.ban(reason = "sh: sudo: heck: hecked")
        await ctx.send(f"`sh: sudo: heck: hecked @{usr}`")
      else:
        await ctx.send("`sh: sudo: heck: select user (@user)`")
    elif arg == "false":
      await ctx.send("`sh: sudo: heck: Canceled`")
    else:
      await ctx.send("`sh: sudo: heck: value must be true or false`")
  elif arg == "heck-lite":
    if arg2 == "true":
      if not usr == None:
        await usr.kick(reason = "sh: sudo: heck-lite: lite-hecked")
        await ctx.send(f"`sh: sudo: heck-lite: lite-hecked @{usr}`")
      else:
        await ctx.send("`sh: sudo: heck-lite: select user (@user)`")
    elif arg == "false":
      await ctx.send("`sh: sudo: heck-lite: Canceled`")
    else:
      await ctx.send("`sh: sudo: heck-lite: value must be true or false`")
  elif arg == "make":
    if arg2 == "meteor":
      await ctx.send("https://c.tenor.com/kJnySS9eKvUAAAAC/crashing-to-earth-meteor-showers101.gif`")
    else:
      await ctx.send("`sh: sudo: make: nothing to do`")
  elif arg == "rickroll":
    if arg2 == "true":
      await usr.send(f"`Hey buddy! @{ctx.author.name} sent you a nitro! Click da link get it:` <http://bit.do/fS2nY>\n`Don't worry! This is not an IP Grabber! Bit.do is website to shorten links!`")
      await ctx.send(f"`Sent rickroll to @{usr}`")
    elif arg2 == "false":
      await ctx.send("`sh: sudo: rickroll: canceled`")
  elif arg == "dm":
    await usr.send(f"`Hey! @{ctx.author.name} sent you a DM! Here is the message!`\n||`{arg2}`||")
    await ctx.send(f"`sh: sudo: dm: sent dm to @{usr}`")
  elif arg == "help":
    await ctx.send(h)
  else:
    await ctx.send("`sh: sudo: use $sudo help to list all commands!`")

client.run("OTI1ODI2MTUxNzUzMDg5MDQ2.Ycywyw.GP2xrfrs3pptB2zIdlUNejw7qGc")

#https://discord.com/oauth2/authorize?client_id=925826151753089046&permissions=8&scope=bot