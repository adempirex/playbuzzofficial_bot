from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatJoinRequest
from aiogram.utils import executor
import logging

API_TOKEN = '7520497210:AAER0NF8rP-cWcfGUuUzkM90Xr-I8JsZRuw'  # Replace if token changes

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
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
            ),
            parse_mode="HTML"
        )
        print(f"Approved: {join_request.from_user.full_name}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)