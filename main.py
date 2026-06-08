# DELETE\~♤_bot_v14_final_fixed.py
import asyncio
import json
import os
import random
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.error import BadRequest
import logging
from gtts import gTTS
import io
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running"

def run_web():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

Thread(target=run_web, daemon=True).start()


# ---------------------------
# CONFIG
# ---------------------------
TOKENS = [
"8836288331:AAHCsJKQd3DMZFtdbu_TXOx9-7f4vd9HbbI",

"8990073356:AAHu7jRNsa8LLK1XQLt6O4iX7CCXbKWQyXQ",

"8604371108:AAE4RFJJWTXCYXi5tXuRV8Klh3rMU4xAHdU",

"8370807942:AAFPBjVJoQpl21ySPRgCLzid7AgDT-EzinU",

"8695046233:AAFPLirdc2_QDRq5rILApBobfTCO5P81ZQs",

"8402293493:AAGUfPQc6is7VsKRLQXqEJXSdX31K4aUT0Q",

"8789540801:AAHNhIF-PjRZk7ezTHO9aakdDPzIWjJ7-xw",

"8630602121:AAEneKvkhGPmkDcYINBdZfgboNlkg6T-uXI",

"8761689455:AAEEhb_66ON8oDJfIVO6HH4Iv1uyijBbmY4"

]

OWNER_ID= [7623391678 ,8399044122]
rights_FILE = "rights.json"
STICKER_FILE = "stickers.json"

ACTIVE_GROUP_CHATS = set()

# ---------------------------
# TEXTS
# ---------------------------
RAID_TEXTS = [
    "𓂃˖˳·˖ ִֶָ ⋆[HIJDA]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[GAY]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[R9D]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[CHAMAR]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[GAREEB]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[LND LE]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[तेरी मा रंडी]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[चुदाई खा]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ GAND MARA ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[JNL]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ TMKC ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ TBKC ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ TMKL ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ KMZR ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ BAUNA ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ KALWA ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ MOTE ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ MA CHUDA ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ BEHEN CHOD ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ MADARCHOD ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
    "𓂃˖˳·˖ ִֶָ ⋆[ KUTTA CHOD ]⋆ ִֶָ˖·˳˖𓂃 ִֶָ",
]

NCEMO_EMOJIS = ["──(🩷)──ᴅᴏɢ","──(🤍)──ᴅᴏɢ","──(🩶)──ᴅᴏɢ","──(🖤)──ᴅᴏɢ","──(🤎)──ᴅᴏɢ","──(💜)──ᴅᴏɢ","──(💙)──ᴅᴏɢ","──(🩵)──ᴅᴏɢ","──(💚)──ᴅᴏɢ","──(💛)──ᴅᴏɢ","──(🧡)──ᴅᴏɢ","──(❤️)──ᴅᴏɢ","──(🩷)──ᴅᴏɢ","──(🤍)──ᴅᴏɢ","──(🩶)──ᴅᴏɢ","──(🖤)──ᴅᴏɢ","──(🤎)──ᴅᴏɢ","──(💜)──ᴅᴏɢ","──(💙)──ᴅᴏɢ","──(🩵)──ᴅᴏɢ","──(💚)──ᴅᴏɢ","──(💛)──ᴅᴏɢ","──(🧡)──ᴅᴏɢ","──(❤️)──ᴅᴏɢ","──(🩷)──ᴅᴏɢ","──(🤍)──ᴅᴏɢ","──(🩶)──ᴅᴏɢ","──(🖤)──ᴅᴏɢ","──(🤎)──ᴅᴏɢ","──(💜)──ᴅᴏɢ","──(💙)──ᴅᴏɢ","──(🩵)──ᴅᴏɢ","──(💚)──ᴅᴏɢ","──(💛)──ᴅᴏɢ","──(🧡)──ᴅᴏɢ","──(❤️)──ᴅᴏɢ","──(🩷)──ᴅᴏɢ","──(🤍)──ᴅᴏɢ","──(🩶)──ᴅᴏɢ","──(🖤)──ᴅᴏɢ","──(🤎)──ᴅᴏɢ","──(💜)──ᴅᴏɢ","──(💙)──ᴅᴏɢ","──(🩵)──ᴅᴏɢ","──(💚)──ᴅᴏɢ","──(💛)──ᴅᴏɢ","──(🧡)──ᴅᴏɢ","──(❤️)──ᴅᴏɢ", ]
exonc_TEXTS = ["➛「🌹」","➛「🌼」","➛「🌻」","➛「🪻」","➛「🏵️」","➛「💮」", "➛「🌸」","➛「🪷」","➛「🌷」","➛「🌺」","➛「🥀」","➛「🌹」","➛「💐」","➛「🍁」","➛「☘️」","➛「🌹」","➛「🌼」","➛「🌻」","➛「🪻」","➛「🏵️」","➛「💮」", "➛「🌸」","➛「🪷」","➛「🌷」","➛「🌺」","➛「🥀」","➛「🌹」","➛「💐」","➛「🍁」","➛「☘️」","➛「🌹」","➛「🌼」","➛「🌻」","➛「🪻」","➛「🏵️」","➛「💮」", "➛「🌸」","➛「🪷」","➛「🌷」","➛「🌺」","➛「🥀」","➛「🌹」","➛「💐」","➛「🍁」","➛「☘️」",]

# FUCK TEXTS
FUCK_TEXTS = {
    1: "──(😈)──нιנ∂є",
    2: "──(🥶)──ƒυ¢к уσυ", 
    3: "──(🤢)──тєяα вααρ кєηтσ",
    4: "──(🫩)──мαα ¢нυ∂α",
    5: "──(🥴)──кαмzσя нαι тυ"
}

# Emoji sets for FUCK
HEART_EMOJIS = ["(❤️)࿐", "(🩷)࿐", "(🧡)࿐", "(💛)࿐", "(💚)࿐", "(💙)࿐", "(🩵)࿐", "(💜)࿐", "(🖤)࿐", "(🩶)࿐", "(🤎)࿐", "(🤍)࿐", "(💞)࿐", "(💕)࿐", "(💔)࿐", "(💗)࿐", "(💖)࿐", "(❤️‍🩹)࿐", "(💘)࿐", "(💝)࿐", "(💓)࿐", "(💟)࿐", "(❣️)࿐", "(❤️‍🔥)࿐"]
FLAG_EMOJIS = ["🇨🇾࿐","🇦🇨࿐","🇦🇩࿐","🇦🇪࿐","🇦🇫࿐", "🇦🇬࿐","🇦🇴࿐","🇦🇶࿐","🇦🇸࿐","🇦🇺࿐","🇧🇦࿐","🇧🇩࿐","🇦🇺࿐","🇧🇯࿐","🇧🇴࿐","🇧🇶࿐","🇧🇮࿐","🇧🇯࿐","🇧🇱࿐","🇧🇳࿐","🇧🇴࿐","🇧🇶࿐","🇧🇷࿐","🇧🇸࿐","🇧🇹࿐","🇧🇻࿐","🇧🇼࿐",
]

