class TennisGame3:

    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name # Zmienione z p1_n
        self.player2_name = player2_name # Zmienione z p2_n
        self.player1_score = 0 # Zmienione z p1
        self.player2_score = 0 # Zmienione z p2

    def add_point(self, player_name): # zmienione z won_point, zmienione n na player_name
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def get_score(self): # zmienione z score, bardziej znaczące działanie metody
        if self._is_early_game():
            return self._get_regular_score()
        if self.player1_score == self.player2_score:
            return "Deuce"
        return self._get_endgame_score()

    def _is_early_game(self):
        return self.player1_score < 4 and self.player2_score < 4 and (self.player1_score + self.player2_score < 6)

    def _get_regular_score(self):
        p1 = self.SCORE_NAMES[self.player1_score]
        p2 = self.SCORE_NAMES[self.player2_score]
        return f"{p1}-All" if self.player1_score == self.player2_score else f"{p1}-{p2}"

    def _get_endgame_score(self):
        score_diff = self.player1_score - self.player2_score
        leading_player = self.player1_name if score_diff > 0 else self.player2_name
        if abs(score_diff) == 1:
            return f"Advantage {leading_player}"
        return f"Win for {leading_player}"