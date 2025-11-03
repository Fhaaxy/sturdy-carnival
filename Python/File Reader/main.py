from PyPDF2 import PdfReader

print("Welcome to the File Reader Program!")
type_of_file = input("Please enter the type of file you want to read (txt/html/java/py/pdf): ").strip().lower()
file_path = input("Please enter the path to the file: ").strip()

#Read and display file content
while True:
    try:
        if type_of_file == "txt" or type_of_file == "html" or type_of_file == "java" or type_of_file == "py":
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print("\nFile Content:\n")
                    print(content)
                break

        elif type_of_file == "pdf":
                    reader = PdfReader(file_path)
                    print("\nPDF Content:\n")
                    for page in reader.pages:
                        print(page.extract_text())
                    break
        else:
                print("Unsupported file type. Please try again.")
                type_of_file = input("Please enter the type of file you want to read (txt/html/java/py/pdf/json/csv): ").strip().lower()
                file_path = input("Please enter the path to the file: ").strip()
            
    except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            file_path = input("Please enter the path to the file: ").strip()