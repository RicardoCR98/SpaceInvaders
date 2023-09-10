import os

class ScoreManager:
    def __init__(self, filename):
        self.filename = filename
        self.scores = []
        self.load_scores()

    def load_scores(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.scores = [int(line.strip()) for line in file]
        except Exception as e:
            print(f"Error loading scores: {e}")

    def save_scores(self):
        try:
            self.scores.sort(reverse=True)
            self.scores = self.scores[:5]
            with open(self.filename, 'w') as file:
                for score in self.scores:
                    file.write(str(score) + '\n')
        except Exception as e:
            print(f"Error saving scores: {e}")

    def add_score(self, score):
        try:
            if isinstance(score, int):
                self.scores.append(score)
                self.scores = list(set(self.scores))  # Elimina duplicados
                self.scores.sort(reverse=True)  # Ordena los puntajes de mayor a menor
                self.scores = self.scores[:5]  # Limita la lista a los mejores 5 puntajes
                self.save_scores()
            else:
                print("Invalid score format. Score must be an integer.")
        except Exception as e:
            print(f"Error adding score: {e}")

    def get_top_scores(self):
        return self.scores[:5]

    def reset_scores(self):
        self.scores = []
        self.save_scores()
