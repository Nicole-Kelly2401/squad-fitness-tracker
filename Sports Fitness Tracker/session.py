class Session:
    activity = "Session"
    multiplier = 1.0
    
    def __init__(self, duration, effort):
        if duration <= 0:
            raise ValueError("The duration must be greater than 0.")
        if not 1 <= effort <= 10:
            raise ValueError("The effort (RPE) must be between 1 and 10.")
        self.duration = duration
        self.effort = effort
        
    def load(self):
        return self.duration * self.effort * self.multiplier
    
    def __str__(self):
        return f"{self.activity}: {self.duration} min, Effort {self.effort}, load {self.load():.0f}"
    
class Training_session(Session):
    activity = "Training"
    
class Match(Session):
    activity = "Match"
    multiplier = 1.2
    
class Gym(Session):
    activity = "Gym"
        