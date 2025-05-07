"""
Script: internal_linking.py
Purpose: Crawls specified blog article URLs, extracts internal links from each, and outputs the results to a CSV for analysis.
Note: All URLs, paths, domains, and proprietary identifiers have been replaced with generic placeholders for demonstration purposes.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 🔍 Blog posts to crawl
blog_urls = [
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
    # Add more if needed
]

# 🎯 Product / feature / solution URLs to track
target_urls = [
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    "https://example.com/path",
    # Add more as needed
]

# ⚙️ Link matching logic
def is_product_link(href, targets):
    return any(target in href for target in targets)

# 🧪 Collect blog links to target pages
data = []

for blog in blog_urls:
    try:
        r = requests.get(blog, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            if is_product_link(href, target_urls):
                data.append({
                    "blog_post": blog,
                    "linked_page": href,
                    "anchor_text": a.get_text(strip=True)
                })
    except Exception as e:
        print(f"Error fetching {blog}: {e}")

# 🧾 Create DataFrame and summary
df = pd.DataFrame(data)
summary = df.groupby("linked_page").agg(link_count=('blog_post', 'count')).reset_index()

# 💾 Save results
df.to_csv("blog_to_product_links.csv", index=False)
summary.to_csv("internal_link_summary.csv", index=False)

print("✅ Analysis complete. Files saved:")
print("- blog_to_product_links.csv")
print("- internal_link_summary.csv")
