anyerror = False
try:
  import discord
  from discord.ext import commands
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install discord")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    import os
    from os import system
    system("title " + "Discord Server Message Auto Saver,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
import json
try:
  json_data = open("settings.json")
  json_data = json.load(json_data)
  token = str(json_data["bot_token"])
except Exception:
  print('Missing "settings.json" File, It Stores All Settings')
  input("")
  exit()

print("Will Not Work If Any Font In The Message, Name Of Server And Channel Names Cannot Include Fonts")

print("Starting Bot...")
#Bot Code
bot = commands.Bot(command_prefix="")
@bot.event
async def on_ready():
  print(f"{bot.user.name} Is Up")


@bot.event
@commands.dm_only()
async def on_message(self):
  try:
    if self.guild.id == None:
      pass
    else:
      content = self.content
      id = self.author.id
      name = self.author.name
      guild_id = self.guild.id
      guild_name = self.guild.name
      channel_name = self.channel.name
      channel_id = self.channel.id
      print(f"{str(id)}/{str(name)} Sent Message: {str(content)}")
      file = open(f"message_logs_{guild_id}.txt", "a")
      n1 = "Discord Name: " + str(name)
      n2 = "Discord Id: " + str(id)
      n3 = "Message Content: " + str(content)
      n4 = "Guild Id: " + str(guild_id)
      n5 = "Guild Name: " + str(guild_name)
      n6 = "Channel Id: " + str(channel_id)
      n7 = "Channel Name: " + str(channel_name)
      file.write(str(n1))
      file.write("\n")
      file.write(str(n2))
      file.write("\n")
      file.write(str(n3))
      file.write("\n")
      file.write(str(n4))
      file.write("\n")
      file.write(str(n5))
      file.write("\n")
      file.write(str(n6))
      file.write("\n")
      file.write(str(n7))
      file.write("\n")
      file.write("--------")
      file.write("\n")
      file.close()
  except Exception:
    print("User Sent Message In Dms Or Message Have Fonts")
    file.write("--------")
    file.write("\n")
    file.close()
  
#---
bot.run(token)
