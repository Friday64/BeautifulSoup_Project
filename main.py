import requests
import os

def save_html_once(url, filename):
    headers = {
        "User-Agent": "SimpleHTMLFetcher/1.0 (http://mywebsite.com/info)"
    }

    try:
        # Fetch the HTML content
        response = requests.get(url, headers=headers, timeout=5)  # Fixed: lowercase 'headers'

        # Check if request was successful
        if response.status_code == 200:
            # Save the contents to a file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"HTML content of {url} has been saved to {filename}")
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error has occurred: {e}")

# Correct URL and filename
save_html_once("https://www.sciencenews.org/", "C:/Users/mcfra/Desktop/scienceNews.html")
