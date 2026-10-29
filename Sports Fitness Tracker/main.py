from session import Training_session, Match, Gym
from recovery import Sleep, Massage, Ice_bath, Stretching
from player import Player
from squad import Squad 

player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

#sample data from gpt
player1.find_load(Training_session(60, 5))
player1.recover(Sleep(8))
player1.log_wellness(8, 2)
 
player2.find_load(Training_session(60, 6))
player2.find_load(Gym(45, 6))
player2.find_load(Match(90, 8))
player2.recover(Sleep(7))
player2.log_wellness(7, 5)
 
player3.find_load(Match(90, 9))
player3.find_load(Training_session(90, 8))
player3.find_load(Gym(60, 8))
player3.log_wellness(5, 8)
 
player4.find_load(Gym(45, 4))
player4.recover(Massage(1))
player4.recover(Sleep(9))
player4.log_wellness(9, 1)

squad = Squad()
for player in [player1, player2, player3, player4]:
    squad.add_player(player)
    
print("~~~~Squad Readiness~~~~")
squad.show_table()

print()
print("~~After removing Player 4~~")
squad.remove_player("Player 4")
squad.show_table()

print()
print("~~~~Bad input~~~~")
try:
    player1.log_wellness(8, 11)
except ValueError as error:
    print("Bad inpuut: ", error)

