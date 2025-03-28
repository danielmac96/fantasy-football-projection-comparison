import requests
import json
import pandas as pd
file_path = "sleeper_data.json"
# Sleeper data - free easy api
#https://api.sleeper.app/projections/nfl/<season>/<week>?season_type=regular&position[]=FLEX&position[]=K&position[]=QB&position[]=RB&position[]=TE&position[]=WR&position[]=DEF
sleeper_projection_url = "https://api.sleeper.app/projections/nfl/2024/1?season_type=regular&position[]=QB"
sleeper_projection_response = requests.get(sleeper_projection_url)
sleeper_projection_json = sleeper_projection_response.json()
sleeper_projection_df = pd.DataFrame(sleeper_projection_json)
sleeper_projection_df.to_json(file_path, orient="records", indent=4)
#print(sleeper_projection_json, indent = 4)

# # ESPN data - unofficial api
# league_id = 123456  # Replace with your ESPN league ID (can be any public league)
# season = 2024
# week = 1
#
# url = f"https://fantasy.espn.com/apis/v3/games/ffl/seasons/{season}/segments/0/leagues/{league_id}?view=mMatchupScore&scoringPeriodId={week}"
# response = requests.get(url)
# data = response.json()
#
# with open(f"espn_projections_week_{week}.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# #fanduel/draftkings data - dfs
# import pandas as pd
#
# url = "https://www.fantasycruncher.com/lineup-rewind/draftkings/NFL"
# df = pd.read_html(url)[0]
#
# print(df.head())
#
# #fantasypros - might be tricky
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.fantasypros.com/nfl/projections/qb.php"
# headers = {"User-Agent": "Mozilla/5.0"}
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
#
# # Extract table rows
# rows = soup.find_all("tr")
#
# for row in rows[1:]:  # Skip header
#     cols = row.find_all("td")
#     if cols:
#         player = cols[0].text.strip()
#         points = cols[-1].text.strip()  # Fantasy points (last column)
#         print(f"{player}: {points} PPR Points")
