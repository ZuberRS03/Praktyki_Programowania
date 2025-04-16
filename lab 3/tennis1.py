class TennisGame1:

    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
    EQUAL_SCORE_NAMES = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0 # zmienione z p1points
        self.player2_score = 0 # zmienione z p2points

    def add_point(self, player_name): # zmienione z won_point
        if player_name == self.player1_name: # zmienione ze sztywnego "player1"
            self.player1_score += 1
        elif player_name == self.player2_name: # Zmienione z else na elif
            self.player2_score += 1

    def get_score(self): # zmienione z score, bardziej znaczące działanie metody
        # usuniete result = "" i temp_score = 0
        # rozdzielenie logiki na mniejsze metody
        if self.player1_score == self.player2_score:
            return self._get_equal_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_advantage_or_win()
        else:
            return self._get_standard_score()

    def _get_equal_score(self):
        return self.EQUAL_SCORE_NAMES.get(self.player1_score, "Deuce")

    def _get_advantage_or_win(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return f"Advantage {self.player1_name}" # zmiana z "player1" na self.player1_name
        elif score_diff == -1:
            return f"Advantage {self.player2_name}" # zmiana z "player2" na self.player1_name
        elif score_diff >= 2:
            return f"Win for {self.player1_name}" # zmiana z "player1" na self.player1_name
        else:
            return f"Win for {self.player2_name}" # zmiana z "player2" na self.player1_name

    def _get_standard_score(self):
        # usuniecie pętli bo niepotrzebna ze możliwość odnoszenia się do zmiennych
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
