import nextcord
from nextcord.ext import commands
import time
import os
import asyncio
import nextcord.ui
from nextcord.ui import View, Select
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents) 
@client.event
async def on_ready():
    print("The bot is now ready for use.")
    try: 
     synced = await client.tree.sync()
     print(f"Synced {len(synced)} command(s).")
    except Exception as e:
      print(e)
# Commands

interaction = nextcord.Interaction

@client.slash_command()
async def commands(interaction):
    await interaction.response.send_message('''**/commands** - Shows the list of commands.
    **/calc** - Calculates a mathematical expression.
    **/pop1** - Pop thingy for computer.
    **/pop2** - Pop thingy for phone.
    **/todayshistory** - Shows famous historical events of your entered day.
    **/todaysholiday** - Shows the holidays of your entered day.
    **/reminder** - Sets a reminder.(recommend using for shorter periods of time.)
    ''')
@client.slash_command()
async def calc(interaction, expression: str):
  result = eval(expression)
  await interaction.response.send_message(result)

@client.slash_command()
async def pop1(interaction):
  embed = nextcord.Embed(description = "||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||")
  await interaction.response.send_message(embed=embed)

@client.slash_command()
async def pop2(interaction):
  embed = nextcord.Embed(description = "||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop|| ||pop||")
  await interaction.response.send_message(embed=embed)

@client.slash_command()
async def todayshistory(interaction, month_in_text: str, date: str):
  await interaction.response.send_message(f"https://history.com/this-day-in-history/day/{month_in_text}-{date}")

@client.slash_command()
async def todaysholiday(interaction, month_in_text: str, date: str):
  await interaction.response.send_message(f"https://nationaltoday.com/{month_in_text}-holidays/#{month_in_text[0:3]}-{date}")

@client.slash_command()
async def reminder(interaction, reminder_text: str, in_days: int, in_hours: int, in_minutes: int, in_seconds: int):
    await interaction.response.send_message(f"I will remind you for `{reminder_text}` in `{in_days} days, {in_hours} hours, {in_minutes} minutes, {in_seconds} seconds`")
    unix_time = 0
    in_days = in_days * 86400
    in_minutes = in_minutes * 60
    in_hours = in_hours * 3600
    unix_time = in_seconds + in_days + in_hours + in_minutes
    await asyncio.sleep(unix_time)
    embed = nextcord.Embed(title=f"Reminder for {interaction.user.name}", description=reminder_text)
    await  interaction.followup.send(interaction.user.mention, embed=embed)

class MySelect_aboutme(View): 
  role_names = ["","He/Him","She/Her","They/Them","Any/Neo-Pronouns","12-13","14-15","16-17","18+","Active","Inactive","Poll","Server Poll","Role Updates","Bot Updates","Single","Taken","Reserved/Interested",'''“It’s Confusing”''']
  @nextcord.ui.select(placeholder="Select your about me roles!",
      options=[
        nextcord.SelectOption(label=role_names[1], value="1"), 
        nextcord.SelectOption(label=role_names[2], value="2"),
        nextcord.SelectOption(label=role_names[3], value="3"),
        nextcord.SelectOption(label=role_names[4], value="4"),
        nextcord.SelectOption(label=role_names[5], value="5"),
        nextcord.SelectOption(label=role_names[6], value="6"),
        nextcord.SelectOption(label=role_names[7], value="7"),
        nextcord.SelectOption(label=role_names[8], value="8"),
        nextcord.SelectOption(label=role_names[9], value="9"),
        nextcord.SelectOption(label=role_names[10], value="10"),
        nextcord.SelectOption(label=role_names[11], value="11",description="Get notified for polls."),
        nextcord.SelectOption(label=role_names[12], value="12",description="Get notified for server related polls."),
        nextcord.SelectOption(label=role_names[13], value="13",description="Get notified for role updates."),
        nextcord.SelectOption(label=role_names[14], value="14",description="Get notified for bot updates."),
        nextcord.SelectOption(label=role_names[15], value="15"),
        nextcord.SelectOption(label=role_names[16], value="16"),
        nextcord.SelectOption(label=role_names[17], value="17"),
        nextcord.SelectOption(label=role_names[18], value="18"),
            ])
  async def select_callback(self, select, interaction):
    select.disabled=False
    role_names = ["","He/Him","She/Her","They/Them","Any/Neo-Pronouns","12-13","14-15","16-17","18+","Active","Inactive","Poll","Server Poll","Role Updates","Bot Updates","Single","Taken","Reserved/Interested",'''“It’s Confusing”''']
    if select.values:
      for value in select.values:
          role_index = int(value)
          role = nextcord.utils.get(interaction.guild.roles, name=role_names[role_index])
          if role:
              await interaction.user.add_roles(role)
              await interaction.response.send_message(f"You have been given the {role.name} role!", ephemeral=True)
          else:
              await interaction.response.send_message(f"The {role.name} role was not found.", ephemeral=True) 
@client.slash_command()
async def aboutme_roles(interaction):
  View = MySelect_aboutme()
  await interaction.response.send_message(view=View)

