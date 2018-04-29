from pymongo import MongoClient

def main():
	client = MongoClient('127.0.0.1', 27017)
	datascience_db = client.get_database('DataScience')
	world_cup = datascience_db.get_collection('WorldCup')
	print(world_cup.find_one())

if __name__ == '__main__':
	main()