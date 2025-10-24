import telebot
from telebot import types
import json
import os
import random
from datetime import datetime, timedelta

# ===================== CONFIG =====================
TOKEN = '7652164784:AAH74wtiAm9Kq2B3W8bv11H7ksq6quIPcO4'
ADMIN_ID = '@Zn_putri'  # ganti dengan telegram ID kamu
MIN_DEPOSIT_PREMIUM = 50000
REKENING = "901757312575 a/n Ipan Nurpana"
# ==================================================

bot = telebot.TeleBot(TOKEN)
DB_FILE = "users.json"

# Load database
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

def save_db():
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def get_level(points):
    return points // 50000 + 1

def init_user(user_id, username):
    users[user_id] = {
        "points": 0,
        "is_premium": False,
        "username": username,
        "last_daily": "",
        "daily_streak": 0,
        "click_count": 0,
        "quests_completed": []
    }
    save_db()

def main_menu(user_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎮 Klik", callback_data="click"),
        types.InlineKeyboardButton("💰 Balance", callback_data="balance"),
        types.InlineKeyboardButton("⭐ Upgrade Premium", callback_data="premium"),
        types.InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard"),
        types.InlineKeyboardButton("💸 Withdraw", callback_data="withdraw"),
        types.InlineKeyboardButton("🎁 Bonus Harian", callback_data="daily_bonus"),
        types.InlineKeyboardButton("🗺 Mission / Quest", callback_data="quest")
    )
    bot.send_message(user_id, "Pilih menu:", reply_markup=markup)

def check_quests(user_id):
    user = users[user_id]
    quest_rewards = []
    
    # Quest 1: Klik 5 kali
    if user["click_count"] >= 5 and 1 not in user["quests_completed"]:
        reward = random.randint(5000, 10000)
        user["points"] += reward
        user["quests_completed"].append(1)
        quest_rewards.append(f"Quest 1 selesai! Kamu dapat {reward} poin 🎯")
    
    # Quest 2: Daily streak 3 hari
    if user["daily_streak"] >= 3 and 2 not in user["quests_completed"]:
        reward = random.randint(5000, 10000)
        user["points"] += reward
        user["quests_completed"].append(2)
        quest_rewards.append(f"Quest 2 selesai! Daily streak 3 hari! Kamu dapat {reward} poin 🔥")
    
    save_db()
    return quest_rewards

@bot.message_handler(commands=["start"])
def sta
