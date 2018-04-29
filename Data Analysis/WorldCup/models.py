class Match:

	def __init__(self, date, home_name, home_goals, away_goals, away_name):
		self.date = date
		self.home_name = home_name
		self.home_goals = home_goals
		self.away_name = away_name
		self.away_goals = away_goals

class Country:

	def __init__(self, name):
		self.name = name
		self.goals_made = 0
		self.goals_taken = 0

	def add_goals_made(self, goals):
		self.goals_made += int(goals)

	def add_goals_taken(self, goals):
		self.goals_taken += int(goals)

	def calculate_score(self):
		return self.goals_made - self.goals_taken