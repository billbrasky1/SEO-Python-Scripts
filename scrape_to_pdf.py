"""
Script: scrape_to_pdf.py
Purpose: Fetches page content with requests/BeautifulSoup and compiles it into a PDF document.
Note: All URLs, paths, domains, and proprietary identifiers have been replaced with generic placeholders for demonstration purposes.
"""

import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

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
    # Add more URLs as needed
]

# Initialize a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Function to scrape content from a URL
def scrape_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract text content; customize this based on your needs
        content = soup.get_text(separator="\n", strip=True)
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return f"Error fetching {url}\n"

# Loop through URLs and add content to the PDF
for url in urls:
    content = scrape_content(url)
    
    # Add a new page for each URL
    pdf.add_page()
    pdf.cell(200, 10, txt=f"Content from {url}", ln=True, align='C')
    
    # Adds the text content to the PDF, handling encoding errors
    pdf.multi_cell(0, 10, txt=content.encode('latin1', 'ignore').decode('latin1'))

# Save the PDF file
output_filename = "GenericName_scraped_content.pdf"
pdf.output(output_filename)
print(f"PDF created successfully: {output_filename}")