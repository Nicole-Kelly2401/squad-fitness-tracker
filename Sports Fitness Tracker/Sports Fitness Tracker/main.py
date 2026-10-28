from session import Training_session, Match, Gym
from recovery import Sleep, Massage, Ice_bath, Stretching
from player import Player

player = Player("Player 1")

print("~~~~~Sessions~~~~~")
for session in [Training_session(60, 6), Match(90, 9), Gym(45, 7)]:
    player.find_load(session)
    print(session)
    print(" ->", player)
    
print()
print("~~~~~Recovery~~~~~")
for recovery in [Sleep(8), Massage(1), Ice_bath(0.5), Stretching(0.5)]:
    player.recover(recovery)
    print(recovery)
    print(" ->", player)
    
print()
print("~~Fatigue can't go below 0~~~")
player.recover(Sleep(10))
player.recover(Sleep(10))
print(" ->", player)

print()
print("~~~~~Bad Input~~~~~")

try:
    Training_session(60,11)
except ValueError as error:
    print("Bad input: ", error)
