import csv
import re
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Country:

	def __init__(self, RANKING, TEAM, POINTS, MATCHES_PLAYED, WINS, DRAWS,
		LOSES, GOALS_SCORED, GOALS_AGAINST, AVERAGE_POINTS, APPEARANCES):
		self.ranking = RANKING
		self.team = TEAM
		self.points = POINTS
		self.matches_played = MATCHES_PLAYED
		self.wins = WINS
		self.draws = DRAWS
		self.loses = LOSES
		self.goals_scored = GOALS_SCORED
		self.goals_against = GOALS_AGAINST
		self.average_points = AVERAGE_POINTS
		self.appearances = APPEARANCES


def main():
	
	dataframe = pd.read_csv('data/WorldCup.csv')

	df_size = len(dataframe)

	cf = dataframe.values

	countries = []

	for i in range(df_size):
		countries.append(Country(cf[i][0], cf[i][1],
			cf[i][2], cf[i][3], cf[i][4], cf[i][5],
			cf[i][6], cf[i][7], cf[i][8], cf[i][9],
			cf[i][10]))
	
	x_axis_01 = []
	y_axis_01 = []

	#x_axis_02 = []
	y_axis_02 = []

	y_axis_03 = []

	for i in range(df_size):
		x_axis_01.append(countries[i].team)
		y_axis_01.append(countries[i].wins)
		y_axis_02.append(countries[i].loses)
		y_axis_03.append(countries[i].draws)

	m1 = max(y_axis_02)
	m2 = max(y_axis_01)

	for i in range(df_size):
		y_axis_02[i] *= -1

	plt.rc('xtick', labelsize = 8)
	plt.xticks(rotation = 90)
	
	# nrows, ncols, index
	plt.bar(x_axis_01, y_axis_01, color = 'blue')
	plt.bar(x_axis_01, y_axis_02, color = 'red')

	plt.xlabel('Countries that participated in a World Cup')
	plt.ylabel('Wins and Loses')

	ax = plt.twinx()
	ax.plot(y_axis_03, 'bo--',color = 'orange', linewidth = 1)
	ax.set_ylim(0 - m1 - 2, m2)
	plt.ylabel('Draws')

	plt.show()


if __name__ == '__main__':
	main()
