from datetime import datetime, date

def get_date_of_birth():
    while True:
        dob = input("Please enter your date of birth (DD-MM-YYYY or YYYY-MM-DD): ")
        try:
            if len(dob.split('-')[0]) == 4:
                dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
            else:
                dob_date = datetime.strptime(dob, '%d-%m-%Y').date()
            if dob_date > date.today():
                print("You can't be born in the future!")
                continue
            return dob_date
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY or YYYY-MM-DD.")

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def calculate_age_in_months(dob):
    today = date.today()
    age_in_months = (today.year - dob.year) * 12 + today.month - dob.month
    age_in_months -= 1 if today.day < dob.day else 0
    return age_in_months

def calculate_age_in_days(dob):
    today = date.today()
    age_in_days = (today - dob).days
    return age_in_days

def display_age(dob, age, age_in_months, age_in_days):
    print(f"Your current age is: {age} years, {age_in_months} months, {age_in_days} days")

def time_until_next_birthday(dob):
    today = date.today()
    next_birthday = date(today.year, dob.month, dob.day)
    if today > next_birthday:
        next_birthday = date(today.year + 1, dob.month, dob.day)
    time_to_birthday = next_birthday - today
    return time_to_birthday.days

def save_dob_and_age(dob, age):
    with open("user_dobs.txt", "a") as file:
        file.write(f"DOB: {dob}, Age: {age}\n")

def main():
    while True:
        dob = get_date_of_birth()
        age = calculate_age(dob)
        age_in_months = calculate_age_in_months(dob)
        age_in_days = calculate_age_in_days(dob)
        display_age(dob, age, age_in_months, age_in_days)
        save_dob_and_age(dob, age)
        
        if (dob.month, dob.day) == (date.today().month, date.today().day):
            print("Happy Birthday!")
        
        print(f"Time left until your next birthday: {time_until_next_birthday(dob)} days")
        
        again = input("Do you want to calculate another age? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()