from data import maps

print("Which map are you playing on?\n")
for i, m in enumerate(maps, start=1):
    print(i,m)

choice = int(input("\nEnter the number corresponding to the map: "))
selected_map = maps[choice - 1]
print(f"You selected: {selected_map}")

print("\nHow do you want to play?")
print("1 Chill")
print("2 Normal")
print("3 Tryhard")

mood = int(input("Enter choice: "))
if mood == 1:
    mood_text = "Chill"
elif mood == 2:
    mood_text = "Normal"
elif mood == 3:
    mood_text = "Tryhard"
else:
    mood_text = "Unknown"
print(f"\nGreat! Today you wanna play: {mood_text}")

if mood == 1:
    role = "Controller or Sentinel"

elif mood == 2:
    role = "Initiator"

elif mood == 3:
    role = "Duelist"

else:
    role = "Flex"

print(f"\nWe recommend you play: {role}")