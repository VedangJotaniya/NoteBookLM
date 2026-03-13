import os
import sys
from src.services.ollama_service import OllamaService
from src.services.tts_service import TTSService
from src.utils.file_handler import read_text_file, ensure_dirs

def main():
    print("==========================================")
    print("Welcome to NotebookLM Local Implementation!")
    print("==========================================")
    
    # Initialize services
    ollama = OllamaService(model="phi3:3.8b") # Defaulting to phi3:3.8b, can be changed
    tts_service = TTSService()
    ensure_dirs()

    file_path = input("Please enter the path or name of the text file in 'data/input/': ")

    # Step 1: Read the text file
    original_text = read_text_file(file_path)
    if not original_text:
        return

    # Step 2: Generate summary using Ollama
    print("\n[AI] Generating summary using Ollama...")
    summary = ollama.summarize(original_text)
    
    if not summary:
        print("Failed to generate summary. Check if Ollama is running.")
        return

    print("\n--- Generated Summary ---")
    print(summary)

    # Step 3: Convert to tutorial using Ollama
    print("\n[AI] Converting summary to tutorial using Ollama...")
    tutorial_content = ollama.generate_tutorial(summary)
    
    if not tutorial_content:
        print("Failed to generate tutorial.")
        return

    print("\n--- Generated Tutorial ---")
    print(tutorial_content)

    # Step 4: Convert tutorial to audio
    output_audio = "data/output/tutorial_audio.mp3"
    audio_file = tts_service.convert_text_to_audio(tutorial_content, output_audio)
    
    if audio_file:
        print(f"\n[Success] Audio tutorial created at: {os.path.abspath(audio_file)}")
    else:
        print("\n[Error] Audio conversion failed.")

if __name__ == "__main__":
    main()
