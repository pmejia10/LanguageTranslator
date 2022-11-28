# Author: Patrick Mejia

from googletrans import Translator

translator = Translator()
language = {"En": "English",
            "Fr": "French",
            "Ge": "German",
            "It": "Italian",
            "Ja": "Japanese",
            "Hi": "Hindi",
            "Ru": "Russian",
            "Ar": "Arabic",
            "Ch": "Chinese",
            "Es": "Spanish"
            }

checkLang = True  # Checks to see if it is a valid language

while checkLang:  # Loop for checking the user input

    userLang = input(
        f"Enter the language you want to translate to. Use the two letter abbreviations for the languages."
        f"Enter 'options' to see possible languages \n")

    if userLang == "options":  # Checks input for options menu
        print("Options Menu")  # Heading of language option menu
        for i in language.items():
            print("Use the two letter abbreviations for the languages.")
            print(i)
            print()

    else:  # validating user input
        for lang in language.keys():
            if lang == userLang:
                print(f"You have selected {language[lang]}")
                checkLang = False
        if checkLang:
            print("It's not a valid language code!")

while True:  # Translation loop for text
    original_text = input(
        "\nEnter the text you would like to translate: \nTo quit the translation, enter 'quit'\n")

    # Using the translation method from the googletrans package
    translated_text = translator.translate(original_text, dest=userLang)
    print(f"\n{language[userLang]} translation: {translated_text.text}")

    if original_text == "quit":  # exit program command
        print("Program has been closed.")
        break
