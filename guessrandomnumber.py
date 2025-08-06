import random

print("🎲 Rate meine Zahl!")

geheime_zahl = random.randint(1, 10)
tipp = int(input("Rate eine Zahl zwischen 1 und 10: "))

if tipp == geheime_zahl:
    print("🎉 Fantastisch! Du hast es richtig geraten!")
else:
    print("❌ Schade! Die Zahl war " + str(geheime_zahl))
    print("Viel Glück beim nächsten Mal!")
