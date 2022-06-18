import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)

@Client.on_message(filters.command(["gz"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.edit("Prot prot ngewe...")
   delta_ping = time() - start
   await m_reply.edit("0% ▒▒▒▒▒▒▒▒▒▒")
   await m_reply.edit("20% ██▒▒▒▒▒▒▒▒")
   await m_reply.edit("40% ████▒▒▒▒▒▒")
   await m_reply.edit("60% ██████▒▒▒▒")
   await m_reply.edit("80% ████████▒▒")
   await m_reply.edit("100% ██████████")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"**┞◈𝗣𝗼𝗻𝗴!!🦍**\n**┞◈Pinger**  - {delta_ping * 1000:.3f} ms \n**┞◈Uptime** - {uptime}")


@Client.on_message(filters.command(["gorzz"], prefixes=f"{HNDLR}"))
async def pong(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   pong = await m.edit("yamete kudasai...")
   delta_ping = time() - start
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏===◈❏◈")
   await pong.edit("❏====❏◈◈")
   await pong.edit("**◈AVVVVV PINGGGG!**")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await pong.edit(
       f"**❏MusicUbot**\n**❏NGENTOT** : {delta_ping * 1000:.3f} ms\n**❏Bot Uptime** : {uptime}")

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Musik Ubot Di Mulai Ulang**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>🥵 Ayang {m.from_user.mention}!

🛠 MENU BANTUAN PEMUTAR MUSIK

⚡ PERINTAH UNTUK SEMUA ORANG
• {HNDLR}play [judul lagu | link youtube | balas file audio] - untuk memutar lagu
• {HNDLR}videoplay [judul video | link youtube | balas file video] - untuk memutar video
• {HNDLR}playlist untuk melihat daftar putar
• {HNDLR}ping - untuk cek status
• {HNDLR}id - untuk melihat id pengguna
• {HNDLR}video - judul video | link yt untuk mencari video
• {HNDLR}song - judul lagu | link yt untuk mencari lagu
• {HNDLR}help - untuk melihat daftar perintah
• {HNDLR}join- untuk join | ke grup 

⚡ PERINTAH UNTUK SEMUA ADMIN
• {HNDLR}resume - untuk melanjutkan pemutaran lagu atau video
• {HNDLR}pause - untuk untuk menjeda pemutaran lagu atau video
• {HNDLR}skip - untuk melewati lagu atau video
• {HNDLR}end - untuk mengakhiri pemutaran</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>🥵 Ayang {m.from_user.mention}!

🗃️ Musik Dan Video Player UBot

🔰 Telegram UBot Untuk Memutar Lagu Dan Video Di Obrolan Suara Telegram.

🦍 Dipersembahkan Oleh 
• [Gorzz](https://t.me/teleidgz)

📝 Persyaratan
• Python 3.8+
• FFMPEG
• Nodejs v16+

[Repo MusikUbot](https://t.me/grzmusik)

📝 Variabel Yang Dibutuhkan
• `API_ID` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `SESSION` - Sesi String Pyrogram.
• `SUDO_USER` - ID Akun Telegram Yang Digunakan Sebagai Admin
• `HNDLR` - Handler untuk menjalankan ubot mu

"""
    await m.reply(REPO, disable_web_page_preview=True)
