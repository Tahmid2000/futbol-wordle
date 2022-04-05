from fastapi import FastAPI
from data import Player

app = FastAPI()
player = Player()


@app.get("/")
async def root():
    return {"player": player.randomPlayer()['short_name']}


@app.get("/player/{query}")
async def getPlayerFromQuery(query: str):
    tempdf = player.playersFromQuery(query)
    result = []
    for index, row in tempdf.iterrows():
        result.append({"short_name": row['short_name'],
                      "player_positions": row['player_positions'], "club_name": row['club_name'], 'league_name': row['league_name'], 'nationality_name': row['nationality_name'], 'player_face_url': row['player_face_url'], 'club_logo_url': row['club_logo_url'], 'nation_flag_url': row['nation_flag_url']})
    return {"results": result}


@app.get("/test/{player1}/{player2}")
async def testPlayerMatching(player1: str, player2: str):
    return {"final": player.matchingPlayer(player1, player2)}
