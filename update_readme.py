from datetime import datetime
import pytz

# India Time
tz = pytz.timezone("Asia/Kolkata")
now = datetime.now(tz)

time_str = now.strftime("%d %B %Y | %I:%M %p IST")

content = f"""
<h1 align="center">Hi 👋, I'm Akshay Kumar</h1>

<p align="center">
🚀 Full Stack & AI Enthusiast <br>
💻 Building Daily <br>
🔥 Consistency is Power
</p>

---

## 🌐 Socials:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akshay-kumar-k786/)

---

## ⏳ Last Updated:
🟢 {time_str}

---

# 💻 Tech Stack:
(Your existing badges remain here)
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
