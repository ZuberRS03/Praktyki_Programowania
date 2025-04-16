class TennisGame2:

    SCORE_MAP = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0 # zmienione z p1points
        self.player2_score = 0 # zmienione z p2points

    def add_point(self, player_name): # zmienione z won_point
        if player_name == self.player1_name: # zmienione ze sztywnego "player1"
            self.player1_score += 1 # usunięcie wykożystania zbędnej metody
        elif player_name == self.player2_name:  # Zmienione z else na elif
            self.player2_score += 1 # usunięcie wykożystania zbędnej metody

    def get_score(self): # zmienione z score, bardziej znaczące działanie metody
        if self.player1_score == self.player2_score:
            return self._get_tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_endgame_score()
        else:
            return self._get_regular_score()

    def _get_tied_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_MAP[self.player1_score]}-All"
        return "Deuce"

    def _get_endgame_score(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_regular_score(self):
        p1_score_name = self.SCORE_MAP[self.player1_score]
        p2_score_name = self.SCORE_MAP[self.player2_score]
        return f"{p1_score_name}-{p2_score_name}"

    # Zostawiłem jakby były używane w testach
    def set_player1_score(self, number):
        for _ in range(number):
            self.player1_score += 1

    def set_player2_score(self, number):
        for _ in range(number):
            self.player2_score += 1
