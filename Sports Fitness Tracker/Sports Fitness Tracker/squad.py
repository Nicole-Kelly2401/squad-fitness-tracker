from readiness import Readiness

from alert import Alert

class Squad:
    
    def __init__(self):
        self.players = []
        self.readiness = Readiness()
        
    def add_player(self, player):
        self.players.append(player)
            
    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                return
        raise ValueError(f"No player called {name}.")
            
    def rank(self):
        return sorted(self.players, key=self.readiness.score, reverse =True)
    
    def check_alert(self, today):
        alerts = []
        for player in self.players:
            ratio = self.readiness.load(player, today)
            score = self.readiness.score(player)
            
            if ratio >= self.readiness.high_spike:
                alerts.append(Alert(player, f"Load spike ({ratio:.1f}x usual)", "High"))
            elif ratio >= self.readiness.medium_spike:
                alerts.append(Alert(player, f"Load rising ({ratio:.1f}x usual)", "Medium"))
                
            if score < self.readiness.low_high:
                alerts.append(Alert(player, f"Low readiness ({score:.0f})", "High"))
            elif score < self.readiness.low_medium:
                alerts.append(Alert(player, f"Readiness dropping ({score:.0f})", "Medium"))
                
        return alerts
    
    def alerts_for(self, player, today):
        player_alerts = []
        for alert in self.check_alert(today):
            if alert.player is player:
                player_alerts.append(alert)
        return player_alerts
    
    def show_levels(self, planners, today):
        print(f"{'Player':<12}{'Readiness':>10}{'Fatigue':>10}{'Load':>8}  Status")
        print("-" * 58)
        for player in self.rank():
            score = self.readiness.score(player)
            alerts = self.alerts_for(player, today)
            print(f"{player.name:<12}{score:>10.0f}", end="")
            for planner in planners:
                print(f"{planner.level(score, alerts):>12}", end="")
        print()
        
    def show_table(self, today):
        print(f"{'Player':<12}{'Readiness':>10}{'Fatigue':>10}{'Load':>8}   Status")
        print("-" * 56)
        for player in self.rank():
            score = self.readiness.score(player)
            ratio = self.readiness.load(player, today)
            status = self.readiness.status(score)
            ratio_text = f"{ratio:.1f}x"
            print(f"{player.name:<12}{score:>10.0f}{player.fatigue:>10.0f}{ratio_text:>8}  {status}")
            
    def plan_week(self, planner, today):
        for player in self.rank():
            score = self.readiness.score(player)
            alerts = self.alerts_for(player, today)
            planner.show_plan(player, score, alerts)
            print()