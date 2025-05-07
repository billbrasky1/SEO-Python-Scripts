# SEO‑Scraper Toolkit

Welcome!  
This repository contains a set of **plug‑and‑play Python utilities** that streamline repetitive technical‑SEO tasks—crawling, archiving, and metadata extraction—so you can spend more time on strategy and less on busywork.

> **Why share these?**  
> I’ve used variations of these scripts on dozens of audits and content projects. After scrubbing all client‑specific details (every URL, brand name, and personal reference has been replaced with generic placeholders), I’m open‑sourcing the toolkit for the SEO community.

---

## 🔧 What's Inside?

| Script | Purpose (one‑liner) |
| ------ | ------------------ |
| **HTML_Combiner.py** | Merge a folder of HTML files into one consolidated text file (handy for keyword analysis). |
| **internal_linking.py** | Crawl a list of URLs and export all internal links to CSV for architecture audits. |
| **json_html_scraper.py** | Fetch raw HTML for each URL via Selenium and save it to a JSON array. |
| **meta_tag_scraper.py** | Collect `<title>` and `<meta description>` from pages—perfect for quick meta audits. |
| **scrape_to_pdf.py** | Grab page content with Requests/BeautifulSoup and compile the results into a single PDF. |
| **stealthy_scraper.py** | Headless Selenium scraper with minimal footprint; outputs to PDF. |
| **ultra_stealthy_scraper.py** | A beefed‑up version with rotating user‑agents and random delays for extra stealth. |

All files start with a short doc‑string explaining what they do and where to drop your own inputs.

---

## 🚀 Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/your‑org/seo‑scraper‑toolkit.git
   cd seo‑scraper‑toolkit
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Heads‑up:
Some scripts rely on Selenium. You’ll need a compatible browser driver
(e.g., ChromeDriver) on your PATH.

Customize placeholders

The repo ships with the generic URL https://example.com/path.
Replace these with your targets before running:

python
Copy
Edit
TARGET_URLS = [
    "https://your‑site.com/page‑1",
    "https://your‑site.com/page‑2",
]
Run a script

bash
Copy
Edit
python meta_tag_scraper.py
Outputs land in the same folder (e.g., meta_tags.csv, archive.pdf, etc.).

📄 Requirements
Python 3.8+

Common libraries (requests, beautifulsoup4, pandas, selenium, pdfkit, etc.)
→ see requirements.txt for the exact list

(Optional) Chrome or Firefox + the matching WebDriver for Selenium scripts

wkhtmltopdf if you use pdfkit

🙌 Contributing
Fork the project & create your branch:
git checkout -b feature/awesome‑idea

Commit your changes:
git commit -m "feat: add awesome idea"

Push to the branch:
git push origin feature/awesome‑idea

Open a Pull Request 🚀

Bug reports, feature suggestions, and performance tweaks are all welcome.
Please keep any client‑specific data out of the PRs.

📜 License
Released under the GNU General Public License v3.0.
See LICENSE for details.

✨ Acknowledgements
Big thanks to the SEO and Python communities for continually sharing knowledge and tooling.
If you find this repo useful, feel free to ⭐ it, fork it, or drop feedback in Issues!

Happy scraping,

Daniel Brinker
