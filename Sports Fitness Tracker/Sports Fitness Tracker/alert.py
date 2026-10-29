class Alert:
    
    def __init__(self, player, reason, level):
        self.player = player
        self.reason = reason
        self.level = level
        
    def __str__(self):
        return f"[{self.level}] {self.player.name}: {self.reason}"