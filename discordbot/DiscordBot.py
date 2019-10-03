import discord
from discord.ext import commands

import random
from time import sleep

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import os

#web scraping
Peterson = 'https://washalert.sdsmt.edu/washalertweb/washalertweb.aspx?location=5013aaa2-fb4a-4f46-97f5-d6c4321a4f1d'
Palmerton = 'https://washalert.sdsmt.edu/washalertweb/washalertweb.aspx?location=76d93bb5-481a-468b-bfdb-45a891a4dd40'
dadJokes = 'http://niceonedad.com/'

tokenFile = open(r'C:\Users\hidde\Desktop\chaosToken.txt')
for line in tokenFile:
    TOKEN = line

client = commands.Bot(command_prefix = '|')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

@client.event

async def on_message(message):    
    author = message.author
    content = message.content
    channel = message.channel

    

    if message.author.id == "554174974982881280" and message.content.startswith('PLUS ULTRA!!!!! '):
        await client.send_message(channel, 'Ugh, that bot annoys me')
        await client.send_message(channel, 'https://78.media.tumblr.com/7a17c7211b1063b465c29da969e58b47/tumblr_o9pmnxz2aI1sw7bx5o1_400.gif')


    if message.content.lower().startswith('i cri'):
        await client.send_message(channel, 'Dont be depresso, have an espresso <:widogasm:549837703189889035> :coffee:')
        await client.send_message(channel, 'https://cdn.chefjohnhowie.com/wp-content/uploads/2018/03/Coffee-tips-from-Erik-Liedholm.jpg')

    if message.content.lower().startswith("m'lady"):
        await client.send_message(channel, 'https://cdn.discordapp.com/attachments/554733032121303063/568520330520428545/image0.png')
    if message.content.lower().startswith("bitch"):
        await clinet.send_message(channel, "Die, hoe")

    else:
        await client.process_commands(message)

@client.event
async def on_ready():
    print('Bot is ready.')
    
@client.command()
async def update():
    os.system(r'cd C:\Users\hidde\Desktop\chaosUpdater.bat')
    #os.system(r'cmd /k chaosUpdater.bat')
    exit()

@client.command()
async def crash():
    await client.say('Did u really think that would work?')
    await client.say('https://cdn.discordapp.com/attachments/554733032121303063/554782439642497054/SqfNnjn.jpg')

@client.command()
async def hai():
    await client.say('Hallo!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
        
    print(output)  
    await client.say(output)

@client.command()
async def wat():
    await client.say('Nani the fuck??')

@client.command(pass_context=True)
@commands.has_role('Powah')
async def power(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.server.roles, name = 'Powah')#discord.utils.get(server.roles, name = 'Powah')
        
    await client.add_roles(member, role)

@client.command()
async def eightball(*args):
    randResponse = random.randint(0, 8)

    ball = open('8ball.txt')
    for i, line in enumerate(ball):
        if i == randResponse:
            responseR = line
            response = responseR[:-1]
    sleep(2)
    await client.say(response)

@client.command()
async def hentaibomb():
    randResponse = random.randint(0, (file_len('nadekoResponse.txt')))
    print(randResponse)
    
    rF = open('nadekoResponse.txt')
    for i, line in enumerate(rF):
        if i == randResponse:
            responseR = line         
            response = responseR[:-1]
        if randResponse == 0:
            response = '<@234383548985901057> Why did you ask for this?'
            
    sleep(2)        
    await client.say(response)


@client.command()
async def compliment(*args):
    #compiles the target's name
    target = ''
    for word in args:
        target += word
        target += ' '
       
    await client.say('No compliments here, ' + target + ', only fire')

@client.command()
async def wink():
    await client.say(':raised_back_of_hand:    :raised_back_of_hand:')
    await client.say(':clap: :clap: :clap: :clap: :clap: :clap: :clap: ')

@client.command()
async def moan():
    await client.say('https://cdn.discordapp.com/attachments/554733032121303063/556018226673352715/shake.gif')
    await client.say('Just for u senpai:')
    await client.say('https://discordapp.com/channels/540286718549688332/540287841721122826/564996910814068737')

@client.command()
async def roast(*args):
    #compiles the target's name
    target = ''
    for word in args:
        target += word
        target += ' '

    #finds random words
    randAdj = random.randint(1,(file_len('adjectives.txt')))
    randMod = random.randint(1,(file_len('adjectives.txt')))
    randNoun = random.randint(1,(file_len('nouns.txt')))

    #gets adjectives
    adjF = open('adjectives.txt')
    for i, line in enumerate(adjF):
        if i == randAdj:
            adjR = line
            adj = adjR[:-1]
        if i == randMod:
            modR = line
            mod = modR[:-1]
    adjF.close()

    #gets noun
    nounF = open('nouns.txt')
    for i, line in enumerate(nounF):
        if i == randNoun:
            nounR = line
            noun = nounR[:-1]
    nounF.close
    
    #relays the insult
    await client.say(target + ', you are one ' + adj + ' ' + mod + ' ' + noun)

@client.command()
async def joke():
    #grabs and reads the html code for the website
    uClient = uReq(dadJokes)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    rawJoke = page_soup.findAll("div",{"class":"JokesJoke"})
    print(rawJoke)
    for x in rawJoke:
        text_container = x.findAll("div", {"class":"text"})
        print(text_container)
        #textList = text_container[0].text
        

@client.command()
async def laundry(building, status_input):
    
    if building == 'Peterson':
        #open connection, grab the page
        uClient = uReq(Peterson)
        page_html = uClient.read()
        uClient.close()
    elif building == 'Palmerton':
        #open connection, grab the page
        uClient = uReq(Palmerton)
        page_html = uClient.read()
        uClient.close()
        

    #html parsing
    page_soup = soup(page_html, "html.parser")

    if status_input == 'Available':
        #grabs each machine that is ready
        MachineList = page_soup.findAll("tr",{"class":"MachineReadyMode"}) + page_soup.findAll("tr",{"class":"MachineDoorOpenReadyMode"})
        
    elif status_input == 'End':
        #grabs finished machines
        MachineList = page_soup.findAll("tr",{"class":"MachineEndOfCycleMode"})
        
    elif status_input == 'Running':
        #grabs running machines
        MachineList = page_soup.findAll("tr",{"class":"MachineRunMode"}) + page_soup.findAll("tr",{"class":"MachineRunModeAlmostDone"})

    allMachines = ''
    for machine in MachineList:
        text = machine.td.text

        status_container = machine.findAll("td", {"class":"status"})
        status = status_container[0].text

        time_container = machine.findAll("td", {"class":"time"})
        time = time_container[0].text

        allMachines += text
        
        if status_input == 'Running':
            allMachines += ': '
            allMachines += time
           
           
        allMachines += ', '


    await client.say(allMachines)

    
client.run(TOKEN)



#old commands
'''


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))'''
