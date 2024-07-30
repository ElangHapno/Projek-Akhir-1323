import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!! bot is ready, I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    # kode untuk bot menerima gambar
    if ctx.message.attachments: 
        for file in ctx.message.attachments: 
            file_name = file.filename 
            file_url = file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=f'./{file.filename}')
            
            # kode untuk memproses gambar (ubah dengan melihat labels.txt)
            if hasil[0] == 'Dampak Buruk bagi Daratan\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah Dampak-dampak Buruk bagi Daratan')
                await ctx.send('ini menunjukkan beberapa Sifat yang dapat menghancurkan Lingkungan Daratan,')
                await ctx.send('Bahkan termasuk Makhluk Hidup seperti Manusia, yakni Kita')
                await ctx.send('Sifat ini bisa saja tidak berbahaya')
                await ctx.send('Tetapi jika kita tidak memperdulikanya, maka sifat ini sangat mematikan!')
            elif hasil[0] == 'Dampak Baik bagi Daratan\n' and hasil[1] >= 0.65:
                await ctx.send('ini menunjukkan beberapa Sifat yang dapat memperbaiki Lingkungan Daratan')
                await ctx.send('Sifat ini WAJIB kita lakukan agar Menjaga Kebersihan Lingkungan Daratan Kita')
                await ctx.send('Jadi Ayo Kita Membersihkan Seluruh Lingkungan Kotor sekitar kita!')
            elif hasil[0] == 'Dampak Buruk bagi Udara\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah Dampak-dampak Buruk bagi Udara')
                await ctx.send('ini menunjukkan beberapa Sifat yang dapat merusak Udara,')
                await ctx.send('Bahkan termasuk Makhluk Hidup seperti Manusia, yakni Kita')
                await ctx.send('Sifat ini mungkin saja tanpa kita sadari telah terbiasa melakukannya berkali-kali')
                await ctx.send('Tetapi Sifat ini Menyebabkan Populasi,')
                await ctx.send('bisa menimbulkan Bahaya banyak orang maupun dirinya sendiri yang melakukannya,')
                await ctx.send('Dan ini penyebabnya Global Warming!')
            elif hasil[0] == 'Dampak Baik bagi Udara\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah Dampak-dampak Baik bagi Udara')
                await ctx.send('ini menunjukkan Jika melestarikan Udara')
                await ctx.send('Terbebas dari Populasi dan Asap Rokok/Vape')
                await ctx.send('Jadi berhentilah Merokok (perlahan-perlahan) agar menghindari Kecanduan merokok dan lestarikan udara!')
            elif hasil[0] == 'Dampak Buruk bagi Lautan\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah Dampak-dampak Buruk bagi Lautan')
                await ctx.send('ini menunjukkan beberapa Sifat yang dapat merusak Lautan,')
                await ctx.send('Ini membuat Makhluk hidup di lautan bisa mati')
                await ctx.send('dan Sifat ini biasanya tidak manusiawi')
                await ctx.send('Pelaku-pelaku yang melakukan hal tersebut harus ditindak!')
            elif hasil[0] == 'Dampak Baik bagi Lautan\n' and hasil[1] >= 0.65:
                await ctx.send('ini adalah Dampak-dampak Baik bagi Lautan')
                await ctx.send('ini menunjukkan Jika menjaga lautan serta penghuninya')
            else:
                await ctx.send('GAMBAR MU KEMUNGKINAN TIDAK KAITANNYA DENGAN SIFAT-SIFATNYA TERSEBUT')
                await ctx.send('KIRIM GAMBAR BARU!')
    else:
        await ctx.send('GAMBAR TIDAK VALID/GAADA')


bot.run("TOKEN")