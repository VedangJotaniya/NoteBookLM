import os

def read_text_file(file_path):
    """Reads content from a given text file."""
    try:
        # Check if it exists as-is, otherwise check data/input/
        if not os.path.exists(file_path):
            potential_path = os.path.join("data", "input", file_path)
            if os.path.exists(potential_path):
                file_path = potential_path
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"Successfully read content from {file_path}")
        return content
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def ensure_dirs():
    """Ensure output directories exist."""
    os.makedirs("data/output", exist_ok=True)
