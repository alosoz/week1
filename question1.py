# 1.Rock-Paper-Scissors
# Take the names of the players and play the stone - paper - scissors game. game 10 hands it will last. 
# At the end of 10 hands, the winner will be determined. The score will be displayed at the end.

player_1 = input("Name of the first player: ")
player_2 = input("Name of the second player: ")

player_1_score = 0
player_2_score = 0
i = 0
while i<3:
    i += 1
    a = input(player_1 + " chouse one of them: 1)stone  2)paper  3)scissors")
    b = input(player_2 + " chouse one of them: 1)stone  2)paper  3)scissors")

    if a == b:
        print("draw")
    elif a == "stone":
        if b == "paper":
            print(player_1 + " won")
            player_1_score += 1
        else:
            print(player_2 + " won")
            player_2_score += 1
    elif a == "scissors":
        if b == "stone":
            print(player_2 + " won")
            player_2_score += 1
        else:
            print(player_1 + " won")
            player_1_score += 1
    elif a == "paper":
        if b == "stone":
            print(player_1 + " won")
            player_1_score += 1
        else:
            print(player_2 + " won")
            player_2_score += 1

print(player_1 + ": " + player_1_score)
print(player_2 + ": " + player_2_score)

if player_1_score > player_2_score:
    print(player_1 + " won")
else:
    print(player_2 + " won")