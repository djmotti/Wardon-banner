# Wardon Dynamic Banner API

This is a simple Flask-based API that generates a dynamic marketing banner for email signatures.
It displays one of 31 promotional messages, based on the day of the month.

## 🛡️ Live Endpoint

**Banner Image URL:**
```
https://wardon-banner.onrender.com/banner.png
```

You can embed this image directly in your email signature:
```html
<img src="https://wardon-banner.onrender.com/banner.png" alt="Wardon Daily Message">
```

## 🚀 How it works
- Built with Python, Flask, and Pillow.
- On each request to `/banner.png`, it generates a PNG with the message of the day.
- 31 messages rotate based on the current UTC day.

## 🔧 Deployment

To deploy your own version:
1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run locally:
   ```bash
   python app.py
   ```
4. Or deploy to Render using:
   - Build command: *(leave empty)*
   - Start command: `gunicorn app:app`

## ✍️ Created by
**Moti Kalimi** – Founder & Developer of Wardon
📩 moti.wardon@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/moti-kalimi)
