import discord

client = discord.Client()

@client.event
async def on_ready():
    print("꿀값봇이 성공적으로 실행되었습니다.")
    game = discord.Game('노아공식총판샵 꿀값공유 하는중 by 고스트#1234')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!꿀값 위도우":
        embed = discord.Embed(title='위도우 꿀값', description='```! FOV : 250 / SPEED : 0.38 / PITCH : 0.25 ```', colour=discord.Colour.green())
        await message.channel.send(embed=embed)
        
    if message.content == "!꿀값 트레":
        embed = discord.Embed(title='트레이서 꿀값', description='```! FOV : 250 / SPEED : 0.08 / PITCH : 0.42 ```', colour=discord.Colour.green())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 맥크리":
        embed = discord.Embed(title='맥크리 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 겐지":
        embed = discord.Embed(title='겐지 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 한조":
        embed = discord.Embed(title='한조 꿀값', description='```! FOV : 250 / SPEED : 0.35 / PITCH : 0.32 ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 둠피":
        embed = discord.Embed(title='둠피 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 애쉬":
        embed = discord.Embed(title='애쉬 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 솔져":
        embed = discord.Embed(title='솔져 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 메이":
        embed = discord.Embed(title='메이 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 정크":
        embed = discord.Embed(title='정크 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 토르":
        embed = discord.Embed(title='토르 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 디바":
        embed = discord.Embed(title='디바 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

    if message.content == "!꿀값 자리야":
        embed = discord.Embed(title='자리야 꿀값', description='```꿀값 추가 준비중.. ```', colour=discord.Colour.red())
        await message.channel.send(embed=embed)

client.run("token")