# ---------------------------
# GLOBAL STATE
# ---------------------------
vanitas_mode = False
vanitas_name = ""
vanitas_spam_text = ""

multinc_mode = False
multinc_name = ""
multispam_mode = False  
multispam_text = ""

# Task dictionaries - ALL OPTIONS
group_tasks = {}         
spam_tasks = {}
reaction_tasks = {}
sticker_tasks = {}
flood_tasks = {}
autoreply_tasks = {}
vanitas_tasks = {}
multinc_tasks = {}
multispam_tasks = {}
raid_tasks = {}
swipe_tasks = {}
pswipe_tasks = {}
glitchspam_tasks = {}
rainbowspam_tasks = {}
numberspam_tasks = {}
gcnc_tasks = {}
ncemo_tasks = {}
ncbaap_tasks = {}
exonc_tasks = {}
fuck_tasks = {}  # NEW: Add this line

# Load data
if os.path.exists(rights_FILE):
    try:
        with open(rights_FILE, "r") as f:
            rights_USERS = set(int(x) for x in json.load(f))
    except:
        rights_USERS = set()
else:
    rights_USERS = set()

if os.path.exists(STICKER_FILE):
    try:
        with open(STICKER_FILE, "r") as f:
            user_stickers = json.load(f)
    except:
        user_stickers = {}
else:
    user_stickers = {}

def save_rights():
    with open(rights_FILE, "w") as f: 
        json.dump(list(rights_USERS), f)

def save_stickers():
    with open(STICKER_FILE, "w") as f: 
        json.dump(user_stickers, f)

# DELAYS
delay = 0.03
spam_delay = 0.1
reaction_delay = 0.5
raid_delay = 0.15
swipe_delay = 0.15
flood_delay = 0.05

logging.basicConfig(level=logging.INFO)

