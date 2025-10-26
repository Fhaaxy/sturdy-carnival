from deep_translator import GoogleTranslator

print("Welcome to the Translator!")

source = input("Select the language to be translated (en, it, fr, de, es...): ").lower()
target = input("Select the language to translate into (en, it, fr, de, es...): ").lower()

while True:
    choice = input("Do you want to translate from a text or a file? (1 for text, 2 for file): ")

    if choice == "1":
        txt = input("Insert the text to be translated: ")
        translation = GoogleTranslator(source=source, target=target).translate(txt)
        break

    elif choice == "2":
        while True:
            path = input("Insert the file path: ")
            try:
                translation = GoogleTranslator(source=source, target=target).translate_file(path)
                break
            except FileNotFoundError:
                print("File not found. Please try again.")
        break

    else:
        print("Invalid choice. Please select 1 or 2.")

print("\nTranslation:\n" + translation)
