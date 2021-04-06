import PlayerStats
import database
import csv
import os
import sys
from datetime import datetime

# Read the list of players from csv file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
playerList = []
with open(os.path.join(__location__, 'Players.csv')) as File:
    reader = csv.DictReader(File)
    for row in reader:
        playerList.append(row)

try:
    # Loop through each player from playerList
    for player in playerList:
        myPlayer = PlayerStats.PlayerStats()
        # Check if PlayerID has a space and replace it with %20 --> Can't call api with spaces
        myPlayerStats = myPlayer.generate_response(player['PlayerID'].replace(' ', '%20'), player['PlayerPlatform'])
        myPlayer.extract_player_stats_from_response(myPlayerStats)
        
        now = datetime.now()
        # DD/MM/YY H:M:S
        dateTimestamp = now.strftime("%d/%m/%Y %H:%M:%S")

        dbpath = os.path.join(__location__, 'main.db')
        database.dbupdate(dbpath, 'INSERT INTO PlayerData (ID, Name, Platform, DateFetched, Ones, Twos, Threes) VALUES (?, ?, ?, ?, ?, ?, ?)', (player['PlayerID'], player['PlayerName'], player['PlayerPlatform'], dateTimestamp, myPlayer.ones, myPlayer.twos, myPlayer.threes))

        print(f"{player['PlayerName']} has been added to the DB on {dateTimestamp}")
except:
    print('something went bad')
