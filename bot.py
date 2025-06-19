import telebot
from telebot import types

# TOKEN
bot = telebot.TeleBot("7642791863:AAG3IhwDMjPwsDIhF85BVa8rkw4gVqvtzDg")

# Boshlanishda salomlashish
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📝 KUNLIK VAZIFALAR")
    btn2 = types.KeyboardButton("📌 MUHIM ESLATMALAR")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        f"Salom {message.from_user.first_name}! ✅\nKunlik motivatsion botga xush kelibsan!",
        reply_markup=markup
    )

# Tugmalar bo‘yicha javob
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📝 KUNLIK VAZIFALAR":
        vazifalar = (
            "📋 BUGUNGI VAZIFALAR:\n\n"
            "1. Tongda 10 daqiqa meditatsiya qilish 🧘‍♂️\n"
            "2. Bugungi 3 ta maqsadingni yozib chiq 📓\n"
            "3. 25 daqiqa davomida muhim vazifa ustida ishlash 🕒\n"
            "4. 10 daqiqa tanaffus qilish ☕\n"
            "5. Kamida 5 sahifa kitob o‘qish 📖\n"
            "6. Shaxsiy rivojlanishga 30 daqiqa vaqt ajrat 🎯\n"
            "7. Yotishdan oldin kunni tahlil qilish 🌙"
        )
        bot.send_message(message.chat.id, vazifalar)
    
    elif message.text == "📌 MUHIM ESLATMALAR":
        eslatmalar = (
            "📍 Vaqtingni qadrlagin\n"
            "📍 Har bir kun — imkoniyat\n"
            "📍 Shaxsiy o‘sishga sodiq qol\n"
            "📍 Salbiy fikrlardan uzoq yur\n"
            "📍 O‘zingga ishongan holda harakat qil"
        )
        bot.send_message(message.chat.id, f"MUHIM ESLATMALAR:\n\n{eslatmalar}")
    
    else:
        bot.send_message(message.chat.id, "Nomaʼlum buyruq! Tugmalardan foydalaning.")

# Ishga tushganini ko‘rsatish
print("Bot ishga tushdi...")

# Botni boshlash
bot.polling(non_stop=True)
