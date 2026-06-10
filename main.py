import requests
from config import TELEGRAM_TOKEN, CAT_API_TOKEN, DOG_TOKEN
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def get_card():
    """Randommer API dan tasodifiy karta olib olish"""
    url = "https://randommer.io/api/Card/"
    headers = {"X-Api-Key": "27ed4274794b4b8f970d384778f42752"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None


def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url, headers={'x-api-key': CAT_API_TOKEN}, timeout=5)
        return response.json()[0]['url'] if response.status_code == 200 else None
    except:
        return None


def get_dog():
    url = "https://api.thedogapi.com/v1/images/search?limit=1"
    try:
        response = requests.get(url, headers={'x-api-key': DOG_TOKEN}, timeout=5)
        return response.json()[0]['url'] if response.status_code == 200 else None
    except:
        return None


def get_currency_rate(code):
    try:
        response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/", timeout=5)
        for item in response.json():
            if item['Ccy'] == code:
                return float(item['Rate'])
    except:
        pass
    return None


def start(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton("Cat"), KeyboardButton("Dog")],
        [KeyboardButton("Kurs"), KeyboardButton("Card")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    
    salom = f"Assalomualikum {update.effective_user.first_name}!\nMeni tanlang:"
    update.message.reply_text(salom, reply_markup=keyboard)


def handle_message(update: Update, context: CallbackContext):
    msg = update.message.text.strip()
    
    if msg[0].isdigit() and " " in msg:
        calculate_currency(update, context)
        return
    
    if "Cat" in msg:
        url = get_cat()
        if url:
            update.message.reply_photo(photo=url)
        else:
            update.message.reply_text("Mushuk topilmadi!")
    
    elif "Dog" in msg:
        url = get_dog()
        if url:
            update.message.reply_photo(photo=url)
        else:
            update.message.reply_text("Ит topilmadi!")
    
    elif "Card" in msg:
        card = get_card()
        if card:
            text = f"""Tasodifiy Karta:
Raqami: {card.get('cardNumber', 'N/A')}
CVV: {card.get('cvv', 'N/A')}
Muddati: {card.get('expirationDate', 'N/A')}"""
            update.message.reply_text(text)
    
    elif "Kurs" in msg:
        update.message.reply_text("Summa va valyutani kiriting (masalan: 100 USD)")


def calculate_currency(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    
    try:
        parts = text.split()
        amount = float(parts[0])
        code = parts[1].upper()
        
        rate = get_currency_rate(code)
        
        if rate:
            result = amount * rate
            msg = f"{amount} {code} = {result:.2f} UZS"
            update.message.reply_text(msg)
        else:
            update.message.reply_text("Valyuta topilmadi!")
    except:
        update.message.reply_text("Noto'g'ri format! Masalan: 100 USD")


def main():

    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    updater.start_polling()
    print("Bot ishlamoqda...")
    updater.idle()


if __name__ == '__main__':
    main()
