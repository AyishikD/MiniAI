import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_search_links(query, num_links=10, api_key=None):
    if api_key is None:
        api_key = os.getenv("SERPAPI_KEY")
    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google",
        "num": num_links
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    links = []

    if "organic_results" in data:
        for result in data["organic_results"]:
            link = result.get("link") or result.get("url") or result.get("source")
            if link and link.startswith("http"):
                links.append(link)
                if len(links) >= num_links:
                    break
    else:
        print("❌ No organic_results found in SerpAPI response")

    return links