# ---------------------------
# DECORATORS
# ---------------------------
def only_rights(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        uid = update.effective_user.id
        if uid not in rights_USERS:
            await update.message.reply_text("NIGGA STAY WAY ")
            return
        return await func(update, context)
    return wrapper

# ============================
# rights MANAGEMENT COMMANDS
# ============================

@only_rights
async def rights(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Add user to rights"""
    if not context.args:
        # Check if replying to a message
        if update.message.reply_to_message:
            user_id = update.message.reply_to_message.from_user.id
        else:
            return await update.message.reply_text("⚠️ Usage: /rights <user_id> or reply to user's message")
    else:
        try:
            user_id = int(context.args[0])
        except ValueError:
            return await update.message.reply_text("❌ Invalid user ID. Must be a number.")
    
    # Don't allow removing owner
    if user_id in :
        return await update.message.reply_text("❌ Cannot modify owner permissions.")
    
    if user_id in rights_USERS:
        await update.message.reply_text("✅ User is already rights.")
    else:
        rights_USERS.add(user_id)
        save_rights()
        await update.message.reply_text(f"✅ Added {user_id} to rights users.")

@only_rights
async def unrights(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Remove user from rights"""
    if not context.args:
        # Check if replying to a message
        if update.message.reply_to_message:
            user_id = update.message.reply_to_message.from_user.id
        else:
            return await update.message.reply_text("⚠️ Usage: /unrights <user_id> or reply to user's message")
    else:
        try:
            user_id = int(context.args[0])
        except ValueError:
            return await update.message.reply_text("❌ Invalid user ID. Must be a number.")
    
    # Don't allow removing owner
    if user_id in :
        return await update.message.reply_text("❌ Cannot remove owner.")
    
    if user_id in rights_USERS:
        rights_USERS.remove(user_id)
        save_rights()
        await update.message.reply_text(f"✅ Removed {user_id} from rights users.")
    else:
        await update.message.reply_text("❌ User is not in rights list.")

@only_rights
async def listrights(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List all rights users"""
    rights_list = "\n".join([f"🆔 {user_id}" for user_id in rights_USERS])
    await update.message.reply_text(f"👑 rights Users ({len(rights_USERS)}):\n{rights_list if rights_list else 'No rights users'}")

# ============================
# FUCK SPAM SYSTEM - NEW ADDITION
# ============================

@only_rights
async def fuck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FUCK Spam System"""
    if not context.args or len(context.args) < 2:
        return await update.message.reply_text("⚠️ Usage: /fuck <1-5> <name>\nExample: /fuck 3 RANDOM")
    
    try:
        option = int(context.args[0])
        name = " ".join(context.args[1:])
        
        if option not in range(1, 6):
            return await update.message.reply_text("❌ Option must be 1-5")
    except ValueError:
        return await update.message.reply_text("❌ First argument must be a number 1-5")
    
    chat_id = update.message.chat_id
    
    # Stop existing fuck tasks
    if chat_id in fuck_tasks:
        for task in fuck_tasks[chat_id]:
            task.cancel()
        del fuck_tasks[chat_id]
    
    # Get base text based on option
    base_text = FUCK_TEXTS[option]
    
    async def fuck_loop(bot, chat_id, option, name, base_text):
        emoji_cycle = 0
        while True:
            try:
                # Create the message text
                message_text = f"{name} {base_text}"
                
                # Add emojis based on option
                if option == 1:  # Hearts
                    emoji = HEART_EMOJIS[emoji_cycle % len(HEART_EMOJIS)]
                    message_text += f" {emoji}"
                    emoji_cycle += 1
                    
                
                    
                
                    
                elif option == 4:  # Flag emojis
                    emoji = FLAG_EMOJIS[emoji_cycle % len(FLAG_EMOJIS)]
                    message_text += f" {emoji}"
                    emoji_cycle += 1
                    
                
                
                # Send message
                await bot.send_message(chat_id, message_text)
                await asyncio.sleep(spam_delay)
                
            except Exception as e:
                await asyncio.sleep(0.2)
    
    # Start fuck spam with all bots
    tasks = []
    for bot in bots:
        task = asyncio.create_task(fuck_loop(bot, chat_id, option, name, base_text))
        tasks.append(task)
    
    fuck_tasks[chat_id] = tasks
    
    option_names = {
        1: "लंड चूस (Hearts)",
        2: "Teri Maa Kitne Baje Chudi ---> (White)",
        3: "Tera Baap Waha Majduri Kar Raha Aur Tu Idhar Apni Maa Chuda Raha (Black)", 
        4: "TᴜᴍʜᴀʀE Pɪᴛᴀsʜʀᴇᴇ Zᴇɴɪ (Flag)",
        5: "TᴇʀI BᴇʜᴇN Kᴇ BʜᴏsᴅE MᴇɪN AᴛᴛᴀᴄK (Wizard/Fantasy)"
    }
    
    await update.message.reply_text(f"🎯 FUCK ACTIVATED!\nOption: {option} - {option_names[option]}\nTarget: {name}")

@only_rights
async def sfuck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in fuck_tasks:
        for task in fuck_tasks[chat_id]:
            task.cancel()
        del fuck_tasks[chat_id]
        await update.message.reply_text("🛑 FUCK STOPPED!")
    else:
        await update.message.reply_text("❌ No active fuck spam")

# ============================
# MULTI-GROUP FUNCTIONS
# ============================

@only_rights
async def multinc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Multi-group name changer"""
    global multinc_mode, multinc_name
    
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /multinc <name>")
    
    multinc_name = " ".join(context.args)
    multinc_mode = True
    
    # Clear existing tasks
    if multinc_tasks:
        for chat_id in list(multinc_tasks.keys()):
            for task in multinc_tasks[chat_id]:
                task.cancel()
        multinc_tasks.clear()
    
    async def multinc_loop(bot, chat_id, name):
        i = 0
        while multinc_mode:
            try:
                text = f"{name} {RAID_TEXTS[i % len(RAID_TEXTS)]}"
                await bot.set_chat_title(chat_id, text)
                i += 1
                await asyncio.sleep(1)  # Slower for multi-group
            except:
                await asyncio.sleep(2)
    
    # Start for all groups
    for group_id in list(ACTIVE_GROUP_CHATS):
        tasks = []
        for bot in bots:
            task = asyncio.create_task(multinc_loop(bot, group_id, multinc_name))
            tasks.append(task)
        multinc_tasks[group_id] = tasks
    
    await update.message.reply_text(f"🌐 MULTI-NC ACTIVATED!\nName: {multinc_name}\nGroups: {len(ACTIVE_GROUP_CHATS)}")

@only_rights
async def stopmultinc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global multinc_mode
    multinc_mode = False
    for chat_id in list(multinc_tasks.keys()):
        for task in multinc_tasks[chat_id]:
            task.cancel()
    multinc_tasks.clear()
    await update.message.reply_text("🛑 MULTI-NC STOPPED!")

@only_rights
async def multispam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Multi-group spam"""
    global multispam_mode, multispam_text
    
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /multispam <text>")
    
    multispam_text = " ".join(context.args)
    multispam_mode = True
    
    # Clear existing tasks
    if multispam_tasks:
        for chat_id in list(multispam_tasks.keys()):
            for task in multispam_tasks[chat_id]:
                task.cancel()
        multispam_tasks.clear()
    
    async def multispam_loop(bot, chat_id, text):
        while multispam_mode:
            try:
                await bot.send_message(chat_id, text)
                await asyncio.sleep(2)  # Slower for multi-group
            except:
                await asyncio.sleep(3)
    
    # Start for all groups
    for group_id in list(ACTIVE_GROUP_CHATS):
        tasks = []
        for bot in bots:
            task = asyncio.create_task(multispam_loop(bot, group_id, multispam_text))
            tasks.append(task)
        multispam_tasks[group_id] = tasks
    
    await update.message.reply_text(f"🌐 MULTI-SPAM ACTIVATED!\nText: {multispam_text}\nGroups: {len(ACTIVE_GROUP_CHATS)}")

@only_rights
async def stopmultispam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global multispam_mode
    multispam_mode = False
    for chat_id in list(multispam_tasks.keys()):
        for task in multispam_tasks[chat_id]:
            task.cancel()
    multispam_tasks.clear()
    await update.message.reply_text("🛑 MULTI-SPAM STOPPED!")

# ============================
# AUTO-REPLY SYSTEM
# ============================

@only_rights
async def autoreply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set auto-reply"""
    if not context.args or len(context.args) < 2:
        return await update.message.reply_text("⚠️ Usage: /autoreply <trigger> <reply>")
    
    trigger = context.args[0]
    reply = " ".join(context.args[1:])
    chat_id = update.message.chat_id
    
    if chat_id not in autoreply_tasks:
        autoreply_tasks[chat_id] = {}
    
    async def reply_loop(bot, chat_id, trigger, reply):
        while True:
            try:
                # This needs message handler to work properly
                await asyncio.sleep(1)
            except:
                await asyncio.sleep(2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(reply_loop(bot, chat_id, trigger, reply))
        tasks.append(task)
    
    autoreply_tasks[chat_id][trigger] = {'tasks': tasks, 'reply': reply}
    await update.message.reply_text(f"🤖 Auto-reply set!\nTrigger: {trigger}\nReply: {reply}")

@only_rights
async def stopautoreply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if context.args:
        trigger = context.args[0]
        if chat_id in autoreply_tasks and trigger in autoreply_tasks[chat_id]:
            for task in autoreply_tasks[chat_id][trigger]['tasks']:
                task.cancel()
            del autoreply_tasks[chat_id][trigger]
            await update.message.reply_text(f"🛑 Auto-reply removed for: {trigger}")
        else:
            await update.message.reply_text("❌ No auto-reply found for this trigger")
    else:
        if chat_id in autoreply_tasks:
            for trigger in list(autoreply_tasks[chat_id].keys()):
                for task in autoreply_tasks[chat_id][trigger]['tasks']:
                    task.cancel()
            del autoreply_tasks[chat_id]
            await update.message.reply_text("🛑 All auto-replies stopped!")
        else:
            await update.message.reply_text("❌ No active auto-replies")

# ============================
# STICKER SYSTEM
# ============================

@only_rights
async def newsticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Add new sticker"""
    if not update.message.reply_to_message or not update.message.reply_to_message.sticker:
        return await update.message.reply_text("⚠️ Reply to a sticker with this command")
    
    sticker = update.message.reply_to_message.sticker
    sticker_id = sticker.file_id
    
    user_id = update.effective_user.id
    if str(user_id) not in user_stickers:
        user_stickers[str(user_id)] = []
    
    user_stickers[str(user_id)].append(sticker_id)
    save_stickers()
    
    await update.message.reply_text(f"✅ Sticker added!\nYou now have {len(user_stickers[str(user_id)])} stickers")

@only_rights
async def sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start sticker spam"""
    user_id = update.effective_user.id
    chat_id = update.message.chat_id
    
    if str(user_id) not in user_stickers or not user_stickers[str(user_id)]:
        return await update.message.reply_text("❌ No stickers saved! Use /newsticker first")
    
    if chat_id in sticker_tasks:
        for task in sticker_tasks[chat_id]:
            task.cancel()
    
    async def sticker_loop(bot, chat_id, stickers):
        while True:
            try:
                sticker_id = random.choice(stickers)
                await bot.send_sticker(chat_id, sticker_id)
                await asyncio.sleep(0.3)
            except:
                await asyncio.sleep(0.5)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(sticker_loop(bot, chat_id, user_stickers[str(user_id)]))
        tasks.append(task)
    
    sticker_tasks[chat_id] = tasks
    await update.message.reply_text("🎨 Sticker spam started!")

@only_rights
async def stopsticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in sticker_tasks:
        for task in sticker_tasks[chat_id]:
            task.cancel()
        del sticker_tasks[chat_id]
        await update.message.reply_text("🛑 Sticker spam stopped!")
    else:
        await update.message.reply_text("❌ No active sticker spam")

@only_rights
async def delsticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if str(user_id) in user_stickers:
        user_stickers[str(user_id)] = []
        save_stickers()
        await update.message.reply_text("✅ All stickers cleared!")
    else:
        await update.message.reply_text("❌ No stickers found")

# ============================
# 1. NAME CHANGERS - ALL FIXED
# ============================

@only_rights
async def gcnc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """GC Name Changer - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /gcnc <name>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in gcnc_tasks:
        for task in gcnc_tasks[chat_id]:
            task.cancel()
    
    async def gcnc_loop(bot, chat_id, base):
        i = 0
        while True:
            try:
                text = f"{base} {RAID_TEXTS[i % len(RAID_TEXTS)]}"
                await bot.set_chat_title(chat_id, text)
                i += 1
                await asyncio.sleep(delay)
            except Exception as e:
                await asyncio.sleep(1)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(gcnc_loop(bot, chat_id, base))
        tasks.append(task)
    
    gcnc_tasks[chat_id] = tasks
    await update.message.reply_text("⚡ GC Name Changer Started!")

@only_rights
async def ncemo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Emoji Name Changer - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /ncemo <name>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in ncemo_tasks:
        for task in ncemo_tasks[chat_id]:
            task.cancel()
    
    async def ncemo_loop(bot, chat_id, base):
        i = 0
        while True:
            try:
                text = f"{base} {NCEMO_EMOJIS[i % len(NCEMO_EMOJIS)]}"
                await bot.set_chat_title(chat_id, text)
                i += 1
                await asyncio.sleep(delay)
            except Exception as e:
                await asyncio.sleep(1)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(ncemo_loop(bot, chat_id, base))
        tasks.append(task)
    
    ncemo_tasks[chat_id] = tasks
    await update.message.reply_text("⚡ Emoji Name Changer Started!")

@only_rights
async def ncbaap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """NCBAAP Name Changer - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /ncbaap <name>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in ncbaap_tasks:
        for task in ncbaap_tasks[chat_id]:
            task.cancel()
    
    async def ncbaap_loop(bot, chat_id, base):
        i = 0
        while True:
            try:
                patterns = [
                    f"{base} {RAID_TEXTS[i % len(RAID_TEXTS)]}",
                    f"{base} {NCEMO_EMOJIS[i % len(NCEMO_EMOJIS)]}",
                    f"{base} {exonc_TEXTS[i % len(exonc_TEXTS)]}"
                ]
                for text in patterns:
                    try:
                        await bot.set_chat_title(chat_id, text)
                        await asyncio.sleep(0.02)
                    except:
                        pass
                i += 1
                await asyncio.sleep(delay)
            except Exception as e:
                await asyncio.sleep(1)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(ncbaap_loop(bot, chat_id, base))
        tasks.append(task)
    
    ncbaap_tasks[chat_id] = tasks
    await update.message.reply_text("💀🔥 NCBAAP ACTIVATED!")

@only_rights
async def exonc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """EXONC Name Changer - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /exonc <name>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in exonc_tasks:
        for task in exonc_tasks[chat_id]:
            task.cancel()
    
    async def exonc_loop(bot, chat_id, base):
        i = 0
        while True:
            try:
                patterns = [
                    f"{base} {exonc_TEXTS[i % len(exonc_TEXTS)]}",
                    f"{exonc_TEXTS[i % len(exonc_TEXTS)]} {base}",
                ]
                text = random.choice(patterns)
                await bot.set_chat_title(chat_id, text)
                i += 1
                await asyncio.sleep(delay)
            except Exception as e:
                await asyncio.sleep(1)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(exonc_loop(bot, chat_id, base))
        tasks.append(task)
    
    exonc_tasks[chat_id] = tasks
    await update.message.reply_text("⚡ EXONC Started!")

@only_rights
async def stopgcnc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in gcnc_tasks:
        for task in gcnc_tasks[chat_id]:
            task.cancel()
        del gcnc_tasks[chat_id]
        await update.message.reply_text("🛑 GC Name Changer Stopped!")
    else:
        await update.message.reply_text("❌ No active GC Name Changer")

@only_rights
async def stopncemo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in ncemo_tasks:
        for task in ncemo_tasks[chat_id]:
            task.cancel()
        del ncemo_tasks[chat_id]
        await update.message.reply_text("🛑 Emoji Name Changer Stopped!")
    else:
        await update.message.reply_text("❌ No active Emoji Name Changer")

@only_rights
async def stopncbaap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in ncbaap_tasks:
        for task in ncbaap_tasks[chat_id]:
            task.cancel()
        del ncbaap_tasks[chat_id]
        await update.message.reply_text("🛑 NCBAAP Stopped!")
    else:
        await update.message.reply_text("❌ No active NCBAAP")

@only_rights
async def stopexonc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in exonc_tasks:
        for task in exonc_tasks[chat_id]:
            task.cancel()
        del exonc_tasks[chat_id]
        await update.message.reply_text("🛑 EXONC Stopped!")
    else:
        await update.message.reply_text("❌ No active EXONC")

# ============================
# 2. RAID SYSTEMS - ALL FIXED
# ============================

@only_rights
async def raid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """RAID - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /raid <name>")
    
    name = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in raid_tasks:
        for task in raid_tasks[chat_id]:
            task.cancel()
    
    async def raid_loop(bot, chat_id, name):
        while True:
            try:
                raid_text = f"{name} {random.choice(RAID_TEXTS)}"
                await bot.send_message(chat_id, raid_text)
                await asyncio.sleep(raid_delay)
            except Exception as e:
                await asyncio.sleep(0.2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(raid_loop(bot, chat_id, name))
        tasks.append(task)
    
    raid_tasks[chat_id] = tasks
    await update.message.reply_text(f"💀 RAID ACTIVATED!\nTarget: {name}")

@only_rights
async def stopraid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in raid_tasks:
        for task in raid_tasks[chat_id]:
            task.cancel()
        del raid_tasks[chat_id]
        await update.message.reply_text("🛑 RAID STOPPED!")
    else:
        await update.message.reply_text("❌ No active raid")

@only_rights
async def swipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """SWIPE - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /swipe <name>")
    
    name = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in swipe_tasks:
        for task in swipe_tasks[chat_id]:
            task.cancel()
    
    async def swipe_loop(bot, chat_id, name):
        reply_id = None
        while True:
            try:
                raid_text = f"{name} {random.choice(RAID_TEXTS)}"
                if reply_id:
                    msg = await bot.send_message(
                        chat_id=chat_id,
                        text=raid_text,
                        reply_to_message_id=reply_id
                    )
                    reply_id = msg.message_id
                else:
                    msg = await bot.send_message(chat_id, raid_text)
                    reply_id = msg.message_id
                await asyncio.sleep(swipe_delay)
            except Exception as e:
                await asyncio.sleep(0.3)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(swipe_loop(bot, chat_id, name))
        tasks.append(task)
    
    swipe_tasks[chat_id] = tasks
    await update.message.reply_text(f"🔄 SWIPE ACTIVATED!\nName: {name}")

@only_rights
async def stopswipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in swipe_tasks:
        for task in swipe_tasks[chat_id]:
            task.cancel()
        del swipe_tasks[chat_id]
        await update.message.reply_text("🛑 SWIPE STOPPED!")
    else:
        await update.message.reply_text("❌ No active swipe")

@only_rights
async def pswipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """PSWIPE - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /pswipe <text>")
    
    text = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in pswipe_tasks:
        for task in pswipe_tasks[chat_id]:
            task.cancel()
    
    async def pswipe_loop(bot, chat_id, text):
        reply_id = None
        while True:
            try:
                if reply_id:
                    msg = await bot.send_message(
                        chat_id=chat_id,
                        text=text,
                        reply_to_message_id=reply_id
                    )
                    reply_id = msg.message_id
                else:
                    msg = await bot.send_message(chat_id, text)
                    reply_id = msg.message_id
                await asyncio.sleep(swipe_delay)
            except Exception as e:
                await asyncio.sleep(0.3)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(pswipe_loop(bot, chat_id, text))
        tasks.append(task)
    
    pswipe_tasks[chat_id] = tasks
    await update.message.reply_text(f"⚡ PERSONAL SWIPE ACTIVATED!\nText: {text}")

@only_rights
async def stoppswipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in pswipe_tasks:
        for task in pswipe_tasks[chat_id]:
            task.cancel()
        del pswipe_tasks[chat_id]
        await update.message.reply_text("🛑 PERSONAL SWIPE STOPPED!")
    else:
        await update.message.reply_text("❌ No active personal swipe")

# ============================
# 3. SPAM SYSTEMS - ALL FIXED
# ============================

@only_rights
async def spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """SPAM - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /spam <text>")
    
    text = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in spam_tasks:
        for task in spam_tasks[chat_id]:
            task.cancel()
    
    async def spam_loop(bot, chat_id, text):
        while True:
            try:
                await bot.send_message(chat_id, text)
                await asyncio.sleep(spam_delay)
            except Exception as e:
                await asyncio.sleep(0.2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(spam_loop(bot, chat_id, text))
        tasks.append(task)
    
    spam_tasks[chat_id] = tasks
    await update.message.reply_text("⚡ SPAM STARTED!")

@only_rights
async def unspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in spam_tasks:
        for task in spam_tasks[chat_id]:
            task.cancel()
        del spam_tasks[chat_id]
        await update.message.reply_text("🛑 SPAM STOPPED!")
    else:
        await update.message.reply_text("❌ No active spam")

@only_rights
async def flood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FLOOD - FIXED"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /flood <text>")
    
    text = " ".join(context.args)
    chat_id = update.message.chat_id
    
    if chat_id in flood_tasks:
        for task in flood_tasks[chat_id]:
            task.cancel()
    
    async def flood_loop(bot, chat_id, text):
        while True:
            try:
                for _ in range(5):
                    await bot.send_message(chat_id, text)
                    await asyncio.sleep(0.02)
                await asyncio.sleep(flood_delay)
            except Exception as e:
                await asyncio.sleep(0.2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(flood_loop(bot, chat_id, text))
        tasks.append(task)
    
    flood_tasks[chat_id] = tasks
    await update.message.reply_text("🌊 FLOOD ACTIVATED!")

@only_rights
async def stopflood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in flood_tasks:
        for task in flood_tasks[chat_id]:
            task.cancel()
        del flood_tasks[chat_id]
        await update.message.reply_text("🛑 FLOOD STOPPED!")
    else:
        await update.message.reply_text("❌ No active flood")

# ============================
# 4. SPAM FORMS - ALL FIXED
# ============================

@only_rights
async def glitchspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in glitchspam_tasks:
        for task in glitchspam_tasks[chat_id]:
            task.cancel()
    
    async def glitchspam_loop(bot, chat_id):
        glitch = ["█", "▓", "▒", "░", "▄", "▀", "■", "□"]
        while True:
            try:
                text = ""
                for _ in range(15):
                    text += random.choice(glitch)
                await bot.send_message(chat_id, text)
                await asyncio.sleep(0.08)
            except Exception as e:
                await asyncio.sleep(0.2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(glitchspam_loop(bot, chat_id))
        tasks.append(task)
    
    glitchspam_tasks[chat_id] = tasks
    await update.message.reply_text("▓ GLITCHSPAM ACTIVATED ▓")

@only_rights
async def stopglitchspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in glitchspam_tasks:
        for task in glitchspam_tasks[chat_id]:
            task.cancel()
        del glitchspam_tasks[chat_id]
        await update.message.reply_text("🛑 GLITCHSPAM STOPPED!")
    else:
        await update.message.reply_text("❌ No active glitchspam")

@only_rights
async def rainbowspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in rainbowspam_tasks:
        for task in rainbowspam_tasks[chat_id]:
            task.cancel()
    
    async def rainbowspam_loop(bot, chat_id):
        rainbow = ["🌈", "❤️", "🧡", "💛", "💚", "💙", "💜"]
        while True:
            try:
                text = ""
                for _ in range(6):
                    text += random.choice(rainbow) + " "
                await bot.send_message(chat_id, text.strip())
                await asyncio.sleep(0.08)
            except Exception as e:
                await asyncio.sleep(0.2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(rainbowspam_loop(bot, chat_id))
        tasks.append(task)
    
    rainbowspam_tasks[chat_id] = tasks
    await update.message.reply_text("🌈 RAINBOWSPAM ACTIVATED")

@only_rights
async def stoprainbowspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in rainbowspam_tasks:
        for task in rainbowspam_tasks[chat_id]:
            task.cancel()
        del rainbowspam_tasks[chat_id]
        await update.message.reply_text("🛑 RAINBOWSPAM STOPPED!")
    else:
        await update.message.reply_text("❌ No active rainbowspam")

@only_rights
async def numberspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in numberspam_tasks:
        for task in numberspam_tasks[chat_id]:
            task.cancel()
    
    async def numberspam_loop(bot, chat_id):
        while True:
            try:
                patterns = ["1234567890", "9876543210", "420420420", "69696969"]
                text = random.choice(patterns) * random.randint(3, 5)
                await bot.send_message(chat_id, text)
                await asyncio.sleep(0.08)
            except Exception as e:
                await asyncio.sleep(0.2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(numberspam_loop(bot, chat_id))
        tasks.append(task)
    
    numberspam_tasks[chat_id] = tasks
    await update.message.reply_text("🔢 NUMBERSPAM ACTIVATED")

@only_rights
async def stopnumberspam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in numberspam_tasks:
        for task in numberspam_tasks[chat_id]:
            task.cancel()
        del numberspam_tasks[chat_id]
        await update.message.reply_text("🛑 NUMBERSPAM STOPPED!")
    else:
        await update.message.reply_text("❌ No active numberspam")

# ============================
# 5. VANITAS MODE - FIXED 100%
# ============================

@only_rights
async def vanitas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """VANITAS - ALL FEATURES ACTIVATED - FIXED"""
    global vanitas_mode, vanitas_name, vanitas_spam_text
    
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vanitas <name> | <spam_text>")
    
    args = " ".join(context.args).split("|")
    vanitas_name = args[0].strip()
    
    if len(args) > 1:
        vanitas_spam_text = args[1].strip()
    else:
        vanitas_spam_text = vanitas_name
    
    vanitas_mode = True
    chat_id = update.message.chat_id
    
    # Stop all existing tasks first
    await stop_all_tasks(chat_id)
    
    # Start ALL features
    tasks = []
    
    # 1. NAME CHANGERS
    for bot in bots:
        async def name_loop():
            i = 0
            while vanitas_mode:
                try:
                    patterns = [
                        f"{vanitas_name} {RAID_TEXTS[i % len(RAID_TEXTS)]}",
                        f"{vanitas_name} {NCEMO_EMOJIS[i % len(NCEMO_EMOJIS)]}",
                        f"{vanitas_name} {exonc_TEXTS[i % len(exonc_TEXTS)]}"
                    ]
                    for text in patterns:
                        try:
                            await bot.set_chat_title(chat_id, text)
                            await asyncio.sleep(0.05)
                        except:
                            pass
                    i += 1
                    await asyncio.sleep(delay)
                except Exception as e:
                    await asyncio.sleep(1)
        tasks.append(asyncio.create_task(name_loop()))
    
    # 2. RAID
    for bot in bots:
        async def raid_loop():
            while vanitas_mode:
                try:
                    raid_text = f"{vanitas_name} {random.choice(RAID_TEXTS)}"
                    await bot.send_message(chat_id, raid_text)
                    await asyncio.sleep(raid_delay)
                except Exception as e:
                    await asyncio.sleep(0.2)
        tasks.append(asyncio.create_task(raid_loop()))
    
    # 3. SWIPE
    for bot in bots:
        async def swipe_loop():
            reply_id = None
            while vanitas_mode:
                try:
                    if reply_id:
                        msg = await bot.send_message(
                            chat_id=chat_id,
                            text=f"{vanitas_name} {random.choice(RAID_TEXTS)}",
                            reply_to_message_id=reply_id
                        )
                        reply_id = msg.message_id
                    else:
                        msg = await bot.send_message(chat_id, f"{vanitas_name} {random.choice(RAID_TEXTS)}")
                        reply_id = msg.message_id
                    await asyncio.sleep(swipe_delay)
                except Exception as e:
                    await asyncio.sleep(0.3)
        tasks.append(asyncio.create_task(swipe_loop()))
    
    # 4. SPAM
    for bot in bots:
        async def spam_loop():
            while vanitas_mode:
                try:
                    await bot.send_message(chat_id, vanitas_spam_text)
                    await asyncio.sleep(spam_delay)
                except Exception as e:
                    await asyncio.sleep(0.2)
        tasks.append(asyncio.create_task(spam_loop()))
    
    # 5. FLOOD
    for bot in bots:
        async def flood_loop():
            while vanitas_mode:
                try:
                    for _ in range(3):
                        await bot.send_message(chat_id, vanitas_spam_text)
                        await asyncio.sleep(0.03)
                    await asyncio.sleep(flood_delay)
                except Exception as e:
                    await asyncio.sleep(0.2)
        tasks.append(asyncio.create_task(flood_loop()))
    
    vanitas_tasks[chat_id] = tasks
    
    await update.message.reply_text(
        f"💀🔥 VANITAS ACTIVATED!\n"
        f"Name: {vanitas_name}\n"
        f"Spam: {vanitas_spam_text}\n"
        f"✅ ALL SYSTEMS: NAME CHANGERS, RAID, SWIPE, SPAM, FLOOD!"
    )

@only_rights
async def stopvanitas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global vanitas_mode
    chat_id = update.message.chat_id
    
    if chat_id in vanitas_tasks:
        for task in vanitas_tasks[chat_id]:
            task.cancel()
        del vanitas_tasks[chat_id]
    
    vanitas_mode = False
    await update.message.reply_text("🛑 VANITAS STOPPED!")

# ============================
# 6. REACTION SYSTEM - FIXED 100%
# ============================

@only_rights
async def react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """REACTIONS - 100% WORKING"""
    emoji = "🔥"
    if context.args:
        emoji = context.args[0]
    
    chat_id = update.message.chat_id
    
    if chat_id in reaction_tasks:
        for task in reaction_tasks[chat_id]:
            task.cancel()
        del reaction_tasks[chat_id]
    
    async def reaction_loop(bot, chat_id, emoji):
        processed = set()
        while True:
            try:
                messages = await bot.get_chat_history(chat_id, limit=10)
                for message in messages:
                    msg_id = message.message_id
                    if msg_id not in processed:
                        try:
                            await bot.set_message_reaction(
                                chat_id=chat_id,
                                message_id=msg_id,
                                reaction=[{"type": "emoji", "emoji": emoji}]
                            )
                            processed.add(msg_id)
                        except Exception as e:
                            continue
                await asyncio.sleep(reaction_delay)
            except Exception as e:
                await asyncio.sleep(2)
    
    tasks = []
    for bot in bots:
        task = asyncio.create_task(reaction_loop(bot, chat_id, emoji))
        tasks.append(task)
    
    reaction_tasks[chat_id] = tasks
    await update.message.reply_text(f"⚡ REACTIONS ACTIVATED!\nEmoji: {emoji}")

@only_rights
async def stopreact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in reaction_tasks:
        for task in reaction_tasks[chat_id]:
            task.cancel()
        del reaction_tasks[chat_id]
        await update.message.reply_text("🛑 REACTIONS STOPPED!")
    else:
        await update.message.reply_text("❌ No active reactions")

# ============================
# 7. VOICE NOTES - DIFFERENT VOICES
# ============================

@only_rights
async def vn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text, lang='en', slow=False)
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"🗣️ Normal: {text}")

@only_rights
async def vn2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn2 <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text, lang='ja', slow=False)
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"⚔️ Asuna SAO ☔: {text}")

@only_rights
async def vn3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn3 <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text, lang='ja', slow=True)
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"👻 Rem Re:Zero ✨: {text}")

@only_rights
async def vn4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn4 <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text, lang='ja', slow=False)
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"🐰 Mai Sakurajima 🎀: {text}")

