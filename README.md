# Neerex (AI Virtual Voice Assistant)

#### This is my attempt to create a smart voice-controlled assistant like JARVIS, named **Neerex**.
#### It's not a movie-level AI yet, but it can do a lot of useful and fun tasks on your PC/laptop — all with your voice.

## Built With

<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>

## Features

It can do a variety of tasks such as:

- Greet user based on time of day
- Activate with wake words: `suno`, `start`, `shur karo`, `neerex`
- Launch desktop applications (e.g., Notepad, Chrome)
- Perform Google searches
- Open websites directly
- Read top headlines using NewsAPI
- Take screenshots on voice command
- Start and stop screen recording
- Answer questions using OpenAI GPT (chatbot style)
- Speak using both pyttsx3 and GTTS (Google Text-to-Speech)
- Provide current time/date
- Shutdown or restart system
- Play YouTube videos based on query
- Exit or pause listening mode via command

## API Keys

To run this program, you’ll need the following API keys:

- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- [NewsAPI Key](https://newsapi.org/)

Add them in `main.py` file:

```python
client = OpenAI(api_key="your_openai_api_key")
newsapi = "your_newsapi_key"
