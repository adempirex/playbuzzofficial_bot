import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import ChatJoinRequest

# Load token securely from environment variable
API_TOKEN = os.getenv("BOT_TOKEN")

# 🔐 Token check (important!)
if not API_TOKEN:
    raise ValueError("❌ BOT_TOKEN is missing! Make sure it is set in Railway environment variables.")

# Bot and dispatcher setup
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.chat_join_request()
async def approve_and_send_custom_message(join_request: ChatJoinRequest):
    try:
        await join_request.approve()
        await bot.send_message(
            chat_id=join_request.from_user.id,
            text=(
                "<b>✅ Playbuzz.club</b>\n"
                "<i>Top Rated International Betting Site</i>\n\n"
                "📽️ <b>How To Register</b> - https://t.me/PlayBuzzVideos/5\n\n"
                "🔗 <b>Register Link</b> - <a href='http://www.Playbuzz.club'>www.Playbuzz.club</a>\n"
                "🔗 <b>Register Link</b> - <a href='http://www.Playbuzz.club'>www.Playbuzz.club</a>\n\n"
                "♠️ <b>Bonus Details</b> ♠️\n"
                "✅ 12% Bonus On First Deposit\n"
                "✅ 06% Bonus Every Time\n\n"
                "🔗 <b>Link</b> - <a href='http://www.Playbuzz.club'>www.Playbuzz.club</a>\n\n"
                "💬 <b>Whatsapp Id Contact</b> 👇\n"
                "🔹 https://wa.link/playbuzz_official\n"
                "🔹 https://wa.link/playbuzz_official\n"
                "🔹 https://wa.link/playbuzz_official\n\n"
                "📞 <b>Customer Care</b> - https://wa.link/playbuzzcare"
            )
        )
        print(f"✅ Approved: {join_request.from_user.full_name}")
    except Exception as e:
        print(f"❌ Error: {e}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
