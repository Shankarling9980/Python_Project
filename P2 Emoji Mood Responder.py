def mood_detector():
    moods = {
        "happy":    ("😊", "That's great to hear!"),
        "sad":      ("🤗", "Cheer up! Here's a hug"),
        "angry":    ("😤", "Take a deep breath"),
        "tired":    ("😴", "Rest well"),
        "excited":  ("🥳", "Let's celebrate!"),
        "stressed": ("😣", "Exerscise to relieve tension"),
        "bored":    ("🥱", "Start new hobby, learn new things"),
    }
    
    print("Welcome to the Mood Detector!")
    print("Type 'exit' anytime to quit.")
    
    while True:
        user_input = input("How are you feeling today? ").strip().lower()
        
        if user_input == "exit":
            print("Goodbye! Have a great day! 👋")
            break
        
        found_mood = False
        for mood, (emoji, response) in moods.items():
            if mood in user_input:
                print(f"{response} {emoji}")
                found_mood = True
                break
                
        if not found_mood:
            print("Sorry, I couldn't detect your mood. Try words like 'happy', 'sad', 'angry', 'tired', 'excited','stressed', 'bored'.")
            
if __name__ == "__main__":

    mood_detector()
