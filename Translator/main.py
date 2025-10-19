from deep_translator import GoogleTranslator

print("Inserisci la lingua da tradudurre: en, it, fr, de, es...")
source = input()

print("Inserisci la lingua in cui tradurre: en, it, fr, de, es...")
target = input()

print("Vuoi tradurre da un testo o da un file? (1 per testo, 2 per file)")
choise = input()

if choise == "1":   
    print("Inserisci il testo da tradurre:")
    txt = input()
    translation = GoogleTranslator(source = source,  target = target).translate(txt)

elif choise == "2":     
    print("Inserisci il path del file da tradurre:")
    path = input()
    translation = GoogleTranslator(source = source,  target = target).translate_file(path)

print("Traduzione:\n" + translation)