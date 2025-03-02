Overview

This project is a web scraper built using Selenium and BeautifulSoup to extract documentation content from multiple sources. The scraped data is saved in a text file for further analysis or processing.

Features

Uses Selenium for dynamic content loading.

Parses and extracts text content with BeautifulSoup.

Saves extracted content into scraped_docs.txt.

Supports multiple documentation websites.

Handles tables, links, and various heading levels.

Requirements

Make sure you have the following dependencies installed:

pip install selenium beautifulsoup4 webdriver-manager

Setup

Clone this repository:

git clone https://github.com/Kunal-bot235/Chatbot.git
cd Chatbot

Install dependencies:

pip install -r requirements.txt

Run the scraper:

python main.py

Configuration

The scraper visits a list of documentation sites, defined in the base_urls list inside main.py. You can modify or add more URLs as needed:

base_urls = [
    "https://docs.zeotap.com/home/en-us/",
    "https://docs.lytics.com/",
    "https://docs.mparticle.com/",
    "https://segment.com/docs/?ref=nav"
]

Output

The scraped content is saved in scraped_docs.txt. The file contains:

Extracted text from headings, paragraphs, lists, and links.

Table contents formatted with tab spacing.

Sections clearly separated by the source URL.

Notes

The script includes a 5-second delay to allow JavaScript elements to load before scraping.

If a website has rate-limiting, adjust time.sleep(3) between requests.

Issues

If you encounter issues with large files, consider using Git Large File Storage (LFS):

git lfs track "*.txt"
git add .gitattributes scraped_docs.txt
git commit -m "Enable LFS for large files"

License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

