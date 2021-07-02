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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Enter a city (chicago, new york or washington): ').lower()
            city_dataframe = pd.read_csv(CITY_DATA[city])
            break
        except:
            print('Please enter a valid city')
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            month = input('Enter a month (January, February, March, April, May, June), or enter "all" for no month filter: ').title()      
            if month != 'all':
                months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
                month = months.index(month) + 1
                [months] == month
            break
        except:
            print('Please enter a valid month from January to June!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Enter a day (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday), or enter "all" for no day filter: ').title()
            if day != 'all':
                days = ['Sunday', 'Monday', 'Tuesday', 'Wedesday', 'Thursday', 'Friday', 'Saturday']
                day = days.index(day) + 1
                [days] == day
            break
        except:
            print('Please enter a valid day')

    print('-'*40)
    return city, month, day

def raw_data(city_dataframe):
    count = 0
    raw_data_request = input('Would you like to display the first 5 rows of the data (continue/stop)? ').lower()
    while True:
        if raw_data_request == 'stop':
            break
        print(city_dataframe[count : count + 5])
        raw_data_request = input('Would you like to display an additional 5 rows (continue/stop)? ').lower()
        count += 5

        
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
    city_dataframe = pd.read_csv(CITY_DATA[city])
    city_dataframe ['Start Time'] = pd.to_datetime(city_dataframe['Start Time'])
    city_dataframe ['Month'] = city_dataframe['Start Time'].dt.month
    city_dataframe ['Day of Week'] = city_dataframe['Start Time'].dt.weekday_name
    
    
    return city_dataframe    


def time_stats(city_dataframe):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_com_month = city_dataframe['Month'].mode()[0]
    print('Most common month: ', most_com_month)

    # TO DO: display the most common day of week
    most_com_day = city_dataframe['Day of Week'].mode()[0]
    print('Most common day of week: ', most_com_day)

    # TO DO: display the most common start hour
    city_dataframe ['Start Hour'] = city_dataframe['Start Time'].dt.hour
    most_com_hour = city_dataframe['Start Hour'].mode()[0]
    print('Most common start hour: ', most_com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(city_dataframe):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_com_start_station = city_dataframe['Start Station'].mode()[0]
    print('Most common start station: ', most_com_start_station)
    
    # TO DO: display most commonly used end station
    most_com_end_station = city_dataframe['End Station'].mode()[0]
    print('Most common end station: ', most_com_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    city_dataframe ['Combination of Start & End'] = city_dataframe['Start Station'] + city_dataframe['End Station']
    most_freq_comb = city_dataframe['Combination of Start & End'].mode()[0]
    print('Most frequent combination of start & end stattion: ', most_freq_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(city_dataframe):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    city_dataframe ['End Time'] = pd.to_datetime(city_dataframe['End Time'])
    city_dataframe ['End Hour'] = city_dataframe ['End Time'].dt.hour
    city_dataframe ['Total Travel Time'] = city_dataframe['End Hour'] - city_dataframe['Start Hour']
    print('Total travel time: ', city_dataframe['Total Travel Time'].sum())

    # TO DO: display mean travel time
    print('Travel time average: ', city_dataframe['Total Travel Time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city_dataframe):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = city_dataframe['User Type'].value_counts()
    print('Count of user types: ', user_types_count)
   
    if 'Gender' in city_dataframe:
    # TO DO: Display counts of gender
        gender_count = city_dataframe['Gender'].value_counts()
        print('Gender count: ', gender_count)
    else:
        print('There are no gender data for washington!')
     
    # TO DO: Display earliest, most recent, and most common year of birth
        
    if 'Birth Year' in city_dataframe:
        sorted_years = np.sort(city_dataframe['Birth Year'])
        print('Earliest year: ', sorted_years[0])
        print('Most recent year: ', sorted_years[-1])
        most_com_year = city_dataframe['Birth Year'].mode()[0]
        print('Most common year: ', most_com_year)
    else:
        print('There are no birth year data for washington!')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        city_dataframe = load_data(city, month, day)
        raw_data(city_dataframe)
        time_stats(city_dataframe)
        station_stats(city_dataframe)
        trip_duration_stats(city_dataframe)
        user_stats(city_dataframe)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
