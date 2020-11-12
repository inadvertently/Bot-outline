import discord
import random

client = commands.Bot(command_prefix = 'INSERT PREFIX HERE')
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Streaming(name="INSERT WHAT YOU WANT IT TO STREAM", url='INSERT STREAM URL')) #This will change the activity of the bot 
print('Bot is now ready.') 

client.run("INSERT BOT TOKEN")
