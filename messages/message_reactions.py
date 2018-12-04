import discord
from my_token import TOKEN, SERVER_ID

client = discord.Client()

@client.event
async def on_ready():
  print("Bot ready with messages::message_reactions")
  await client.change_presence(game=discord.Game(name="messages::message_reactions"))

@client.event
async def on_reaction_add(reaction, user):
  await client.send_message(discord.Object(id = SERVER_ID), f"user {user.name} reacted with {reaction.emoji} for message {reaction.message.content}")

@client.event
async def on_reaction_remove(reaction, user):
  await client.send_message(discord.Object(id = SERVER_ID), f"user {user.name} removed reaction {reaction.emoji} from message {reaction.message.content}")

client.run(TOKEN)
