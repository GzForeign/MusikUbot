import asyncio
from pytgcalls import idle
from config import call_py, bot


async def main():
    print("MEMULAI UBOT CLIENT")
    await bot.start()
    print("MEMULAI PYTGCALLS CLIENT")
    await call_py.start()
    print(
        """
    ------------------------
   | MusikUbot Aktif! |
    ------------------------
"""
    )
    await idle()
    await pidle()
    print("UBOT BERHENTI")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
