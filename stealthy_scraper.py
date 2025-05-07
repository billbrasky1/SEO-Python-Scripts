"""
Script: stealthy_scraper.py
Purpose: Leverages headless Selenium to scrape webpages stealthily and save their contents into a PDF.
Note: All URLs, paths, domains, and proprietary identifiers have been replaced with generic placeholders for demonstration purposes.
"""

from selenium import webdriver
from fpdf import FPDF
import time
import re

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# List of URLs to scrape
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
    "https://example.com/path"
]



# Initialize a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Function to clean content (remove unsupported characters)
def clean_content(content):
    # Replace smart quotes and other problematic characters
    content = content.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    content = re.sub(r'[^\x00-\x7F]+', ' ', content)  # Remove non-ASCII characters
    return content

# Function to scrape content using Selenium
def scrape_content(url):
    try:
        driver.get(url)
        time.sleep(3)  # Give time for JavaScript to execute (increase if needed)
        
        content = driver.find_element("tag name", "body").text
        return content
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return f"Error fetching {url}\n"

# Loop through URLs and add content to the PDF
for url in urls:
    content = scrape_content(url)
    content = clean_content(content)  # Clean the content
    
    # Add a new page for each URL
    pdf.add_page()
    pdf.cell(200, 10, txt=f"Content from {url}", ln=True, align='C')
    
    # Adds the cleaned text content to the PDF, handling encoding issues
    pdf.multi_cell(0, 10, txt=content)

# Save the PDF file
output_filename = "Elastic_scrape.pdf"
pdf.output(output_filename)
print(f"PDF created successfully: {output_filename}")

# Close the Selenium driver
driver.quit()