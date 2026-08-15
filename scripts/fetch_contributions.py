import json
import sys
import requests
from bs4 import BeautifulSoup

def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    days = []
    
    for td in soup.select("td.ContributionCalendar-day, td[data-date]"):
        date = td.get("data-date")
        level = td.get("data-level", "0")
        if date:
            days.append({"date": date, "level": int(level)})

    with open("data/contributions.json", "w") as f:
        json.dump({"days": days}, f, indent=2)
    print(f"Fetched {len(days)} contribution records for {username}.")

if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else "rajshankar1230"
    fetch_contributions(user)
