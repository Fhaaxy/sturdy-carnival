from gtts import gTTS

print("Text to Speech")

#Get user input for language selection
lan = input("Select language: en/fr/es/de/it: ").lower()

#Get user input for text source
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
                file_path = input("Enter file path: ")
    elif choice == 'n':
        txt = input("Enter text: ")
        break
    else:
        print("Invalid choice. Try again.")

#Create gTTS object and save as mp3
tts = gTTS(text=txt, lang=lan)

filename = input("Insert filename (without extension): ") + ".mp3"
tts.save(filename)

print("File saved successfully.")
