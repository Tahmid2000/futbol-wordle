import pandas as pd
import pycountry_convert as pc
from random import randrange


class Player:

    def __init__(self):
        self.allPlayers()

    def allPlayers(self):
        df = pd.read_csv("players_22.csv", low_memory=False)
        self.possiblePlayers = df[['short_name', 'player_positions', 'club_name', 'league_name',
                                   'nationality_name', 'player_face_url', 'club_logo_url', 'nation_flag_url']].head(2500)
        self.possibleAnswers = self.possiblePlayers.head(500)

    def randomPlayer(self):
        num = randrange(500)
        return self.possibleAnswers.iloc[[num]]

    def playerContinent(self, country):
        continents = {
            'NA': 'North America',
            'SA': 'South America', 
            'AS': 'Asia',
            'OC': 'Australia',
            'AF': 'Africa',
            'EU': 'Europe'
        }
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        return continents[continent_name]

    def playersFromQuery(self, query):
        return self.possiblePlayers[self.possiblePlayers['short_name'].str.contains(query, case=False)]
