import discord, asyncio, datetime, pytz

client = discord.Client()

token = "ODYyMzcwNTcxOTA3MTA0Nzg4.YOXXLg.OoLgeDKodzrohw8xZxMCXQRiHIw"

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("보리 수확"))

@client.event
async def on_message(message):
    if message.content == "보리야": # 메세지 감지
        await message.channel.send ("보리!!보리!!")
        await message.author.send ("안녕하세요 {} 님 보리봇입니다".format( message.author.mention))
        

    if message.content == "보리야 출첵":
        ch = client.get_channel(862660735121227776)
        await ch.send ("{},이가 출첵되었다보리!!".format(message.author.mention))


@client.event
async def on_message(message):
      if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="보리Bot", description="안녕하세요 보리봇입니다!! 보리빵드실래요?",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="보리봇 start day ",value="2021년도 7월10일", inline=False)

        embed.add_field(name="보리봇 기능",value="아직 할수있는게 없어요ㅠㅠ", inline=False)


        embed.set_footer(text="made_아싸#2140", icon_url="https://cdn.discordapp.com/attachments/862378917011521539/863138670211366932/4e2f3ec1058efac0.jpeg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/862378917011521539/863138670211366932/4e2f3ec1058efac0.jpeg")
        await message.channel.send (embed=embed)
# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run(token)
