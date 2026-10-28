class Player:
    fatigue_per_load = 0.05
    
    def __init__(self,name):
        self.name = name
        self.fatigue = 0 
        self.sessions = []
        self.recoveries = []
        self.injured = False
        
        
    def set_fatigue(self, value):
        self.fatigue = max(0, min(100, value))
        
    def find_load(self, session):
        self.sessions.append(session)
        self.set_fatigue(self.fatigue + session.load() * self.fatigue_per_load)
        
    def recover(self, recover):
        self.recoveries.append(recover)
        self.set_fatigue(self.fatigue - recover.remove_fatigue())
        
    def __str__(self):
        return f"{self.name}: fatigue {self.fatigue:.0f}/100, {len(self.sessions)} sessions, {len(self.recoveries)} recoveries."