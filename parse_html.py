import pandas as pd
from bs4 import BeautifulSoup

def parse_html_to_dataframe(html_file, output_csv=None):
    """
    Parse the saved HTML file and extract data into a pandas DataFrame.

    Args:
        html_file (str): Path to the saved HTML file.
        output_csv (str): (Optional) Path to save the DataFrame as a CSV file.

    Returns:
        pd.DataFrame: The extracted data as a DataFrame.
    """
    try:
        # Open and read the HTML file
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Extract data (e.g., article titles and links)
        articles = []
        for article in soup.find_all('article'):  # Adjust based on actual HTML structure
            title = article.find('h2').get_text(strip=True) if article.find('h2') else None
            link = article.find('a')['href'] if article.find('a') else None
            articles.append({'Title': title, 'Link': link})

        # Convert to DataFrame
        df = pd.DataFrame(articles)

        # Save to CSV if output_csv is provided
        if output_csv:
            df.to_csv(output_csv, index=False, encoding='utf-8')
            print(f"Data saved to {output_csv}")

        return df

    except Exception as e:
        print(f"An error occurred while parsing: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
