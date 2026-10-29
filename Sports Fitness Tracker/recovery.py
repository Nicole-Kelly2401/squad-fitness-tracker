class Recovery:
    activity = "Recovery"
    effect = 0
    
    def __init__(self, hours):
         if not 0 < hours <= 24:
             raise ValueError("Hours must be more than 0 and less than 24.")
         self.hours = hours
            
    def remove_fatigue(self):
        return self.hours * self.effect #how much fatigue this activity removes - hours * effect
    
    def __str__(self):
        return f"{self.activity}: {self.hours} hours, removes {self.remove_fatigue():.1f} fatigue"
    
class Sleep(Recovery):
    activity = "Sleep"
    effect = 3.0
    
class Massage(Recovery):
    activity = "Massage"
    effect = 2.5
    
class Ice_bath(Recovery):
    activity = "Ice Bath"
    effect = 2.0
    
class Stretching(Recovery):
    activity = "Stretching"
    effect = 1.0