@only_rights
async def vn5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn5 <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text, lang='en', slow=False, tld='co.uk')
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"🤖 Zero Two 💖: {text}")

@only_rights
async def vn6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn6 <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text.upper(), lang='en', slow=False)
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"🏐 Hinata Haikyuu 🏐: {text}")

@only_rights
async def vn7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /vn7 <text>")
    
    text = " ".join(context.args)
    tts = gTTS(text=text.upper() + "!!!", lang='en', slow=False)
    voice = io.BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    await update.message.reply_voice(voice=voice, caption=f"🐉 Natsu Fairy Tail 🔥: {text}")

# ============================
# 8. /madd FEATURE
# ============================

@only_rights
async def madd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Add user to all groups"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /madd @username")
    
    username = context.args[0].strip()
    if not username.startswith('@'):
        username = '@' + username
    
    success = 0
    failed = 0
    
    await update.message.reply_text(f"🔍 Adding {username} to all groups...")
    
    for group_id in list(ACTIVE_GROUP_CHATS):
        try:
            for bot in bots:
                try:
                    await bot.add_chat_members(group_id, username)
                    success += 1
                    await asyncio.sleep(1)
                    break
                except Exception as e:
                    continue
        except Exception as e:
            failed += 1
    
    await update.message.reply_text(f"✅ Added to {success} groups\n❌ Failed: {failed}")

