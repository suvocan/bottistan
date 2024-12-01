import discord
import random
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.


@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def atık(ctx):
    await ctx.send("Hangi maddenin doğada ne kadar sürede kaybolduğunu öğrenmek istersin? (kelimeler: plastik, kağıt, tişört, cam şişe)")

    # Kullanıcıdan cevap bekler
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
        
        msg = await bot.wait_for("message", check=check, timeout=30.0)
        cevap = msg.content.lower()
        
        if cevap == "plastik":
            await ctx.send("450 yıl")
        elif cevap == "kağıt":
            await ctx.send("2-5 ay")
        elif cevap == "tişört":
            await ctx.send("50-100 yıl")
        elif cevap == "cam şişe":
            await ctx.send("4000 yıl")
        else:
            await ctx.send("Kelimeyi doğru yazdığınızdan emin olun.")

# Çevre dostu görevler
@bot.command()
async def cevre_gorevi(ctx):
    gorevler = [
        "Bugün 10 dakika boyunca dışarıda çöpleri topla! ♻️",
        "Evde plastik yerine kağıt kullanmaya çalış! 📜",
        "Kompost yapmak için eski yemekleri sakla! 🥕"
    ]
    gorev = random.choice(gorevler)
    await ctx.send(f"Bugünün çevre görevi: {gorev}")   

bot.run(add token)
