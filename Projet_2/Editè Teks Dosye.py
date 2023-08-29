def read_file(path):
    try:
        with open(path, 'r') as file:
            kontni = file.read()
            return kontni
    except FileNotFoundError:
        return "File not found."

def display_text(kontni):
    print("\nContents of the file:\n---------------------\n")
    print(kontni)

def update_text(kontni):
    print("Enter the new content (type 'done' on a new line to finish editing):\n")
    new_lines = kontni.split('\n')
    while True:
        line = input()
        if line == 'done':
            break
        new_lines.append(line)
    updated_content = '\n'.join(new_lines)
    return updated_content

def clean_text(kontni):
    cleaned_content = ' '.join(kontni.split())  # Retire espas devan ak deye
    cleaned_content = ''.join(char for char in cleaned_content if char.isalnum() or char.isspace()) # Retire karakte espesyal yo
    return cleaned_content

def save_text(path, kontni):
    with open(path, 'w') as file:
        file.write(kontni)
    print(f"File \"{path}\" saved successfully.")

def main():
    print("Welcome to the Text File Editor!\n")
    while True:
        print("\n1. Read Text File\n2. Display Text\n3. Update Text\n4. Clean Text\n5. Save Text\n6. Exit")
        chwa = input("\nPlease select an option: ")

        if chwa == '1':
            file_path = input("\nEnter the path to the text file: ")
            kontni = read_file(file_path)

        elif chwa == '2':
            display_text(kontni) if 'kontni' in locals() else print("No content available.")

        elif chwa == '3':
            if 'kontni' in locals():
                print("1. Add to the end\n2. Insert at a specific index")
                edit_choice = input("Please select an editing option: ")

                if edit_choice == '1':
                    updated_content = update_text(kontni)
                    kontni = updated_content
                elif edit_choice == '2':
                    index = int(input("Enter the index where you want to insert the text: "))
                    if index < 0 or index > len(kontni):
                        print("Invalid index.")
                    else:
                        new_text = input("Enter the text to insert: ")
                        updated_content = kontni[:index] + new_text + kontni[index:]
                        kontni = updated_content
                else:
                    print("Invalid editing option.")
            else:
                print("No content available.")

        elif chwa == '4':
            if 'kontni' in locals():
                cleaned_content = clean_text(kontni)
                kontni = cleaned_content
                print("Text cleaned successfully.")
            else:
                print("No content available.")

        elif chwa == '5':
            if 'kontni' in locals():
                save_text(file_path, kontni)
            else:
                print("No content available.")

        elif chwa == '6':
            print("Exiting the Text File Editor. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
