#sadGeb.py
import discord
import random
import datetime
import asyncio

TOKEN = "NjA0MDkxMzcwNDkxMDg0ODAw.XUBzsQ.CBzP0WFLU6HFeI4WSYlp6ivZ45o"

client = discord.Client()

reminders = {}
replies = ["With that's the second time bout of you go away", "Give Khepri a gun","They don't think it be like it is, but it do", "Sobek is a lizard", "What are you gonna do, kill me?", "Did you know that Petey is gay?"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f"Hello {message.author.mention}")

    if message.content.count('sad')>0:
        await message.channel.send(random.choice(replies))

    if message.content.startswith('!remind'):
        userRoles = message.author.roles
        admin = False
        for role in userRoles:
            adminCheck = role.permissions.administrator
            if adminCheck == True:
                admin = True
        if admin == True:
            try:
                info = message.content.split(' ')
                currentDate = datetime.datetime.now()
                remindDate = datetime.datetime.strptime(info[1], '%m/%d/%Y')
                time = info[2].split(':')
                remindDate = remindDate.replace(hour=int(time[0]), minute=int(time[1]))
                timedelta = remindDate - currentDate
                if remindDate > currentDate:
                    await message.channel.send(f"I will remind you in {timedelta}")
                    msg = ''
                    i = 3
                    while i < len(info):
                        msg += info[i]
                        msg+= ' '
                        i += 1
                    message.content = msg

                    waitTime = round((int(timedelta.days)*3600*24)+(int(timedelta.seconds)))
                #    reminders += {remindDate: [message.author, msg]}
                    await asyncio.sleep(waitTime)
                    await message.channel.send(f"{message.author.mention} {msg}")
                else:
                    await message.channel.send("The given time has already passed.")
            except ValueError:
                await message.channel.send("Something went wrong. Make sure you format your request correctly.")
        else:
            await message.channel.send("This function is for Admin ranks only.")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    reminders = {}



client.run(TOKEN)
