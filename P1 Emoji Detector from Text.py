emotion_dict = {
    'happy': 'joy',
    'glad': 'joy',
    'smile': 'joy',
    'cry': 'sadness',
    'sad': 'sadness',
    'angry': 'anger',
    'mad': 'anger',
    'scared': 'fear',
    'afraid': 'fear',
}

emoji_dict = {
    'joy': '😊',
    'sadness': '😢',
    'anger': '😠',
    'fear': '😱',
}

while True:
    user_input = input("Enter a sentence (or type 'exit' to quit): ").lower()
    if user_input == 'exit':
        break
    words = user_input.split()
    emotion_count = {}
    for word in words:
        emotion = emotion_dict.get(word)
        if emotion:
            emotion_count[emotion] = emotion_count.get(emotion, 0) + 1
    if emotion_count:
        detected_emotion = max(emotion_count, key=emotion_count.get)
        emoji = emoji_dict[detected_emotion]
        print(f"Detected Emotion: {detected_emotion.title()} {emoji}")
    else:

        print("No major emotion detected. Try expressing more feeling!")
