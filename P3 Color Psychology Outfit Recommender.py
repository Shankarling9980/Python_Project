import random

color_mapping = {
    "happy": ("yellow", "Try a cheerful yellow blouse with casual jeans 😊"),
    "calm": ("blue", "Wear a soothing blue shirt and khaki trousers 🛀"),
    "confident": ("red", "Rock a bold red shirt with black jeans 💪"),
    "energetic": ("yellow", "Choose a vibrant yellow tee and white sneakers ⚡"),
    "stressed": ("green", "Opt for a calming green sweater with dark pants 🍃"),
}

event_mapping = {
    "interview": ("blue", "For trust and confidence, wear a navy suit or dress 👔"),
    "date": ("red", "For romance, choose a maroon or red dress/shirt ❤️"),
    "party": ("yellow", "Bring energy with a bright yellow or orange top 🥳"),
    "casual outing": ("green", "Stay fresh with olive or sage tones and denim 👟"),
}

# Main logic example
user_type = input("Are you dressing for mood or event? (mood/event): ").strip().lower()
if user_type == "mood":
    mood = input("Describe your mood: ").strip().lower()
    suggestion = color_mapping.get(mood, ("black", "Try a classic black outfit for timeless style 🖤"))
    print(suggestion[1])
elif user_type == "event":
    event = input("What is the event? ").strip().lower()
    suggestion = event_mapping.get(event, ("white", "Go for a simple white shirt and comfy jeans 🤍"))
    print(suggestion[1])
else:
    print("Please enter 'mood' or 'event'.")

# Optional: Random tip
style_tips = [
    "Mix neutrals with one accent color for a balanced look.",
    "Accessorize with statement jewelry to elevate any outfit.",
    "Layering gives depth, especially in winter months.",
]
print("Tip:", random.choice(style_tips))
