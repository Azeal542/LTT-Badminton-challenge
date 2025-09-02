import pandas as pd
import numpy as np

datasheet = "Player sheet.csv"
data = pd.read_csv(datasheet)
#print(data)
def create_user(name):
    name = name.upper()
    if data.empty:
        next_id = 1
    else:
        last_id = data['UserID'].iloc[-1]
        next_id = int(last_id) + 1  

    new = pd.DataFrame([[next_id, name, 1800]], columns=['UserID', 'Name', 'ELO'])
    new.to_csv(datasheet, mode='a', index=False, header=False)

def elo_calc(win, los):
    player1 = win.upper()
    player2 = los.upper()

    winner = data.loc[data['Name'] == player1]
    loser =  data.loc[data['Name'] == player2]
    
    A = int(winner['ELO'].iloc[-1])
    B = int(loser['ELO'].iloc[-1])
    diff = B - A
    div = diff / 400
    exp = 1 + (10**div)
    dev = 1/exp
    eval = round(20 * (1 - dev))
    As = A + eval
    Bs = B - eval
    #print(As)
    #print(Bs)
    windex = data.loc[data['Name'] == player1].index[0]
    losdex = data.loc[data['Name'] == player2].index[0]

    data.loc[windex, 'ELO'] = As
    data.loc[losdex, 'ELO'] = Bs
    data.to_csv(datasheet, index=False)
    
    gamerec = "GameRecord.csv"
    game = pd.read_csv(gamerec)

    if game.empty:
        next_id = 1
    else:
        last_id = data['UserID'].iloc[-1]
        next_id = int(last_id) + 1  

    new = pd.DataFrame([[next_id, player1, player2, eval]], columns=['GameID', 'Winner', 'Loser', 'ELO change'])
    new.to_csv(gamerec, mode='a', index=False, header=False)

#elo_calc()
#create_user()