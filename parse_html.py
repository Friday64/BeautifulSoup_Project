import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_html_to_dataframe(html_file, output_csv=None, article_tag='article', title_tag='h2', link_tag='a'):
    """
    Parses an HTML file to extract article titles and links, then saves them to a CSV.

    Args:
        html_file (str): Path to the HTML file to parse.
        output_csv (str): Optional. Path to save the parsed data as a CSV. Defaults to DESKTOP_PATH.
        article_tag (str): Tag representing an article in the HTML.
        title_tag (str): Tag representing the title within an article.
        link_tag (str): Tag representing the link within an article.

    Returns:
        pd.DataFrame: DataFrame containing parsed titles and links, or None if an error occurs.
    """
    try:
        # Get desktop path from .env
        desktop_path = os.getenv("DESKTOP_PATH")
        if not desktop_path:
            raise ValueError("DESKTOP_PATH is not set in the .env file.")

        if not output_csv:
            output_csv = os.path.join(desktop_path, "parsed_data.csv")
        
        logging.info(f"Desktop path: {desktop_path}")
        logging.info(f"Output CSV path: {output_csv}")

        # Open and read the HTML file
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract data
        articles = []
        for article in soup.find_all(article_tag):
            title = article.find(title_tag).get_text(strip=True) if article.find(title_tag) else None
            link = article.find(link_tag)['href'] if article.find(link_tag) else None
            articles.append({'Title': title, 'Link': link})

        # Convert to DataFrame
        df = pd.DataFrame(articles)
        logging.info("Parsed data:")
        logging.info(df)

        # Save to CSV
        logging.info(f"Saving DataFrame to {output_csv}")
        df.to_csv(output_csv, index=False, encoding='utf-8')
        logging.info(f"Data saved to {output_csv}")

        return df

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
