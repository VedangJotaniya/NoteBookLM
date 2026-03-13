# NotebookLM Local Implementation

A Python-based local implementation of a NotebookLM-like workflow. This project transforms local text files into concise summaries, structured tutorials, and synthesized audio format using local AI models.

## 🚀 Features

- **Text Processing**: Robust reading and processing of local text files.
- **AI Summarization**: Powered by **Ollama** (e.g., Llama 3) for high-quality, local LLM summarization.
- **Tutorial Generation**: Automatically converts summaries into educational, step-by-step tutorials using Ollama.
- **Local Text-to-Audio**: Converts tutorials into MP3 audio files using **Coqui TTS**.
- **Privacy Focused**: No external cloud APIs are used; everything runs on your machine.

## 🛠️ Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) (Installed and running)
- [Coqui TTS](https://github.com/coqui-ai/TTS)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vedangjotaniya/NotebookLM.git
   cd NotebookLM
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull the LLM model**:
   ```bash
   ollama pull llama3
   ```

## 📖 Usage

1. **Place your input files**: Put your `.txt` files in the `data/input/` directory.
2. **Run the application**:
   ```bash
   python notebook_lm.py
   ```
3. **Follow the prompt**: Enter the name of your file (e.g., `sample_text.txt`).
4. **Retrieve Output**: 
   - Summary and Tutorial will be displayed in the terminal.
   - The audio file will be saved in `data/output/tutorial_audio.mp3`.

## 📂 Project Structure

```text
NotebookLM/
├── data/
│   ├── input/           # Place source .txt files here
│   └── output/          # Generated audio files
├── src/
│   ├── services/
│   │   ├── ollama_service.py  # AI Generation logic
│   │   └── tts_service.py     # Text-to-Speech logic
│   └── utils/
│       └── file_handler.py    # File I/O operations
├── notebook_lm.py       # Main entry point
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## ⚙️ How it Works

The project follows a modular 4-step pipeline:
1. **Read**: Extracts text via `src/utils/file_handler.py`.
2. **Summarize**: Real-time summary generation using the local Ollama API.
3. **Tutorialize**: Structures content using Ollama with custom system prompts.
4. **Synthesize**: High-quality audio generation via `src/services/tts_service.py`.

## 📄 License

[MIT License](LICENSE)
