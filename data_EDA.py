import nltk
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

nltk.download('stopwords')
df = pd.read_csv('Cleaned Data.csv')
df.drop("Unnamed: 0", inplace=True, axis=1)

# Top 20 Best Topscorer 2021/22

sorted_by_goals = df.sort_values("Goals", ascending=False).iloc[:20]
topscorer_graph = px.bar(sorted_by_goals, x="Player", y="Goals")
topscorer_graph.show()

# Top 20 Best Assistmaker 2021/22

sorted_by_assists = df.sort_values("Assists", ascending=False).iloc[:20]
assistmaker_graph = px.bar(sorted_by_assists, x="Player", y="Assists")
assistmaker_graph.show()

# rank leagues with cards

liga_with_the_most_cards_graph = px.histogram(df, x="Comp", y="total_cards", color="Player")
liga_with_the_most_cards_graph.show()

# best G/A player
best_GA_Player = df.sort_values("G/A", ascending=False).iloc[:20]
best_GA_Player_graph = px.bar(best_GA_Player, x="Player", y="G/A", color="played_whole_season", pattern_shape="played_whole_season_from_start")
best_GA_Player_graph.show()

# best OG Player
best_OG_Player = df.sort_values("OG", ascending=False).iloc[1:21]
best_OG_Player_graph = px.bar(best_OG_Player, x="Player", y="OG")
best_OG_Player_graph.show()

# PasTotCmp PasTotAtt PasTotCmp% PasTotDist PasTotPrgDist PasShoCmp PasShoAtt PasShoCmp% PasMedCmp PasMedAtt PasMedCmp%
# PasLonCmp PasLonAtt PasLonCmp%
all_passing_columns = df[["Rk", "PasTotCmp", "PasTotAtt", "PasTotCmp%", "PasTotDist", "PasTotPrgDist", "PasShoCmp",
                          "PasShoAtt", "PasShoCmp%", "PasMedCmp", "PasMedAtt", "PasMedCmp%","PasLonCmp", "PasLonAtt", "PasLonCmp%"]]
all_passing_columns_graph = px.parallel_coordinates(all_passing_columns, color="Rk")
all_passing_columns_graph.show()

# Goals Shots SoT SoT% G/Sh G/SoT ShoDist ShoFK ShoPK
matrix_of_goals_shots = df[["Player", "Goals", "Shots", "SoT", "SoT%", "G/Sh", "G/SoT", "ShoDist", "ShoFK", "ShoPK"]]
matrix_of_goals_shots_graph = px.scatter_matrix(matrix_of_goals_shots,
                                          dimensions=["Goals", "Shots", "SoT", "SoT%", "G/Sh", "G/SoT", "ShoDist", "ShoFK", "ShoPK"],
                                          color="Player")
matrix_of_goals_shots_graph.show()

# Division of Positions in Competitions
positions_in_competitions = px.sunburst(df, path=["Comp", "Pos"], color="Age")
positions_in_competitions.show()

# Nationality of Players in leagues
top_nations = df.groupby("Nation").filter(lambda x: len(x) > 25)
top_nations_graph = px.sunburst(top_nations, path=["Nation", "Comp"])
top_nations_graph.show()

# Nationality of Players in leagues in percent
nation_total_count = df['Nation'].value_counts()[df['Nation'].value_counts() > 20]
nation_unique = nation_total_count.index.unique()
top_nations_in_percent_graph = px.pie(df, values=nation_total_count, names=nation_unique, title="top_nations_in_percent")
top_nations_in_percent_graph.show()

# card per foul
players_with_most_fouls = df.sort_values("Fls", ascending=False).iloc[:20]
card_per_foul_graph = px.scatter(players_with_most_fouls, x="Fls", y="total_cards", hover_name="Player")
card_per_foul_graph.show()

# heatmap of ScaDef GcaDef TklDef3rd PresDef3rd TouDefPen TouDef3rd
defensive_columns = df[["ScaDef", "GcaDef", "TklDef3rd", "PresDef3rd", "TouDefPen", "TouDef3rd"]]
defensive_columns_graph = px.imshow(defensive_columns)
defensive_columns_graph.show()

# wordcloud of words

words = " ".join(df['Squad'])


def punctuation_stop(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    return [w.lower() for w in word_tokens if w not in stop_words and w.isalpha()]


words_filtered = punctuation_stop(words)

text = " ".join(list(words_filtered))
wc = WordCloud(background_color="white", random_state=1, stopwords=STOPWORDS, max_words=2000, width=800, height=1500)
wc.generate(text)

plt.figure(figsize=[10, 10])
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
