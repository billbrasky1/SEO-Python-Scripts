"""
Script: HTML_Combiner.py
Purpose: Combines individual HTML files from a directory into a single consolidated text file with URL headers.
Note: All URLs, paths, domains, and proprietary identifiers have been replaced with generic placeholders for demonstration purposes.
"""

import os
from pathlib import Path

# Input folder: Desktop/GenericName_Scrape
input_dir = Path.home() / "Desktop" / "GenericName_HTML_Scrape"

# Output file path
output_file = Path.home() / "Desktop" / "GenericName_All_HTML.txt"

# Initialize content collector
combined_html = []

# Loop through each HTML file
for file in sorted(input_dir.glob("*.html")):
    # Recover the URL from the filename (rough decode)
    base_name = file.stem  # e.g. example_com_index
    url = base_name.replace('_', '.').replace('.index', '').replace('.html', '')
    if not url.startswith("http"):
        url = f"https://example.com/path"

    # Read HTML content
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Append separator + content
    combined_html.append(f"\n\n{'='*80}\nURL: {url}\n{'='*80}\n\n{html}")

# Write to output file
with open(output_file, 'w', encoding='utf-8') as out:
    out.write("\n".join(combined_html))

print(f"\n✅ Combined HTML written to: {output_file}")
