import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def parse_html_to_dataframe(html_file, output_csv=None):
    try:
        # Get desktop path from .env
        desktop_path = os.getenv("DESKTOP_PATH", "C:/Users/mcfra/Desktop")
        if not output_csv:
            output_csv = os.path.join(desktop_path, "parsed_data.csv")
        
        print(f"Desktop path: {desktop_path}")
        print(f"Output CSV path: {output_csv}")

        # Open and read the HTML file
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract data (e.g., article titles and links)
        articles = []
        for article in soup.find_all('article'):
            title = article.find('h2').get_text(strip=True) if article.find('h2') else None
            link = article.find('a')['href'] if article.find('a') else None
            articles.append({'Title': title, 'Link': link})

        # Convert to DataFrame
        df = pd.DataFrame(articles)
        print("Parsed data:")
        print(df)

        # Save to CSV
        print(f"Saving DataFrame to {output_csv}")
        df.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"Data saved to {output_csv}")

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()
