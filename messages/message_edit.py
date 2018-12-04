import discord
from my_token import TOKEN, SERVER_ID

client = discord.Client()


client_messages = []

@client.event
async def on_ready():
  print("Bot ready with messages::message_edit")
  await client.change_presence(game=discord.Game(name="messages::message_edit"))



@client.event
async def on_message(message):
  if(len(message.mentions) > 0):
    for msg in client.messages:
      print(msg.content)
    return

  if(message.author == client.user):
    if(message.content.startswith("editting...")):
      return
    client_messages.append(message)
  else:
    if(message.content.startswith("!edit")):
      msg = await client.send_message(discord.Object(id = SERVER_ID), "editting...")
      for message in client_messages:
        await client.edit_message(message, new_content="Ye XD")
      await client.edit_message(msg, new_content="editting... finished!")
    else:
      await client.send_message(discord.Object(id = SERVER_ID), message.content)
    

client.run(TOKEN)

