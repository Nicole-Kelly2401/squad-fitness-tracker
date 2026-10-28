from session import Training_session, Match, Gym
from player import Player

player = Player("Player 1")

for session in [Training_session(60, 6), Match(90, 9), Gym(45, 7)]:
    player.find_load(session)
    print(session)
    print(" ->", player)
    
try:
    Training_session(60,11)
except ValueError as error:
    print("Bad input: ", error)
