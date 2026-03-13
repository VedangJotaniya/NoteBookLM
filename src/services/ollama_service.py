import requests
import json

class OllamaService:
    def __init__(self, base_url="http://localhost:11434", model="llama3"):
        self.base_url = f"{base_url}/api/generate"
        self.model = model

    def generate(self, prompt, system_prompt=None):
        """
        Sends a request to the local Ollama API.
        """
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if system_prompt:
            payload["system"] = system_prompt

        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            return None

    def summarize(self, text):
        system_prompt = "You are a helpful assistant that provides concise and accurate summaries of long-form text."
        prompt = f"Please provide a comprehensive summary of the following text:\n\n{text}"
        return self.generate(prompt, system_prompt)

    def generate_tutorial(self, summary):
        system_prompt = "You are an educator who creates structured, easy-to-follow tutorials based on complex summaries."
        prompt = f"Convert the following summary into a structured tutorial with 3-5 clear steps:\n\n{summary}"
        return self.generate(prompt, system_prompt)
