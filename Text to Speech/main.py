from gtts import gTTS

print("Text to Speech")

lan = input("Select language: en/fr/es/de/it: ").lower()

while True:
    choice = input("Do you want to import text from a file? (y/n): ").lower()
    if choice == 'y':
        while True:
            file_path = input("Enter file path: ")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    txt = file.read()
                break
            except FileNotFoundError:
                print("File not found. Please try again.")
        break
    elif choice == 'n':
        txt = input("Enter text: ")
        break
    else:
        print("Invalid choice. Try again.")

tts = gTTS(text=txt, lang=lan)

filename = input("Insert filename (without extension): ") + ".mp3"
tts.save(filename)

print("File saved successfully.")
