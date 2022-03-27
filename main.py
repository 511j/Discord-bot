# Codeing by lord4tb , [ @ilord4tb ]
# github : 511j
# Free src in >> https://github.com/511j/tellonym-info
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='1')# Prefix

@bot.command()
async def avatar(ctx, member: discord.Member=None):# avatar command <1avatar>
	if member is None:
		me = ctx.author
		av = me.avatar_url
	else:
		av = member.avatar_url
	eme = discord.Embed()
	eme.set_image(url=av)
	await ctx.reply(embed = eme, mention_author=True)

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

bot.run("OTU3MjIwNDg5NDk4MDc5MjYy.Yj7nDA.nDVnRb9hWi0T04T1W-EukycK3-E") # Bot Token https://discord.com/developers/applications
