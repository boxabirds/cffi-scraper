from curl_cffi import requests 
from pathlib import Path
import sys
import re

def get_tripadvisor_homepage():
    """Gets the contents of the tripadvisor homepage using curl_cffi."""
    try:
        # Use impersonate to mimic a real browser
        # tripadvisor has notoriously powerful anti-scraping measures but this seems to work
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
    if len(sys.argv) < 2:
        print("Usage: python scrape.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    # domain = re.search(r'https?://([^/]+)', url).group(1)
    content = requests.get(url, impersonate="chrome").content
    if content:
        save_to_file(content, Path(f"output/{url.replace('https://', '').replace('http://', '')}/index.html"))
