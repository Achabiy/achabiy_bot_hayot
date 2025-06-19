import telebot
from telebot import types
import datetime

TOKEN = "7642791863:AAG3IhwDMjPwsDIhF85BVa8rkw4gVqvtzDg"
bot = telebot.TeleBot(TOKEN)

checklists = {
    "Monday": ["📖 Kitob o'qish", "💪 Sport bilan shug‘ullanish", "🧠 Yangi narsa o‘rganish", "🧹 Xonani tartibga keltirish"],
    "Tuesday": ["📚 Dars qilish", "📅 Reja tuzish", "🧘‍♂️ Meditatsiya", "📥 Mail tekshirish"],
    "Wednesday": ["🏃‍♂️ Yengil yugurish", "📘 Kitob yozish", "🎧 Podcast tinglash", "🛍 Zaruriy xaridlar"],
    "Thursday": ["📖 Qur'on o‘qish", "🖋 Yozuv mashqlari", "💼 Portfolioni yangilash", "📷 Rasmlar arxivlash"],
    "Friday": ["🕌 Juma namozi", "📓 Haftani tahlil qilish", "🎯 Maqsadlarni qayta ko‘rib chiqish", "🍲 Oila bilan ovqatlanish"],
    "Saturday": ["🧹 Uy tozalash", "🎮 Sevimli o‘yin", "👨‍👩‍👧 Oila bilan vaqt", "🛀 Dam olish"],
    "Sunday": ["📝 Yozuv ishlari", "🎥 Kino ko‘rish", "📖 Yangi maqola o‘qish", "📲 Telefonni tozalash"]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("📋 Bugungi checklist")
    markup.add(item)
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}! ✅ \nKunlik motivatsion botga xush kelibsan!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📋 Bugungi checklist")
def send_checklist(message):
    today = datetime.datetime.now().strftime("%A")
    tasks = checklists.get(today, ["Bugun uchun belgilangan topshiriqlar yo‘q."])
    checklist_text = f"📅 <b>{today}</b> uchun vazifalar:\n\n" + "\n".join([f"▫️ {task}" for task in tasks])
    bot.send_message(message.chat.id, checklist_text, parse_mode='HTML')

bot.polling()
