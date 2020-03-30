import discord 
import random
from discord.ext import commands
from  db import *
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 

token = 'your_discordbot_taken'
client = commands.Bot(command_prefix = '!')
member_id = 0
member_name = ''


@client.event
async def on_ready():	
	print("bot is online")
	
   
@client.event
async def on_message(message):
	global member_id , member_name
	member_id = (message.author.id)
	member_name = (message.author.name)
	if (message.content.lower() == 'hi' or  message.content.lower() == 'hello' or message.content.lower() == 'hey'):
		await message.channel.send(f'Hello {member_name}')
	
	await client.process_commands(message)
	

#google search result command
@client.command(pass_context=True)
async def google(ctx, *, questions): 
	
	save_search(questions,member_name, member_id)

	for j in search(questions, tld="com", num=10, stop=5, pause=1): 
		await ctx.send(j)
	

# History Check command
@client.command(pass_context=True)
async def recent(ctx, * , questions):
	print(member_id)
	search_history = get_search(questions, member_id)
	
	if search_history == False:
		await ctx.send("No result found")
	else:
		for x in search_history:
			x = str(x)
			x =  x.strip("',()")
			await ctx.send(x)	

client.run(token)
