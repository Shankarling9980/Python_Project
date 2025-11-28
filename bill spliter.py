def get_float_input(prompt, min_val=0):
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt, min_val=1):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Number of people must be >= {min_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def even_split(total, num_people, names=None):
    share = total / num_people
    if names:
        for name in names:
            print(f"{name}: ${share:.2f}")
    else:
        print(f"Each person pays: ${share:.2f}")
    return share

def uneven_split(total, num_people, names):
    percentages = []
    print("Enter percentage for each person (must sum to 100%):")
    for name in names:
        while True:
            try:
                pct = float(input(f"{name}: "))
                if pct < 0 or pct > 100:
                    print("Percentage must be between 0 and 100.")
                    continue
                percentages.append(pct)
                break
            except ValueError:
                print("Enter a valid percentage.")
    
    total_pct = sum(percentages)
    if abs(total_pct - 100) > 0.01:
        print(f"Total percentages = {total_pct:.2f}%. Must be 100%. Try again.")
        return uneven_split(total, num_people, names)
    
    print("Split amounts:")
    amounts = []
    for i, (name, pct) in enumerate(zip(names, percentages)):
        amount = total * (pct / 100)
        print(f"{name}: ${amount:.2f}")
        amounts.append(amount)
    return amounts

def export_to_file(names, amounts, filename="bill_split.txt"):
    with open(filename, 'w') as f:
        f.write("Bill Split Results:")
        f.write("="*30 + "")
        for name, amount in zip(names, amounts):
            f.write(f"{name}: ${amount:.2f}")
    print(f"Results exported to {filename}")

# Main loop
while True:
    print("" + "="*50)
    print("BILL SPLITTER APP")
    print("="*50)
    
    total_bill = get_float_input("Enter total bill amount: $")
    num_people = get_int_input("Enter number of people: ")
    
    use_names = input("Enter names? (y/n): ").lower() == 'y'
    names = []
    if use_names:
        print("Enter names:")
        for i in range(num_people):
            names.append(input(f"Person {i+1}: ").strip())
    
    split_type = input("Even (e) or Uneven (u) split? ").lower()
    
    if split_type == 'e':
        amounts = [even_split(total_bill, num_people, names if use_names else None)]
    else:
        if not use_names:
            print("Names required for uneven split.")
            continue
        amounts = uneven_split(total_bill, num_people, names)
    
    if amounts and input("Export to file? (y/n): ").lower() == 'y':
        export_names = names if use_names else [f"Person {i+1}" for i in range(num_people)]
        export_amounts = [amounts[0]] * num_people if split_type == 'e' else amounts
        export_to_file(export_names, export_amounts)
    
    if input("Another split? (y/n): ").lower() != 'y':
        break

print("Thanks for using Bill Splitter!")