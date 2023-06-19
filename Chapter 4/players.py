players = ['alice', 'david', 'peter', 'john']
print(players[0:2])

print(players[1:2])

print(players[1:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())