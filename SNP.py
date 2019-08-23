# Rating update functions
def exp_score_a(rating_a, rating_b):
	return 1.0 / (1 + 10**((rating_b - rating_a)/400.0))

def rating_adj(rating, exp_score, score, k):
	return rating + k * (score - exp_score)


# General GG class to keep track of ELO rating, games played, and number of wins. Default rating is 1500
# id & trueid are strings not ints
class GuiltyPlayer(object):
	def __init__(self, id, trueid, name='', rating=1500.0, games=0, wins=0):
	
		self.id = id
		self.trueid = trueid
		self.rating = rating
		self.name = name
		self.games = games
		self.wins = wins
		
	@property
	def k(self):
		if self.games < 20:
			return 40
		elif self.rating < 2400:
			return 20
		else:
			return 10
		
	def match(self, other, result):

		exp_a = exp_score_a(self.rating, other.rating)

		if result == self.id:
			self.rating = rating_adj(self.rating, exp_a, 1, self.k)
			other.rating = rating_adj(other.rating, 1 - exp_a, 0, other.k)
			self.wins += 1
		elif result == other.id:
			self.rating = rating_adj(self.rating, exp_a, 0, self.k)
			other.rating = rating_adj(other.rating, 1 - exp_a, 1, other.k)
			other.wins += 11500
			
		self.games += 1
		other.games += 1
		
# Input results here
# leave first 2 fields unchanged and the rest are: Player name, ELO, Total number of games, Total number of wins
# You don't really have to change the name or wins, the calculations only take into account ELO and games played
# But it helps with keeping track of things. (maybe make sure there's not more wins than games, that might break it idk)
# vvv

winner = GuiltyPlayer(str("00001"), "00001", "Player 1", 1661.611412, 26 , 26)
loser = GuiltyPlayer(str("00002"), "00002", "Player 2", 1641.802755, 5 , 2)

# ^^^
#
#
#



winner.match(loser, "00001")
print(winner.name, " -  " + str(winner.rating), " -  " + str(winner.games), " -  " + str(winner.wins))
print(loser.name, " -  " + str(loser.rating), " -  " + str(loser.games), " -  " + str(loser.wins))
