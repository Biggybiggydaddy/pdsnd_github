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

    # TO DO: Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input("What city would you like to know more about(chicago, new york city, washington): ").lower()
        except:
            print('Ooops...I don\'t understand that!. Please input a valid city')
            continue

        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print('Sorry, that\'s not a valid city. Kindly input a valid city')
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            month = input("What month would you like to know more about(all, january, february, ... , june): ").lower()
        except:
            print('Ooops...I don\'t understand that!. Please input a valid month')
            continue

        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Sorry, that\'s not a valid month. Kindly input a valid month')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("What day of the week would you like to know more about(all, monday, tuesday, ... sunday): ").lower()
        except:
            print('Ooops...I don\'t understand that!. Please input a valid day of the week')
            continue

        if day.title() not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            print('Sorry, that\'s not a valid day of the week. Kindly input a valid day of the week')
            continue
        else:
            break


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
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month (from 0 to 5)
    common_month = df['month'].mode()[0]

    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week

    # extract day of the week from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day

    # find the most common day of the week (from 0 to 6)
    common_day_of_the_week = df['day'].mode()[0]
    print('Most Common Day of the Week:', common_day_of_the_week)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most Commonly Used Start Station:', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most Commonly Used End Station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    start_station_and_end_station = df.groupby(['Start Station','End Station']).size().idxmax()

    print('Most Frequent Combination of Start Station and End Station Trip:', start_station_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except KeyError:
        print('No Gender Column for Selected City')


    # TO DO: Display earliest, most recent, and most common year of birth
         # Earliest
    try:
        earliest = int(df['Birth Year'].min())
        print('Earliest Year of Birth:', earliest)

        # Most Recent
        most_recent = int(df['Birth Year'].max())
        print('Most Recent Year of Birth:', most_recent)

        # Most Common Year of Birth
        most_common = int(df['Birth Year'].mode())
        print('Most Common Year of Birth:', most_common)
    except KeyError:
        print('No Gender Birth Year Column for Selected City')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    i=0
    while True:
        display_raw = input('Do you need to see the raw data? Kindly input either yes or no: ').lower()

        if display_raw == 'yes':
            rows = df.iloc[i:i+5]
            print(rows)
            i+=5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
