class Player:
    fatigue_per_load = 0.05
    
    def __init__(self,name):
        self.name = name
        self.fatigue = 0
        self.sleep_hours = 8
        self.soreness = 1
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
        
    def log_wellness(self, sleep_hours, soreness):
        if not 0 <= sleep_hours <= 24:
            raise ValueError("Hours must be between 0 and 24")
        if not 1 <= soreness <= 10:
            raise ValueError("Soreness must be between 1 and 10")
        self.sleep_hours = sleep_hours
        self. soreness = soreness
        
    def __str__(self):
        return f"{self.name}: fatigue {self.fatigue:.0f}/100, " f"{len(self.sessions)} sessions, {len(self.recoveries)} recoveries."