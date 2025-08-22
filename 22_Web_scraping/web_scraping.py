# Day 22 - 30DaysOfPython Challenge
# Web Scraping

# 1 - Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup, Tag
import json
from datetime import datetime
import re

def scrape_website(url: str = 'http://www.bu.edu/president/boston-university-facts-stats/'):
    # Fetch the page and return None if Error
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code}")
        return None

    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract data
    data = {
        "url": url,
        "title": soup.title.get_text(strip=True),
        "scraped_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "sections": {}
    }

    # Look for all sections with h2 or h3 as headers
    for header in soup.find_all(["h2", "h3"]):
        section_title = header.get_text(strip=True)
        section_content = []

        for sibling in header.find_next_siblings():
            # Only process if sibling is a Tag
            if isinstance(sibling, Tag):
                if sibling.name in ["h2", "h3"]:
                    break  # Stop at next section

                if sibling.name == "p":
                    text = sibling.get_text(strip=True)
                    if text:
                        section_content.append(text)
                elif sibling.name == "ul":
                    items = [li.get_text(strip=True) for li in sibling.find_all("li")]
                    if items:
                        section_content.append({"list": items})
                elif sibling.name == "table":
                    rows = sibling.find_all("tr")
                    table = []
                    for row in rows:
                        cells = [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
                        if cells:
                            table.append(cells)
                    if table:
                        section_content.append({"table": table})

        if section_content:
            data["sections"][section_title] = section_content

    # Save to JSON file
    with open(r"22_Web_scraping/bu_facts_stats.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data successfully saved to 22_Web_scraping/bu_facts_stats.json")
    return data

# Run the scraper
# scraped_data = scrape_website()

"""
After much troubleshooting and code refactoring with AI-assistance,
I realised that the BU website has changed and no longer uses simple
<h2>, <h3>, <p>, <table> tags.
It looks like the page is now JavaScript-driven and the data is not
emedded in plain HTML.
Only using requests and BeautifulSoup won't allow to scrape meaningful content.

I decided to leave the code as is. It is good-working code although not for modern webpages.

AI provided with the following simulation to obtain what could have been the output of the original func:
"""
def scrape_website_SIMULATED():
    data = {
        "url": "http://www.bu.edu/president/boston-university-facts-stats/",
        "title": "BU Facts & Stats | Office of the President",
        "scraped_at": "22-08-2025 15:26:11",
        "sections": {
            "Fast Facts": [
                "Total Enrollment: 36,691",
                "Undergraduate: 18,367",
                "Graduate: 18,324",
                "Faculty: Over 4,000"
            ],
            "Research": [
                "Annual Research Expenditure: $600M+",
                "NIH Funding: Top 10 private universities"
            ],
            "Diversity": [
                {"list": ["135+ countries represented", "50% women in undergraduate population"]}]
        }
    }

    with open("22_Web_scraping/bu_facts_stats.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved (simulated).")
    return data

# 2 - Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
""" 
URL not available.
"""

# 3 - Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
def scrape_presidents(url: str = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"):

    # Fetch the page and return None if error
    response = requests.get(url)
    if response.status_code != 200:
        print(f"ERROR: HTTP {response.status_code}")
        return None
    
    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the main presidents table
    # Look for the first <table class="wikitable"> after any heading with "Presidents"
    table = None
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        if 'president' in heading.get_text().lower():
            table = heading.find_next("table", class_="wikitable")
            if table:
                break

    if not table:
        print("Could not find the presidents table.")
        return None

    # Extract rows
    rows = table.find_all("tr")
    presidents = []

    for row in rows[1:]:  # Skip header row
        cells = row.find_all(["td", "th"])
        if len(cells) < 6:  # Skip malformed rows
            continue

        def get_text(cell):
            return " ".join(cell.stripped_strings).strip()

        # Extract portrait image
        portrait = ""
        img = cells[1].find("img") if len(cells) > 1 else None
        if img and img.get("src"):
            portrait = "https:" + img["src"]

        president = {
            "no": get_text(cells[0]).rstrip('.'),  # Remove period
            "name": re.sub(r'\[.*?\]', '', get_text(cells[2])).strip(),  # Remove [a], [b]
            "term": get_text(cells[3]),
            "party": get_text(cells[4]),
            "election": get_text(cells[5]),
            "vice_president": get_text(cells[6]) if len(cells) > 6 else ""
        }
        if portrait:
            president["portrait"] = portrait

        presidents.append(president)

    # Build final data
    data = {
        "url": url,
        "title": "List of Presidents of the United States",
        "scraped_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "total_presidents": len(presidents),
        "presidents": presidents
    }

    # Save to JSON
    with open("22_Web_scraping/presidents.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Data successfully saved!")
    
    return data

# Run the scraper
# scraped_data = scrape_presidents()