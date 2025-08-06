print("🌡️ Temperatur Umrechner")

celsius = float(input("Temperatur in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("\n🔥 Ergebnis:")
print(str(celsius) + "°C = " + str(round(fahrenheit, 1)) + "°F")

if celsius < 0:
    print("🧊 Brrrr! Das ist gefroren!")
elif celsius < 15:
    print("🧥 Zieh dir eine Jacke an!")
elif celsius < 25:
    print("👕 Perfektes Wetter!")
else:
    print("☀️ Es ist heiß draußen!")
