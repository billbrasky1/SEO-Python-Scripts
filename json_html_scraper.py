"""
Script: json_html_scraper.py
Purpose: Uses Selenium to fetch raw HTML for a list of pages and serializes them to a JSON file.
Note: All URLs, paths, domains, and proprietary identifiers have been replaced with generic placeholders for demonstration purposes.
"""

import time
import random
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ------------------------------------------------------------
# 1. Selenium WebDriver Setup
# ------------------------------------------------------------
chrome_options = Options()

# If you need to manually solve CAPTCHA or debug, comment out this line:
#chrome_options.add_argument("--headless")

# Try to reduce Selenium "bot" fingerprinting
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Provide a "realistic" user-agent
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/109.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=chrome_options)

# ------------------------------------------------------------
# 2. List of URLs to scrape
# ------------------------------------------------------------
urls = [
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path"
]

# ------------------------------------------------------------
# 3. Scrape and Collect HTML
# ------------------------------------------------------------
all_pages_data = []

for url in urls:
    print(f"Scraping: {url}")
    driver.get(url)
    # Random delay to look less like a bot
    time.sleep(random.uniform(3, 7))

    # Get the raw HTML of the page
    html_content = driver.page_source

    # Store in a dict to keep track of URL + HTML
    all_pages_data.append({
        "url": url,
        "html": html_content
    })

# ------------------------------------------------------------
# 4. Write All Pages to a Single JSON File
# ------------------------------------------------------------
output_file = "dental office_all_pages.json"

with open(output_file, "w", encoding="utf-8") as f:
    # indent=2 for readability; ensure_ascii=False to keep special chars
    json.dump(all_pages_data, f, ensure_ascii=False, indent=2)

print(f"All page data saved to {output_file}")

# ------------------------------------------------------------
# 5. Close Browser
# ------------------------------------------------------------
driver.quit()
print("Done.")
