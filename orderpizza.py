print("🍕 Pizza Palace - Bestell-Rechner")

pizza_preis = 12
getränk_preis = 3

print("Pizza: €12 pro Stück")
print("Getränk: €3 pro Stück")

pizzen = int(input("Wie viele Pizzen? "))
getränke = int(input("Wie viele Getränke? "))

gesamt = (pizzen * pizza_preis) + (getränke * getränk_preis)

print("\n📋 Deine Bestellung:")
print(str(pizzen) + " Pizzen = €" + str(pizzen * pizza_preis))
print(str(getränke) + " Getränke = €" + str(getränke * getränk_preis))
print("─" * 20)
print("Gesamt: €" + str(gesamt))
print("🚚 Danke für deine Bestellung!")
