import requests
import csv
from bs4 import BeautifulSoup

# API link
api_link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send a GET request to the API link
response = requests.get(api_link)
data = response.json()

# Extract the required attributes from the API response
episodes = data["_embedded"]["episodes"]

# Create a CSV file and write the extracted data
with open("westworld_episodes.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(["id", "url", "name", "season", "number", "type", "airdate", "airtime", "runtime",
                     "average_rating", "summary", "medium_image_link", "original_image_link"])
    
    # Write data for each episode
    for episode in episodes:
        id = episode["id"]
        url = episode["url"]
        name = episode["name"]
        season = episode["season"]
        number = episode["number"]
        type = episode["type"]
        airdate = episode["airdate"]
        airtime = episode["airtime"]
        runtime = episode["runtime"]
        average_rating = episode["rating"]["average"]
        summary = BeautifulSoup(episode["summary"], "html.parser").get_text()
        medium_image_link = episode["image"]["medium"]
        original_image_link = episode["image"]["original"]
        
        # Write a row with the extracted data
        writer.writerow([id, url, name, season, number, type, airdate, airtime, runtime,
                         average_rating, summary, medium_image_link, original_image_link])

print("Data extraction complete. The CSV file has been created.")