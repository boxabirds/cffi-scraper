from curl_cffi import requests 
from pathlib import Path
def get_tripadvisor_homepage():
    """Gets the contents of the tripadvisor homepage using curl_cffi."""
    try:
        # Use impersonate to mimic a real browser
        response = requests.get("https://www.tripadvisor.com/", impersonate="chrome")
        return response.content
    except Exception as e:
        print(f"Error getting tripadvisor homepage: {e}")
        return None

def save_to_file(content, filepath):
    """Saves the content to a specified file."""
    try:
        # Ensure the directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with filepath.open('wb') as file:
            file.write(content)
        print(f"Content saved to {filepath}")
    except Exception as e:
        print(f"Error saving content to file: {e}")

if __name__ == "__main__":
    content = get_tripadvisor_homepage()
    if content:
        save_to_file(content, Path("output/tripadvisor/index.html"))
