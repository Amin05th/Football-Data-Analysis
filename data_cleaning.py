import pandas as pd
import numpy as np

# pd.set_option('display.max_rows', None)

df = pd.read_csv('2021-2022 Football Player Stats.csv')

# remove dublicates
df.drop_duplicates(subset=["Player"], keep="first", inplace=True)

# has got � in name
df['unreadable_name'] = df['Player'].apply(lambda x: 1 if '�' in x.lower() else 0)

# got subbed in
df['subbed_in'] = df['MP'] - df['Starts']

# change column names
df['Goals/90s'] = df['Goals']
df['Goals'] = np.round(df['Goals'] * df['90s'])

df['Assists/90s'] = df['Assists']
df['Assists'] = np.round(df['Assists'] * df['90s'])

df['OG/90s'] = df['OG']
df['OG'] = np.round(df['OG'] * df['90s'])

# Played whole season
total_games = 38
bundesliga_total_games = 34

df['played_whole_season'] = df.apply(lambda x: 1 if x.MP == total_games else 0 if x['Comp'] != "Bundesliga" else 1 if x["MP"] == bundesliga_total_games else 0, axis=1)
df['played_whole_season_from_start'] = df.apply(lambda x: 1 if x['Starts'] == total_games else 0 if x['Comp'] != "Bundesliga" else 1 if x["Starts"] == bundesliga_total_games else 0, axis=1)

# count all Cards
total_yellow_cards = np.round(df['CrdY'] * df['90s'])
total_red_cards = np.round(df['CrdR'] * df['90s'])
df['total_cards'] = total_yellow_cards + total_red_cards

# multiply columns by 90s to get total things and not per 90 minutes

total_div_to_convert = df[['Shots', 'SoT', 'ShoFK', 'ShoPK', 'PKatt', 'PasTotCmp', 'PasTotAtt', 'PasShoCmp',
    'PasShoAtt', 'PasMedCmp', 'PasMedAtt', 'PasLonCmp', 'PasLonAtt', 'PasAss', 'Pas3rd', 'PPA',
    'CrsPA', 'PasProg', 'PasAtt', 'PasLive', 'PasDead', 'PasFK', 'TB', 'PasPress', 'Sw', 'PasCrs',
    'CK', 'CkIn', 'CkOut', 'CkStr', 'PasGround', 'PasLow', 'PasHigh', 'PaswLeft', 'PaswRight', 'PaswHead',
    'TI', 'PaswOther', 'PasCmp', 'PasOff', 'PasOut', 'PasInt', 'PasBlocks', 'SCA', 'ScaPassLive', 'ScaPassDead',
    'ScaDrib', 'ScaSh', 'ScaFld', 'ScaDef', 'GCA', 'GcaPassLive', 'GcaPassDead', 'GcaDrib', 'GcaSh',
    'GcaFld', 'GcaDef', 'Tkl', 'TklWon', 'TklDef3rd', 'TklMid3rd', 'TklAtt3rd', 'TklDri', 'TklDriAtt',
    'TklDriPast', 'Press', 'PresSucc', 'PresDef3rd', 'PresMid3rd', 'PresAtt3rd', 'Blocks', 'BlkSh',
    'BlkShSv', 'BlkPass', 'Int', 'Tkl+Int', 'Clr', 'Err', 'Touches', 'TouDefPen', 'TouDef3rd', 'TouMid3rd',
    'TouAtt3rd', 'TouAttPen', 'TouLive', 'DriSucc', 'DriAtt', 'DriPast', 'DriMegs', 'Carries', 'CarProg', 'Car3rd',
    'CPA', 'CarMis', 'CarDis', 'RecTarg', 'Rec', 'CrdY', 'CrdR', '2CrdY', 'Fls', 'Fld', 'Off', 'Crs', 'TklW',
    'PKwon', 'PKcon', 'Recov', 'AerWon', 'AerLost']]

for column in total_div_to_convert.columns:
    df[column] = np.round(df[column] * df['90s'])

# Card per Foul

df['Card/Foul'] = df['total_cards'] / df['Fls']

df.to_csv("Cleaned Data.csv")

