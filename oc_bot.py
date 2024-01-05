import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def create_course(ctx, course_name:str):
    # Create a new role
    course_name = course_name.upper()

    purple_color = discord.Colour.purple()  
    new_role = await ctx.guild.create_role(name=course_name, color=purple_color)
    await ctx.send(f'Role `{new_role.name}` has been created.')

    # Find the category named "Course Help"
    category = discord.utils.get(ctx.guild.categories, name="Course Help")
    if category is None:
        await ctx.send("Category 'Course Help' not found.")
        return

    # Create a new text channel
    new_channel = await ctx.guild.create_text_channel(name=course_name, category=category)
    await ctx.send(f'Channel `{new_channel.name}` has been created.')


#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    print("Detected a message")
#
#    content = message.content
#    channel = message.channel.name
#    author  = message.author.name
#
#    print(f'Channel: {channel}.\nAuthor: {author}.\nContent: "{content}"')
#
#    if content.startswith('$hello'):
#        await message.channel.send('Hello!')



client.run('MTE4NDIyMTcxMTMxMTMxMDg1MQ.G3LTSj.K7dPwiX8wfTTzoJhi4RQ5EFhkzxogFtmZDyLkM')
