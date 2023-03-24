import random
class Score:
    def __init__(self, n):
        self.scores = [['-' for i in range(n)] for i in range(n)]

    def print(self):
        print(self.scores)

class Tournament:
    def __init__(self, n):
        self.score = Score(n)
        print('Start the simulation')
        self.a,self.b = self.choose_players()

    def choose_players(self):
        p1 = random.randint(1,n)
        p1 = random.randint(1,n)
        return 1,2
        
    
        

n = int(input('enter the no of players:'))
Tournament(n)