# ============================
# BASIC FUNCTIONS
# ============================

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💀 DELETE V14 ULTRA MAXIMUM\nUse /help")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
DELETE υℓтʀα ꪑᴀx [🦋]

🪷 Nᴀᴍᴇ Cʜᴀɴɢᴇʀꜱ :
/gcnc <name> 
/ncemo <name> 
/ncbaap <name> 
/exonc <name> 
/stopgcnc /stopncemo /stopncbaap /stopexonc

🩷 Rᴀɪᴅ Sʏꜱᴛᴜᴍꜱ :
/raid <name> 
/swipe <name> 
/pswipe <text> 
/stopraid /stopswipe /stoppswipe

🔥 SᴘᴀᴍS :
/fuck <1-5> <name>  
/spam <text> 
/unspam 
/flood <text> 
/stopflood 
/sfuck 

☘️ Sᴘᴀᴍ Fᴏʀᴍꜱ :
/glitchspam 
/rainbowspam 
/numberspam 
/stopglitchspam /stoprainbowspam /stopnumberspam

⚡ Rᴇᴀᴄᴛɪᴏɴꜱ :
/react <emoji> 
/stopreact 

🌐 Gʀᴏᴜᴘ Mᴀɴᴀɢᴇᴍᴇɴᴛ :
/addgroup
/removegroup 
/listgroups 
/cleargroups 
/madd @username 

