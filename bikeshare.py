import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print ('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("Please choose one of these cities ? (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print ("This City is not available, please choose one of these cities ")

                    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ["all" , "january" , "february" , "march" , "april" , "may" , "june"]
    while True:
        month = input("In which of these months? or all? (all , january , february , march, april, may, june): ").lower()
        if month in month_list:
            break
        else:
            print ("This month is not available, please choose one of these months")
        
           
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ["all" , "monday" , "tuesday" , "wednesday" , "thuresday" , "friday" , "saturday" , "sunday"]
    while True:
        day = input("In Which week day? or all? (all , monday , tuesday , wednesday , thuresday , friday , saturday , sunday): ").lower()
        if day in days_list:
            break
        else:
            print ("This is not a valid Day, please choose one of these days ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name().str.lower()
    
    if month != "all":
        month_list = ["january" , "february" , "march" , "april" , "may" , "june"]
        month = month_list.index(month) +1 
        df = df[df["month"] == month]
    else:
        print("No month filter")
        
    if day != "all":
        df = df[df["day"] == day]
    else:
        print("No day filter")
      
    return df

def display_raw_data(df):
    
    # To Display the data that has been loaded in raws of 5, using the data returned from def load data
   print('\nRaw data is available to check... \n')
   start_loc = 0
   while True:
       display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes \no').lower()
       if display_opt not in ['yes', 'no']:
           print('That\'s invalid choice, pleas type yes or no')

       elif display_opt == 'yes':
           print(df.iloc[start_loc:start_loc+5])
           start_loc+=5

       elif display_opt == 'no':
           print('\nExiting...')
           break
           
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month is: {}" .format(df["month"].mode()[0]))

    # TO DO: display the most common day of week
    print("the most common day of week is: {}" .format(df["day"].mode()[0]))   

    # TO DO: display the most common start hour    
    df["hour"] = df["Start Time"].dt.hour
    print("the most common start hour is:{}" .format(df["hour"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station is: {}" .format(df["Start Station"].mode())) 


    # TO DO: display most commonly used end station
    print("the most commonly used end station is: {}" .format(df["End Station"].mode())) 

    # TO DO: display most frequent combination of start station and end station trip
    df["Route"] = df["Start Station"] + "  " + df ["End Station"]
    print("the most commonly used route is: {}" .format(df["Route"].mode()))
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Trips Duration: " .format (df["Trip Duration"].sum()))


    # TO DO: display mean travel time
    print("Average Trip Duration: " .format (df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"]. value_counts())
          
    # TO DO: Display counts of gender       
    if "Gender" in df :
        print(df["Gender"].value_counts())
          
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth year" in df :
          print("The Earliest Year of Birth: " .int(df["Birth Year"].max()))
          print("The Most Recent Year of Birth: " .int(df["Birth Year"].min()))
          print("The Most Commom Year of Birth: " .int(df["Birth Year"].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
