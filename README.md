# Voice Recognition System

A Python-based voice-activated assistant that listens to user commands, searches Wikipedia for information, and reads the results aloud using text-to-speech technology.

## Features

- **Speech Recognition** — Converts spoken words into text using Google Speech Recognition API
- **Wikipedia Search** — Automatically searches Wikipedia based on voice commands
- **Text-to-Speech** — Reads Wikipedia summaries aloud using pyttsx3
- **Real-Time Listening** — Listens through the computer's microphone in real time

## Prerequisites

- Python 3.7+
- A working microphone
- Internet connection (required for Google Speech Recognition and Wikipedia API)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/coder11293/Voice_Recognition.git
cd Voice_Recognition
```

2. Install the required dependencies:

```bash
pip install SpeechRecognition pyttsx3 wikipedia
```

## Usage

Run the script:

```bash
python voice_recognition.py
```

1. The program will start listening through your microphone
2. Speak your query clearly (e.g., "Python programming language")
3. The program will search Wikipedia and read the summary aloud

## Dependencies

| Library | Purpose |
|---------|---------|
| `SpeechRecognition` | Converts speech to text |
| `pyttsx3` | Text-to-speech conversion |
| `wikipedia` | Fetches data from Wikipedia |

## How It Works

1. **Initialize** — The text-to-speech engine and speech recognizer are set up
2. **Listen** — The microphone captures audio input from the user
3. **Recognize** — Google Speech Recognition API converts audio to text
4. **Search** — The recognized text is used as a query to fetch a Wikipedia summary
5. **Respond** — The summary is displayed in the terminal and read aloud

## License

This project is open source and available for educational purposes.

## Author

**coder11293** — [GitHub Profile](https://github.com/coder11293)
