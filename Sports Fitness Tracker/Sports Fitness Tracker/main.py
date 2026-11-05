from session import Training_session, Match, Gym
from recovery import Sleep, Massage, Ice_bath, Stretching
from recovery_planner import Cautious, Balanced, Aggressive
from player import Player
from squad import Squad

def log_day(player, day, session, sleep_hours):
    player.find_load(session, day)
    player.recover(Sleep(sleep_hours))

player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")

for day in [1, 3, 5, 7, 9, 11 ,13]:
    log_day(player1, day, Training_session(60, 5), 8)
player1.log_wellness(8, 2)

for day in [1, 3, 5, 7 ,9, 11]:
    log_day(player2, day, Training_session(60, 5), 8)
log_day(player2, 12, Match(90, 8), 6)
log_day(player2, 13, Training_session(60,5), 8)
log_day(player2, 14, Gym(60, 8), 6)
player2.log_wellness(6, 6)

for day in range(1, 15):
    log_day(player3, day, Training_session(75, 7), 5)
player3.log_wellness(5,8)

for day in [2, 6, 10, 13]:
    log_day(player4, day, Gym(45, 4), 9)
player4.log_wellness(9, 1)

squad = Squad()
for player in [player1, player2, player3, player4]:
    squad.add_player(player)
    
today = 14
    
print("~~~~Squad Readiness (day 14)~~~~")
squad.show_table(today)

print()
print("~~~~~Alerts~~~~~")
alerts = squad.check_alert(today)
for alert in alerts:
    print(alert)
if len(alerts) == 0:
    print("No alerts!")

print()
print("~~~~Week level by planner style~~~~")
planners = [Cautious(), Balanced(), Aggressive()]
squad.show_levels(planners, today)

print()
print("~~~~Balanced plan for the week~~~~")
squad.plan_week(Balanced(), today)

print("~~~~Cautious plan for Player 2~~~~")
player2_score = squad.readiness.score(player2)
Cautious().show_plan(player2, player2_score, squad.alerts_for(player2, today))

print()
print("~~~~Bad input~~~~")
try:
    player1.find_load(Gym(45, 5), 0)
except ValueError as error:
    print("Bad inpuut: ", error)

