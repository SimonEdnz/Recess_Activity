from bs4 import BeautifulSoup
import requests
import json

url = "https://xeno-canto.org/explore?query=grp%3Abirds&pg={}&dir=0&order=en"

# Getting the audio list and species.
audio_list = []
species_list = []
for i in range(10):
    request_result = requests.get(url.format(str(i)))
    soup = BeautifulSoup(request_result.text, "html.parser")
    links = soup.find_all("audio")
    for link in links:
        audio_list.append("https:" + link.attrs["src"])
    names = soup.find_all("span", class_="common-name")
    for name in names:
        speciesData = name.find("a")
        species_list.append(
            {"species": speciesData.text, "species_link": speciesData.attrs["href"]}
        )

# Dumping them into a json file.
with open("bird_songs.json", "+a") as file:
    json.dump({"bird_songs": audio_list, "bird_species": species_list}, file)

# Using the api.
result = requests.get("https://xeno-canto.org/api/2/recordings?query=cnt:brazil&page=5")

# Prints values from the API in json format
print(result.json())
