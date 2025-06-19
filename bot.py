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
            "✅ Ertalab 5:00 da uyg‘onish\n"
            "✅ Sovuq suvda yuzni yuvish\n"
            "✅ 20 daqiqa badantarbiya\n"
            "✅ 1 soat kitob o‘qish\n"
            "✅ Reja asosida kunni boshlash\n"
            "✅ Tanaffusda chuqur nafas olish\n"
            "✅ Harakatda bo‘lish va dangasalikdan qochish\n"
            "✅ Kun yakunida qisqa hisobot yozish"
        )
        bot.send_message(message.chat.id, f"KUNLIK VAZIFALAR:\n\n{vazifalar}")
    
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