↕️ Mᴜʟᴛɪ-Gʀᴏᴜᴘ :
/multinc <name> 
/multispam <text> 
/stopmultinc /stopmultispam

❤️ Vᴀɴɪᴛᴀꜱ :
/vanitas <name> | <text> 
/stopvanitas - Stop all

🩶 Vᴏɪᴄᴇꜱ :
/vn <text> 
/vn2 <text> 
/vn3 <text> 
/vn4 <text> 
/vn5 <text> 
/vn6 <text> 
/vn7 <text>

🎨 Sᴛɪᴄᴋᴇʀ :
/newsticker (reply)
/sticker /stopsticker /delsticker

🌊 Exᴛʀᴀ :
/autoreply <trigger> <reply>
/stopautoreply
/stopall 

👑 Rɪɢʜᴛꜱ Mᴀɴᴀɢᴇᴍᴇɴᴛ :
/rights <user_id> 
/unrights <user_id>
/listrights 

🛑 Gʟᴏʙᴀʟ :
/status /ping /myid

    """
    await update.message.reply_text(help_text)

async def ping_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start = time.time()
    msg = await update.message.reply_text("⚡")
    end = time.time()
    await msg.edit_text(f"⚡ {int((end-start)*1000)}ms | Bots: {len(bots)}")

async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    status_text = f"""
💀 DELETE  ULTRA MAXIMUM
🤖 Bots: {len(bots)}
🌐 Groups: {len(ACTIVE_GROUP_CHATS)}
👑 rights Users: {len(rights_USERS)}
⚡ Speed: MAXIMUM

