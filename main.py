# Codeing by lord4tb , [ @ilord4tb ]
# github : 511j
# Free src in >> https://github.com/511j/tellonym-info
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='1')# Prefix

@bot.command()
async def avatar(ctx):
    member = ctx.author
    e = discord.Embed(title="avatar link ", url=f"{member.avatar_url}",coulor=0xF40E0E)
    e.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    e.set_image(url=f"{member.avatar_url}")
    e.set_footer(text=f"requested by {member.name}", icon_url=f"{member.avatar_url}")
    await ctx.send(embed=e)

# event 
@bot.event
async def on_ready():
        print (f"[ * ] I am running now ..") # if bot online print online
        print(f"[ * ] Bot username >> " + bot.user.name)
        print(f"[ * ] Bot username >> " + bot.user.id)
        print("")
        await bot.change_presence(status = discord.Status.idle, activity = discord.Game("hi ")) # status in discord
        print(f"\n Enter To Exit: ", end="")
        input()
        exit()

@bot.command()# اذا كتبت في الشات id
async def id(ctx):# ومنشنت احد البوت يرسل لك ايديه
  await ctx.send(f"{ctx.author.mention}, **Your discord ID is** ||{ctx.author.id}||")

bot.run("TOKEN HERE") # Bot Token https://discord.com/developers/applications
