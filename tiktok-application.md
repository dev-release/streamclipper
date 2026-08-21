# TikTok app submission — texts to paste

Заповнені поля заявки. Англійською, бо розгляд ведеться англійською.

---

## App name

StreamClipper

## Category

Tools / Content creation

## Short description (shown to users on the authorization screen)

StreamClipper turns my own game streams into short clips and uploads the ones
I approve to my own TikTok account.

## Full description

StreamClipper is a personal tool that runs on my own computer. It takes a
recording of my own game stream, finds the moments where I react — laughter,
surprise, a good play — and cuts them into short vertical clips.

Each clip is sent to me in Telegram for review, together with a suggested
caption. Nothing is published automatically: a clip goes to TikTok only when
I press the upload button for that specific clip.

The tool has a single user — me, the owner of the account. There is no sign-up,
no other users, and no content from anyone else is processed.

---

## Products

- Login Kit
- Content Posting API (Direct Post увімкнено)

## Redirect URI (Login Kit → Web)

https://dev-release.github.io/streamclipper/auth.html

Має збігатися символ у символ із `TIKTOK_REDIRECT_URI` у config.py.

---

## How each requested scope is used

**user.info.basic** — used to show which account the tool is connected to.
After authorization the tool reads the display name once and shows it in the
confirmation screen, so I can see I am about to publish to the right account.

**video.upload** — used to transfer a video file from my computer to my own
TikTok account. The file is a clip cut from my own stream recording. Every
upload is started manually by me.

**video.publish** — used to publish an approved clip with the caption I have
already seen and confirmed. Before every publish the tool shows a confirmation
screen with the account name, the privacy level options returned by TikTok,
the content disclosure toggles and the Music Usage Confirmation notice. Nothing
is scheduled, batched or published without my action.

---

## What the demo video must show (1–5 files, mp4/mov, max 50 MB each)

Запис екрана телефона, одним дублем, без монтажу. Знімати в пісочниці —
для несхвалених застосунків це вимога самої форми подання.

1. `/connect tiktok <client_key> <client_secret>` у Telegram → бот дає посилання
2. **Екран згоди TikTok повністю** — назва застосунку й усі три дозволи
3. Сторінка повернення з кодом → команда боту → «TikTok підключено: <нік>»
4. Готовий кліп у боті — з заголовком, описом і тегами
5. Кнопка TikTok → **екран підтвердження**: нік, вибір доступу, перемикачі
   розкриття, текст Music Usage Confirmation. Поклацати перемикачі
6. «Опублікувати» → «✅» → **не зупиняючи запис**, відкрити TikTok і показати
   ролик у профілі

У пісочниці доступний лише рівень «Тільки я» — це очікувано й перевіряльників
не бентежить.

---

## URLs

- Website: https://dev-release.github.io/streamclipper/
- Terms of Service: https://dev-release.github.io/streamclipper/terms.html
- Privacy Policy: https://dev-release.github.io/streamclipper/privacy.html

## Platform

Web — авторизація проходить через сторінку на тому ж домені, що й Website URL.
Сам інструмент працює на компʼютері власника акаунта.
