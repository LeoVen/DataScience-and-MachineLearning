import csv
import re
from datetime import datetime
import matplotlib.pyplot as plt

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

def main():
	
	i = 0

	with open('data/WorldCupMatchesNorm.csv', encoding='cp1252') as file:
		content_spam = csv.reader(file, delimiter=',')

		# Filter for match contents
		match_array = []

		for row in content_spam:
			# DateTime(1)
			# HomeTeamName(5) HomeTeamGoals(6)
			# AwayTeamGoals(7) AwayTeamName(8)
			date = datetime.strptime(row[1], '%d/%m/%Y - %H:%M')

			match_array.append(Match(date, row[5], row[6], row[7], row[8]))

		# Create a set of unique country Names
		name_set = set()

		for m in match_array:
			name_set.add(m.home_name)
			name_set.add(m.away_name)

		# Array of Country objects
		country_array = []

		for s in name_set:
			country_array.append(Country(s))

		# Adding up scores
		for country in country_array:
			for match in match_array:
				if match.home_name == country.name:
					country.add_goals_made(match.home_goals)
				elif match.away_name == country.name:
					country.add_goals_taken(match.away_goals)

		country_array.sort(key = lambda c: c.goals_made, reverse = True)

		# Making a plot
		y_axis = [n.name for n in country_array]
		x_axis = [c.calculate_score() for c in country_array]

		cut = len(x_axis)

		# plt.bar(y_axis[:cut], width = 0.5, height = x_axis[:cut])
		plt.plot(y_axis[:cut], x_axis[:cut])
		plt.show()


if __name__ == '__main__':
	main()
