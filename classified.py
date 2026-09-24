user_input = input("Classifier: ")
def classified():
    target_words = ["james", "james.", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
    target_words [0:7] = [word.lower() for word in target_words]
    global user_input
    for word in user_input.split():
        if word.lower() in target_words:
            user_input = user_input.replace(word, "[REDACTED]")
    print(user_input)
classified()