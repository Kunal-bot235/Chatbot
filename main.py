# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # Set up Chrome options
# chrome_options = Options()
# # Remove headless mode so the browser will be visible
# # chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")  # Unique user data directory
# chrome_options.add_argument("--no-sandbox")  # Useful for running in root mode
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Set up the WebDriver (update the path to your chromedriver)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# # List of URLs to scrape
# urls = [
#     "https://segment.com/docs/getting-started/",
#     "https://segment.com/docs/getting-started/01-what-is-segment/",
#     "https://segment.com/docs/getting-started/implementation-guide/",
#     "https://segment.com/docs/getting-started/02-simple-install/",
#     "https://segment.com/docs/getting-started/03-planning-full-install/",
#     "https://segment.com/docs/getting-started/04-full-install/",
#     "https://segment.com/docs/getting-started/05-data-to-destinations/",
#     "https://segment.com/docs/getting-started/06-testing-debugging/",
#     "https://segment.com/docs/getting-started/whats-next/",
#     "https://segment.com/docs/getting-started/use-cases/",
#     "https://segment.com/docs/getting-started/use-cases/guide/",
#     "https://segment.com/docs/getting-started/use-cases/setup/",
#     "https://segment.com/docs/getting-started/use-cases/reference/",
#     "https://segment.com/docs/guides/",
#     "https://segment.com/docs/guides/intro-impl/",
#     "https://segment.com/docs/guides/intro-user/",
#     "https://segment.com/docs/guides/intro-admin/",
#     "https://segment.com/docs/guides/filtering-data/",
#     "https://segment.com/docs/guides/duplicate-data/",
#     "https://segment.com/docs/guides/ignore-bots/",
#     "https://segment.com/docs/guides/segment-vs-tag-managers/",
#     "https://segment.com/docs/guides/what-is-replay/",
#     "https://segment.com/docs/guides/regional-segment/",
#     "https://segment.com/docs/guides/audiences-and-journeys/",
#     "https://segment.com/docs/guides/how-to-guides/",
#     "https://segment.com/docs/guides/how-to-guides/automated-multichannel-reengagement/",
#     "https://segment.com/docs/guides/how-to-guides/collect-on-client-or-server/",
#     "https://segment.com/docs/guides/how-to-guides/collect-pageviews-serverside/",
#     "https://segment.com/docs/guides/how-to-guides/create-push-notification/",
#     "https://segment.com/docs/guides/how-to-guides/cross-channel-tracking/",
#     "https://segment.com/docs/guides/how-to-guides/dynamic-coupon-program/",
#     "https://segment.com/docs/guides/how-to-guides/forecast-with-sql/",
#     "https://segment.com/docs/guides/how-to-guides/import-historical-data/",
#     "https://segment.com/docs/guides/how-to-guides/join-user-profiles/",
#     "https://segment.com/docs/guides/how-to-guides/measure-advertising-funnel/",
#     "https://segment.com/docs/guides/how-to-guides/measure-marketing-roi/",
#     "https://segment.com/docs/guides/how-to-guides/migrate-from-other-tools/",
#     "https://segment.com/docs/guides/how-to-guides/segment-and-attribution/",
#     "https://segment.com/docs/guides/how-to-guides/set-up-notifications-alerts/"
# ]

# # Open a text file to save the data
# with open("segment_docs.txt", "w", encoding="utf-8") as file:
#     for url in urls:
#         driver.get(url)

#         # Wait for a specific element to load (example: wait for the first <h1> tag to appear)
#         try:
#             # Wait until the <h1> tag is visible to confirm the page has loaded
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.TAG_NAME, 'h1'))
#             )
#             print(f"Page loaded successfully: {url}")

#             # Get the page source after it has been loaded
#             page_source = driver.page_source

#             # Parse the page using BeautifulSoup
#             soup = BeautifulSoup(page_source, "html.parser")

#             # Extract data from the page using BeautifulSoup
#             try:
#                 # Find all the relevant elements (headings, paragraphs, links, and tables)
#                 elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'span', 'li'])

#                 # Write the URL to the file as a header for context
#                 file.write(f"\n\nScraping Data from: {url}\n{'='*50}\n")

#                 # Loop through the elements and save them in the order
#                 for element in elements:
#                     if element.text.strip():  # Avoid writing empty strings
#                         file.write(f"{element.text.strip()}\n")

#                 # Handle tables: Extract data from tables and save as plain text
#                 tables = soup.find_all('table')
#                 for table in tables:
#                     for row in table.find_all('tr'):
#                         columns = row.find_all(['td', 'th'])
#                         columns_text = [col.get_text(strip=True) for col in columns]
#                         if columns_text:
#                             file.write("\t".join(columns_text) + "\n")

#                 print(f"Data saved for {url}")

