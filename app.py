from flask import Flask, send_file
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

# רשימת 31 הודעות שיווקיות
messages = [
    "🚀 Just launched Wardon's POC – Try it now!",
    "🎯 New feature: Role-based access control!",
    "🔐 Real-time threat detection is now smarter!",
    "📊 SOC 2 dashboard – beta available!",
    "💡 Built with passion by Moti Kalimi",
    "☁️ Cloud-first, security-always – Wardon",
    "🔄 Instant IP blocklisting – with 1 click",
    "📈 Monitor threats in real-time",
    "🧠 Machine learning-based detection just got better",
    "🛡️ DDoS protection built-in",
    "📁 Data encryption at the highest level",
    "🧪 Try our vulnerability scanner now",
    "📅 7-day free access – no credit card",
    "📤 Centralized access control for the cloud",
    "🎛️ Fully customizable alert system",
    "🔍 Geolocation filtering is now live!",
    "📢 GDPR & SOC 2 ready reports – try now",
    "🌐 Built for AWS, Azure & GCP",
    "⚙️ API-first. DevOps-friendly. Wardon.",
    "🧰 Simplified cloud compliance",
    "🧱 Stop misconfigurations before they spread",
    "🚨 Get alerts when you need them – not after",
    "👨‍💻 Made for security engineers, by security engineers",
    "🧭 Built to support startups and enterprises alike",
    "💼 Manage multiple projects from one dashboard",
    "📍 Location-based access enforcement",
    "🧬 Smart behavior analytics built in",
    "🔔 Never miss a threat again – real-time alerts",
    "📊 All logs, fully searchable – all yours",
    "🛠️ Your cloud. Our security. Wardon.",
    "💬 Feedback drives our roadmap – talk to us!"
]

@app.route("/banner.png")
def banner():
    today = datetime.utcnow().day
    message = messages[(today - 1) % len(messages)]

    # יצירת תמונה
    img = Image.new('RGB', (700, 80), color=(234, 244, 255))  # רקע כחול בהיר
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("David.ttf", 28)  # גופן דוד (אם נתמך)
    except:
        font = ImageFont.load_default()

    # ציור מלבן למסגור
    draw.rectangle([(0, 0), (699, 79)], outline=(180, 180, 180), width=1)  # מסגרת אפורה
    draw.text((20, 22), message, fill=(0, 0, 0), font=font)

    # החזרת התמונה כ-response
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route("/")
def home():
    return "Wardon Banner API is running. Use /banner.png to get today's message."

if __name__ == "__main__":
    app.run(debug=True)
