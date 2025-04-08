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




## Installation

- First, clone this repository:
    ```bash
    git clone https://github.com/your-username/neerex.git
    cd neerex
    ```

- Install all the required Python packages:
    ```bash
    pip install speechrecognition pyttsx3 gtts pygame keyboard opencv-python numpy pyautogui requests openai
    ```

- (Optional) If you face microphone/audio issues, install PyAudio from a `.whl` file as shown in this [guide](https://stackoverflow.com/a/55630212)

- Add your API keys in the `main.py` file:
    ```python
    client = OpenAI(api_key="your_openai_api_key")
    newsapi = "your_newsapi_key"
    ```

- Finally, run the assistant:
    ```bash
    python main.py
    ```

- Say any wake word like **"suno"**, **"start"**, **"shur karo"**, or **"neerex"** to begin using your voice assistant!


## Code Structure

├── driver
├── Neerex # Main folder for features
│ ├── config # Contains all secret API Keys
│ ├── features # All functionalities of Neerex
│ └── utils # GUI images or reusable utilities
├── init.py # Definition of feature's functions
├── gui.ui # GUI file (optional, if using PyQt/PySide)
├── main.py # Main driver program of Neerex
├── requirements.txt # All dependencies of the program

- The code structure is kept simple and modular. Easy to customize and scale.

- To add a new feature:
  - Create a new Python file inside the `features` folder and write your feature’s function
  - Add that function’s reference inside `__init__.py`
  - Add voice command keywords that will trigger this function during execution

