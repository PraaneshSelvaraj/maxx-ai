# Maxx-AI

Maxx-AI is an open-source gen ai voice assistant.

## Prerequisites

Before running Maxx-AI, ensure you have the following:

- `ffplay` installed (download and install from [FFmpeg](https://ffmpeg.org/download.html))
- Environment variables set for the following API keys:
    - `groq_api_key`: Your Groq API key
    - `deepgram_api_key`: Your Deepgram API key
    - `wit_ai_key`: Your Wit.ai API key

## Installation
You can easily install Maxx-AI by following these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/PraaneshSelvaraj/maxx-ai.git
    ```
2. Install dependencies:

    ```bash
    cd voice-assistant
    pip install -r requirements.txt
    ```

## Usage
### Starting the Assistant:

Run the main script:
```bash
    python main.py
```
### Activating the Assistant:

1. **Taskbar:**

    Once Maxx-AI is running, locate the Maxx-AI icon on your taskbar. Click on the icon to activate the assistant.

2. **Keyboard Shortcut:**

    Alternatively, you can activate the assistant using a keyboard shortcut. Press the specified key combination (default: ctrl+alt+space) to trigger Maxx-AI to start listening.