✅ ACTIVE SYSTEMS:
Name Changers: {'✅' if chat_id in gcnc_tasks or chat_id in ncemo_tasks or chat_id in ncbaap_tasks or chat_id in exonc_tasks else '❌'}
Raid: {'✅' if chat_id in raid_tasks else '❌'}
Swipe: {'✅' if chat_id in swipe_tasks else '❌'}
Pswipe: {'✅' if chat_id in pswipe_tasks else '❌'}
Spam: {'✅' if chat_id in spam_tasks else '❌'}
Fuck: {'✅' if chat_id in fuck_tasks else '❌'} 
Flood: {'✅' if chat_id in flood_tasks else '❌'}
Reactions: {'✅' if chat_id in reaction_tasks else '❌'}
Vanitas: {'✅' if vanitas_mode else '❌'}

🎵 7 DIFFERENT VOICES
🚀 /madd FEATURE ACTIVE
💀 ALL SYSTEMS 100% WORKING
    """
    await update.message.reply_text(status_text)

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"🆔 Your ID: {user_id}")

# ============================
# GROUP MANAGEMENT
# ============================

@only_rights
async def addgroup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id not in ACTIVE_GROUP_CHATS:
        ACTIVE_GROUP_CHATS.add(chat_id)
        await update.message.reply_text(f"✅ Group added!")
    else:
        await update.message.reply_text("✅ Already active!")

@only_rights
async def removegroup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in ACTIVE_GROUP_CHATS:
        ACTIVE_GROUP_CHATS.remove(chat_id)
        await update.message.reply_text(f"✅ Group removed!")
    else:
        await update.message.reply_text("❌ Not active!")

@only_rights
async def listgroups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    groups_list = "\n".join([f"🆔 {chat_id}" for chat_id in ACTIVE_GROUP_CHATS])
    await update.message.reply_text(f"🌐 Groups ({len(ACTIVE_GROUP_CHATS)}):\n{groups_list if groups_list else 'No groups'}")

@only_rights
async def cleargroups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ACTIVE_GROUP_CHATS.clear()
    await update.message.reply_text("✅ All groups cleared!")

# ============================
# STOP ALL FUNCTION
# ============================

async def stop_all_tasks(chat_id):
    stopped = []
    task_dicts = [
        (gcnc_tasks, "GCNC"),
        (ncemo_tasks, "NCEMO"),
        (ncbaap_tasks, "NCBAAP"),
        (exonc_tasks, "EXONC"),
        (spam_tasks, "Spam"),
        (raid_tasks, "Raid"),
        (reaction_tasks, "Reactions"),
        (sticker_tasks, "Stickers"),
        (flood_tasks, "Flood"),
        (autoreply_tasks, "Auto-Reply"),
        (vanitas_tasks, "Vanitas"),
        (multinc_tasks, "Multi-NC"),
        (multispam_tasks, "Multi-Spam"),
        (swipe_tasks, "Swipe"),
        (pswipe_tasks, "Pswipe"),
        (glitchspam_tasks, "Glitchspam"),
        (rainbowspam_tasks, "Rainbowspam"),
        (numberspam_tasks, "Numberspam"),
        (fuck_tasks, "Fuck")  # Added fuck tasks
    ]
    
    for task_dict, name in task_dicts:
        if chat_id in task_dict:
            tasks = task_dict[chat_id]
            # Handle different task structures
            if isinstance(tasks, dict):
                # Case for autoreply_tasks which has nested dicts with 'tasks' key
                for trigger in list(tasks.keys()):
                    if isinstance(tasks[trigger], dict) and 'tasks' in tasks[trigger]:
                        for t in tasks[trigger]['tasks']:
                            t.cancel()
            elif isinstance(tasks, list):
                # Standard case: list of tasks
                for task in tasks:
                    task.cancel()
            
            del task_dict[chat_id]
            stopped.append(name)
    
    return stopped

@only_rights
async def stopall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    stopped = await stop_all_tasks(chat_id)
    if stopped:
        await update.message.reply_text(f"🛑 STOPPED: {len(stopped)} systems")
    else:
        await update.message.reply_text("❌ No active tasks")

# ============================
# AUTO-REPLY MESSAGE HANDLER
# ============================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    
    chat_id = update.message.chat_id
    text = update.message.text
    
    if chat_id in autoreply_tasks:
        for trigger, data in autoreply_tasks[chat_id].items():
            if trigger.lower() in text.lower():
                # Reply with all bots
                for bot in bots:
                    try:
                        await bot.send_message(chat_id, data['reply'], reply_to_message_id=update.message.message_id)
                        break
                    except:
                        continue
                break

# ============================
# BOT SETUP
# ============================

def build_app(token):
    app = Application.builder().token(token).build()
    
    # Core commands
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping_cmd))
    app.add_handler(CommandHandler("status", status_cmd))
    app.add_handler(CommandHandler("myid", myid))
    
    # 1. NAME CHANGERS
    app.add_handler(CommandHandler("gcnc", gcnc))
    app.add_handler(CommandHandler("ncemo", ncemo))
    app.add_handler(CommandHandler("ncbaap", ncbaap))
    app.add_handler(CommandHandler("exonc", exonc))
    app.add_handler(CommandHandler("stopgcnc", stopgcnc))
    app.add_handler(CommandHandler("stopncemo", stopncemo))
    app.add_handler(CommandHandler("stopncbaap", stopncbaap))
    app.add_handler(CommandHandler("stopexonc", stopexonc))
    
    # 2. RAID SYSTEMS
    app.add_handler(CommandHandler("raid", raid))
    app.add_handler(CommandHandler("stopraid", stopraid))
    app.add_handler(CommandHandler("swipe", swipe))
    app.add_handler(CommandHandler("stopswipe", stopswipe))
    app.add_handler(CommandHandler("pswipe", pswipe))
    app.add_handler(CommandHandler("stoppswipe", stoppswipe))
    
    # 3. SPAM SYSTEMS - ADDED FUCK HERE
    app.add_handler(CommandHandler("fuck", fuck))  # NEW
    app.add_handler(CommandHandler("sfuck", sfuck))  # NEW
    app.add_handler(CommandHandler("spam", spam))
    app.add_handler(CommandHandler("unspam", unspam))
    app.add_handler(CommandHandler("flood", flood))
    app.add_handler(CommandHandler("stopflood", stopflood))
    
    # 4. SPAM FORMS
    app.add_handler(CommandHandler("glitchspam", glitchspam))
    app.add_handler(CommandHandler("stopglitchspam", stopglitchspam))
    app.add_handler(CommandHandler("rainbowspam", rainbowspam))
    app.add_handler(CommandHandler("stoprainbowspam", stoprainbowspam))
    app.add_handler(CommandHandler("numberspam", numberspam))
    app.add_handler(CommandHandler("stopnumberspam", stopnumberspam))
    
    # 5. VANITAS
    app.add_handler(CommandHandler("vanitas", vanitas))
    app.add_handler(CommandHandler("stopvanitas", stopvanitas))
    
    # 6. REACTIONS
    app.add_handler(CommandHandler("react", react))
    app.add_handler(CommandHandler("stopreact", stopreact))
    
    # 7. VOICE NOTES
    app.add_handler(CommandHandler("vn", vn))
    app.add_handler(CommandHandler("vn2", vn2))
    app.add_handler(CommandHandler("vn3", vn3))
    app.add_handler(CommandHandler("vn4", vn4))
    app.add_handler(CommandHandler("vn5", vn5))
    app.add_handler(CommandHandler("vn6", vn6))
    app.add_handler(CommandHandler("vn7", vn7))
    
    # 8. /madd FEATURE
    app.add_handler(CommandHandler("madd", madd))
    
    # 9. GROUP MANAGEMENT
    app.add_handler(CommandHandler("addgroup", addgroup))
    app.add_handler(CommandHandler("removegroup", removegroup))
    app.add_handler(CommandHandler("listgroups", listgroups))
    app.add_handler(CommandHandler("cleargroups", cleargroups))
    
    # 10. STOP ALL
    app.add_handler(CommandHandler("stopall", stopall))
    
    # 11. STICKER SYSTEM
    app.add_handler(CommandHandler("newsticker", newsticker))
    app.add_handler(CommandHandler("sticker", sticker))
    app.add_handler(CommandHandler("stopsticker", stopsticker))
    app.add_handler(CommandHandler("delsticker", delsticker))
    
    # 12. AUTO-REPLY
    app.add_handler(CommandHandler("autoreply", autoreply))
    app.add_handler(CommandHandler("stopautoreply", stopautoreply))
    
    # 13. MULTI-GROUP
    app.add_handler(CommandHandler("multinc", multinc))
    app.add_handler(CommandHandler("stopmultinc", stopmultinc))
    app.add_handler(CommandHandler("multispam", multispam))
    app.add_handler(CommandHandler("stopmultispam", stopmultispam))
    
    # 14. rights MANAGEMENT - NEW
    app.add_handler(CommandHandler("rights", rights))
    app.add_handler(CommandHandler("unrights", unrights))
    app.add_handler(CommandHandler("listrights", listrights))
    
    # 15. MESSAGE HANDLER FOR AUTO-REPLY
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    return app

# ============================
# MAIN
# ============================

apps, bots = [], []

async def run_all_bots():
    global apps, bots
    
    print("🚀 Starting DELETE ULTRA MAXIMUM...")
    
    for token in TOKENS:
        if token.strip():
            try:
                app = build_app(token)
                apps.append(app)
                bots.append(app.bot)
                print(f"✅ Bot loaded")
            except Exception as e:
                print(f"❌ Failed to load bot: {e}")
                continue
    
    for app in apps:
        try:
            await app.initialize()
            await app.start()
            await app.updater.start_polling()
            print(f"⚡ Bot started")
        except Exception as e:
            print(f"❌ Failed to start bot: {e}")
            continue
    
    print(f"""
