import discord 
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import os
            
BOT_PREFIX = ("neko? ","Neko? ")
NoCopyList = []
bot = Bot(command_prefix=BOT_PREFIX)


@bot.command(name="nocopy", 
	aliases=['Nocopy',"nocp","NoCp"], 
	description="Make Copy Cat Stop Copying You Until She Goes Offline",
	brief="Stop Copying Me") 
async def NoCopy(message):
	print("On Command: "+"NoCopy")
	print(NoCopyList)
	usr_id = message.author.id
	print(usr_id)
	if usr_id in NoCopyList:
		await message.channel.send(message.author.display_name+" Stop Messing with me!:pouting_cat:")
	else:
		NoCopyList.append(usr_id)
		await message.channel.send(message.author.display_name+" Fine, I'll stop copying you :pouting_cat:")
		print(NoCopyList)


@bot.command(name="dummys",
	description='Display the list of "Party Poopers"(Stop Mocking list)', 
	brief="Display Stop Mocking list",
	aliases=["dummies","Dummys","Dummies","nocopylist", "NocopyList"])
async def dummys(message):
	print("On Command: "+"dummys")
	if len(NoCopyList) == 0:
		await message.channel.send("Yes!!:smiley_cat: No Party Poopers!!")
	else:
		await message.channel.send("Heres a list of **Party Poopers** :smirk_cat:")
		for name in NoCopyList:
			print(str(name))
			await message.channel.send(bot.get_user(name)) #######<<===============


@bot.command(name="copyme",brief="Removes you from No Copy List", aliases=["Copyme"])
async def copyme(message):
	print("On Command: "+"copyme")
	print(NoCopyList)
	usr_id = message.author.id
	if usr_id in NoCopyList:
		print("IN")
		print(usr_id)
		print("INDEXING: "+ str(NoCopyList.index(usr_id)) +"|"+ str(NoCopyList[NoCopyList.index(usr_id)]))
		del NoCopyList[NoCopyList.index(usr_id)]
		await message.channel.send(message.author.mention+" I can now copy you!:joy_cat:")
		print(NoCopyList)
	else:
		await message.channel.send(message.author.mention+" Something went Wrong.:pouting_cat:\nI still cant play with you")
		print(NoCopyList)

@bot.event
async def on_message(message):                        # NEED TO IGNORE MESSAGE STARTING WITH neko? and the 
	print("NEW MESSAGE")
	usr_id = message.author.id
	print(NoCopyList)
	print(usr_id)
	print("-----")
	print(message.author.display_name)
	
	if usr_id in NoCopyList:
		if message.content.startswith(BOT_PREFIX):
			if message.author != bot.user:                  # we do not want the bot to reply to itself   
				pass

# check for images in message and repost them	
	elif len(message.attachments) > 0:
		if message.author != bot.user:                      # we do not want the bot to reply to itself
			print("Message lenght: ",len(message.content))                        
			if len(message.content) > 0:
				try:
					print(message.content)
					await message.channel.send(message.content)
				except Exception as e:
					print("ERROR",e)

			print("Attachments")
			print("AUTHOR:",message.author.display_name)
			attachment = message.attachments
			for obj in attachment:
				print(obj.url)
				print('>------')
				await message.channel.send(obj.url) # output Copy of orginal message
	elif bot.user.mentioned_in(message):
		if message.author != bot.user:
			print(message.content)
			if "🍣" in message.content.lower():
				await message.channel.send("Oishii..")
		

				await message.channel.trigger_typing()
				await asyncio.sleep(5)
				await message.channel.send("Arigato,  {}  Senpai. thx:smiley_cat:".format(message.author.display_name))
			else:
				await message.channel.send("What do you want!?:pouting_cat:")

	elif "hentai" in message.content.lower():
		await message.channel.send("HENTAI!!!:heart_eyes_cat:")
		await asyncio.sleep(1)
		await message.channel.send("GIVE IT TO ME!!!")
			
	else:
		if message.author != bot.user:
			await message.channel.send(message.content) # output Copy of orginal message

	await bot.process_commands(message)

@bot.command(name="temp")
async def tempconversion(temp):
	if 'c' in str(temp).lower():
		f = (float(temp.replace(temp[-1],""))*float(1.80))+32
		await bot.say("{} now becomes {}.".format(temp,f))
	elif "f" in str(temp).lower():
		c = (float(temp.replace(temp[-1],""))-32)/float(1.80)
		await bot.say("{} now becomes {}.".format(temp,c))
	else:
		await bot.say("Something went wrong. Check your units maybe?")		





@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print("Activating watching status")
	activity = discord.Activity(name=' Hentai', type=discord.ActivityType.watching)
	await bot.change_presence(activity=activity)

bot.run(str(os.environ.get('BOT_TOKEN')))

