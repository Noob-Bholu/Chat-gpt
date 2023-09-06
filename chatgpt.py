
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging

FORMAT = "[NOOB-BHOLU] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
𝐇ᴇʏ, 𝐈 𝐀ᴍ {BOT_NAME}
➻ 𝐀ɴ 𝐎ᴘᴇɴ-𝐀ɪ-𝐁ᴀsᴇᴅ 𝐂ʜᴀᴛɢᴘᴛ.
──────────────────
𝐈 𝐀ᴍ 𝐀ᴅᴠᴀɴᴄᴇ 𝐁ᴏᴛ 𝐀ɴᴅ 𝐂ᴀɴ 
𝐀ɴsᴡᴇʀ 𝐘ᴏᴜʀ 𝐀ɴʏ 𝐐ᴜᴇsᴛɪᴏɴ 𝐄ᴀsʟɪʏ


๏ 𝐓ᴏ 𝐆ᴇᴛ 𝐇ᴇʟᴘ 𝐔sᴇ /help
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ 𝐇ᴇʏ, 𝐈 𝐀ᴍ [{BOT_NAME}]
➻ 𝐀ɴ 𝐎ᴘᴇɴ-𝐀ɪ-𝐁ᴀsᴇᴅ 𝐂ʜᴀᴛɢᴘᴛ.
──────────────────
𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐓ʜᴇ 𝐒ᴏᴜʀᴄᴇ 𝐂ᴏᴅᴇ
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text=" 𝐃ᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text=" 𝐒ᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐔ʀ 𝐆ʀᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" 𝐇ᴇʟᴘ & 𝐂ᴍᴅs ", callback_data="HELP"),
        InlineKeyboardButton(text=" 𝐔ᴘᴅᴀᴛᴇs ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]
X = [
    [
        InlineKeyboardButton(
            text="𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐔ʀ 𝐆ʀᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" 𝐃ᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/{OWNER_USERNAME}"),
        
        InlineKeyboardButton(text=" 𝐒ᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
     [
         InlineKeyboardButton(text=" 𝐃ᴇᴠᴇʟᴏᴘᴇʀ ",
                              url=f" https://t.me/{OWNER_USERNAME}"),
         InlineKeyboardButton(text=" 𝐒ᴜᴘᴘᴏʀᴛ ", 
                              url=f"https://t.me/{SUPPORT_GRP}"),
     ]
]

HELP_READ = "**➻ 𝐔sᴀɢᴇ** /ask <prompt>\n\n 𝐄xᴀᴍᴘʟᴇ: `/ask 𝐔sᴇ 𝐓ʜɪs 𝐓𝐨 𝐀sᴋ 𝐀ɴʏ 𝐐ᴜᴇsᴛɪᴏɴ 𝐓ᴏ 𝐌ᴇ`\n\n**➻ 𝐔sᴀɢᴇ** : /generate <prompt> \n𝐄xᴀᴍᴘʟᴇ: `/generate 𝐓ᴏ 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐀 𝐏ʜᴏᴛᴏ`  \n\n➻ 𝐔sᴀɢᴇ /lyrics : 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀ᴜᴅɪᴏ 𝐅ɪʟᴇ 𝐓ᴏ 𝐃ᴇᴛᴇᴄᴛ 𝐋ʏʀɪᴄꜱ**\n\n➻ 𝐔sᴀɢᴇ /ping 𝐓ᴏ 𝐂ʜᴇᴄᴋ 𝐓ʜᴇ 𝐏ɪɴɢ 𝐎ғ 𝐓ʜᴇ 𝐁ᴏᴛ.**\n\n©️ @Tricky_heaveN**"
HELP_BACK = [
     [
           InlineKeyboardButton(text="𝐐ᴜᴇꜱᴛɪᴏɴ 𝐓ʜᴀᴛ 𝐂ʜᴀᴛɢᴘᴛ 𝐂ᴀɴ 𝐒ᴏʟᴠᴇ ", url=f"https://t.me/intangible_fed/1066"),
           
     ],
    [
           InlineKeyboardButton(text=" 𝐁ᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("𝐏ɪɴɢ 𝐏ᴏɴɢ 𝐒ᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )

#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ριиgιиg..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ριиgιиg.....")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"𝐇ᴇʏ !!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) 𝐈ꜱ 𝐀ʟɪᴠᴇ 𝐀ɴᴅ 𝐖ᴏʀᴋɪɴɢ 𝐅ɪɴᴇ 𝐖ɪᴛʜ 𝐏ɪɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**𝐌ᴀᴅᴇ 𝐖ɪᴛʜ 🖤 𝐁ʏ || [𝐑ᴀʜᴜʟ](https://t.me/itzme_dear)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/ask 𝐖ʜᴀᴛ 𝐈s 𝐌ᴀᴛʜᴇᴍᴀᴛɪᴄs?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"➥ {message.from_user.first_name} 𝐀ꜱᴋᴇᴅ:\n\n {a} \n\n➥ {BOT_NAME} 𝐀ɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n➥ 𝐓ɪᴍᴇ 𝐓ᴀᴋᴇɴ  {telegram_ping} \n\n➥ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ @Tricky_heaveN 🖤", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**𝐄ʀʀᴏʀ: {e} \n\n➥ 𝐑ᴇᴘᴏʀᴛ 𝐇ᴇʀᴇ:- @Tricky_heaveN")

#  bard 

'''bard = Bard(token=BARD_TOKEN)   
@Mukesh.on_message(filters.command("bard"))
async def bard_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n` /bard How r u? `")
        else:
            a = message.text.split(' ', 1)[1]
            response=bard.get_answer(f"{a}")["content"]
            await message.reply_text(f"{response}\n\n➥ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Tricky_heaveN ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**𝐄ʀʀᴏʀ:  {e} ")

    '''
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["image","photo","img","gen"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**Example:**\n\n`/gen 𝐓ᴏ 𝐆ᴇɴᴀʀᴀᴛᴇ 𝐘ᴏᴜʀ 𝐃ᴇsɪʀᴇᴅ 𝐏ɪᴄᴛᴜʀᴇ`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"➥ 𝐓ɪᴍᴇ 𝐓ᴀᴋᴇɴ {telegram_ping} \n\n➥ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ:- @Tricky_heaveN ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} ` \n\n➥ 𝐑ᴇᴘᴏʀᴛ 𝐇ᴇʀᴇ:- @Tricky_heaveN ")
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["text","audiototext","lyrics"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message and message.reply_to_message.media:
            
            m = await message.reply_to_message.download(file_name="rahul.mp3")
            audio_file = open(m, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            x=transcript["text"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"`{x}` \n➥ 𝐓ɪᴍᴇ 𝐓ᴀᴋᴇɴ {telegram_ping} \n\n➥ 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ:- @UNKNOWN_CRITERIA_RK")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")



s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()

if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} 𝐈s 𝐀ʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @Tricky_heaveN
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
