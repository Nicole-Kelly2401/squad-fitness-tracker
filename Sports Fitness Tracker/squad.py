from readiness import Readiness

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
        
    def show_table(self):
        print(f"{'Player':<12}{'Readiness':>10}{'Fatigue':>10}   Status")
        print("-" * 42)
        for player in self.rank():
            score = self.readiness.score(player)
            status = self.readiness.status(score)
            print(f"{player.name:<12}{score:>10.0f}{player.fatigue:>10.0f}  {status}")