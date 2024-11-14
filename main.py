import requests
import os
def save_html_once(url, filename):
    headers ={
        "user-Agent":"SimpleHTMLFetcher/1.0 (http://mywebsite.com/info)"
    }

    try:
        #fetch the HTML content
        response = requests.get(url, Headers = headers, timeout=5)

        #check if request was successful 
        if response.status_code == 200:
            # Save the contents to a file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"HtMLcontent of {url} has been saved to {filename}")
        else:
            print(f"Failed to fetch {url}, Satus code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error has occured: {e}")
    save_html_once("https:/https://www.sciencenews.org/", "/Users/yourname/Desktop/scienceNews.html")