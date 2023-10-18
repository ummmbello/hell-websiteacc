import re, os, asyncio, random, string
from discord.ext import commands, tasks

user_token = os.environ['token']
spam_id = "959021150585896970"

client = commands.Bot(command_prefix= '.' )
intervals = [2.4, 2.8]

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],7)*3))

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()
      
@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')

from flask import Flask
from threading import Thread
app = Flask('')

@app.route('/')
def main():
  return "Spammer is Alive!"
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
  server = Thread(target=run)
  server.start()
  
print(f'Made by CoolName')
keep_alive()
client.run(f"{user_token}")