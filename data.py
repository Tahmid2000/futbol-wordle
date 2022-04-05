from lib2to3.pgen2.pgen import DFAState
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


    def matchingPlayer(self, player1, player2):
        player1_df = self.playersFromQuery(player1)
        player2_df = self.playersFromQuery(player2)
        p1 = []
        p2 = []
        final = {}

        for index, row in player1_df.iterrows():
            p1.append({"short_name": row['short_name'], "player_positions": row['player_positions'], "club_name": row['club_name'], 'league_name': row['league_name'], 'nationality_name': row['nationality_name'], 'player_face_url': row['player_face_url'], 'club_logo_url': row['club_logo_url'], 'nation_flag_url': row['nation_flag_url']})

        for index, row in player2_df.iterrows():
            p2.append({"short_name": row['short_name'], "player_positions": row['player_positions'], "club_name": row['club_name'], 'league_name': row['league_name'], 'nationality_name': row['nationality_name'], 'player_face_url': row['player_face_url'], 'club_logo_url': row['club_logo_url'], 'nation_flag_url': row['nation_flag_url']})

        # Position Check



        # Country Check
        if (p1[0]['nationality_name'] == p2[0]['nationality_name']):
            final['country'] = 'green'
        elif (self.playerContinent(p1[0]['nationality_name']) == self.playerContinent(p2[0]['nationality_name'])):
            final['country'] = 'yellow'
        else:
            final['country'] = 'black'


        # Club Check
        if (p1[0]['club_name'] == p2[0]['club_name']):
            final['club'] = 'green'
        elif (p1[0]['league_name'] == p2[0]['league_name']):
            final['club'] = 'yellow'
        else:
            final['club'] = 'black'

        print(p1[0])
        print(p2[0])
        print(final)



player = Player()
player.matchingPlayer('neymar', 'messi')    
