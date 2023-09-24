from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""📟¦اهلا بـك عزيـزي 📬 {msg.from_user.mention},
🖱 ¦ يـمكنك استـخـراج الـتـالـي 📥
📟 ¦ تيرمـكـس تليثون للحسـابـات 🥷
📡 ¦ تيرمـكـس تليثون للبوتــات 🎭
🎸 ¦ بايـروجـرام مـيوزك للحسابات 🥷
🔮 ¦ بايـروجـرام مـيوزك للبوتات 🎭
🔗 ¦ بايـروجـرام مـيوزك احدث اصدار 📀

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت

بواسطـة : [𓏺 •𝐾 𝐺•™ 𝙇𝙚𝘼𝙙𝙀𝙧 ™⤶ .](tg://user?id=5593884330) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📥 ⍆ اضغط لبدا استخراج كود ⍅ 📥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" 📡 الــســــوࢪس", url="https://t.me/V_P_N_8 "),
                    InlineKeyboardButton("𓏺 •𝐾 𝐺•™ 𝙇𝙚𝘼𝙙𝙀𝙧 ™⤶ .", user_id=5593884330)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
