from soccer_data_api import SoccerDataAPI

soccer_data = SoccerDataAPI()

EN=soccer_data.english_premier()
LA=soccer_data.la_liga()
LI1=soccer_data.ligue_1()
BU=soccer_data.bundesliga()
SA=soccer_data.serie_a()
RUS=soccer_data.russian_premier()
ENCHAMP=soccer_data.english_championship()

print("League Codes","English Premier --> 1","LaLiga --> 2","Ligue1 --> 3","Bundesliga --> 4","SerieA --> 5","Russian Premier --> 6","English Championship --> 7","\n",sep="\n")

b=input("Lig Kodunu Giriniz --> ")
c={"1":EN,"2":LA,"3":LI1,"4":BU,"5":SA,"6":RUS,"7":ENCHAMP}
a=c[b]

print("    Team                           Matches      Wins     Losses     Goals For    Goals Against     Points")

for i in range(len(a)):
    if i>8:
        print(125*"-")
        print(a[i]['pos'],"-",a[i]['team'],(30-len(a[i]['team']))*" ",a[i]['matches_played'],8*" ",a[i]['wins'],5*" ",a[i]['losses'],8*" ", a[i]['goals_for'],10*" ",a[i]['goals_against'],14*" ",a[i]['points'])
    else:
        print(125 * "-")
        print("0"+a[i]['pos'],"-",a[i]['team'], (30-len(a[i]['team'])) * " ", a[i]['matches_played'],8*" ",a[i]['wins'],5*" ",a[i]['losses'],8*" ", a[i]['goals_for'],10*" ",a[i]['goals_against'],14*" ",a[i]['points'])


        



