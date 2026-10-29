class Readiness:
    fatigue_weight = 0.5
    sleep_weight = 25
    soreness_weight = 25
    ideal_sleep = 8
    
    def score(self, player):
        fatigue_penalty = player.fatigue * self.fatigue_weight
        
        sleep_missing = max(0, self.ideal_sleep - player.sleep_hours)
        sleep_penalty = sleep_missing / self.ideal_sleep * self.sleep_weight
        
        soreness_penalty = player.soreness / 10 * self.soreness_weight
        
        result = 100 - fatigue_penalty - sleep_penalty - soreness_penalty
        return max(1, min(100, result))
    
    def status(self, score):
        if score >= 70:
            return "Ready to play"
        if score >= 40:
            return "Be cautious"
        return "Mandatory rest"