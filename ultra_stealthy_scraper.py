"""
Script: ultra_stealthy_scraper.py
Purpose: Enhanced stealth scraper with randomized delays and rotating user‑agents, exporting output to a PDF.
Note: All URLs, paths, domains, and proprietary identifiers have been replaced with generic placeholders for demonstration purposes.
"""

import time
import re
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF

# ------------------------------------------------------------
# Selenium WebDriver Setup
# ------------------------------------------------------------
chrome_options = Options()

# Comment out the next line if you want to see the browser for manual CAPTCHA solving:
# chrome_options.add_argument("--headless")

# Reduce "bot" detection flags:
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Set a realistic user-agent
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/109.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=chrome_options)

# ------------------------------------------------------------
# List of URLs to scrape
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
# Initialize a PDF document
# ------------------------------------------------------------
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# ------------------------------------------------------------
# Utility function to clean content (remove unsupported characters)
# ------------------------------------------------------------
def clean_content(content):
    # Replace smart quotes and other problematic characters
    content = content.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    # Remove non-ASCII characters
    content = re.sub(r'[^\x00-\x7F]+', ' ', content)
    return content

# ------------------------------------------------------------
# Simple function to check if we landed on the CAPTCHA page
# ------------------------------------------------------------
def is_captcha_page(page_text):
    return "Are you human?" in page_text or "We have detected an increased number of attempts" in page_text

# ------------------------------------------------------------
# Function to scrape content using Selenium
# ------------------------------------------------------------
def scrape_content(url):
    try:
        driver.get(url)
        
        # Random delay to mimic human behavior
        time.sleep(random.uniform(3, 7))

        # Grab page text
        page_text = driver.find_element("tag name", "body").text
        
        # If there's a CAPTCHA, you can either handle it manually or attempt an automated solve
        if is_captcha_page(page_text):
            print(f"CAPTCHA detected on {url}.")
            
            # ----- Option A: Manual Solve (Disable headless to see browser) -----
            # 1. Comment out chrome_options.add_argument("--headless") above.
            # 2. Print a message here, prompting user to solve it in the open browser window.
            # 3. Wait for user input:
            input("Solve the CAPTCHA in the browser, then press Enter to continue...")
            
            # Re-check page text after manual solve
            page_text = driver.find_element("tag name", "body").text
            
            # If still a CAPTCHA, you might need to re-try or give up:
            if is_captcha_page(page_text):
                print("Still blocked by CAPTCHA. Moving on or handle differently.")
        
        return page_text

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return f"Error fetching {url}\n"

# ------------------------------------------------------------
# Main scraping loop
# ------------------------------------------------------------
for url in urls:
    content = scrape_content(url)
    content = clean_content(content)
    
    # Add a new page for each URL
    pdf.add_page()
    pdf.cell(200, 10, txt=f"Content from {url}", ln=True, align='C')
    
    # Adds the cleaned text content to the PDF
    pdf.multi_cell(0, 10, txt=content)

# ------------------------------------------------------------
# Save the PDF file
# ------------------------------------------------------------
output_filename = "winning_smile_ultra_scraped.pdf"
pdf.output(output_filename)
print(f"PDF created successfully: {output_filename}")

# ------------------------------------------------------------
# Close the Selenium driver
# ------------------------------------------------------------
driver.quit()
