# Neerex - AI Virtual Voice Assistant

**Neerex** ek voice-controlled AI assistant hai jo Python mein bana hai. Yeh aapki awaaz se system ke tasks, web search, screen recording, news reading aur kai aur kaam karta hai. Isme OpenAI ka GPT model bhi integrated hai jo smart responses deta hai.

---

## 🔧 Features

- 🎙️ Voice command recognition (English + Hindi)
- 🧠 AI answers via OpenAI GPT
- 🌐 Web browsing aur Google search
- 🖥️ Applications open karna (e.g. Notepad, Chrome)
- 🖼️ Screenshot lena
- 📹 Screen recording with voice command
- 📰 News headlines sunana (via NewsAPI)
- 🔊 Text-to-speech (GTTS + Pygame)
- 🕒 Time-based greetings
- 🔌 System shutdown / restart
- 🎬 YouTube video search aur auto-play

---

## 💻 Installation & Setup

### 1. Clone ya code download karo

```bash
git clone https://github.com/your-username/neerex.git
cd neerex
Required packages install karo:

bash
Copy
Edit
pip install speechrecognition pyttsx3 gtts pygame keyboard opencv-python numpy pyautogui requests openai
API Keys add karo main.py mein:

python
Copy
Edit
client = OpenAI(api_key="your_openai_api_key")
newsapi = "your_newsapi_key"
 API Keys ke liye:

OpenAI → https://platform.openai.com/account/api-keys

NewsAPI → https://newsapi.org/

 How to Run
bash
Copy
Edit
python main.py
Fir assistant wake word sunega. Aap bol sakte ho:

suno

start

shur karo

neerex

Uske baad assistant active hoke aapke commands sunega. Aap bol sakte ho:

open notepad

search python tutorial

start screen recording

news

shutdown

exit (command mode band karne ke liye)

🎙️ Sample Commands
🗣 Command	✅ Action
open notepad	Notepad kholta hai
search python tips	Google search karta hai
screenshot	Screenshot leta hai
news	Latest headlines sunata hai
shutdown	System shutdown hota hai
start screen recording	Screen recording start karta hai
exit / stop / back	Assistant listening band kar deta
