import json
from datetime import datetime, timedelta

FESTIVAL_FILE = "festivals.json"

def load_festivals():
    try:
        with open(FESTIVAL_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_festivals(festivals):
    with open(FESTIVAL_FILE, "w") as f:
        json.dump(festivals, f, indent=4)

def add_festival(festivals):
    name = input("Festival name: ").strip()
    date_str = input("Date (YYYY-MM-DD): ").strip()
    description = input("Description (optional): ").strip()
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        festivals.append({"name": name, "date": date_str, "description": description})
        print("Festival added successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def delete_festival(festivals):
    view_all_festivals(festivals)
    idx = int(input("Enter number to delete: ")) - 1
    if 0 <= idx < len(festivals):
        del festivals[idx]
        print("Festival deleted.")
    else:
        print("Invalid selection.")

def view_all_festivals(festivals):
    if not festivals:
        print("No festivals saved.")
    for idx, fest in enumerate(sorted(festivals, key=lambda x: x['date'])):
        print(f"{idx+1}. {fest['name']} - {fest['date']} ({fest.get('description', '')})")

def check_reminders(festivals):
    today = datetime.now().date()
    upcoming = []
    for fest in festivals:
        fest_date = datetime.strptime(fest['date'], "%Y-%m-%d").date()
        days_diff = (fest_date - today).days
        if days_diff == 0:
            print(f"🎉 Today is {fest['name']}! {fest.get('description', '')}")
        elif 0 < days_diff <= 7:
            print(f"Upcoming Festival: {fest['name']} in {days_diff} day(s). {fest.get('description', '')}")
            upcoming.append(fest)
    if not upcoming:
        print("No festivals in the next 7 days.")

def main():
    festivals = load_festivals()
    while True:
        print("\nFestival Reminder Bot")
        print("1. View all festivals\n2. Add festival\n3. Delete festival\n4. Check reminders\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            view_all_festivals(festivals)
        elif choice == "2":
            add_festival(festivals)
            save_festivals(festivals)
        elif choice == "3":
            delete_festival(festivals)
            save_festivals(festivals)
        elif choice == "4":
            check_reminders(festivals)
        elif choice == "5":
            save_festivals(festivals)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":

    main()
