import random

nickname_history = []

fun_meanings = [
    "The Creative One", "Secret Code", "Sassy Mix", "Energetic Spirit", "Mysterious Vibes",
    "Friendly Star", "Dynamic Duo", "Playful Wonder", "Bold Inventor"
]

def combine_names_style_1(name1, name2):
    return name1[:2] + name2[-2:]

def combine_names_style_2(name1, name2):
    half1 = name1[:len(name1)//2]
    half2 = name2[len(name2)//2:]
    return half1 + half2

def combine_names_style_3(name1, name2):
    return name1[:3] + name2[:3]

def combine_names_style_4(name1, name2):
    chars_name1 = list(name1)
    chars_name2 = list(name2)
    chosen = random.sample(chars_name1 + chars_name2, min(6, len(chars_name1)+len(chars_name2)))
    return ''.join(chosen)

def combine_names_style_5(name1, name2):
    return name2[::-1][:3] + name1[::-1][:3]

def generate_nickname(name1, name2, style):
    if style == 1:
        return combine_names_style_1(name1, name2)
    elif style == 2:
        return combine_names_style_2(name1, name2)
    elif style == 3:
        return combine_names_style_3(name1, name2)
    elif style == 4:
        return combine_names_style_4(name1, name2)
    elif style == 5:
        return combine_names_style_5(name1, name2)
    else:
        return "Invalid style!"

def main():
    print("Welcome to the Python Nickname Generator!")
    while True:
        name1 = input("Enter the first name: ")
        name2 = input("Enter the second name: ")
        print("Choose a combination style:")
        print("1. First 2 letters of Name1 + Last 2 letters of Name2")
        print("2. First half of Name1 + Second half of Name2")
        print("3. First 3 letters of both names")
        print("4. Random characters from both names")
        print("5. Reversed combination (first 3 letters reversed from both)")

        try:
            style = int(input("Enter style number (1-5): "))
        except ValueError:
            print("Invalid input; defaulting to style 1.")
            style = 1
        name1 = name1.strip().capitalize()
        name2 = name2.strip().capitalize()
        nickname = generate_nickname(name1, name2, style)
        meaning = random.choice(fun_meanings)
        
        print(f"Generated Nickname: {nickname}")
        print(f"Nickname Meaning: {meaning}")
        nickname_history.append(nickname)
        
        print("History:", ', '.join(nickname_history))
        
        another = input("Generate another nickname? (y/n): ")
        if another.lower() != 'y':
            break

if __name__ == "__main__":

    main()
