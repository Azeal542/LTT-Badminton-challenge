import pandas as pd
import numpy as np

datasheet = "Player sheet.csv"
data = pd.read_csv(datasheet)
#print(data)
def create_user():
    name = input("Enter player name:", )
    last_id = data['UserID'].iloc[-1]
    next_id = int(last_id) + 1

    new = pd.DataFrame([[next_id, name, 1500]], columns=['UserID', 'NAME', 'ELO'])
    new.to_csv(datasheet, mode='a', index=False, header=False)

create_user()