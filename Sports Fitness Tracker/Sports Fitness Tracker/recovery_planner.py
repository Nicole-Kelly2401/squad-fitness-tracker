from recovery import Sleep, Massage, Ice_bath, Stretching

class recovery_plan:
    style = "Planner"
    rest_below = 50
    light_below = 70
    
    patterns = {
        "Rest":   ["Rest", "Rest", "Light", "Light", "Normal", "Normal", "Normal"],
        "Light":  ["Light", "Light", "Normal", "Normal", "Normal", "Normal", "Normal"],
        "Normal": ["Normal", "Normal", "Normal", "Normal", "Normal", "Normal", "Normal"]
        }
    
    def level(self, score, alerts):
        if score < self.rest_below:
            return "Rest"
        if score < self.light_below:
            return "Light"
        for alert in alerts:
            if alert.level == "High":
                return "Light"
        return "Normal"
        
        
    def activities(self, day_type):
        if day_type == "Rest":
            return [Sleep(9), Massage(1), Ice_bath(0.5)]
        if day_type == "Light":
            return [Sleep(8), Massage(0.5), Stretching(0.5)]
        return [Sleep(8), Stretching(0.5)]
    
    def advice(self, day_type):
        if day_type == "Rest":
            return "No training or matches"
        if day_type == "Light":
            return "Light training only!"
        return "Train as normal"
    
    def show_plan(self, player, score, alerts):
        level = self.level(score, alerts)
        pattern = self.patterns[level]
        total_removed = 0
        print(f"{player.name}  |  {self.style} plan  |  readiness{score:.0f}  |  {level} week")
        
        for day in range(7):
            day_type = pattern[day]
            names = []
            for recovery in self.activities(day_type):
                names.append(recovery.activity)
                total_removed += recovery.remove_fatigue()
            print(f" Day {day + 1}: {self.advice(day_type):<24}{', '.join(names)}")
        print(f" Expected fatigue removed this week: {total_removed:.0f}")
        
class Cautious(recovery_plan):
    style = "Cautious"
    rest_below = 70
    light_below = 85
    
class Balanced(recovery_plan):
    style = "Balanced"
    rest_below = 50
    light_below = 70
    
class Aggressive(recovery_plan):
    style = "Aggressive"
    rest_below = 35
    light_below = 55
        
        