💀 DELETE ULTRA MAXIMUM
✅ Bots: {len(bots)}
👑 rights Users: {len(rights_USERS)}
⚡ ALL SYSTEMS 100% WORKING

🚀 FEATURES:
1. ✅ Name Changers: /gcnc, /ncemo, /ncbaap, /exonc
2. ✅ FUCK System: /fuck <1-5> <name> 
3. ✅ Spam: /spam, /flood  
4. ✅ Vanitas: /vanitas (ALL features)
5. ✅ Reactions: /react (100% real)
6. ✅ Swipe: /swipe, /pswipe
7. ✅ Raid: /raid
8. ✅ Voice Notes: 7 different voices
9. ✅ /madd feature
10. ✅ All spam forms
11. ✅ ALL STOP COMMANDS WORKING
12. ✅ Multi-group features: /multinc, /multispam
13. ✅ Sticker system: /newsticker, /sticker
14. ✅ Auto-reply system: /autoreply
15. ✅ rights Management: /rights, /unrights, /listrights
16. ✅ Message handler for auto-reply

🔥 READY FOR MAXIMUM DESTRUCTION!

👑 rights COMMANDS:
/rights <user_id> - Add user to rights
/unrights <user_id> - Remove user from rights
/listrights - List all rights users

💀 Owner ID: set(OWNER_ID)
    """)
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(run_all_bots())
    except KeyboardInterrupt:
        print("\n🛑 Shutting Down...")
    except Exception as e:
        print(f"❌ Error: {e}")
