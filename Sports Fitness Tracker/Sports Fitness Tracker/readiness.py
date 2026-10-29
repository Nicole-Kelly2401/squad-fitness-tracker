class Readiness:
    fatigue_weight = 0.5
    sleep_weight = 25
    soreness_weight = 25
    ideal_sleep = 8
    
    high_spike = 1.5
    medium_spike = 1.3
    low_high = 40
    low_medium = 55
    
    def score(self, player):
        fatigue_penalty = player.fatigue * self.fatigue_weight
        
        sleep_missing = max(0, self.ideal_sleep - player.sleep_hours)
        sleep_penalty = sleep_missing / self.ideal_sleep * self.sleep_weight
        
        soreness_penalty = player.soreness / 10 * self.soreness_weight
        
        result = 100 - fatigue_penalty - sleep_penalty - soreness_penalty
        return max(1, min(100, result))
    
    def load(self, player, today):
        recent_load = player.load_between(today -2, today)
        usual_load = player.load_between(today - 13, today) / 14
        
        if usual_load == 0:
            return 0
        return (recent_load / 3) / usual_load
    
    def status(self, score):
        if score >= 70:
            return "Ready to play"
        if score >= 40:
            return "Be cautious"
        return "Mandatory rest"