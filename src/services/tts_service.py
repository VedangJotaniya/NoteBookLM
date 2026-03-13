import os

class TTSService:
    def __init__(self, model_name="tts_models/en/ljspeech/vits"):
        self.model_name = model_name
        self.tts = None

    def _load_model(self):
        if self.tts is None:
            try:
                from TTS.api import TTS
                print(f"Loading Coqui TTS model: {self.model_name}...")
                self.tts = TTS(model_name=self.model_name, progress_bar=False, gpu=False)
            except ImportError:
                print("Error: 'TTS' library not found. Please install it using 'pip install TTS'.")
                return False
            except Exception as e:
                print(f"An error occurred while loading the TTS model: {e}")
                return False
        return True

    def convert_text_to_audio(self, text, output_filename="data/output/tutorial_audio.mp3"):
        """
        Converts text to an audio file using Coqui TTS.
        """
        if not self._load_model():
            return None

        try:
            print(f"Converting text to audio: {output_filename}...")
            # Synthesize the text to a file
            self.tts.tts_to_file(text=text, file_path=output_filename)
            print(f"Audio saved to {output_filename}")
            return output_filename
        except Exception as e:
            print(f"An error occurred during text-to-audio conversion: {e}")
            return None
