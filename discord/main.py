import os

import discord
from dotenv import load_dotenv


# Intent Configuration
# intents = discord.Intents(messages=True)
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True


# Client Configuration
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


# Bot Configuration
bot = discord.Bot(intents=intents)
# bot = discord.Bot(intents=discord.intents.message_content())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="say hello")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

# Waiting for user response
@bot.command()
async def gtn(ctx):
    """
    A Game
    """
    await ctx.respond("Guess: ")
    guess = await bot.wait_for('message', check=lambda msg: msg.author == ctx.author)
    print(guess.content, guess)
    if guess.content == "...":
        await ctx.send(f"{guess.content} you too")
    else:
        await ctx.send(f"No thank you, {guess.content}")


if __name__ == "__main__":    
    load_dotenv('.env')

    TOKEN = os.getenv("TOKEN")
    APP_ID = os.getenv("APP_ID")
    PUB_KEY = os.getenv("PUBLIC_KEY")

    # Client
    # client = MyClient(intents=intents)
    # client.run(TOKEN)

    # Bot
    bot.run(TOKEN)

