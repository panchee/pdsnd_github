import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city':'new_york_city.csv',
              'washington':'washington.csv' }
def get_city():
    city_valid = False
    while city_valid == False:
        city_choices = ['chicago','new york city', 'washington']
        city = input("Would you like to see the data for Chicago, New York City or Washington?\n").lower()
        if city in city_choices:
            city_valid = True
            print("You have selected data from: {}".format(city))
            return city
        else:
            print("That is not a valid city. Check for spaces and typos before trying again.")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()
    # get user input if they would like to filter by month, day, both or none at all
    filter_valid = False
    while filter_valid == False:
            choice_choices = ['month', 'day', 'both', 'none']
            choice = input('Would you like to filter by month, day, both, or none at all?\n').lower()
            if choice in choice_choices:
                filter_valid = True
                print("You have selected to filter by: {}".format(choice))
            else:
                print("That is not a valid choice. Check for spaces and typos before trying again.")

    # get user input for month (all, january, february, ... , june)
    month = 'all'
    day = 'all'
    if choice == 'month':
        month = get_month()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    elif choice == 'day':
        day = get_day()
    elif choice == 'both':
        month = get_month()
        day = get_day()

    print('-'*40)
    return city, month, day

def get_fiveline(df):
    """
    Prints five rows from the filtered DataFrame based on the return value from 'get_fivechoice()' function.

    This function loops until the returned choice from the 'get_fivechoice()' function is False.
    """
    i = 0
    choice = True
    while choice == True:
        choice = get_fivechoice()

        if choice == True:
            for i in range(i, i+5):
                print('-'*40)
                print(df.iloc[i])
                print('-'*40)
            i += 1
        elif choice == False:
            return

def get_fivechoice():
    """
    Asks user to specify if they would like to see five lines of raw data from filtered DataFrame.

    This function loops until the input by the user is verified to exist in the list of allowed inputs.
    The input is then used to set the return value of True or False.

    Returns:
        (boolean) selected_choice - True or False depending on 'yes' or 'no' entered.
    """
    get_five_valid = False
    while get_five_valid == False:
        get_five_choices = ['yes','no']
        get_five_choice = input("Would you like to see five lines of raw data? Yes or No?\n").lower()
        if get_five_choice in get_five_choices:
            get_five_valid = True
            if get_five_choice == 'yes':
                print("You have selected: Yes")
                selected_choice = True
            elif get_five_choice == 'no':
                print("You have selected: No")
                selected_choice = False
            return selected_choice
        else:
            print("This is not a valid option. Check for spaces and typos before trying again.")

def get_month():
    """
    Asks user to specify the month they would like to filter the DataFrame by.

    This function loops until the input by the user is verified to exist in the list of allowed inputs.

    Returns:
        (str) month - the month to filter by.
    """
    month_valid = False
    while month_valid == False:
            month_choices = ['january','february','march','april','may','june']
            month = input("Which month? January, February, March, April, May, or June? Please type out the full month name:\n").lower()
            if month in month_choices:
                month_valid = True
                print("You have selected the following month: ", month)
                return month
            else:
                print("That is not a valid month. Check for spaces and typos before trying again.")

def get_day():
    """
    Asks user to specify the day they would like to filter the DataFrame by.

    This function loops until the input by the user is verified to exist in the list of allowed inputs.

    Returns:
        (str) day - the day to filter by.
    """
    day_valid = False
    while day_valid == False:
            day_choices = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            day = input("Which day of the week? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? Please type out the full day of the week:\n").title()
            if day in day_choices:
                day_valid = True
                print("You have selected the following day: ", day)
                return day
            else:
                print("That is not a valid day of the week. Check for spaces and typos before trying again.")

def get_restart():
    """
    Asks user to specify if they would like to restart the program.

    This function loops until the input by the user is verified to exist in the list of allowed inputs.
    The input is then used to set the return value of True or False.

    Returns:
        (boolean) restart_choice - True or False depending on 'yes' or 'no' entered.
    """
    restart_valid = False
    while restart_valid == False:
        restart_choices = ['yes','no']
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart in restart_choices:
            restart_valid = True
            if restart == 'yes':
                restart_choice = True
            else:
                restart_choice = False
                print("Terminating Program...")
        else:
            print("This is not a valid option. Try again.")
    return restart_choice

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_Of_Week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month_index = months.index(month) + 1
        df = df[df['Month'] == month_index]

    if day != 'all':
        df = df[df['Day_Of_Week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if df['Month'].value_counts().count() != 1:
         common_month = df['Month'].mode()[0]
         common_month_count = df['Month'][df['Month'] == common_month].count()
         print("The most common month is: {}. Count: {}".format(common_month, common_month_count))

    # display the most common day of week
    if df['Day_Of_Week'].value_counts().count() != 1:
        common_day = str(df['Day_Of_Week'].mode()[0])
        common_day_count = df['Day_Of_Week'][df['Day_Of_Week'] == common_day].count()
        print("The most common day of week is: {}. Count: {}".format(common_day, common_day_count))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    common_hour_count = df['Hour'][df['Hour'] == common_hour].count()
    print("The most common start hour is: {}. Count: {}".format(common_hour, common_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    common_start_station_count = df['Start Station'][df['Start Station'] == common_start_station].count()
    print("The most commonly used start station is: {}. Count: {}".format(common_start_station,common_start_station_count))
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    common_end_station_count = df['End Station'][df['End Station'] == common_end_station].count()
    print("The most commonly used end station is: {}. Count: {}".format(common_end_station,common_end_station_count))

    # display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ':' + df['End Station']
    common_station_combination = df['Combination'].mode()[0]
    common_station_combination_start = df['Combination'].mode()[0].split(':')[0]
    common_station_combination_end = df['Combination'].mode()[0].split(':')[1]
    common_station_combination_count = df['Combination'][df['Combination'] == common_station_combination].count()
    print("The most frequent combination of start station and end station trip is:\n\'{}\' and \'{}\'. Count: {}".format(common_station_combination_start,common_station_combination_end,common_station_combination_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    trip_count = df['Trip Duration'].count()
    print("Total travel time is: {} seconds. Count: {}".format(total_travel_time, trip_count))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: {} seconds.".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Displaying User Types: \n", user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("Displaying Gender Counts: \n", gender)
    else:
        print("No gender information for the selected dataset.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        df.dropna(inplace=True)
        df['Birth Year'] = df['Birth Year'].astype('int64',copy=False)
        earliest_birthyear = df['Birth Year'].min()
        recent_birthyear = df['Birth Year'].max()
        common_birthyear = df['Birth Year'].mode()[0]
        print("The earliest year of birth: {}\nThe most recent year of birth: {}\nThe most common year of birth: {}".format(earliest_birthyear,recent_birthyear,common_birthyear))
    else:
        print("No birth year information for the selected dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    """
    This is the main body of code. This function loops until the variable restart_choice is set to False.

    """
    restart_choice = True
    while restart_choice == True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df.rename( columns={'Unnamed: 0':'Trip ID'}, inplace=True )

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_fiveline(df)
        restart_choice = get_restart()


if __name__ == "__main__":
	main()