#             except Exception as e:
#                 print(f"An error occurred while extracting data from {url}: {e}")

#         except Exception as e:
#             print(f"Error loading page {url}: {e}")

#         # Wait for 5 seconds before proceeding to the next URL
#         time.sleep(5)

# # Close the browser after all URLs are processed
# driver.quit()
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Set up WebDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# # List of base documentation URLs to start from
# base_urls = [
#     "https://docs.zeotap.com/home/en-us/",
#     "https://docs.lytics.com/",
#     "https://docs.mparticle.com/",
#     "https://segment.com/docs/?ref=nav"
# ]

# # Function to extract all links from a documentation homepage
# def get_all_links(base_url):
#     driver.get(base_url)
#     time.sleep(5)  # Give time for JavaScript to load
#     soup = BeautifulSoup(driver.page_source, "html.parser")
    
#     links = set()
#     for a_tag in soup.find_all("a", href=True):
#         href = a_tag["href"]
#         if href.startswith("/"):
#             href = base_url.rstrip("/") + href  # Convert relative URLs to absolute
#         if base_url in href:
#             links.add(href)
    
#     return list(links)

# # Collect all links from all documentation sites
# all_links = set()
# for base_url in base_urls:
#     print(f"Extracting links from {base_url}...")
#     try:
#         links = get_all_links(base_url)
#         all_links.update(links)
#         print(f"Found {len(links)} links in {base_url}")
#     except Exception as e:
#         print(f"Error extracting links from {base_url}: {e}")

# # Open a text file to save the scraped data
# with open("scraped_docs.txt", "w", encoding="utf-8") as file:
#     for url in all_links:
#         driver.get(url)
        
#         try:
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.TAG_NAME, 'h1'))
#             )
#             print(f"Scraping: {url}")
            
#             soup = BeautifulSoup(driver.page_source, "html.parser")
#             elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'span', 'li'])
            
#             file.write(f"\n\nScraping Data from: {url}\n{'='*50}\n")
#             for element in elements:
#                 if element.text.strip():
#                     file.write(f"{element.text.strip()}\n")
            
#             tables = soup.find_all('table')
#             for table in tables:
#                 for row in table.find_all('tr'):
#                     columns = row.find_all(['td', 'th'])
#                     columns_text = [col.get_text(strip=True) for col in columns]
#                     if columns_text:
#                         file.write("\t".join(columns_text) + "\n")
#             print(f"Data saved for {url}")
        
#         except Exception as e:
#             print(f"Error scraping {url}: {e}")
        
#         time.sleep(3)  # Delay to prevent rate-limiting

# # Close the browser
# driver.quit()
# print("Scraping complete.")
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/tmp/chrome_user_data")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# List of base documentation URLs
base_urls = [
    "https://docs.zeotap.com/home/en-us/",
    "https://docs.lytics.com/",
    "https://docs.mparticle.com/",
    "https://segment.com/docs/?ref=nav"
]

# Function to extract all links from a documentation homepage
def get_all_links(base_url):
    driver.get(base_url)
    time.sleep(5)  # Give time for JavaScript to load
    soup = BeautifulSoup(driver.page_source, "html.parser")

    links = set()
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.startswith("/") or base_url in href:
            full_link = href if href.startswith("http") else base_url.rstrip("/") + href
            links.add(full_link)

    return list(links)

# Collect all links from all documentation sites
all_links = set()
for base_url in base_urls:
    print(f"Extracting links from {base_url}...")
    try:
        links = get_all_links(base_url)
        all_links.update(links)
        print(f"Found {len(links)} links in {base_url}")
    except Exception as e:
        print(f"Error extracting links from {base_url}: {e}")

# Debugging: Print the number of collected links
print(f"Total unique links collected: {len(all_links)}")

# Open a text file to save the scraped data
with open("scraped_docs.txt", "w", encoding="utf-8") as file:
    for url in all_links:
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
            print(f"Scraping: {url}")

            soup = BeautifulSoup(driver.page_source, "html.parser")
            elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'span', 'li'])

            file.write(f"\n\nScraping Data from: {url}\n{'='*50}\n")
            for element in elements:
                if element.text.strip():
                    file.write(f"{element.text.strip()}\n")

            # Handle tables
            tables = soup.find_all('table')
            for table in tables:
                for row in table.find_all('tr'):
                    columns = row.find_all(['td', 'th'])
                    columns_text = [col.get_text(strip=True) for col in columns]
                    if columns_text:
                        file.write("\t".join(columns_text) + "\n")

            print(f"Data saved for {url}")

        except Exception as e:
            print(f"Error scraping {url}: {e}")

        time.sleep(3)  # Delay to prevent rate-limiting

# Close the browser
driver.quit()
print("Scraping complete.")
