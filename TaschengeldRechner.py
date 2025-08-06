print("💰 Taschengeld Rechner")

taschengeld = float(input("Wie viel Taschengeld bekommst du pro Woche? €"))
wunsch_preis = float(input("Was kostet dein Wunsch? €"))

wochen = wunsch_preis / taschengeld

print("\n💡 Dein Sparplan:")
print("Taschengeld pro Woche: €" + str(taschengeld))
print("Ziel: €" + str(wunsch_preis))
print("Du brauchst " + str(round(wochen, 1)) + " Wochen zum Sparen!")

if wochen <= 4:
    print("🚀 Das schaffst du schnell!")
elif wochen <= 12:
    print("💪 Ein bisschen Geduld, dann klappt's!")
else:
    print("🎯 Das ist ein großer Traum - bleib dran!")
