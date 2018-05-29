import re
from csv import DictReader


def get_total_budget_value(csv_filepath, year):
	"""Compute the total USD value of projects for the input year.
	Args:
	csv_filepath (str): A path to a CSV file containing three columns: project-id; start-date; total-budget-value-usd.
	year (int): A value corresponding to a year.

	Returns:
	(float) The USD value of projects that start in the given year
	"""
	# Write your code here
	# TODO:  validate csv file
	try:
		# check if year entered is an integer or can be cast to int
		int(year)
		# open file in read mode
		open(csv_filepath, "r")

	except IOError:
		print("Check file path: file does not exist")
	except ValueError:
		print("Input Year must be an Integer") 
	else:
		with open(csv_filepath) as file:
			csv_reader = DictReader(file)
			# rename fieldnames to check errors
			start_date = csv_reader.fieldnames[1]
			total_budget_value_usd = csv_reader.fieldnames[2]
			project_id = csv_reader.fieldnames[0]
 
			#Initialise the sum of budget to 0
			total_budget_value_for_given_year = 0
			# iterate through the csv file and get the sum of all budget in the required year
			for row in csv_reader:
			# validate year format
				r = re.compile('[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])')
				if r.match(row[csv_reader.fieldnames[1]]) is None:
				# Display line csv line number that has the error
					print (f"There is an error in row {csv_reader.line_num}. Date must be in YYYY-MM-DD")
					break
				if int(row[start_date][:4]) == year:
					try:
						total_budget_value_for_given_year += float(row[total_budget_value_usd])
					except (TypeError, ValueError) :
						print("Error: ALl budget values must be in figures")
						break
			else:
				return total_budget_value_for_given_year

print (get_total_budget_value("tests/sample_data_fully_valid_10_rows.csv", 2018))