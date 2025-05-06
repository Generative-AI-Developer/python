bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])


message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


for value in range(1, 5):
    print(value)

number =  list(range(1, 6))
print(number)


even_numbers = list(range(3, 21,3 ))
print(even_numbers)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

for player in players[:3]:
    print(player.title())

