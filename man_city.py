# Task 1: Create Player Data
player_info = [
  {"name": "Abdukodir Khusanov", "position": "Defender", "jersey_number": "45", "ethnicity": "Uzbekistan", "strikes": 14},
  {"name": "Omar Marmoush", "position": "Forward", "jersey_number": "7", "ethnicity": "Egypt", "strikes": 17},
  {"name": "Erling Haaland", "position": "Forward", "jersey_number": "9", "ethnicity": "Norway", "strikes": 23}
]

# Task 2: Analyze Player Positions
positions = [player["position"] for player in player_info]
print("Player position: ", positions)

# Task 3: Update Player Statistics
player_info[0]["strikes"] += 3
print("Khusanov stats: ", player_info[0]["strikes"])

# Task 4: Calculate Average Stats
average_strikes = sum(player["strikes"] for player in player_info) / len(player_info)
print("Avg strikes: ", average_strikes)