class MySelect_custom(View): 
  role_names = ["","Author","Musician","Gamer","Artist","Calculator","Gamble","Therapist","Camouflage","Cookie Role","Genius","Haha Funny","Mosh Pit","Music Addict","Probably Horny","Rainbow Squad","Soldier","Smart Dumbass","Sugar Whore","Twink","Weeb"]
  @nextcord.ui.select(placeholder="Select your custom roles!",    
      options=[
        nextcord.SelectOption(label=role_names[1], value="1"), 
        nextcord.SelectOption(label=role_names[2], value="2"),
        nextcord.SelectOption(label=role_names[3], value="3"),
        nextcord.SelectOption(label=role_names[4], value="4"),
        nextcord.SelectOption(label=role_names[5], value="5"),
        nextcord.SelectOption(label=role_names[6], value="6"),
        nextcord.SelectOption(label=role_names[7], value="7"),
        nextcord.SelectOption(label=role_names[8], value="8"),
        nextcord.SelectOption(label=role_names[9], value="9"),
        nextcord.SelectOption(label=role_names[10], value="10"),
        nextcord.SelectOption(label=role_names[11], value="11"),
        nextcord.SelectOption(label=role_names[12], value="12"),
        nextcord.SelectOption(label=role_names[13], value="13"),
        nextcord.SelectOption(label=role_names[14], value="14"),
        nextcord.SelectOption(label=role_names[15], value="15"),
        nextcord.SelectOption(label=role_names[16], value="16"),
        nextcord.SelectOption(label=role_names[17], value="17"),
        nextcord.SelectOption(label=role_names[18], value="18"),
        nextcord.SelectOption(label=role_names[19], value="19"),
        nextcord.SelectOption(label=role_names[20], value="20")
            ])
  async def select_callback(self, select, interaction):
    select.disabled=False
    role_names = ["","Author","Musician","Gamer","Artist","Calculator","Gamble","Therapist","Camouflage","Cookie Role","Genius","Haha Funny","Mosh Pit","Music Addict","Probably Horny","Rainbow Squad","Soldier","Smart Dumbass","Sugar Whore","Twink","Weeb"]
    if select.values:
      for value in select.values:
          role_index = int(value)
          role = nextcord.utils.get(interaction.guild.roles, name=role_names[role_index])
          if role:
              await interaction.user.add_roles(role)
              await interaction.response.send_message(f"You have been given the {role.name} role!", ephemeral=True)
          else:
              await interaction.response.send_message(f"The {role.name} role was not found.", ephemeral=True) 
@client.slash_command()
async def custom_roles(interaction):
  View = MySelect_custom()
  await interaction.response.send_message(view=View)

@client.slash_command()
async def remove_role(interaction, role_name: str):
  role = nextcord.utils.get(interaction.guild.roles, name=role_name)
  if role:
   await interaction.user.remove_roles(role)
   await interaction.response.send_message(f"The {role_name} role has been removed.", ephemeral=True)
  else:
    await interaction.response.send_message(f"The {role_name} role was not found or I do not have access to it.", ephemeral=True)


  
# Events
@client.event
async def on_message_delete(message):
  if message.guild.id == 962547827655995463:
   channel = client.get_channel(1178597348713168936)
  elif message.author.id == 408785106942164992:
    return
  elif message.author.id == 270904126974590976:
    return
  embed = nextcord.Embed(title=f"{message.author.display_name} deleted:", description=f'''{message.content}'''
 f'''

In: {message.channel.name}
Time: <t:{int(time.time())}:f>''', color=0x8c214)
  await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):
  if message_before.content == nextcord.StickerFormatType.gif:
    return
  elif "https" in message_before.content:
    return
  elif message_before.author.id == 408785106942164992:
    return
  elif message_before.author.id == 270904126974590976:
    return
  channel = client.get_channel(1178597439566008381)
  embed = nextcord.Embed(title=f"{message_before.author.display_name} edited:", description=f'''"{message_before.content}"
  to
"{message_after.content}"'''
 f'''

In: {message_before.channel.name}
Time: <t:{int(time.time())}:f>''', color=0x8c214)
  await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    channel = client.fetch_channel(1178597711960883212)
    if member.guild.id == 962547827655995463 :
      channel = client.fetch_channel(1178597711960883212 )
    embed = nextcord.Embed(description=f"**{member.mention} left the server**\n\nTime: <t:{int(time.time())}:R>\nUser Id: {member.id}", color=0xe74c3c)
    await channel.send_message(embed=embed)

@client.event
async def on_member_join(member):
    channel = client.fetch_channel(1178597711960883212)
    if member.guild.id == 962547827655995463 :
      channel = client.fetch_channel(1178597711960883212 )
    embed = nextcord.Embed(description=f"**{member.mention} joined the server!**\n\nTime: <t:{int(time.time())}:R>\nUser Id: {member.id}", color=0x8c214)
    await channel.send(embed=embed)


client.run("MTA3NzQ1MDgyNTQ2NDU2NTgwMA.G7hLMM.KjyQvvntH7oC0dVJYzgZqvSEk7lXZo-1VxmAb8")
