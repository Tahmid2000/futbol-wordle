import pandas as pd
df = pd.read_csv("players_22.csv", low_memory=False)
dfclean = df[['short_name', 'player_positions', 'club_name', 'league_name',
              'nationality_name', 'player_face_url', 'club_logo_url', 'nation_flag_url']].head(1000)
print(dfclean)
