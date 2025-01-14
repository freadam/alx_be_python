from datetime import datetime, timedelta

def display_current_datetime ():
    current_date = datetime.now()
    date_time_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print('Current date and time: ', date_time_str)

def calculate_future_date():
    input_date = input("Enter the number of days to add to the current date: ")
    future_date = datetime.today() + timedelta(days=int(input_date))
    date_str = future_date.strftime("%Y-%m-%d ")
    print ("Future date: ", date_str)
