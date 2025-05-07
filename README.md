SEO‑Scraper Python Toolkit
Welcome! This repository hosts a set of plug‑and‑play Python utilities that make common technical‑SEO chores—crawling, archiving, and metadata extraction—quick and painless. Every script has been fully anonymized so you can drop in your own URLs without worrying about client privacy.

What’s Inside
Script	Purpose (one‑liner)
HTML_Combiner.py	Merge a folder of HTML files into one consolidated text file—great for keyword analysis or bulk search.
internal_linking.py	Crawl a list of URLs and export every internal link to CSV for architecture audits.
json_html_scraper.py	Use Selenium to fetch raw HTML from a URL list and serialize to JSON.
meta_tag_scraper.py	Collect <title> and <meta description> tags from pages for quick meta audits.
scrape_to_pdf.py	Fetch page content with Requests + BeautifulSoup and compile results into a single PDF.
stealthy_scraper.py	Headless Selenium scraper with a minimal footprint; outputs to PDF.
ultra_stealthy_scraper.py	Beefed‑up stealth scraper with rotating user agents and random delays.

Each file begins with a succinct doc‑string that explains what it does and where to plug in your own inputs.

Quick Start
Clone the repository
git clone https://github.com/your‑org/seo‑scraper‑toolkit.git
cd seo‑scraper‑toolkit

(Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  (Windows: venv\Scripts\activate)

Install dependencies
pip install -r requirements.txt
Some scripts rely on Selenium; ensure you have a compatible browser driver (e.g., ChromeDriver) on your PATH.

Customize placeholders
Every script ships with the generic URL https://example.com/path. Replace these with your own targets. Example:
TARGET_URLS = ["https://your‑site.com/page‑1", "https://your‑site.com/page‑2"]

Run a script
python meta_tag_scraper.py
Outputs will appear in the project folder (e.g., meta_tags.csv, archive.pdf).

Requirements
Python 3.8 or newer

Libraries listed in requirements.txt (requests, beautifulsoup4, pandas, selenium, pdfkit, etc.)

Chrome or Firefox plus the matching WebDriver for Selenium scripts

wkhtmltopdf if you use pdfkit

Contributing
Fork the repo and create a feature branch: git checkout -b feature/awesome‑idea

Commit your changes: git commit -m "feat: add awesome idea"

Push to GitHub: git push origin feature/awesome‑idea

Open a Pull Request

Bug reports, feature suggestions, and performance tweaks are all welcome. Please keep any client‑specific data out of your contributions.

License
Released under the GNU General Public License v3.0. See the LICENSE file for details.

Acknowledgements
Huge thanks to the SEO and Python communities for continually sharing knowledge and tooling. If you find this useful, feel free to star the repo, fork it, or open an issue with feedback.

Happy scraping!

Daniel Brinker
