# Telegram Echo Bot 🤖

Bu telegram bot 3 ta funksiyaga ega:
- 🐱 **Cat** - Tasodifiy mushuk rasmini yuboradi
- 🐕 **Dog** - Tasodifiy it rasmini yuboradi  
- 💵 **Kurs** - USD, EUR, RUB-ni UZS-ga aylantiradi

## Setup (O'rnatish)

### 1. Requirements o'rnatish
```bash
pip install -r requirements.txt
```

### 2. .env faylini yaratish

`.env.example` faylini `.env` deb nomlashtiring va quyidagilarni qo'ying:

```
TELEGRAM_TOKEN=your_telegram_bot_token_here
CAT_API_TOKEN=your_cat_api_token_here
DOG_API_TOKEN=your_dog_api_token_here
```

### 3. API Tokenlarni olish

#### Telegram Bot Token
1. Telegram-da @BotFather-ga yozing
2. `/newbot` komandasini yuboring
3. Bot nomini va username-ni kiriting
4. Token-ni olishni tugatgach, uni `.env` fayliga joylashtiring

#### Cat API Token
1. https://thecatapi.com ga o'ting
2. Sign Up qiling
3. API Key-ni oling va `.env` fayliga joylashtiring

#### Dog API Token
1. https://thedogapi.com ga o'ting
2. Sign Up qiling
3. API Key-ni oling va `.env` fayliga joylashtiring

## Ishlatish

```bash
python main.py
```

Bot ishga tushibgach, Telegram-da botni topib `/start` komandasini yuboring.

## Tugmalar

- **🐱 Cat** - Random mushuk rasmi olish
- **🐕 Dog** - Random it rasmi olish
- **💵 Kurs** - Valyuta konversiyasi (masalan: 100 USD)

## Fayllar Tuzilishi

```
echobot/
├── main.py              # Asosiy bot fayli (cat, dog, usd integratsiyasi)
├── config.py            # Konfiguratsiya fayli
├── settings.py          # Settings
├── cat.py               # Cat API client (eski - main.py-da integratsiyalandi)
├── dog.py               # Dog API client (eski - main.py-da integratsiyalandi)
├── usd.py               # USD konversiyasi (eski - main.py-da integratsiyalandi)
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables namunasi
└── README.md            # Bu fayl
```

## Xatoliklarni Tuzatish

### "Invalid TOKEN" xatosi
- `.env` faylidagi TELEGRAM_TOKEN to'g'ri ekanligini tekshiring
- BotFather-dan token-ni qaytadan oling

### "No module named 'telegram'" xatosi
- `pip install -r requirements.txt` buyrug'ini qaytadan bajaring

### Rasmlar yuklanmayotgan bo'lsa
- CAT_API_TOKEN va DOG_API_TOKEN to'g'ri ekanligini tekshiring
- API keys ish vaqti tugalgan bo'lishi mumkin, yangi key-lar oling
