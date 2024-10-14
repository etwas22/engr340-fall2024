import sys
import math


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here

    # This print function is for better formatting, making it easier to view the answers for question one
    print("\nAnswers to Question 1:")

    # Created an empty list set for the dates of Harrisonburg and Rockingham to parse through
    harrisonburg_dates = []
    rockingham_dates = []

    # A For loop that iterates through all the entries from the covid data
    for (date, county, state, cases, deaths) in data:

        # If statement that requires Harrisonburg and Virginia for the county and state, respectively
        if county == "Harrisonburg city" and state == "Virginia":

            # Appends the dates that covid showed up in Harrisonburg into the covid date into the empty list
            harrisonburg_dates.append(date)


        # Else/If statement that requires Rockingham and Virginia for the county and state, respectively, after
        # gathering the Harrisonburg dates
        elif county == "Rockingham" and state == "Virginia":

            # Appends the dates that covid showed up in Rockingham into the covid date into the empty list
            rockingham_dates.append(date)


    # I thought of using min(harrisonburg_dates), but decided to change it to be the number of the first index, [0],
    # of the dates. If the data was mixed and not linearly increasing, then I would use the min function or perhaps the
    # sort function alongside what I currently have.
    ## These two functions find the first date that Harrisonburg and Rockingham had a covid case by storing the day of
    ## the initial index.
    harrisonburg_first = harrisonburg_dates[0]
    rockingham_first = rockingham_dates[0]

    # Prints the answers to question one.
    print(harrisonburg_first, "is the earliest date that Harrisonburg had it's first recorded covid case")
    print(rockingham_first, "is the earliest date that Rockingham had it's first recorded covid case")

    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """

    # your code here

    # Better formatting, easier to view answers to question two
    print("\nAnswers to Question 2:")

    # Created empty lists for the cases and dates for Harrisonburg to later parse through. Also created a daily cases
    # list to go through.
    harrisonburg_cases = []
    harrisonburg_dates = []
    harrisonburg_cases_daily = []

    # Created empty lists for the cases and dates for Rockingham to later parse through. Also created a daily cases
    # list to go through.
    rockingham_cases = []
    rockingham_dates = []
    rockingham_cases_daily = []


    # Same as question one, a for-loop that iterates through all the entries from the covid data. Checks for
    # Harrisonburg and Rockingham counties and Virginia as a state and appends their respective cases and dates to their
    # respective lists.
    for (date, county, state, cases, deaths) in data:
        if county == "Harrisonburg city" and state == "Virginia":
            harrisonburg_cases.append(cases)
            harrisonburg_dates.append(date)

        elif county == "Rockingham" and state == "Virginia":
            rockingham_cases.append(cases)
            rockingham_dates.append(date)



    ##### Start of Harrisonburg answer: #####

    # This For loop loops through the range of the size of the harrisonburg_cases list. The minus one is required as
    # otherwise it introduces an index that doesn't exist in the actual list.
    for n in range(len(harrisonburg_cases) - 1):

        # This if-loop is to simply add the initial case that Harrisonburg has to the daily cases list. It may seem that
        # the loop is unnecessary, but if I didn't have it, the harrisonburg_cases_diff would try to subtract the case
        # from the zero index and the one before that, which ends up being the last index in the list. This results in
        # a massive negative number, which may not matter with how the data is being analyzed, but ultimately it's not
        # correct.
        if n == 0:
            harrisonburg_cases_daily.append(harrisonburg_cases[0])

        # This part of the if-loop goes through each subsequent number after checking if it's the zeroth index.
        else:

            # Takes the nth indexed covid case (n) and subtracts it from the previous covid case (n-1).
            # Ex. if 3/2/2021 was 100 cases and 3/3/2021 was 105 cases, then it's effectively doing 105 - 100,
            # reporting 5 cases back. Same thing happens if cases stay the same or decrease the next day.
            harrisonburg_cases_diff = harrisonburg_cases[n] - harrisonburg_cases[n - 1]

            # Appends the differences to the daily cases list.
            harrisonburg_cases_daily.append(harrisonburg_cases_diff)


    # Takes the max increase in day-to-day covid cases
    harrisonburg_cases_max = max(harrisonburg_cases_daily)

    # Takes the index of the max daily increase
    harrisonburg_cases_max_index = harrisonburg_cases_daily.index(harrisonburg_cases_max)

    # Gets the total cases that the max daily occurs on from the index of the max daily, as they share the same index
    # in different lists
    harrisonburg_cases_current = harrisonburg_cases[harrisonburg_cases_max_index]

    # Gets the previous number of total cases from index of the max daily
    harrisonburg_cases_previous = harrisonburg_cases[harrisonburg_cases_max_index - 1]

    # Gets the day that the daily maximum occurred, also shares the same index in different lists
    harrisonburg_date_daily_max = harrisonburg_dates[harrisonburg_cases_max_index]


    # Prints the Harrisonburg answer to question two
    print("On", harrisonburg_date_daily_max, "Harrisonburg experienced the highest increase in daily covid cases at",
          harrisonburg_cases_max, "cases, increasing from", harrisonburg_cases_previous, "the previous day, to",
          harrisonburg_cases_current, "cases")



    ##### Start of Rockingham Answer: #####

    # This For loop loops through the range of the size of the rockingham_cases list. The minus one is required as
    # otherwise it introduces an index that doesn't exist in the actual list.
    for n in range(len(rockingham_cases) - 1):

        # This if loop is simply to add the initial case that Rockingham has to the daily cases list for the same
        # reason as with the Harrisonburg portion
        if n == 0:
            rockingham_cases_daily.append(rockingham_cases[0])

        # This part of the if-loop goes through each subsequent number after checking if it's the zeroth index.
        else:

            # Takes the nth indexed covid case (n) and subtracts it from the previous covid case (n-1).
            rockingham_cases_diff = rockingham_cases[n] - rockingham_cases[n - 1]

            # Appends the differences to the daily cases list.
            rockingham_cases_daily.append(rockingham_cases_diff)


    # Takes the max increase in day-to-day covid cases
    rockingham_cases_daily_max = max(rockingham_cases_daily)

    # Takes the index of the max daily increase
    rockingham_cases_max_index = rockingham_cases_daily.index(rockingham_cases_daily_max)

    # Gets the total cases that the max daily occurs on from the index of the max daily, as they share the same index
    # in different lists
    rockingham_cases_current = rockingham_cases[rockingham_cases_max_index]

    # Gets the previous number of total cases from index of the max daily
    rockingham_cases_previous = rockingham_cases[rockingham_cases_max_index - 1]

    # Gets the day that the daily maximum occurred, also shares the same index in different lists
    rockingham_date_daily_max = rockingham_dates[rockingham_cases_max_index]

    # Prints the Rockingham answer to question two
    print("On", rockingham_date_daily_max, "Rockingham experienced the highest increase in daily covid cases at",
          rockingham_cases_daily_max, "cases, increasing from", rockingham_cases_previous, "the previous day, to",
          rockingham_cases_current, "cases")

    return

def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    # your code here

    # Better formatting, easier to view answers to question three
    print("\nAnswers to Question 3:")

    # Created empty lists for the cases and dates for Harrisonburg to later parse through. Also created a daily cases
    # list to go through and a moving average (move_ave) list as well.
    harrisonburg_cases = []
    harrisonburg_dates = []
    harrisonburg_cases_daily = []
    harrisonburg_cases_move_ave = []

    # Created empty lists for the cases and dates for Rockingham to later parse through. Also created a daily cases
    # list to go through and a moving average (move_ave) list as well.
    rockingham_cases = []
    rockingham_dates = []
    rockingham_cases_daily = []
    rockingham_cases_move_ave = []


    # Same as question one and two, a for-loop that checks through all the entries from the covid data to append
    # Harrisonburg and Rockingham dates and cases to their respective lists
    for (date, county, state, cases, deaths) in data:
        if county == "Harrisonburg city" and state == "Virginia":
            harrisonburg_cases.append(cases)
            harrisonburg_dates.append(date)

        elif county == "Rockingham" and state == "Virginia":
            rockingham_cases.append(cases)
            rockingham_dates.append(date)


    # For loop for the storage of the moving average for Harrisonburg, does the same as in question two
    for n in range(len(harrisonburg_cases) - 1):
        if n == 0:
            harrisonburg_cases_daily.append(harrisonburg_cases[0])
        else:
            harrisonburg_cases_daily.append(harrisonburg_cases[n] - harrisonburg_cases[n - 1])


    # For loop for the storage of the moving average for Rockingham, does the same as in question two
    for n in range(len(rockingham_cases) - 1):
        if n == 0:
            rockingham_cases_daily.append(rockingham_cases[0])
        else:
            rockingham_cases_daily.append(rockingham_cases[n] - rockingham_cases[n - 1])



    ##### Start of Harrisonburg answer: #####

    # For-loop that goes through the range of the length of the harrisonburg_cases list. The minus seven is there for
    # purpose of making sure that the loop ends seven indexes or "days" prior to the last index, otherwise the last few
    # moving averages wouldn't be for the 7-day period
    for n in range(len(harrisonburg_cases) - 7):

        # Takes the daily cases from the nth index through the next six indices, for a total of 7 indices, which is the
        # same as n + 7, and stores it in a variable until it reaches the end of the range.
        harrisonburg_cases_week = harrisonburg_cases_daily[n : n + 7]

        # Sums the seven indices and divides the sum by seven to get a moving average for each 7-day period
        harrisonburg_moving_ave = (sum(harrisonburg_cases_week))/7

        # Appends the moving average to the Harrisonburg moving cases average list
        harrisonburg_cases_move_ave.append(harrisonburg_moving_ave)


    # Finds the largest moving average
    harrisonburg_move_max = max(harrisonburg_cases_move_ave)

    # Gets the index of the largest moving average in the moving cases average list
    harrisonburg_cases_max_index = harrisonburg_cases_move_ave.index(harrisonburg_move_max)

    # Gets the first day that the largest 7-day moving average that it includes and starts on
    harrisonburg_week_max_first = harrisonburg_dates[harrisonburg_cases_max_index]

    # Gets the last day of the largest 7-day moving average that it includes and ends on
    harrisonburg_week_max_last = harrisonburg_dates[harrisonburg_cases_max_index + 6]

    # Rounds up the max moving average to the next integer as there cannot be 0.xxxx of a person catching covid
    harrisonburg_move_max_round = math.ceil(harrisonburg_move_max)


    # Prints Harrisonburg answer to question three
    print("During a 7-day period, from", harrisonburg_week_max_first,"to", harrisonburg_week_max_last,
          "Harrisonburg had a maximum weekly average increase of", harrisonburg_move_max, "cases per day, or roughly",
          harrisonburg_move_max_round, "cases a day")



    ##### Start of Rockingham answer: #####

    # For-loop that goes through the range of the length of the harrisonburg_cases list. The minus seven is there for
    # purpose of making sure that the loop ends seven indexes or "days" prior to the last index, otherwise the last few
    # moving averages wouldn't be for the 7-day period
    for n in range(len(rockingham_cases) - 7):

        # Takes the daily cases from the nth index through the next six indices, for a total of 7 indices, which is the
        # same as n + 7, and stores it in a variable until it reaches the end of the range.
        rockingham_cases_week = rockingham_cases_daily[n : n + 7]

        # Sums the seven indices and divides the sum by seven to get a moving average for each 7-day period
        rockingham_moving_ave = sum(rockingham_cases_week)/7

        # Appends the moving average to the Rockingham moving cases average list
        rockingham_cases_move_ave.append(rockingham_moving_ave)


    # Finds the largest moving average
    rockingham_move_max = max(rockingham_cases_move_ave)

    # Gets the index of the largest moving average in the moving cases average list
    rockingham_cases_max_index = rockingham_cases_move_ave.index(rockingham_move_max)

    # First day of the 7-day period that
    rockingham_week_move_max_first = rockingham_dates[rockingham_cases_max_index]

    # Gets the first day that the largest 7-day moving average that it includes and starts on
    rockingham_week_move_max_last = rockingham_dates[rockingham_cases_max_index + 6]

    # Rounds up the max moving average to the next integer as there cannot be 0.xxxx of a person catching covid
    rockingham_move_max_round = math.ceil(rockingham_move_max)


    # Prints Rockingham answer to question three
    print("During a 7-day period, from", rockingham_week_move_max_first,"to", rockingham_week_move_max_last,
          "Rockingham had a maximum weekly average increase of", rockingham_move_max, "cases per day, or roughly",
          rockingham_move_max_round, "cases a day")

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    #for (date, county, state, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)


