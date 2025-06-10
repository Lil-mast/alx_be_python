from datetime import datetime, timedelta

def main():
    current_time = datetime.now()
    print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

    days_to_add = int(input("Enter number of days to add: "))
    future_date = current_time + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()